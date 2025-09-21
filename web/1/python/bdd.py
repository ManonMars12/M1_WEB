from flask import g
import mysql.connector

DATABASE = "2025_M1"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          
    "password": "",          
    "database": DATABASE
}

def get_db():
    if "db" not in g:
        g.db = mysql.connector.connect(**DB_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
