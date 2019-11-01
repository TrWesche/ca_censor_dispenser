# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_string_val(search_text: str, censor_search_val, censor_character:str = "x"):
    t_output = []
    output = ""
    t_censor_value = []
    for i in range(len(censor_search_val)):
        t_censor_value.append(censor_character)
    # t_censor_value = [t_censor_value.append(censor_character) for i in range(len(censor_search_val))]
    censor_value = "".join(t_censor_value)

    replace_start_location = search_text.find(censor_search_val)
    output = search_text
    while replace_start_location >= 0:
        t_output = output.partition(censor_search_val)
        output = (f"{t_output[0]}{censor_value}{t_output[2]}")
        replace_start_location = output.find(censor_search_val)
    return output

print(censor_string_val(email_one,"learning algorithms"))