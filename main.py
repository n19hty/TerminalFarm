# This is the start to Terminal Farm in Python.
# The goal is to learn python better, but also to build a fun terminal game you can play.
# I would like it to be similar to stardew but with typing mechanics.

from datetime import datetime 
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

##Set up for the game

current_game_day = 1
menu_section = "  Main Game"


## Player Data
player_name = "Player 1"



## Inventory
player_coin = 0
amount_of_corn = 0



#Plant Data

#corn
corn_harvest_time = 3


#Set up the 4 plots 2x2

a1_planted = False
a1_seed = "none"
a1_watered = False
a1_time_planted = "xx:xx:xx"
a1_day_planted = 0

a2_planted = False
a2_seed = "none"
a2_watered = False
a2_time_planted = "xx:xx:xx"
a2_day_planted = 0

b1_planted = False
b1_seed = "none"
b1_watered = False
b1_time_planted = "xx:xx:xx"
b1_day_planted = 0


b2_planted = False
b2_seed = "none"
b2_watered = False
b2_time_planted = "xx:xx:xx"
b2_day_planted = 0


def configure_plot():
    pass

def plant_menu_printout_plot():
    clear_screen()
    menu_content = f"""
               ======================================
              |   Terminal Farm - Current Day: {current_game_day}     |
               ======================================
               {player_name}                   {menu_section}
               Coins: {player_coin}
                  🌽: {amount_of_corn}

                                             
                    1. Plot A1
                    2. Plot A2
                    3. Plot B1
                    4. Plot B2
                """
    
    user_input = int(input(menu_content))
    if user_input == 1:
        return int(user_input)
    elif user_input == 2:
        return int(user_input)
    elif user_input == 3:
        return int(user_input)
    elif user_input == 4:
        return int(user_input)
    else:
        return "Broken"

def plant():
     
    #ask the user which plot they would like to plant
    # plant_location = input("Where would you like to plant? Select a1, a2, b1, b2 : ")
    plant_location = plant_menu_printout_plot()
    print(plant_location)
    print(type(plant_location))
        
    global a1_planted
    global a1_seed
    global a1_time_planted
    global a1_day_planted
    global a2_planted
    global a2_seed
    global a2_time_planted
    global a2_day_planted
    global b1_planted
    global b1_seed
    global b1_time_planted
    global b1_day_planted
    global b2_planted
    global b2_seed
    global b2_time_planted
    global b2_day_planted

    # create the if choices here
    if plant_location == 1:
        print("Great you are planting in " + str(plant_location))
        now = datetime.now().strftime("%H:%M:%S")
        a1_planted = True
        a1_seed = "corn"
        a1_time_planted = now
        a1_day_planted = current_game_day
        
    elif plant_location == 2:
        print("Great you are planting in " + str(plant_location))
        now = datetime.now().strftime("%H:%M:%S")
        a2_planted = True
        a2_seed = "corn"
        a2_time_planted = now
        a2_day_planted = current_game_day

    elif plant_location == 3:
        print("Great you are planting in " + str(plant_location))
        now = datetime.now().strftime("%H:%M:%S")
        b1_planted = True
        b1_seed = "corn"
        b1_time_planted = now
        b1_day_planted = current_game_day
    
    elif plant_location == 4:
        print("Great you are planting in " + str(plant_location))
        now = datetime.now().strftime("%H:%M:%S")
        b2_planted = True
        b2_seed = "corn"
        b2_time_planted = now
        b2_day_planted = current_game_day
    
    else:
        print("You've entered something wrong please check your input and try again. (must be a1, a2, b1, or b2)")

def water():

    print("Currently watering all plots...")
    global a1_watered
    global a2_watered
    global b1_watered
    global b2_watered

    a1_watered = True
    a2_watered = True
    b1_watered = True
    b2_watered = True

def reset_plot(plot_id):
    pass

def harvest_plants():
    #check plot status
    #check a1 harvest status
    #global current_game_day
    global a1_day_planted
    global amount_of_corn
    global corn_harvest_time
    global a1_planted
    global a1_watered

    a1_harvest_status = current_game_day - a1_day_planted

    if a1_planted == True and a1_watered == True and a1_harvest_status >= corn_harvest_time:
        print("A1 is ready to be harvested.")
        print("Harvesting A1...")
        
        global a1_seed
        global a1_time_planted
        
        a1_planted = False
        a1_day_planted = None
        a1_watered = False
        a1_seed = None
        a1_time_planted = None

        amount_of_corn += 1

        time.sleep(1)
    else:
        print("This is broken.")
    pass

