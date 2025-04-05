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
        
    # Recursive algorithm creates all sensical splits 
    else:
       calcsplit(splits_arr,week_arr,0,days_per_week,0,ppl)
    
    
    print(str(len(splits_arr))+" splits were successfully generated, here are my reccomendations:")
    
    splitgrader(splits_arr)



######################################################################################                                                                             
# ,-----.   ,---.   ,--.     ,-----.  ,---.   ,------.  ,--.    ,--. ,--------.     #
#'  .--./  /  O  \  |  |    '  .--./ '   .-'  |  .--. ' |  |    |  | '--.  .--'     # 
#|  |     |  .-.  | |  |    |  |     `.  `-.  |  '--' | |  |    |  |    |  |        # 
#'  '--'\ |  | |  | |  '--. '  '--'\ .-'    | |  | --'  |  '--. |  |    |  |        #
# `-----' `--' `--' `-----'  `-----' `-----'  `--'      `-----' `--'    `--'        #
######################################################################################                                                                                    

############################################################################################################################################################################################################################
#this should spit out an array of potential weeks (also arrays) to be evaluated    
def calcsplit(splits_arr,week,position,days_per_week,days_so_far,ppl):
    new_week=[]
    yesterday= 6 if position-1==-1 else position-1 # we do this to avoid index out of bound from first check
    today=position
    tomorrow= 0 if position==6 else position+1 #we do this so that we do not get index out of bounds error, and the last day of the week refers to the first day of the next week for tomorrow.


    #Case where we have completed the amount of days that we are training, cut recursion short
    if days_per_week == days_so_far:
        splits_arr.append(week)
    
        

    elif week[today]==False:
        new_week=week.copy()
        calcsplit(splits_arr,new_week,position+1,days_per_week,days_so_far,ppl)
    
    #from here in out its all true working days
    else: 
        upper=True
        lower=True
        full=True
        push=ppl
        pull=ppl

        if week[tomorrow]!= False:
            full=False

        if week[tomorrow]=="full":
            return

        if week[yesterday]=="upper" or week[tomorrow]=="upper": # the we check tomorrow as well to catch sunday/monday
            upper=False
            push=False
            pull=False
            full=False

        if week[yesterday]=="lower"or week[tomorrow]=="lower":
            lower=False
            full=False
        
        if week[yesterday]=="push" or week[tomorrow]=="push":
            upper=False
            push=False
            full=False
        if week[yesterday] == "pull" or week[tomorrow]=="pull":
            upper=False
            pull=False
            full=False


    #Below handles recursive calling
        if upper:
            new_week=week.copy() #we copy in a new week instead of just using week because week is A REFERENCE TO THE WEEK ARRAY, using copy segments out some new memory for a new week 
            new_week[today]="upper"
            calcsplit(splits_arr,new_week,position+1,days_per_week,days_so_far+1,ppl)

        if lower:
            new_week=week.copy() #we copy in a new week instead of just using week because week is A REFERENCE TO THE WEEK ARRAY, using copy segments out some new memory for a new week 
            new_week[today]="lower"
            calcsplit(splits_arr,new_week,position+1,days_per_week,days_so_far+1,ppl)
        if push:
            new_week=week.copy() #we copy in a new week instead of just using week because week is A REFERENCE TO THE WEEK ARRAY, using copy segments out some new memory for a new week 
            new_week[today]="push"
            calcsplit(splits_arr,new_week,position+1,days_per_week,days_so_far+1,ppl)
        if pull:
            new_week=week.copy() #we copy in a new week instead of just using week because week is A REFERENCE TO THE WEEK ARRAY, using copy segments out some new memory for a new week 
            new_week[today]="pull"
            calcsplit(splits_arr,new_week,position+1,days_per_week,days_so_far+1,ppl)     
        if full:
            new_week=week.copy() #we copy in a new week instead of just using week because week is A REFERENCE TO THE WEEK ARRAY, using copy segments out some new memory for a new week 
            new_week[today]="full"
            calcsplit(splits_arr,new_week,position+1,days_per_week,days_so_far+1,ppl)      


    
