import DatabaseOperations as dbops
import asciiArt
import commands as com
import cameraOperations as camops
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Class for Custom Exceptions
class CustomException(Exception):
    pass

asciiArt.showName() # Intro Logo
print("\n\033[33mType 'help' to get a list and description of commands\033[0m")
print("\033[33mCaptured Images are stored in C:/FolLockCaptured\033[0m\n")
dbops.startDB() # Start Database and perform basic DB operations for Smooth functioning

authCount = 0 # Number of times user entered incorrect credentials

run = False # Keep the tool running

while authCount <= 3:
    auth = dbops.authenticate() # Prompt user for Password; Returns True if credentials are correct, else returns False
    if auth == True:
        print("\n\033[32mWelcome!! Authentication Successful!\033[0m\n")
        run = True
        break
    else:
        authCount += 1
        print("\033[31mAuthentication Failed! Incorrect Password\033[0m\n")
        run = False
        if authCount >= 3:
            camops.capture()
            break

while run:
    # Define max input length to prevent overflow
    max_command_length = 20
    max_path_length = 32766

    try:
        print("\n\033[33mType 'help' to get a list and description of commands\033[0m")
        command = str(input("\nEnter a command: "))
        if len(command) > max_command_length:
            raise CustomException("Input is too long! Please refer the docs to enter a valid command")
        
        else:
            if command == "exit":
                run = False
            else:
                com.executeCommand(command)

    except CustomException as e:
        print("\033[31mError Occured: \033[0m", str(e))
