# This is the start to Terminal Farm in Python.
# The goal is to learn python better, but also to build a fun terminal game you can play.
# I would like it to be similar to stardew but with typing mechanics.

from datetime import datetime 
import time
#Set up for the game
player_name = "Player 1"

current_game_day = 0
menu_section = "menu_section"
#Set up the 4 plots 2x2

a1_planted = False
a1_seed = "none"
a1_time_planted = "xx:xx:xx"
a1_day_planted = 0

a2_planted = False
a2_seed = "none"
a2_time_planted = "xx:xx:xx"
a2_day_planted = 0

b1_planted = False
b1_seed = "none"
b1_time_planted = "xx:xx:xx"
b1_day_planted = 0

b2_planted = False
b2_seed = "none"
b2_time_planted = "xx:xx:xx"
b2_day_planted = 0


def configure_plot():
    pass


def plant():

        
    #ask the user which plot they would like to plant
    plant_location = input("Where would you like to plant? Select a1, a2, b1, b2 : ")
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
    if plant_location == "a1":
        print("Great you are planting in " + plant_location)
        now = datetime.now().strftime("%H:%M:%S")
        a1_planted = True
        a1_seed = "corn"
        a1_time_planted = now
        a1_day_planted = current_game_day
        
    elif plant_location == "a2":
        print("Great you are planting in " + plant_location)
        now = datetime.now().strftime("%H:%M:%S")
        a2_planted = True
        a2_seed = "corn"
        a2_time_planted = now
        a2_day_planted = current_game_day

    elif plant_location == "b1":
        print("Great you are planting in " + plant_location)
        now = datetime.now().strftime("%H:%M:%S")
        b1_planted = True
        b1_seed = "corn"
        b1_time_planted = now
        b1_day_planted = current_game_day
    
    elif plant_location == "b2":
        print("Great you are planting in " + plant_location)
        now = datetime.now().strftime("%H:%M:%S")
        b2_planted = True
        b2_seed = "corn"
        b2_time_planted = now
        b2_day_planted = current_game_day
    
    else:
        print("You've entered something wrong please check your input and try again. (must be a1, a2, b1, or b2)")


def print_plots():

    print("This is what the current plots look like: ")
    print("\n")
    print("\n")
    print("A1 Planted:", a1_planted, "A1 Day Planted:", a1_day_planted, "A1 Time Planted:", a1_time_planted, "A1 Seed:", a1_seed)
    print("A2 Planted:", a2_planted, "A2 Day Planted:", a2_day_planted, "A2 Time Planted:", a2_time_planted, "A2 Seed:", a2_seed)
    print("B1 Planted:", b1_planted, "B1 Day Planted:", b1_day_planted, "B1 Time Planted:", b1_time_planted, "B1 Seed:", b1_seed)
    print("B2 Planted:", b2_planted, "B2 Day Planted:", b2_day_planted, "B2 Time Planted:", b2_time_planted, "B2 Seed:", b2_seed)

def end_day():
    global current_game_day
    current_game_day += 1


def main():
    ans=True
    while ans:
        print("Welcome to Terminal Farm.")
        print(f"""
               ======================================
              |   Terminal Farm - Current Day: {current_game_day}     |
               ======================================
               {player_name}   -   {menu_section}
                                             
                    1.Plant
                    2.Water
                    3.Print Plots
                    4.End Day
                    5.Exit/Quit
              """)
        
        default_sleep_time = 5
        
        ans = input("What would you like to do? ")
        if ans == "1":
            print("\n Planting Seeds...")
            plant()
            time.sleep(default_sleep_time)
        elif ans == "2":
           print("\n \nWatering plants")
           time.sleep(default_sleep_time)
        elif ans == "3":
           print("\n Printing Plots...")
           print_plots()
           time.sleep(default_sleep_time)           
        elif ans == "4":
           print("\n Ending the day ...")
           end_day()
           print("The current day is now: ", current_game_day)
           time.sleep(default_sleep_time)
        elif ans == "4":
           print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")

    plant()


main()
