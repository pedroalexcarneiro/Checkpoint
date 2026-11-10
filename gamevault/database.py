"""SQLite transacional, migrações incrementais e backup consistente."""
import sqlite3
from contextlib import closing
from pathlib import Path

MIGRATIONS = [
"""
CREATE TABLE games (
 id INTEGER PRIMARY KEY, title TEXT NOT NULL CHECK(length(trim(title))>0),
 description TEXT NOT NULL DEFAULT '', developer TEXT NOT NULL DEFAULT '',
 publisher TEXT NOT NULL DEFAULT '', release_date TEXT NOT NULL DEFAULT '',
 platform TEXT NOT NULL DEFAULT 'PC', genre TEXT NOT NULL DEFAULT '',
 status TEXT NOT NULL DEFAULT 'Não iniciado', rating INTEGER CHECK(rating BETWEEN 0 AND 10),
 favorite INTEGER NOT NULL DEFAULT 0, notes TEXT NOT NULL DEFAULT '',
 source TEXT NOT NULL DEFAULT 'Manual', cover TEXT NOT NULL DEFAULT '',
 banner TEXT NOT NULL DEFAULT '', logo TEXT NOT NULL DEFAULT '',
 executable TEXT NOT NULL DEFAULT '', category TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT(strftime('%Y-%m-%dT%H:%M:%SZ','now')),
 updated_at TEXT NOT NULL DEFAULT(strftime('%Y-%m-%dT%H:%M:%SZ','now')),
 completed_at TEXT, deleted_at TEXT);
CREATE INDEX games_title ON games(title COLLATE NOCASE);
CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE diary_entries (id INTEGER PRIMARY KEY, game_id INTEGER NOT NULL REFERENCES games(id),
 created_at TEXT NOT NULL, text TEXT NOT NULL, progress TEXT NOT NULL DEFAULT '');
CREATE TABLE media_files (id INTEGER PRIMARY KEY, game_id INTEGER REFERENCES games(id),
 path TEXT NOT NULL UNIQUE, caption TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL, kind TEXT NOT NULL);
CREATE TABLE achievements (id INTEGER PRIMARY KEY, game_id INTEGER NOT NULL REFERENCES games(id),
 title TEXT NOT NULL, source TEXT NOT NULL DEFAULT 'Pessoal', unlocked_at TEXT);
CREATE TABLE play_sessions (id INTEGER PRIMARY KEY, game_id INTEGER NOT NULL REFERENCES games(id),
 started_at TEXT NOT NULL, ended_at TEXT, duration_seconds INTEGER NOT NULL DEFAULT 0,
 state TEXT NOT NULL DEFAULT 'active', pid INTEGER);
CREATE TABLE wishlist (game_id INTEGER PRIMARY KEY REFERENCES games(id), target_cents INTEGER,
 currency TEXT NOT NULL DEFAULT 'BRL');
CREATE TABLE price_history (id INTEGER PRIMARY KEY, game_id INTEGER NOT NULL REFERENCES games(id),
 store TEXT NOT NULL, price_cents INTEGER NOT NULL, currency TEXT NOT NULL, url TEXT NOT NULL, checked_at TEXT NOT NULL);
CREATE TABLE external_identifiers (game_id INTEGER REFERENCES games(id), provider TEXT NOT NULL,
 external_id TEXT NOT NULL, PRIMARY KEY(game_id,provider), UNIQUE(provider,external_id));
CREATE TABLE emulators (id INTEGER PRIMARY KEY, name TEXT NOT NULL, executable TEXT NOT NULL);
CREATE TABLE emulator_profiles (id INTEGER PRIMARY KEY, emulator_id INTEGER REFERENCES emulators(id),
 platform TEXT NOT NULL, arguments_json TEXT NOT NULL DEFAULT '["{rom}"]', extensions TEXT NOT NULL DEFAULT '');
CREATE TABLE game_files (id INTEGER PRIMARY KEY, game_id INTEGER REFERENCES games(id),
 drive_id TEXT UNIQUE, original_name TEXT NOT NULL, extension TEXT NOT NULL DEFAULT '',
 size INTEGER, parent_id TEXT, folder_path TEXT NOT NULL DEFAULT '', modified_at TEXT, md5 TEXT,
 platform TEXT NOT NULL DEFAULT '', local_path TEXT, available INTEGER NOT NULL DEFAULT 0,
 review_state TEXT NOT NULL DEFAULT 'pending');
CREATE TABLE rom_versions (id INTEGER PRIMARY KEY, file_id INTEGER NOT NULL UNIQUE REFERENCES game_files(id),
 region TEXT NOT NULL DEFAULT '', revision TEXT NOT NULL DEFAULT '', profile_id INTEGER REFERENCES emulator_profiles(id));
CREATE TABLE save_configurations (id INTEGER PRIMARY KEY, game_id INTEGER REFERENCES games(id),
 directory TEXT NOT NULL, patterns_json TEXT NOT NULL, drive_folder_id TEXT);
CREATE TABLE save_backups (id INTEGER PRIMARY KEY, configuration_id INTEGER REFERENCES save_configurations(id),
 created_at TEXT NOT NULL, path TEXT NOT NULL, sha256 TEXT NOT NULL, drive_id TEXT, manifest_json TEXT NOT NULL);
CREATE TABLE integration_settings (provider TEXT PRIMARY KEY, state TEXT NOT NULL DEFAULT 'Não configurada',
 config_json TEXT NOT NULL DEFAULT '{}');
""",
"""
CREATE TABLE rom_catalog (id INTEGER PRIMARY KEY, source TEXT NOT NULL, platform TEXT NOT NULL,
 title TEXT NOT NULL, rom_name TEXT NOT NULL, size INTEGER, md5 TEXT, sha1 TEXT, crc32 TEXT);
CREATE INDEX rom_catalog_md5 ON rom_catalog(md5);
CREATE INDEX rom_catalog_sha1 ON rom_catalog(sha1);
CREATE INDEX rom_catalog_crc32 ON rom_catalog(crc32);
""",
]

class Database:
    def __init__(self, path: Path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self.connection = sqlite3.connect(path, timeout=10)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute('PRAGMA foreign_keys=ON')
        self.connection.execute('PRAGMA journal_mode=WAL')
        version = self.connection.execute('PRAGMA user_version').fetchone()[0]
        if version > len(MIGRATIONS):
            self.connection.close()
            raise RuntimeError('Banco criado por uma versão mais recente do Checkpoint.')
        for index in range(version, len(MIGRATIONS)):
            try:
                self.connection.executescript('BEGIN IMMEDIATE;\n' + MIGRATIONS[index] + f'\nPRAGMA user_version={index+1};\nCOMMIT;')
            except Exception:
                self.connection.rollback()
                self.connection.close()
                raise

    def backup(self, target: Path):
        target = Path(target)
        if target.resolve() == self.path.resolve():
            raise ValueError('O destino não pode ser o banco em uso.')
        with closing(sqlite3.connect(target)) as destination:
            self.connection.backup(destination)

    def close(self):
        self.connection.close()
