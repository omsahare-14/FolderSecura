import DatabaseOperations as dbops
import FolderOperations as folops

# TODO Add the list of dirs in lock dirs database

def executeCommand(com):
    if com == "help": # DONE
        dbops.showHelp()
    
    elif com == "lock": # DONE
        folops.hideFolder()
    
    elif com == "unlock": # DONE
        folops.unhideFolder()
    
    elif com == "show": # DONE
        dbops.showLockedDirs()
    
    elif com == "change passwd": # DONE
        dbops.forgotPasswd()
    
    else:
        print("Invalid Command")