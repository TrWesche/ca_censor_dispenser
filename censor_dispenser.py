# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# def censor_single_string(search_text: str, censor_search_val, c_character:str = "x"):
#     t_output = []
#     output = ""
#     t_censor_value = []
#     for i in range(len(censor_search_val)):
#         t_censor_value.append(c_character)
#     # t_censor_value = [t_censor_value.append(censor_character) for i in range(len(censor_search_val))]
#     censor_value = "".join(t_censor_value)

#     replace_start_location = search_text.find(censor_search_val)
#     output = search_text
#     while replace_start_location >= 0:
#         t_output = output.partition(censor_search_val)
#         output = (f"{t_output[0]}{censor_value}{t_output[2]}")
#         replace_start_location = output.find(censor_search_val)
#     return output

# print(censor_single_string(email_one,"learning algorithms"))




def censor_single_string(search_text: str, censor_search_val, c_character:str = "x"):
    t_output = []
    output = ""
    t_censor_value = []
    for i in range(len(censor_search_val)):
        t_censor_value.append(c_character)
    censor_value = "".join(t_censor_value)

    replace_start_location = search_text.find(censor_search_val)
    output = search_text
    while replace_start_location >= 0:
        t_output = output.partition(censor_search_val)
        # Perform additional checks to make sure the value found is not part of a different word.
        if len(t_output[0]) > 0:                        #Check the value preceeding the search value
            t_checks = not t_output[-1][0].isalpha() and ord(t_output[-1][0]) != 45 #Not alphabetical and not a dash (-)
        else:
            t_checks = True

        if (len(t_output[2]) > 0) and t_checks:         #Check the value following the search value
            t_checks = not t_output[2][0].isalpha() and ord(t_output[2][0]) != 45   #Not alphabetical and not a dash (-)
        else:
            t_checks = True
        if t_checks == True:
            output = (f"{t_output[0]}{censor_value}{t_output[2]}")
        
        if replace_start_location + 1 < len(search_text):   #Make sure the next search does not catch a previously found string & will not cause an error
            find_strt_loc = replace_start_location + 1      
        else:
            break
        replace_start_location = output.find(censor_search_val,find_strt_loc)
    return output