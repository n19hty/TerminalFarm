# This is the start to Terminal Farm in Python.
# The goal is to learn python better, but also to build a fun terminal game you can play.
# I would like it to be similar to stardew but with typing mechanics.

from datetime import datetime 

print("Welcome to Terminal Farm.")


def configure_plot():
    pass


def plant():

    a1_planted = False
    a1_time_planted = ""
    
    a2_planted = False
    a2_time_planted = ""
    
    b1_planted = False
    b1_time_planted = ""
    
    b2_planted = False
    b2_time_planted = ""
    
    
    #ask the user which plot they would like to plant
    plant_location = input("Where would you like to plant? Select a1, a2, b1, b2 : ")


    # create the if choices here
    if plant_location == "a1":
        print("Great you are planting in " + plant_location)
        now = datetime.now().strftime("%H:%M:%S")
        a1_time_planted = now
        

    elif plant_location == "a2":
        print("Great you are planting in " + plant_location)
        pass
    elif plant_location == "b1":
        print("Great you are planting in " + plant_location)
        pass
    elif plant_location == "b2":
        print("Great you are planting in " + plant_location)
        pass
    else:
        print("You've entered something wrong please check your input and try again. (must be a1, a2, b1, or b2)")


    print("This is what the current plots look like: ")
    print("A1 Planted: ", a1_planted, "A1 Time Planted: ", a1_time_planted)
    print("A2 Planted: ", a2_planted, "A2 Time Planted: ", a2_time_planted)
    print("B1 Planted: ", b1_planted, "B1 Time Planted: ", b1_time_planted)
    print("B2 Planted: ", b2_planted, "B2 Time Planted: ", b2_time_planted)




def main():
    plant()


main()
