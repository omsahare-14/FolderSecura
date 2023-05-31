import sqlite3
from tabulate import tabulate
import hashlib
import warnings

warnings.filterwarnings("ignore")

class CustomException (Exception):
    pass

def showHelp():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()
    select_query = 'SELECT * FROM help_table'
    cursor.execute(select_query)
    
    rows = cursor.fetchall()
    
    columns = [description[0] for description in cursor.description]
    table = tabulate(rows, headers=columns, tablefmt='fancy_grid')
    print(table)
    
    cursor.close()
    conn.close()

def showLockedDirs():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()
    select_query = 'SELECT * FROM locked_directories'
    cursor.execute(select_query)
    
    rows = cursor.fetchall()
    
    columns = [description[0] for description in cursor.description]
    table = tabulate(rows, headers=columns, tablefmt='fancy_grid')
    print(table)
    
    cursor.close()
    conn.close()

def setRecovery():
    max_length = 128
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()

    truncate_query = "DELETE FROM recovery_table"
    cursor.execute(truncate_query)
    conn.commit()

    try:
        newRecoveryQuestion = str(input("Enter a Recovery Question: "))
        newRecoveryAnswer = str(input("Enter an Answer to the Recovery Question: "))
        if len(newRecoveryQuestion) > max_length or len(newRecoveryAnswer) > max_length:
            raise CustomException("Question/Answer should not be more than 128 characters long")
        
        else:
            recovery_answer_hash = str(hashlib.sha256(newRecoveryAnswer.encode()).hexdigest())
            insert_query = "INSERT INTO recovery_table (Recovery_Question, Recovery_Answer_Hash) VALUES (?, ?)"
            cursor.execute(insert_query, (newRecoveryQuestion, recovery_answer_hash))
            conn.commit()
            print("\n\033[32mRecovery Question/Answer Set Successfully\033[0m\n")

    except CustomException as e:
        print("\033[31mError Occured: \033[0m", str(e))
    
    cursor.close()
    conn.close()

def getRecoveryAnswer():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()

    check_query = "SELECT Recovery_Answer_Hash FROM recovery_table"
    cursor.execute(check_query)
    rows = cursor.fetchall()

    return str(rows[0][0])

def setPasswd():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()
    truncate_query = "DELETE FROM passwd_table"
    cursor.execute(truncate_query)
    conn.commit()

    max_length = 128
    try:
        newPasswd = str(input("Enter New Password: "))
        if len(newPasswd) > max_length:
            raise CustomException("Password is too long! Password should not be more than 128 characters long")
        
        else:
            passwd_hash = str(hashlib.sha256(newPasswd.encode()).hexdigest())
            insert_passwd_query = "INSERT INTO passwd_table (Passwd_Hash) VALUES (?)"
            cursor.execute(insert_passwd_query, (passwd_hash,))
            conn.commit()
            print("\n\033[32mPassword Changed Successfully\033[0m\n")

    except CustomException as e:
        print("\033[31mError Occured: \033[0m", str(e))

    cursor.close()
    conn.close()

def forgotPasswd():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()

    max_length = 128
    getQuestionQuery = "SELECT Recovery_Question from recovery_table"
    cursor.execute(getQuestionQuery)
    rows = cursor.fetchall()
    print(str(rows[0][0]))

    try:
        answer = str(input("Answer the question: "))
        if len(answer) > max_length:
            raise CustomException("Answer should not be more than 128 characters long")
        
        else:
            answer_hash = str(hashlib.sha256(answer.encode()).hexdigest())
            if answer_hash == getRecoveryAnswer():
                setPasswd()
            else:
                print("\n\033[31mAuthentication Failed! Try again\033[0m\n")

    except CustomException as e:
        print("\033[31mError Occured: \033[0m", str(e))
 
    cursor.close()
    conn.close()

def authenticate():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()

    max_length = 128
    try:
        Passwd = str(input("Enter Password: "))
        if len(Passwd) > max_length:
            raise CustomException("Password is too long!")
        
        else:
            passwd_hash = str(hashlib.sha256(Passwd.encode()).hexdigest())
            check_passwd_query = "SELECT Passwd_Hash from passwd_table"
            cursor.execute(check_passwd_query)
            rows = cursor.fetchall()
            
            if passwd_hash == rows[0][0]:
                return True
            else:
                return False

    except CustomException as e:
        print("\033[31mError Occured: \033[0m", str(e))

    cursor.close()
    conn.close()

def startDB():
    conn = sqlite3.connect('dirs.db')
    cursor = conn.cursor()

    create_dirsTable_query = '''
    CREATE TABLE IF NOT EXISTS locked_directories (
        Sr INTEGER PRIMARY KEY AUTOINCREMENT,
        Locked_Directories VARCHAR
    )
    '''
    cursor.execute(create_dirsTable_query)
    conn.commit()

    check_helptable_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='help_table'"
    cursor.execute(check_helptable_query)
    res = cursor.fetchone()

    if res is not None:
        pass
    else:
        create_helpTable_query = '''
        CREATE TABLE IF NOT EXISTS help_table (
        Command VARCHAR,
        Description VARCHAR
        )
        '''
        cursor.execute(create_helpTable_query)
        conn.commit()

        insert_command_query = "INSERT INTO help_table (Command, Description) VALUES ('help', 'Display a list of all available commands')"
        cursor.execute(insert_command_query)
        conn.commit()
        
        insert_command_query = "INSERT INTO help_table (Command, Description) VALUES ('lock', 'Lock a particular directory')"
        cursor.execute(insert_command_query)
        conn.commit()
        
        insert_command_query = "INSERT INTO help_table (Command, Description) VALUES ('unlock', 'Unlock a particular directory')"
        cursor.execute(insert_command_query)
        conn.commit()
        
        insert_command_query = "INSERT INTO help_table (Command, Description) VALUES ('show', 'Display a list of all locked directories')"
        cursor.execute(insert_command_query)
        conn.commit()

        insert_command_query = "INSERT INTO help_table (Command, Description) VALUES ('change passwd', 'Change password')"
        cursor.execute(insert_command_query)
        conn.commit()
    
        insert_command_query = "INSERT INTO help_table (Command, Description) VALUES ('exit', 'Exit the tool')"
        cursor.execute(insert_command_query)
        conn.commit()
    
    check_passwdtable_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='passwd_table'"
    cursor.execute(check_passwdtable_query)
    res2 = cursor.fetchone()

    if res2 is not None:
        pass
    else:
        create_passwdTable_query = '''
        CREATE TABLE IF NOT EXISTS passwd_table (
        Passwd_Hash VARCHAR
        )
        '''
        cursor.execute(create_passwdTable_query)
        conn.commit()

        print("\033[34mSet Password to Lock/Unlock Folders\033[0m\n")
        setPasswd()
    
    check_recoverytable_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='recovery_table'"
    cursor.execute(check_recoverytable_query)
    res3 = cursor.fetchone()

    if res3 is not None:
        pass
    else:
        create_recoveryTable_query = '''
        CREATE TABLE IF NOT EXISTS recovery_table (
        Recovery_Question VARCHAR,
        Recovery_Answer_Hash VARCHAR
        )
        '''
        cursor.execute(create_recoveryTable_query)
        conn.commit()
        setRecovery()


    conn.commit()
    cursor.close()
    conn.close()
