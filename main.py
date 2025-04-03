import shutil

POSITVE_INDICATORS=["yes","y","yeah","ye","yep","confirm",]

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

    #loops until confirmed
    while True:
        availability_ingest  = collect_availability()
        dotw= availability_ingest[0]     #a dictionary with keys monday-friday with true or false as values
        mins_per_workout=availability_ingest[1]
        days_per_week = availability_ingest[2]

        working_days = " ,".join([day for day, value in dotw.items() if value])
       
        
        if input("So you want to work out on "+working_days + " for "+str(mins_per_workout)+ "minutes? [Y/N]").lower() in POSITVE_INDICATORS:
            break
            
    #Splits
    # this section should end up with a 
    #Full body is always an option
    # Upper/ lower needs 2 days, and will always be allowed 
    week_arr=list(dotw.values())
    ppl = True if days_per_week > 3 else False
    splits_arr= []
    #When only 1 day per week, in order to have full body frequency we need to be upper body
    if days_per_week == 1:
        for key,value in dotw.items(): 
            if value == True:
                dotw[key]='full'
        splits_arr.append([dotw])
    # All other cases covered by cursed as fuck algorithm 
    else:
        #this fucked up recursive algorithm for algorithm design
        
        splits_arr=calcsplit(splits_arr,week_arr,0,days_per_week,0,ppl)
    
    for split in splits_arr:
        print("Monday:" + str(split[0]))
        print("Tuesday:" + str(split[1]))
        print("Wednesday:" + str(split[2]))
        print("Thursday:" + str(split[3]))
        print("Friday:" + str(split[4]))
        print("Saturday:" + str(split[5]))
        print("Sunday:" + str(split[6]))




############################################################################################################################################################################################################################
#this should spit out an array of potential weeks (also arrays) to be evaluated    
def calcsplit(splits_arr,week,position,days_per_week,days_so_far,ppl):

    yesterday= 6 if position-1==-1 else position-1 # we do this to avoid index out of bound from first check
    today=position
    tomorrow= 0 if position+1==6 else position+1 #we do this so that we do not get index out of bounds error, and the last day of the week refers to the first day of the next week for tomorrow.


    #Case where we have completed the amount of days that we are training, cut recursion short
    if days_per_week == days_so_far:
        return splits_arr.append(week)



    if week[today]==False:
            return calcsplit(splits_arr,week,position+1,days_per_week,days_so_far,ppl)
    
    
    
    else: #True from here on out
        #Not training today or tomorrow = anything
        match week[yesterday]:
            case False: #No training yesterday, today could be anything
                
                #Upper/lower will always been an option
                week[today]="upper"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
                week[today]="lower"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
                
                #Full body will only be an option if not training tomorrow
                if week[tomorrow] == False:
                    
                    week[today]="full"
                    splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                    
                    
                #ppl is an option if enough days in the week support it
                if ppl:

                    week[today]="push"
                    splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                    
                    week[today]="pull"
                    splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                    
            case "upper":
                
                #Only lower can occur
                week[today]="lower"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
            
            case "lower":
                #upper, push or pull can occur
                
                week[today]="upper"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
                if ppl:
                    week[today]="push"
                    splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                        
                    week[today]="pull"
                    splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
            
            case "push":
                #only pull or lower can occur
                
                week[today]="pull"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
                week[today]="lower"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
            case "pull":
                #only push or lower can occur
                
                week[today]="pull"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
                week[today]="lower"
                splits_arr.extend(calcsplit(splits_arr,week,position+1,days_per_week,days_so_far+1,ppl))
                
            case "full":
                print("You fucked up, I found yesterday as 'full' fucking idiot")
            
            case _:
                print("Error, default case reached in calcsplit, yesterday was"+str(week[yesterday]))
                
            
        return splits_arr
                
        
    
        
    


    

    

############################################################################################################################################################################################
# Returns an array
       #return[0] = DOTW dictionary
       #return[1] = minutes/workout
       #return[2] = days per week working out
def collect_availability():
    #Constrains workout times
    MIN_MINUTES =15
    MAX_COMFY_MINUTES = 120 #user will get an warning if exceeding this
    MAX_MINUTES = 180
    mins_per_workout= 0
    days_per_week = 0
    
    
    
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
    while True:
        for day in DOTW:
            if(input(f"\nWould you like to work out on "+ day+"?")).lower()[0]=='y':
                DOTW[day]= True 
                print(day+" Has been added as a workout day!")
                days_per_week+=1
        
        if days_per_week==0: #Catching case where they say no to every day
            print("Error, you must work out for at least one day")
        else:
            break


    return [DOTW,mins_per_workout,days_per_week]

main()



