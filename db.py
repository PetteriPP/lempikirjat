import sqlite3
from flask import g

def casefold(text):
    return text.casefold() if text is not None else None

def get_connection():
    con = sqlite3.connect("database.db")
    con.create_function("casefold", 1, casefold, deterministic=True)
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con


def execute(sql, params=[]):
    con = get_connection()
    try:
        result = con.execute(sql, params)
        con.commit()
        g.last_insert_id = result.lastrowid
        return result.rowcount
    finally:
        con.close()


def insert_with_links(sql, params, link_sql, link_ids):
    con = get_connection()
    try:
        result = con.execute(sql, params)
        row_id = result.lastrowid
        con.executemany(link_sql, [(row_id, link_id) for link_id in link_ids])
        con.commit()
        return row_id
    finally:
        con.close()


def execute_transaction(commands):
    con = get_connection()
    try:
        for sql, params in commands:
            con.execute(sql, params)
        con.commit()
    finally:
        con.close()

def last_insert_id():
    return g.last_insert_id    
    
def query(sql, params=[]):
    con = get_connection()
    try:
        result = con.execute(sql, params).fetchall()
        return result
    finally:
        con.close()
