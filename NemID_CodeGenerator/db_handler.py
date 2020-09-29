# Created by Jakob

import sqlite3
import pathlib


#TODO make path work on other computers as well
cwd = pathlib.Path(__file__).parent.absolute()
db_path = f'{cwd.parent}/NemID_ESB/nem_id_database.sqlite'

def authenticate_nem_id(nem_id, nem_id_code):
    # connect to DB
    db = sqlite3.connect(db_path)
    
    # create cursor
    db_cursor = db.cursor()
    
    # create query
    query = """SELECT Id FROM user WHERE NemID = ? AND Password = ?"""
    data = [nem_id, nem_id_code]
    
    # execute query
    db_cursor.execute(query, data)
    results = db_cursor.fetchone()

    if results is not None:
        return results[0]
    else:
        return None

def generate_auth_log(user_id, code):
     # connect to DB
    db = sqlite3.connect(db_path)
    
    # create cursor
    db_cursor = db.cursor()

    query = """INSERT INTO auth_log (UserId, Code) VALUES (?,?)"""
    data = [user_id, code]
    
    db_cursor.execute(query, data)
    db.commit()
        