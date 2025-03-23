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
    
    mins_per_workout= 0
    
    DOTW = {
        "Monday":False,
        "Tuesday":False,
        "Wednesday":False,
        "Thursday":False,
        "Friday":False,
        "Saturday":False,
        "Sunday":False,
    }

     print("Workouts are best between 30 minutes and 2 hours! Any less and its hard to get enough volume of training to make gains, any higher and most people are too tired by the end for any of the last excersizes to count. If you're unsure where to start, try 1 hour and see how it goes :)")

    while True:
        mins_per_workout=input("How many minutes would you like your workouts to be? (30-120) ")
            if not isinstance(mins_per_workout,int):
                print("Error, Please only enter a number")
            
            if mins_per_workout < 15:
                print("")


    for day in DOTW:
        if(input(f"\nWould you like to work out on "+ day+"?")).lower()[0]=='y':
            DOTW[day]= True
            print(day+" Has been added as a workout day!")
                

main()