#############################################################################################################################################################################################
#  ________     _______    ___         __      ___________        _______     _______         __       ________     _______    _______   
# /"       )   |   __ "\  |"  |       |" \    ("     _   ")      /" _   "|   /"      \       /""\     |"      "\   /"     "|  /"      \  
#(:   \___/    (. |__) :) ||  |       ||  |    )__/  \\__/      (: ( \___)  |:        |     /    \    (.  ___  :) (: ______) |:        | 
# \___  \      |:  ____/  |:  |       |:  |       \\_ /          \/ \       |_____/   )    /' /\  \   |: \   ) ||  \/    |   |_____/   ) 
#  __/  \\     (|  /       \  |___    |.  |       |.  |          //  \ ___   //      /    //  __'  \  (| (___\ ||  // ___)_   //      /  
# /" \   :)   /|__/ \     ( \_|:  \   /\  |\      \:  |         (:   _(  _| |:  __   \   /   /  \\  \ |:       :) (:      "| |:  __   \  
#(_______/   (_______)     \_______) (__\_|_)      \__|          \_______)  |__|  \___) (___/    \___)(________/   \_______) |__|  \___) 
######################## ###  ############################################################################################################################################################################################                                                                                                                                               
def splitgrader(splits_arr):
    #runner variables are so user can have a look at the next best options if they didnt like the first one
    
    best_upper= {"split":[],"upper_score":0,"upper_freq":0,"lower_score":0,"lower_freq":0}
    runner_upper= {"split":[],"upper_score":0,"upper_freq":0,"lower_score":0,"lower_freq":0}
    best_balanced= {"split":[],"balance_score":100,"freq_balance":0}
    runner_balanced= {"split":[],"balance_score":100,"freq_balance":0}
    best_lower = {"split":[],"upper_score":0,"lower_score":0,"upper_freq":0,"lower_freq":0}
    runner_lower = {"split":[],"upper_score":0,"lower_score":0,"upper_freq":0,"lower_freq":0}


   
    for split in splits_arr:
        
        push=0
        pull=0
        lower=0
        upper_freq=0
        lower_freq=0
        
        for day in split: #score the split 
            if day == 'full':
                push+=1
                pull+=1
                lower+=2
                upper_freq+=1
                lower_freq+=1
            elif day=='upper':
                push+=2
                pull+=2
                upper_freq+=1
            elif day == 'lower':
                lower+=4
                lower_freq+=1
            elif day == 'push':
                push+=4
                upper_freq+=11
            elif day == 'pull':
                pull+=4
                upper_freq+=1
            
        upper=push+pull
        total=upper+lower
        
        if push==0 or pull ==0 or lower== 0: #anything with no volume for a muscle is not gonna fly
            continue
        if upper>=lower*2 or upper*2<=lower: #too unbalanced
            continue
        
       
        
        #we calculate a volume score to be the primary consideration for the splits, upper and lower take absolute volume and balanced takes the difference in volumes
        if upper > best_upper["upper_score"] or (upper == best_upper["upper_score"] and lower > best_upper["lower_score"]): #prioritizes having the highest score for upper, then having lower secondarily
            runner_upper=best_upper.copy() 
            best_upper["split"]=split
            best_upper["upper_score"] = upper
            best_upper["lower_score"] = lower
            best_upper["upper_freq"] = upper_freq 
            best_upper["lower_freq"] = lower_freq 
            
        elif upper == best_upper["upper_score"]: #if the volume is the same as the best split so far, we instead compare the frequency, which seems to have some level of effect
            if upper_freq > best_upper["upper_freq"]:
                runner_upper=best_upper.copy() 
                best_upper["split"]=split
                best_upper["upper_score"] = upper
                best_upper["lower_score"] = lower
                best_upper["upper_freq"] = upper_freq 
                best_upper["lower_freq"] = lower_freq
            elif upper_freq==best_upper["upper_freq"] and lower_freq>best_upper["lower_freq"]:
                runner_upper=best_upper.copy() 
                best_upper["split"]=split
                best_upper["upper_score"] = upper
                best_upper["lower_score"] = lower
                best_upper["upper_freq"] = upper_freq 
                best_upper["lower_freq"] = lower_freq

        volume_balance = max(push,pull,lower)-min(push,pull,lower)
        freq_balance= max(upper_freq,lower_freq) - min(upper_freq,lower_freq)
        
        if volume_balance< best_balanced["balance_score"]:
            runner_balanced= best_balanced.copy()
            best_balanced["split"] = split
            best_balanced["balance_score"] = volume_balance
            best_balanced["freq_balance"] = freq_balance
        #secondarily,optimise for frequency
        elif volume_balance == best_balanced["balance_score"] and freq_balance < best_balanced["freq_balance"]:
            runner_balanced= best_balanced.copy()
            best_balanced["split"] = split
            best_balanced["balance_score"] = volume_balance
            best_balanced["freq_balance"] = freq_balance
        
            
        if lower > best_lower["lower_score"] or (lower == best_lower["lower_score"] and push+pull > best_lower["lower_score"]):#prioritizes ahving the highest score for lower, then upper secondarily
            runner_lower=best_lower.copy() 
            best_lower["split"] = split
            best_lower["upper_score"] = upper
            best_lower["lower_score"] = lower
            best_lower["upper_freq"] = upper_freq 
            best_lower["lower_freq"] = lower_freq
            
        elif lower ==best_lower["lower_score"]: #if the volume is the same as the best split so far, we instead compare the frequency, which seems to have some level of effect
            if lower_freq >best_lower["lower_freq"]:
               runner_lower=best_lower.copy()
               best_lower["split"]=split
               best_lower["upper_score"] = upper
               best_lower["lower_score"] = lower
               best_lower["upper_freq"] = upper_freq 
               best_lower["lower_freq"] = lower_freq
            #if lower frequency already as good as the best, then optimise for upper 
            elif lower_freq==best_lower["lower_freq"] and upper_freq>best_lower["upper_freq"]:
               runner_lower=best_lower.copy()
               best_lower["split"]=split
               best_lower["upper_score"] = upper
               best_lower["lower_score"] = lower
               best_lower["upper_freq"] = upper_freq 
               best_lower["lower_freq"] = lower_freq
        
    print("The best lower split is "+ str(best_lower["split"]))
    print("The 2nd best lower split is "+ str(runner_lower["split"]))
    
    print("The best balanced split is "+ str(best_balanced["split"]))
    print("The 2nd best balanced split is "+ str(runner_balanced["split"]))

    
    print("The best upper split is "+ str(best_upper["split"]))
    print("The 2nd best upper split is "+ str(runner_upper["split"]))
    
    return 
###############################################################################################################################################
#  _____ _   _  _____ ______  _____ _______   __ 
# |_   _| \ | |/ ____|  ____|/ ____|__   __| /_ |
#   | | |  \| | |  __| |__  | (___    | |     | |
#   | | | . ` | | |_ |  __|  \___ \   | |     | |
#  _| |_| |\  | |__| | |____ ____) |  | |     | |
# |_____|_| \_|\_____|______|_____/   |_|     |_|
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



