import warnings

warnings.filterwarnings("ignore")
def showName():
    devName = """
     _______        _     _____             _ _   _______          _         
    | __   __|      | |   |  __ \           (_) | |__   __|        | |      _ 
        | | ___  ___| |__ | |  | | _____   ___| |    | | ___   ___ | |___  (_)
        | |/ _ \/ __| '_ \| |  | |/ _ \ \ / / | |    | |/ _ \ / _ \| / __|    
        | |  __/ (__| | | | |__| |  __/\ V /| | |    | | (_) | (_) | \__ \  _ 
        |_|\___|\___|_| |_|_____/ \___| \_/ |_|_|    |_|\___/ \___/|_|___/ (_)                                                                                                                                               

    """

    toolName = """
  ______    _     _           _____                           
 |  ____|  | |   | |         / ____|                          
 | |__ ___ | | __| | ___ _ _| (___   ___  ___ _   _ _ __ __ _ 
 |  __/ _ \| |/ _` |/ _ \ '__\___ \ / _ \/ __| | | | '__/ _` |
 | | | (_) | | (_| |  __/ |  ____) |  __/ (__| |_| | | | (_| |
 |_|  \___/|_|\__,_|\___|_| |_____/ \___|\___|\__,_|_|  \__,_|
                                                                                                                                                                           
    """

    print(f"\033[91m{devName}\033[0m")
    print(f"\033[34m{toolName}\033[0m")