


def load_croptypes_from_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        return [line.strip() for line in file]

croptype_list = 'config/crop_types'

crop_types = load_croptypes_from_file(croptype_list) #loads crop_types from the croptype_list


def plant_crops():
    
    print('Available crops: \n')
    for crop in crop_types:
        print(crop)
    
    user_input= input('\nWhat type of crop do you want to plant?')

    return user_input
    

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

