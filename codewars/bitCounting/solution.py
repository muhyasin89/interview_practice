def count_bits(n):
    result = '{0:08b}'.format(abs(n))
#     print(result)
    return result.count('1')


#more efficient solution
def countBits(n):
    return bin(n).count("1")


