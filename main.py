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
    #Constrains workout times
    MIN_MINUTES =15
    MAX_COMFY_MINUTES = 120 #user will get an warning if exceeding this
    MAX_MINUTES = 180
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
        
        try:
            mins_per_workout = int(mins_per_workout)
        except ValueError:
            print("Error, Please only enter whole numbers")
            continue
        
        int(mins_per_workout)
        #can be done, not super worth it, this value may change
        if mins_per_workout <  MIN_MINUTES:
            print("Workouts below fifteen minutes are near impossible, please at least allow for 15 minutes")
            continue
        
        #over 120mins of workout is not likely to be beneficial to anyone due to the idea of junk volume
        elif mins_per_workout >  MAX_COMFY_MINUTES:
            print("Whilst workouts above two hours can prove beneficial in some cases, please note that they are highly overkill and the last parts of the workout tend not to be very effective")
            if(input("Type 'Y' if you are happy to proceed anyway, or type anything else to go back and add a different number").lower()=='y'):
                break
            else:
                continue
        
        #We prevent over three hour workouts as to not brick the algorithm probably
        elif mins_per_workout > MAX_MINUTES:
            print("Sorry, I cant do workouts over three hours")
        
        #exit condition
        break
        
    print("Fantastic, " +str(mins_per_workout)+" minutes it is!")
    for day in DOTW:
        if(input(f"\nWould you like to work out on "+ day+"?")).lower()[0]=='y':
            DOTW[day]= True 
            print(day+" Has been added as a workout day!")
                

main()



