def addBinary(num1, num2):
    num1_str = str(bin(num1))[2:]
    num2_str = str(bin(num2))[2:]
    len1 = len(num1_str)
    len2 = len(num2_str)
    print(num1_str)
    print(num2_str)
    result = ""
    carry = 0
    while len1 >= 0 or len2 >= 0:
        num = int(num1_str[len1 - 1]) + int(num2_str[len2 - 1]) + carry
        if num < 2:
            num_add = num
            carry = 0
        else:
            num_add = 0
            carry = 1
        len1 -= 1
        len2 -= 1
        result = str(num_add) + result
    print('0b'+result)
    return result

    # num1_list=num1_str.split("")


# print(addBinary(123, 456))
print(int(addBinary(123, 456)))

