# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# V3 of the censor single string has been built for more dynamic censoring capabilities & allowing for a wider breadth of censors (i.e. words before and after censor value can additionally be censored)
def censor_single_string(search_text: str, censor_search_val, c_breadth = 0, c_character: str = "x"):
    # Convert search text into a list of strings
    st_list = []
    st_list_spaces = search_text.split(" ")
    for val in st_list_spaces:
        t_list = val.splitlines(True)
        if len(t_list) > 1:
            for sub_l in t_list:
                st_list.append(sub_l)
        else:
            st_list.append(val)

    len_st_list = len(st_list)
    cs_val_list = censor_search_val.split(" ")                                          # Convert censor search value into a list of strings
    cs_val_lens = [len(val) for val in cs_val_list]                                     # Calculate the length of each censor search value
    len_cs_val_list = len(cs_val_list)

    # Begin searching list items for the search term 
    for i in range(len_st_list):
        replace_start_location = st_list[i].lower().find(cs_val_list[0])                #Makes the text in the item lowercase and searches the list value for the first search term 
        if replace_start_location >= 0:                                                 #If something found continue

            if (i + len_cs_val_list - 1) > len_st_list:                                 # Check to exit loop and counter calls outside of list range
                break

            # Checks strings to make sure the value found is valid
            t_checks = True
            for i_cs_val in range(len_cs_val_list):
                if len(st_list[i+i_cs_val]) != cs_val_lens[i_cs_val]:                   # Check to see if the cs search value and the value in the list are the same length
                    t_output = st_list[i+i_cs_val].partition(cs_val_list[i_cs_val])     # Break the string into 3 parts around the search value

                    if t_checks:
                        if len(t_output[0]) > 0:                                        #Check the value preceeding the search value
                            t_checks = not t_output[0][-1].isalpha() and ord(t_output[0][-1]) != 45 #Not alphabetical and not a dash (-)
                        else:
                            t_checks = True
                    if t_checks:
                        if len(t_output[2]) > 0:                                        #Check the value following the search value
                            t_checks = (not t_output[2][0].isalpha() or (len(t_output[2]) == 1 and ord(t_output[2][0]) == 115)) and ord(t_output[2][0]) != 45   #Not alphabetical and not a dash (-) with exception, single character 's'
                        else:
                            t_checks = True

            #Performs the replace of the censored word with the censor value if the previous checks were found to be ok
            if t_checks:

                #Calculate the size of the censor index iterator
                if c_breadth > 0:
                    censor_iterator = len_cs_val_list + c_breadth * 2
                else:
                    censor_iterator = len_cs_val_list

                # Create the censor replacement values using the exact length of the values being used to perform the search
                for i_cs_val in range(censor_iterator):

                    # First check to make sure the cited index replacement location is valid (i.e. in this case not negative and less then max length)
                    index_loc = i - c_breadth + i_cs_val
                    if index_loc >= 0 and index_loc < len_st_list:

                        # Pull in the string to be replaced for evaluation
                        processing_string = st_list[index_loc]
                        censor_value = []

                        # Check to see if there are any escape characters in the string (for example \n, \t, etc.)
                        if processing_string.isprintable():
                            for c in range(len(processing_string)):
                                censor_value.append(c_character)
                            st_list[index_loc] = "".join(censor_value)

                        # If there are escape characters loop through the entire list searching for the characters in question
                        else:
                            c = 0
                            while c < len(processing_string):
                                if ord(processing_string[c]) <= 31:
                                    censor_value.append(processing_string[c])
                                    c += 1
                                else:
                                    censor_value.append(c_character)
                                    c += 1
                            st_list[index_loc] = "".join(censor_value)

    return " ".join(st_list)                                                            #Return new string


def censor_repeats(search_text: str, censor_search_vals: list, repeats_allowed = 1, c_character: str = "x"):
    # Convert search text into a list of strings
    st_list = []
    st_list_spaces = search_text.split(" ")
    for val in st_list_spaces:
        t_list = val.splitlines(True)
        if len(t_list) > 1:
            for sub_l in t_list:
                st_list.append(sub_l)
        else:
            st_list.append(val)

    len_st_list = len(st_list)
    repeat_counter = 0

    for val in censor_search_vals:
        cs_val_list = val.split(" ")                                                    # Convert censor search value into a list of strings
        cs_val_lens = [len(val) for val in cs_val_list]                                 # Calculate the length of each censor search value
        len_cs_val_list = len(cs_val_list)   

    # Begin searching list items for the search term 
        for i in range(len_st_list):
            replace_start_location = st_list[i].lower().find(cs_val_list[0])                #Makes the text in the item lowercase and searches the list value for the first search term 
            if replace_start_location >= 0:                                                 #If something found continue

                if (i + len_cs_val_list - 1) > len_st_list:                                 # Check to exit loop and counter calls outside of list range
                    break

                # Checks strings to make sure the value found is valid
                t_checks = True
                for i_cs_val in range(len_cs_val_list):
                    if len(st_list[i+i_cs_val]) != cs_val_lens[i_cs_val]:                   # Check to see if the cs search value and the value in the list are the same length
                        t_output = st_list[i+i_cs_val].partition(cs_val_list[i_cs_val])     # Break the string into 3 parts around the search value

                        if t_checks:
                            if len(t_output[0]) > 0:                                        #Check the value preceeding the search value
                                t_checks = not t_output[0][-1].isalpha() and ord(t_output[0][-1]) != 45 #Not alphabetical and not a dash (-)
                            else:
                                t_checks = True
                        if t_checks:
                            if len(t_output[2]) > 0:                                        #Check the value following the search value
                                t_checks = (not t_output[2][0].isalpha() or (len(t_output[2]) == 1 and ord(t_output[2][0]) == 115)) and ord(t_output[2][0]) != 45   #Not alphabetical and not a dash (-) with exception, single character 's'
                            else:
                                t_checks = True

                #Performs the replace of the censored word with the censor value if the previous checks were found to be ok
                if t_checks:
                    repeat_counter += 1
                    if repeat_counter > repeats_allowed:

                        # Create the censor replacement values using the exact length of the values being used to perform the search
                        for i_cs_val in range(len_cs_val_list):
                            
                            index_loc = i + i_cs_val
                            # Pull in the string to be replaced for evaluation
                            processing_string = st_list[index_loc]
                            censor_value = []

                            # Check to see if there are any escape characters in the string (for example \n, \t, etc.)
                            if processing_string.isprintable():
                                for c in range(len(processing_string)):
                                    censor_value.append(c_character)
                                st_list[index_loc] = "".join(censor_value)
                                
                            # If there are escape characters loop through the entire list searching for the characters in question
                            else:
                                c = 0
                                while c < len(processing_string):
                                    if ord(processing_string[c]) <= 31:
                                        censor_value.append(processing_string[c])
                                        c += 2
                                    else:
                                        censor_value.append(c_character)
                                        c += 1
                                st_list[index_loc] = "".join(censor_value)

    return " ".join(st_list)     


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_list_strings(search_text: str, censor_search_vals: list,censor_breadth: int = 0, censor_character:str = "x"):
    output_text = search_text
    for val in censor_search_vals:
        output_text = censor_single_string(output_text,val,censor_breadth,censor_character)
    return output_text

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

print(censor_single_string(email_one,"learning algorithms"))

print(censor_list_strings(email_two,proprietary_terms,0))

print(censor_repeats(email_three,negative_words,1))

print(censor_list_strings(email_four, proprietary_terms + negative_words, 1))