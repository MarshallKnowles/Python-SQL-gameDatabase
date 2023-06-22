#returns a positive integer value based on user input
def get_int( prompt, error_message):
    int_value = "not an integer"
    while (True):
        try:
            int_value = int(input( prompt ))
            if(int_value < 0):
                print("Please enter a positive integer.")
                continues
            else:
                return int_value
        except:
            print(error_message)

#returns a string that is shorter than the input length based on user input
def get_str_less( prompt, error_message, length):
    str_value = input(prompt)
    while ( len(str_value) > length):
        str_value = input(error_message)

    return str_value
