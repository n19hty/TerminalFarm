


## Define Character Stats
character_level = None
experience_points = None


# talents

hp = None
strength = None

## Skills

woodworking = 0
farming = 0
cooking = 0
mining = 0
firstaid = 0


## Tracking from last session

current_day = None
current_xp = 0



## Track whats in your pockets

front_pockets = []
back_pockets = []


## Track whats in your backpack

backpack_small = []
backpack_medium = []
backpack_large = []


## Track what in your bank

bank_checking = 0
bank_level = 0
bank_items = []

## Track what in your hands
left_hand = None
right_hand = None



decision_request = """
Please decide on what you are doing here?

w - work


"""


print(decision_request)

u_input = input('')


if u_input == 'w':
    print('You selected to do some work.')

    work_request_text = '''
What work are you trying to do right now?

f - farm
w - woodworking
c - cooking
m - mining
x - firstaid

'''
    print(work_request_text)

    w_request = input('')
    ## This is where we decide on what type of farming we are doing today.

    if w_request == 'f':
        print(' We are farming!')

        type_farm_request_text = '''
What work are you trying to do right now?

w - wheat
r - rice
c - corn

'''
        print(type_farm_request_text)
        type_farm_request = input('')
        
        if type_farm_request == 'w':
            print('You chose to farm wheat.')
        elif type_farm_request == 'r':
            print('You chose to farm rice.')
        elif type_farm_request == 'c':
            print('You chose to farm corn.')


       