import random


## Define Character Stats
character_level = None
experience_points = None


# talents

hp = 100
strength = 100
stamina = 100

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
bank_savings = 0
bank_level = 0
bank_items = []

## Track what in your hands
left_hand = None
right_hand = None

## Miscellaneous Configs

gift_options = ['Car(200)', 'Taco(10)', 'Double(x2)']



## Miscellaneous Functions

def gift_randomizer(gift_options):
    return random.choice(gift_options)


### Farming:

### First you plant the seed of the plant

def plant_seed(type):
    if type == 'strawberry':
        print(f'Planting {type}...')
        print('Cost is 1 stamina.')
        global stamina 
        stamina -= 1
    elif type == 'wheat':
        print(f'Planting {type}...')
        print('Cost is 1 stamina.')
        stamina -= 1
    elif type == 'corn':
        print(f'Planting {type}...')
        print('Cost is 1 stamina.')
        stamina -= 1
    elif type == 'rice':
        print(f'Planting {type}...')
        print('Cost is 1 stamina.')
        stamina -= 1
    else:
        print('Error processing plant_seed')

### Next you water the seed

def water_seed(type):
    pass

### Next feed your seed

def feed_seed(type):
    pass

### Next harvest your seed

def harvest_seed(type):
    pass
    
## Farm Wheat Function

def farm_wheat():
    ### Farm Wheat Function
    
    print('You chose to farm wheat.')

    ## Wheat cost 1 strength each time
    global stamina

    stamina -= 1
    print(f'It cost 1 stamina to farm wheat, you are now at {stamina} stamina left.')

    ## Sometimes when farming wheat you can encounter bugs.
    ## Sometimes when farming wheat you can encounter a gift.
    ## Sometimes when farming wheat you can encounter nothing.

    possible_outcomes = ['bug', 'gift', 'nothing']

    outcome = random.choice(possible_outcomes)

    if outcome == 'bug':
        print('bug')
        global hp
        hp -= 1
    elif outcome == 'gift':
        global gift_options
        gift_item = gift_randomizer(gift_options)
        print(f'You found a {gift_item} ')
        return gift_item
    elif outcome == 'nothing':
        return 'You received Nothing'
    else:
        print('error')

### Farm Rice Function

def farm_rice():
    ### Farm Rice Function
    
    print('You chose to farm rice.')

    ## Rice cost 1 strength each time
    global strength

    strength -= 1
    print(f'It cost 1 strength to farm wheat, you are now at {strength} strength left.')

    ## Sometimes when farming wheat you can encounter bugs.
    ## Sometimes when farming wheat you can encounter a gift.
    ## Sometimes when farming wheat you can encounter nothing.

    possible_outcomes = ['bug', 'gift', 'nothing']

    outcome = random.choice(possible_outcomes)

    if outcome == 'bug':
        print('bug')
        global hp
        hp -= 1
    elif outcome == 'gift':
        global gift_options
        gift_item = gift_randomizer(gift_options)
        print(f'You found a {gift_item} ')
        return gift_item
    elif outcome == 'nothing':
        return 'You received Nothing'
    else:
        print('error')
    print('You chose to farm rice.')

### Farm Corn Function

def farm_corn():
   ### Farm Rice Function
   
   print('You chose to farm corn.')
   
   ## Rice cost 1 strength each time
   
   global strength
   strength -= 1
   
   print(f'It cost 1 strength to farm wheat, you are now at {strength} strength left.')
   
   ## Sometimes when farming wheat you can encounter bugs.
   ## Sometimes when farming wheat you can encounter a gift.
   ## Sometimes when farming wheat you can encounter nothing.
   
   possible_outcomes = ['bug', 'gift', 'nothing']
   
   outcome = random.choice(possible_outcomes)
   
   if outcome == 'bug':
        print('bug')
        global hp
        hp -= 1
   elif outcome == 'gift':
        global gift_options
        gift_item = gift_randomizer(gift_options)
        print(f'You found a {gift_item} ')
        return gift_item
   elif outcome == 'nothing':
       return 'You received Nothing'
   else:
    print('error')
    




def make_decision():
      
    print('🥕')
    decision_request_text = """
    Please decide on what you are doing here?
    
    w - work
    
    """
    print(decision_request_text)
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
            What work are you trying to farm right now?
            w - wheat
            r - rice
            c - corn
            
            '''

            print(type_farm_request_text)
            type_farm_request = input('')
            
            if type_farm_request == 'w':
                farm_wheat()
            elif type_farm_request == 'r':
                farm_rice()
            elif type_farm_request == 'c':
                farm_corn()

while stamina > 0:
    make_decision()


       