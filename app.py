
## Plots

a1_info = {
    'plot_id' : 'a1',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

a2_info = {
    'plot_id' : 'a2',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

a3_info = {
    'plot_id' : 'a3',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

b1_info = {
    'plot_id' : 'b1',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

b2_info = {
    'plot_id' : 'b2',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

b3_info = {
    'plot_id' : 'b3',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

c1_info = {
    'plot_id' : 'c1',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

c2_info = {
    'plot_id' : 'c2',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

c3_info = {
    'plot_id' : 'c3',
    'seed_type': None,
    'watered': False,
    'time_planted': None,
    'days_until_harvest': None
    }

crop_plots = [
    a1_info,
    a2_info,
    a3_info,
    b1_info,
    b2_info,
    b3_info,
    c1_info,
    c2_info,
    c3_info
    ]


def load_croptypes_from_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        return [line.strip() for line in file]

croptype_list = 'config/crop_types'

crop_types = load_croptypes_from_file(croptype_list) #loads crop_types from the croptype_list


def plant_crops():
    
    print('Available crops: \n')
    for crop in crop_types:
        print(crop)
    
    user_input = input('\nWhat type of crop do you want to plant?')
    
    if user_input == '':
        "Nothing entered please make a selection: "
        return
    elif user_input == 'corn':
        a1_info.update({'seed_type': 'corn'})
    
    else:
        print('Broken')
    

    print(a1_info)
    



def water_crops():
    exit()

def harvest_crops():
    exit()

def sell_crops():
    exit()

def pass_day():
    exit()

def menu_option():
    
    menu_print = '''
    Input menu:

    1: plant_crops()
    2: water_crops()
    3: sell_crops()
    4: pass_day()

    '''
    user_input = input(menu_print)

    return user_input


if menu_option() == '1':
    print('Plant crops was selected.')
    plant_crops()
elif menu_option() == '2':
    print('Water crops was selected.')
    water_crops()
elif menu_option() == '3':
    print('sell crops was selected.')
    sell_crops()
elif menu_option() == '4':
    print('Passing a day.')
    pass_day()
else:
    print('Invalid Selction')

