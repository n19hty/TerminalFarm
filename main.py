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
pa011 = 'empty'
pa012 = 'empty'
pa013 = 'empty'
pa014 = 'empty'
pa015 = 'empty'
pa016 = 'empty'
pa021 = 'empty'
pa022 = 'empty'
pa023 = 'empty'
pa024 = 'empty'
pa025 = 'empty'
pa026 = 'empty'
pa031 = 'empty'
pa032 = 'empty'
pa033 = 'empty'
pa034 = 'empty'
pa035 = 'empty'
pa036 = 'empty'
pa041 = 'empty'
pa042 = 'empty'
pa043 = 'empty'
pa044 = 'empty'
pa045 = 'empty'
pa046 = 'empty'
pa051 = 'empty'
pa052 = 'empty'
pa053 = 'empty'
pa054 = 'empty'
pa055 = 'empty'
pa056 = 'empty'
pa061 = 'empty'
pa062 = 'empty'
pa063 = 'empty'
pa064 = 'empty'
pa065 = 'empty'
pa066 = 'empty'
pa071 = 'empty'
pa072 = 'empty'
pa073 = 'empty'
pa074 = 'empty'
pa075 = 'empty'
pa076 = 'empty'
pa081 = 'empty'
pa082 = 'empty'
pa083 = 'empty'
pa084 = 'empty'
pa085 = 'empty'
pa086 = 'empty'
pa091 = 'empty'
pa092 = 'empty'
pa093 = 'empty'
pa094 = 'empty'
pa095 = 'empty'
pa096 = 'empty'

## 

def plant_seed(type, working_plot):
    plot_seed = {'plot_id':{working_plot}, 'type_of_plot': 'plant', 'type_of_seed': {type},'soil_status':'unwatered'}
    plot_num_norm = 'pa0'+ input
    plot_num_norm 


# working_plot = 'pa' + input('Enter the plot you want to impact?')
# if working_plot == 0:
#     print('Not valid input. Select another plot number.')
# if working_plot == '11':
#     plant_seed
# if working_plot == '12':
#     pass
# if working_plot == '13':
#     pass
# if working_plot == '14':
#     pass
# if working_plot == '15':
#     pass
# if working_plot == '16':
#     pass





def basic_menu(u_input='w'):
    while u_input != 'e':
        
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
            u_input = input('Enter and option to either plant or sell:')



u_input = input('Enter and option to either plant or sell:')
basic_menu(u_input)

