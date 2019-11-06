import re

# check if get exist
def check_in_parantesis(list_character):
    if "(" in list_character:
        # find  ( )
        index_a = [list_character.start() for list_character in re.finditer('(', list_character)]
        index_a_end = [list_character.start() for list_character in re.finditer(')', list_character)]

        # if ( not have ) not same number
        if len(index_a) == len(index_a_end):
            return True

            for i in len(index_a):
                if index_a_end[i] > index_a[i]:
                    return False
                else:
                    return True
        else:
            return False

    if "[" in list_character:
        # find [ ]
        index_b = [list_character.start() for list_character in re.finditer('[', list_character)]
        index_b_end = [list_character.start() for list_character in re.finditer(']', list_character)]

        # if [ not have ] not same number
        if len(index_b) == len(index_b_end):
            return True
        
            for i in len(index_b):
                if index_b_end[i] > index_a[i]:
                    return False
                else:
                    return True
        else:
            return False

    if "{" in list_character:
        # find { }
        index_c = [list_character.start() for list_character in re.finditer('{', list_character)]
        index_c_end = [list_character.start() for list_character in re.finditer('}', list_character)]

        # if { not have } not same number
        if len(index_c) == len(index_c_end):
            return True

            for i in len(index_b):
                if index_c_end[i] > index_c[i]:
                    return False
                else:
                    return True
        else:
            return False


list_character = input("input list character:")

hasil = check_in_parantesis(list_character)
print(hasil)