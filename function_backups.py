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
                            t_checks = (not t_output[2][0].isalpha() or (len(t_output[2]) == 1 and ord(t_output[2][0]) == 115)) and ord(t_output[2][0]) != 45   #Not alphabetical and not a dash (-) with exception, single character 's'
                        else:
                            t_checks = True

            if t_checks:                                                                #If ok replace strings with censor values
                for i_cs_val in range(len_cs_val_list):
                    st_list[i+i_cs_val] = censor_values[i_cs_val]

    return " ".join(st_list)                                                            #Return new string


    def censor_repeats(search_text: str, censor_search_val, repeats_allowed = 1, c_character: str = "x"):
    st_list = search_text.split(" ")                                                    # Convert search text into a list of strings
    len_st_list = len(st_list)
    cs_val_list = censor_search_val.split(" ")                                          # Convert censor search value into a list of strings
    cs_val_lens = [len(val) for val in cs_val_list]                                     # Calculate the length of each censor search value
    len_cs_val_list = len(cs_val_list)   
    repeat_counter = 0

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
                            while c < range(len(processing_string)):
                                if ord(processing_string[c]) <= 31:
                                    censor_value.append(processing_string[c])
                                    censor_value.append(processing_string[c+1])
                                    c += 2
                                else:
                                    censor_value.append(c_character)
                            st_list[index_loc] = "".join(censor_value)

    return " ".join(st_list)     