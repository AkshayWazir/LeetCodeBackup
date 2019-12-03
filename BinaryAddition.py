def sum_binary(num1, num2):
    return str(bin(int(num1, 2) + int(num2, 2)))[2:]


nu1, nu2 = input().split()
print(sum_binary(nu1, nu2))
