import time

current_time = 0
coin_purse = 0


## Types of Plat

## plant
## mineral


## Types of seeds

## Sunflower

sunflower_stats = {'days_to_mature' : 5, 'sale_price' : 15}


## 
## 

## Soil Status

## empty
## unwatered
## watered
## fertilized


## Set up the patches
patch_1 = {}

## 

def plant_seed(type, working_plot):
    plot_seed = {'plot_id':working_plot, 'type_of_plot': 'plant', 'type_of_seed': type,'soil_status': 'unwatered', 'start_time': 0}
    global patch_1 
    patch_1.update(plot_seed)

def basic_menu(u_input='w'):
        
        if u_input == "p":
            plot_id_input = input('Enter your plot id.')
            plant_seed('sunflower', plot_id_input)
            print('You selected to plant.')
                    
        elif u_input == 's':
            print('You selected to sell.')
        
        elif u_input == 'e':
            exit()        
        
        else:
            print('Not a valid selection.')
            #u_input = input('Enter and option to either plant or sell:')



u_input = input('Enter and option to either plant or sell:')
basic_menu(u_input)
print(f'This is currently on patch_1 = {patch_1}')
