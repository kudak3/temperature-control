
import time


def main():
    print('Hi ,This Program simulates switching on/off a heater depending on the supplied temperature \n')

    # keep program running
    while True:
        input_value = input('Enter temperature:\t')  # get input from  user
        if input_value == 'Q' or input_value == 'q':
            # stop program if user presses Q
            print('Stopping program......')
            break
        else:
            try:
                # convert string input to floating point number
                input_temp = float(input_value)
                control(input_temp)
            except ValueError:
                print("Enter a valid number")


def control(input_temp):
    """A simple function that switches on/off based on temperature"""
    global min_temp

    if input_temp < min_temp:
        print('The temperature is too low and below minimum optimal temperature')
        switch('on')
    elif min_temp <= input_temp <= max_temp:
        print('The temperature is optimal')
        switch('off')
    elif input_temp > max_temp:
        print('The temperature is too high and above maximum optimal temperature')
        switch('off')


def switch(operation):
    """Function to switch on/off heater"""
    global switch_state
    if operation == 'on':
        if not switch_state:
            print('Switching heater on ...')
            time.sleep(1)  # pause for 1 second to simulate switching
            switch_state = True
            print('Heater now on')
        else:
            print('Heater is already switched on')

    if operation == 'off':
        if switch_state:
            print('Switching heater off ..')
            time.sleep(1) # pause for 1 second to simulate switching
            switch_state = False
            print('Heater now off')
        else:
            print('Heater is already switched off')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    min_temp = 30.0
    max_temp = 40.0
    switch_state = False
    main()
