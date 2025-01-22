import time
from auxilary_functions import get_current_timestamp
from auxilary_functions import float_form
from datetime import datetime, timedelta
from water_filling import filling

# Get the number of cows drinking from user input and change it to a float number
number_of_cows = input('How many cows would like to drink: ')
number_of_cows = float(number_of_cows)

# Set constant values
original_cow_drink_pro_second = 0.2  # liters per second per cow
constant_cow_drink_pro_second = original_cow_drink_pro_second
pump_system_speed = 1  # liters per second (same as one 60 liters per minute pump)
original_tub_size = 500.0  # liters (starting size of the tub)
constant_tub_size = original_tub_size
drinking_time = 0.16  # minutes (time for cows to drink)
liter_pro_cow = input('How many liters would the cow drink: ')
liter_pro_cow = float(liter_pro_cow)

# Initialize variables to keep track of water drunk and pump state
amount_of_water_drunk = 0
pump_start_level = 0.95  # percentage of water in the tub before starting the pump
drinking = 0  # 0 means cows are not drinking, 1 means they are
state_of_pump = 0  # 0 means pump is off, 1 means pump is on
update_time = 1.0  # seconds between each update
start_time = None  # when cows started drinking

while True:
    # Wait for update time interval
    time.sleep(update_time)

    if drinking == 0:
        drinking = 1
        print('The cows are drinking.')
        start_time = datetime.now()  # record the start time

    # Decrease the water in the tub as cows drink
    original_tub_size -= (update_time * (number_of_cows * original_cow_drink_pro_second))
    original_tub_size = float_form(original_tub_size)  # format the tub size
    timestamp = get_current_timestamp()  # get the current time
    print(timestamp)
    print(f'Amount of water in the tub: {original_tub_size} liter')

    # Increase the total amount of water drunk by cows
    amount_of_water_drunk += constant_cow_drink_pro_second * number_of_cows
    amount_of_water_drunk = float_form(amount_of_water_drunk)  # format the amount drunk
    print(f'Amount of water drunk: {amount_of_water_drunk} liter')

    # Check if cows have drunk the required amount
    if amount_of_water_drunk >= liter_pro_cow * number_of_cows:
        drinking = 1
        break

    # Refill the tub if needed
    filling(original_tub_size, constant_tub_size, pump_system_speed, update_time, pump_start_level)

print(f'Cows do not drink anymore. Water level: {original_tub_size} liter')

# Refill the tub to its original size
while True:
    time.sleep(1)
    if original_tub_size <= constant_tub_size:
        original_tub_size += pump_system_speed * update_time  # add water to the tub
        print(f'Pump on, water in tub: {original_tub_size} liter')
    else:
        print('The tub is full.')
        break
