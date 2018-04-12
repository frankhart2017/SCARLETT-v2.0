def help_com():
    print("\nType 'all' for accessing all commands, for help on specific command enter hc/command_name\n")
    
def all_com():
    print("\nscan -> To scan particular defined locations")
    print("bye -> Bid me farewell")
    print("whost -> Open web hosting package")
    print("pma -> Open php myadmin")
    print("xampp -> Start apache and mysql on xampp")
    print("repo -> To create a github repository")
    print("who -> To know about scarlett")
    print("Type hc/command_name to get more info on that\n")

def hc(command):
    if(command == "scan"):
        print("\nLocations available:")
        print("1) desktop")
        print("2) downloads")
        print("3) entertainment")
        print("4) work")
        print("All the above mentioned entries are case-sensitive\n")
        
    else:
        print("\n******No further help on this******\n")
