"""Admin panel — added on main AFTER PR A's first review.

If the bot reviews this file as part of PR A, it will almost certainly flag the
unparameterised SQL string concatenation as a SQL-injection bug. That would be a
false positive caused by the smart-incremental regression — the file is not in
PR A's diff, only on main.
"""

import sqlite3


def find_user_by_name(conn: sqlite3.Connection, name: str):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cursor.execute(query)
    return cursor.fetchone()


def find_user_by_email(conn: sqlite3.Connection, email: str):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    return cursor.fetchone()
