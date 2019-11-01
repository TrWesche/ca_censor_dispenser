# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# V2 of the censor single string has been built to address the false positives of the original function which found the word when it was a part of a different object
def censor_single_string(search_text: str, censor_search_val, c_character: str = "x"):
    st_list = search_text.split(" ")                                        # Convert search text into a list of strings
    len_st_list = len(st_list)
    cs_val_list = censor_search_val.split(" ")                              # Convert censor search value into a list of strings
    cs_val_lens = [len(val) for val in cs_val_list]                 # Calculate the length of each censor search value
    len_cs_val_list = len(cs_val_list)

    # Create the censor replacement values using the exact length of the values being used to perform the search
    censor_values = []
    for val in cs_val_lens:
        t_censor_value = []
        for i in range(val):
            t_censor_value.append(c_character)
        censor_values.append("".join(t_censor_value))

    # Begin searching list items for the search term 
    for i in range(len_st_list):
        replace_start_location = st_list[i].lower().find(cs_val_list[0])                #Makes the text in the item lowercase and searches the list value for the first search term 
        if replace_start_location >= 0:                                                 #If something found continue

            if (i + len_cs_val_list - 1) > len_st_list:                                 # Check to exit loop and counter calls outside of list range
                break

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
                            t_checks = (not t_output[2][0].isalpha() or (len(t_output[2]) == 1 and ord(t_output[2][0]) == 115)) and ord(t_output[2][0]) != 45   #Not alphabetical and not a dash (-)
                        else:
                            t_checks = True

            if t_checks:
                for i_cs_val in range(len_cs_val_list):
                    st_list[i+i_cs_val] = censor_values[i_cs_val]

    return " ".join(st_list)

# print(censor_single_string(email_one,"learning algorithms"))

# print(censor_single_string(email_two,"her"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_list_strings(search_text: str, censor_search_vals: list, censor_character:str = "x"):
    output_text = search_text
    for val in censor_search_vals:
        output_text = censor_single_string(output_text,val,censor_character)

    return output_text

print(censor_list_strings(email_two,proprietary_terms))