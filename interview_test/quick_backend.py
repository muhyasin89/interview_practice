def given_array(arr, number):
    return arr.count(number)

input_array = input("insert your list separated by ','")

input_number = input("Insert number you wanna search?")

hasil = given_array(list(input_array), input_number)

print(hasil)