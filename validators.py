
def validate_string(list_in, string_type):
    '''
    This function validates user input. It loops until the user input matches a string found within a given list.
    :param list_in: input list to search within
    :param string_type: for output purposes, the type (such as GEONAME). Essentially the column name (could be improved)
    :return: found_term, the user input which was found in the list
    '''
    while True:
        try:
            print('Enter', string_type, ':')
            input_string = input().lower()
            matches = [found_term for found_term in list_in if input_string in found_term.lower()]
            if matches:
                found_term = matches[0]
                print(f"Using closest match.")
                break
            else:
                print("Invalid", string_type, ". Please enter a value that exists in the DataFrame.")
        except ValueError:
            print("Invalid", string_type, ". Please enter a value that exists in the DataFrame.")
    return found_term


def validate_int_list(list_in, int_type):
    '''
    This function validates user input. It loops until the user input matches an int found within a given list.
    :param list_in: input list to search within
    :param int_type: for output purposes, the type (such as census code). Essentially the column name (could be improved)
    :return: found_term, the user input which was found in the list
    '''
    while True:
        try:
            print("Enter", int_type, ":")
            input_int = int(input())
            if input_int in list_in:
                break
            else:
                print("Invalid", int_type, "Please enter a value that exists in the DataFrame.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the", int_type)
    return input_int


def validate_int_min(lower):
    '''
    This function validates integers. It is passed a lower threshold, and runs until the input exceeds it. (used in custom area building)
    '''
    while True:
        try:
            num = int(input())
            if num > lower:
                return num
            else:
                print(f"The number must be greater than {lower}.")
        except ValueError:
            print(f"Invalid input. Please enter a number greater than {lower}.")


def validate_weights(name_list):
    '''
    This function creates a list of weights that can be used for custom census areas. It validates all user input, and ensures the weights total to 1.
    :param name_list: the list of geonames. It is used to know the appropriate length of the weight list, as well as which specific place to ask for.
    :return: name_list, a list of the percentages.
    '''
    weight_choice = input("Would you like to use custom weights? (Y/N)")
    if weight_choice.lower() == 'y':
        while True:
            try:
                weights = []
                for name in name_list:
                    while True:
                        try:
                            print(f"Enter the weight for {name} (as a decimal, e.g. 0.5):")
                            input_percent = float(input())
                            if 0 <= input_percent <= 1:
                                weights.append(input_percent)
                                break
                            else:
                                print(f"Invalid weight for {name}. Please enter a value between 0 and 1.")
                        except ValueError:
                            print(f"Invalid input for {name}. Please enter a valid decimal number.")

                if sum(weights) == 1.0:
                    return weights
                else:
                    print("The total of weights does not add up to 1.0. Please re-enter.")
                    weights.clear()
            except ValueError:
                print("Invalid input. Please enter valid decimal number.")
    else:
        weights = []
        return weights
