def descending_order(num):
    # Bust a move right here
    
    list = [int(char) for char in str(num)]
    list.sort(reverse=True)
    str1 = ''.join([str(elem) for elem in list])
    return int(str1)
    
    