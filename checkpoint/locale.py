"""Datas PT-BR na apresentação; ISO nos contratos e no SQLite."""
from datetime import date,datetime


def date_display(value):
    if not value:return ''
    try:return date.fromisoformat(str(value)[:10]).strftime('%d/%m/%Y')
    except ValueError:return str(value)


def date_storage(value):
    value=value.strip()
    if not value:return ''
    return datetime.strptime(value,'%d/%m/%Y').date().isoformat() if '/' in value else date.fromisoformat(value).isoformat()


def datetime_display(value):
    if not value:return ''
    try:return datetime.fromisoformat(value.replace('Z','+00:00')).strftime('%d/%m/%Y %H:%M')
    except ValueError:return str(value)
