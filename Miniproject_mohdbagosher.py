""" written by Muhammad Bagosher M00977907
mini project 1
This program is about a computer configuration support system, it presents the user with a variety of
computer components alongside some helpful tips, it also provides the user with extra information
and explanations about some of the important component to help the user learn about the benifits of their 
choices as well as help them decide their computer specifications.
by the end of the program the user will be presented with a full breakdown of their configured
computer as well as the estimated price.
the program also reacts to the users familiarity with computers, and adapts accordingly to provide
the best user experience based on their level(beginner or intermediate)
-in beginner the system asks the user a few questions then automatically finds the best specification based on the users answers
-in intermediate the system allows the user to chose a few of the components then fills the rest of the specifications based on the users answers
"""
from specs_configurator import *
from beginner_functions import *



#End of variable and functions setup
    
"""the programe code starts HERE"""

answer = "y" #Sets answer to y to run the program for the first time, this variable will be used to enable the user to restart the program
while(answer == "Y" or answer == "y"): #starts a loop which only runs if the answer of the user is equal to Y/y, the user will be asked at the end of the program if they want to restart the program
    print("Hello and welcome to the smart computer configurator!! please type in your name to start the experience!")
    user_name = input("Name: ")#asks for user name and saves it in a variable
    x = True #we start by setting a random variable to TRUE which will be used in the loop to prevent crash in case of wrong input
    while x: #starts a loop to prevent crash in case of wrong user input for computer knowledge
        user_level = eval(input(f'Hey {user_name}!! how would you rate your computer knowledge?\ntype 1 for beginner, 2 for intermediate: '))#this line asks for the user level to determine the type of experience to provide, it also uses the user_name variable inside the input
        if (user_level == 1):# if the user chooses level 1 which is the beginner level the below code will start running
            print("You have chosen the beginner level, as such we will provide as much support as possible to help you configure your computer")
            print("First lets put a budget, how much are you willing to spend? \nchoose from the following list(prices are in dollars):",prices)#the line presents the available price points by calling out the prices list
            while x:#starts a second loop to prevent crash in case of wrong user input for price range
                try: #first step of the loop that tries if the input is correct
                    price_range = int(input("--->"))#asks the user to choose from the list and stores it in a variable, this variable is very imporant because it will be used in all functions   
                    tier = tier_function(price_range)#calls the tier function which will determine the specs based on the price, it was called inside the loop to check for wrong input
                except: #end of Price range loop, if the input was wrong then the print function below will execute
                    print("you have made an invalid choice, try again")
                    continue#repeats the function to give the user another attempt
                while x:#starts a loop for use case
                    print("Your budget is",price_range, "dollars, next tell us about your desired use for the computer, do you want it for gaming or professional work?")
                    user_usecase = input("type G or g for gaming , or P or p for professional work: ")# asks for use case, it accepts upper and lower case g and p and rejects anything else, this value is stored in a variable called user_usecase
                    
                    if (user_usecase == "G" or user_usecase == "g"):#if the user choses gaming, the function pc_specs_g will be called which uses the tier variable to determine the specs
                        pc_specs_g(tier)
                        print("these are the current recomended specs to match your budget, the total price is around", price_range, "dollars")

                        x = False # the variable x is now set to False to break the loop
                    elif (user_usecase == "P" or user_usecase == "p"):#if the user choses professional work, the function pc_specs_p will be called which uses the tier variable to determine the specs
                        pc_specs_p(tier) 
                        print("these are the current recomended specs to match your budget, the total price is around", price_range, "dollars")
         
                        x = False # the variable x is now set to False to break the loop
                    else:#end of use case loop which allows for another attempt
                        print("\nyou have made an invalid choice, try again!!\n")
                                    
            
    #next is the intermediate level, in this stage the user is able to chose some of the components and will be given a brief explanation to help them as well, the rest of the components will be chosen automatically by the program to match their PC            
        elif (user_level == 2):
            
            intermediate_pc = []#this is the list in which the intermediate pc specification choices will be stored
            while x:#loop to prevent crash in case of wrong user input
                print("you have chosen the intermediate level experience, in this level you will be given a few of the components to choose from and provided with a short explanation")
                print("First lets put a budget, how much are you willing to spend? \nchoose from the following list(prices are in dollars):",prices)
                try:#first step of the loop that tries if the input is correct
                    price_range = int(input("--->"))#the user choosses from the list then inputs the value
                    tier = tier_function(price_range)#call out the tier function to determine the level of specs for the computer, it was called inside the loop to check for wrong input
                except:#if the input is not correct the user will be given another chance
                    print("you have made an invalid choice, try again")
                    continue#repeats the function to give the user another attempt
                #if the input was correct the loop will break and the code below will start running
                print("Your budget is",price_range, "dollars")#uses the price_range variable inputed by the user to present the budget
                #first the user is given all the availabe cpus in their chosen price range
                while x:#loop to prevent crash in case of wrong input
                    print("the CPUs available at your price range are:\n",cpu[tier],"\n",cpu[tier+1],"\ntype 1 for",cpu[tier],"and 2 for",cpu[tier+1])
                    user_choice1 = int(input("--->"))#the user choice for CPU will be stored here
                    if user_choice1 == 1 or user_choice1 == 2:#first step of the loop which only runs the code if the input is 1 or 2
                        pc_part = cpu[(user_choice1 + tier -1)]#a new variable called PC_part will store the users chosen component by taking the user_choice value + the tier value -1, the reason there is -1 becuse lists index in python start at 0 instead of 1
                        intermediate_pc .insert( 0 , pc_part)#the pc_part chosen by the user will now be added to the intermediate_pc list started previously, the cpu will be inserted at index 0
                        print("you have chosen",intermediate_pc)#prints out the chosen parts so far
                        break#breaks the loop to continue to the next part
                    else:
                        print("\nyou have made an invalid choice, try again!!\n")#if wrong value is inputed the user will be asked to try again
                #next the user can chose the gpu
                while x:#loop to prevent crash in case of wrong input
                    print("the GPUs available at your price range are:\n",gpu[tier],"\n",gpu[tier +1],"\ntype 1 for",gpu[tier],"and 2 for",gpu[tier +1])
                    user_choice2 = int(input("--->"))#the user choice for GPU will be stored here
                    if user_choice2 == 1 or user_choice2 == 2:#first step of the loop which only runs the code if the input is 1 or 2
                        pc_part = gpu[(user_choice2 + tier -1)]#a new variable called PC_part will store the users chosen component by taking the user_choice value + the tier value -1, the reason there is -1 becuse lists index in python start at 0 instead of 1
                        intermediate_pc .insert( 1 , pc_part)#the pc_part chosen by the user will now be added to the intermediate_pc list started previously, the GPU will be inserted at index 1
                        print("you have chosen",intermediate_pc)#prints out the chosen parts so far
                        break#breaks the loop to continue to the next part
                    else:
                        print("\nyou have made an invalid choice, try again!!\n")

                #finally the user can choose the amount of ram they want
                while x:#loop to prevent crash in case of wrong input
                    print("the ram available at your price range are:\n",ram[tier],"\n",ram[tier +1],"\ntype 1 for",ram[tier],"and 2 for",ram[tier +1])
                    user_choice3 = int(input("--->"))
                    if user_choice3 == 1 or user_choice3 == 2:#first step of the loop which only runs the code if the input is 1 or 2
                        pc_part = ram[(user_choice3 + tier -1)]#a new variable called PC_part will store the users chosen component by taking the user_choice value + the tier value -1, the reason there is -1 becuse lists index in python start at 0 instead of 1
                        intermediate_pc .insert( 2 , pc_part)#the pc_part chosen by the user will now be added to the intermediate_pc list started previously, the cpu will be inserted at index 2
                        print("you have chosen",intermediate_pc)#prints out the chosen parts so far
                        x = False # the variable x is now set to False to end the loop and move to the next value
                    else:
                        print("\nyou have made an invalid choice, try again!!\n")#if wrong value is inputed the user will be asked to try again

                #the program will now choose the remaining parts to complete the build, it picks values from the lists called in the beginning of the program
                intermediate_pc .extend([motherboard[tier],cpu_cooling[tier],storage[tier],psu[tier]])#extends the intermediate pc list with values from the other lists
                print("the appropriate specs based on your budget and the components picked are:")
                print("CPU: " + cpu[(user_choice1 + tier -1)],"GPU: " + gpu[(user_choice2+tier-1)],"RAM: " + ram[(user_choice3+tier-1)],"Motherboard: " + motherboard[tier],"CPU cooling: " + cpu_cooling[tier],"storage: " + storage[tier],"PSU: " + psu[tier],sep='\n')
                print("the total price is around", price_range, "dollars")
                break#breaks the loop and ends the program
        else:
            print("\nyou have made an invalid choice, try again\n") 
    answer = input("do you want to repeat the experience? typeY/y: ")#End of first while loop and the end of the program, it asks the user if they want to restart, else if will end the program

