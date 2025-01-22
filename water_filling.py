def filling(original_tub_size, constant_tub_size, pump_system_speed, update_time, pump_start_level):
    # Check if the water in the tub is less than pump_start_level of its full size
    if original_tub_size < (constant_tub_size * pump_start_level):
        # Increase the amount of water in the tub
        original_tub_size = original_tub_size + pump_system_speed * update_time
        state_of_pump = 1  # Turn on the pump
        print(f'Pump on, water in tub: {original_tub_size}')
