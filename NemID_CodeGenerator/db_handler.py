import sqlite3
import pathlib

#TODO make path work on other computers as well

def authenticate_nem_id(nem_id, nem_id_code):
    # connect to DB
    db = sqlite3.connect(r'c:\Users\Jakob\Desktop\Mandatory_1\nem_id_database.sqlite')
    
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
    db = sqlite3.connect(r'c:\Users\Jakob\Desktop\Mandatory_1\nem_id_database.sqlite')
    
    # create cursor
    db_cursor = db.cursor()

    query = """INSERT INTO auth_log (UserId, Code) VALUES (?,?)"""
    data = [user_id, code]
    
    db_cursor.execute(query, data)
    db.commit()
        
if __name__ == "__main__":
    cwd = pathlib.Path(__file__).parents[0].absolute()
    print(cwd)