import DatabaseOperations as dbops
import asciiArt
import commands as com
import cameraOperations as camops

# Class for Custom Exceptions
class CustomException(Exception):
    pass

asciiArt.showName() # Intro Logo
print("\nType 'help' to get a list and description of commands")
print("Captured Images are stored in C:/FolLockCaptured\n")
dbops.startDB() # Start Database and perform basic DB operations for Smooth functioning

authCount = 0 # Number of times user entered incorrect credentials

run = False # Keep the tool running

while authCount <= 3:
    auth = dbops.authenticate() # Prompt user for Password; Returns True if credentials are correct, else returns False
    if auth == True:
        print("\nWelcome!! Authentication Successful!\n")
        run = True
        break
    else:
        authCount += 1
        print("Authentication Failed! Incorrect Password\n")
        run = False
        if authCount >= 3:
            camops.capture()
            break

while run:
    # Define max input length to prevent overflow
    max_command_length = 20
    max_path_length = 32766

    try:
        print("\nType 'help' to get a list and description of commands")
        command = str(input("\nEnter a command: "))
        if len(command) > max_command_length:
            raise CustomException("Input is too long! Please refer the docs to enter a valid command")
        
        else:
            if command == "exit":
                run = False
            else:
                com.executeCommand(command)

    except CustomException as e:
        print("Error Occured: ", str(e))
