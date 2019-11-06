def most_popular_number(numb_list):
    counter = 0
    num = numb_list[0]

    for i in numb_list:
        curr_frequency = numb_list.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num=i

        return num

input_number = input("input number for list separated by ','")

print("Most popular number {}, appear {} time".format(most_popular_number(list(input_number)), sum(len(i) for i in list(input_number))))