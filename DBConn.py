import sqlite3

localDB = "/home/kali/Documents/SecureWebAppDB.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("could not create connection")

    return conn

def get_user(username):
    conn = create_connection(localDB)
    cur = conn.cursor()
    sql = "SELECT username, password FROM users WHERE username=?"
    cur.execute(sql, username)
    user = cur.fetchone()
    return user