import DatabaseOperations as dbops
import FolderOperations as folops
import warnings

warnings.filterwarnings("ignore")

def executeCommand(com):
    if com == "help":
        dbops.showHelp()
    
    elif com == "lock":
        folops.hideFolder()
    
    elif com == "unlock":
        folops.unhideFolder()
    
    elif com == "show":
        dbops.showLockedDirs()
    
    elif com == "change passwd":
        dbops.forgotPasswd()
    
    else:
        print("\033[91mInvalid Command\033[0m")