def sell_plants():
    pass

def print_plots():
    clear_screen()
    
    not_watered_icon = "🌵"
    watered_icon = "💧"
    dead_plant = "☠️"
    time_icon = "⏱️"
    day_icon = "🗓️"
    green_check_icon = "✅"
    red_cross_mark = "❌"
    prohibit_emoji = "🚫"



    layout_printout = f"""
              #======================================#
              #   Terminal Farm - Current Day: {current_game_day}     #
              #======================================#
               {player_name}                   {menu_section}
               Coins: {player_coin}
                  🌽: {amount_of_corn}

              ########################################
              #    A1 | {day_icon}:{a1_day_planted}      #    B1 | {day_icon}:{b1_day_planted}     #
              #                   #                  #
              # {watered_icon}:{green_check_icon}             # {watered_icon}:{green_check_icon}            #
              # {watered_icon}:{prohibit_emoji}             # {watered_icon}:{prohibit_emoji}            #
              # Type:{prohibit_emoji}           # Type:{prohibit_emoji}          #
              #                   #                  #
              ########################################
              #    A2 | {day_icon}:{a2_day_planted}      #    B2 | {day_icon}:{b2_day_planted}     #
              #                   #                  #
              # {watered_icon}:{green_check_icon}             # {watered_icon}:{green_check_icon}            #
              # {watered_icon}:{prohibit_emoji}             # {watered_icon}:{prohibit_emoji}            #
              # Type:{prohibit_emoji}           # Type:{prohibit_emoji}          #
              #                   #                  #
              ########################################
                              
                """
    
    print(layout_printout)

    time.sleep(10)

    
    # print("This is what the current plots look like: ")
    # print('🌽')
    # print("\n")
    # print("\n")
    # print("A1 Planted:", a1_planted, "A1 Day Planted:", a1_day_planted, "A1 Watered:", a1_watered, "A1 Time Planted:", a1_time_planted, "A1 Seed:", a1_seed)
    # print("A2 Planted:", a2_planted, "A2 Day Planted:", a2_day_planted, "A2 Watered:", a2_watered, "A2 Time Planted:", a2_time_planted, "A2 Seed:", a2_seed)
    # print("B1 Planted:", b1_planted, "B1 Day Planted:", b1_day_planted, "B1 Watered:", b1_watered, "B1 Time Planted:", b1_time_planted, "B1 Seed:", b1_seed)
    # print("B2 Planted:", b2_planted, "B2 Day Planted:", b2_day_planted, "B2 Watered:", b2_watered, "B2 Time Planted:", b2_time_planted, "B2 Seed:", b2_seed)

def end_day():
    global current_game_day
    current_game_day += 1

def menu_printout():
    menu_content = f"""
               ======================================
              |   Terminal Farm - Current Day: {current_game_day}     |
               ======================================
               {player_name}                   {menu_section}
               Coins: {player_coin}
                  🌽: {amount_of_corn}

                                             
                    1.Plant seed
                    2.Water Plot
                    3.Print Plots
                    4.Harvest Plants
                    5.Sell Plants
                    6.End Day - Adds +1 to current day
                    7.Exit/Quit
              """
    print(menu_content)

def main():
    
    
    ans=True
    
    while ans:
        clear_screen()
        menu_printout()
        #print(menu_printout)
            
        default_sleep_time = 0.5
        
        ans = input("What would you like to do? ")

        if ans == "1":

            print("\nPlanting Seeds...")
            plant()
            time.sleep(default_sleep_time)
        
        elif ans == "2":
           
           print("\nWatering plants...")
           water()
           time.sleep(default_sleep_time)
        
        elif ans == "3":
           
           print("\nPrinting Plots...")
           print_plots()
           time.sleep(default_sleep_time)           
        
        elif ans == "4":
           
           print("\nTrying to Harvesting Crops...")
           harvest_plants()
           time.sleep(default_sleep_time)
        
        elif ans == "5":
           
           print("\nSelling Plants...")
           sell_plants()
           time.sleep(default_sleep_time)

        elif ans == "6":
           
           print("\nEnding the day...")
           end_day()
           print("The current day is now: ", current_game_day)
           time.sleep(default_sleep_time)
        
        elif ans == "7":
           
           print(f'\nGoodbye, {player_name}!\n\n')
           time.sleep(1)
           exit()

        elif ans != "":
            print("\n Not Valid Choice Try again")

main()
