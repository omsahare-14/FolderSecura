import win32api
import win32con
import DatabaseOperations as dbops
import sqlite3

def hideFolder():
    folder_path = str(input("Enter the Directory to Lock: "))
    new_path = folder_path.replace('\\', '/')
    try:
        # Set the folder attribute to hidden
        attributes = win32api.GetFileAttributes(new_path)
        win32api.SetFileAttributes(new_path, attributes | win32con.FILE_ATTRIBUTE_HIDDEN)

        conn = sqlite3.connect('dirs.db')
        cursor = conn.cursor()
        insert_query = "INSERT INTO locked_directories (Locked_Directories) VALUES (?)"
        cursor.execute(insert_query, (new_path,))
        conn.commit()
        cursor.close()
        conn.close()


        print(f"Folder hidden: {new_path}\n")
    except Exception as e:
        print(f"Error hiding folder: {e}")


def unhideFolder():
    folder_path = input("Enter the Directory to Unlock: ")
    new_path = folder_path.replace('\\', '/')
    try:
        # Get the current attributes of the folder
        attributes = win32api.GetFileAttributes(new_path)

        # Remove the hidden attribute from the attributes
        attributes &= ~2

        # Set the new attributes for the folder
        win32api.SetFileAttributes(new_path, attributes)

        conn = sqlite3.connect('dirs.db')
        cursor = conn.cursor()
        delete_query = f"DELETE FROM locked_directories WHERE Locked_Directories = ?"
        cursor.execute(delete_query, (new_path,))
        conn.commit()
        cursor.close()
        conn.close()

        print(f"Folder unhidden: {new_path}\n")

    except Exception as e:
        print(f"Error unhide folder: {e}")