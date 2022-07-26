def raise_to_power(base_num , pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
a = (input("Please enter raise number : "))
b = (input("Please enter power number : "))
print(raise_to_power(int(a),int(b)))