import shutil


def main():
    #Find the character width of CLI so that title banner is correct size
    terminal_width = shutil.get_terminal_size().columns
    
    print("*" * terminal_width)
    print(r"""*
*  _____________.___.  _____ __________    ________________  
* /  _____/\__  |   | /     \\______   \  /  _  \__    ___/ 
*/   \  ___ /   |   |/  \ /  \|       _/ /  /_\  \|    |    
*\    \_\  \\____   /    Y    \    |   \/    |    \    |    
* \______  // ______\____|__  /____|_  /\____|__  /____|    
*        \/ \/              \/       \/         \/          
""")
    print("*" * terminal_width)
    
    1

    print("Welcome to GymRat v0.1! This program is a backend proof of concept for an app for hypertrophy style gym planning and training which gamifies the process by making your digital rat friend get swole!. This verison has no such GUI or capability, and is more of a practice excersize for the developer, Benjamin Roseby.\n")
    print("Please press the corresponding number in order to get started:")
    print("1. Create a new workout plan.")
    
    match input("Your selection: "):
        case "1":
            new_workout()

def new_workout():
    
    days_per_week=input("Which days per week would you like to train?")
        while True:
            print("Please enter the days per week you would like to train, enter the letter C when done")
            day_selection=input("")

main()


