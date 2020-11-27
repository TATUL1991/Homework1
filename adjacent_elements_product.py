number = input("Enter digit")

num = number.split()

result = int(num[0]) * int(num[1])

for i in range(1, len(num)-1):

    product = int(num[i])*int(num[i+1])

    if result <= product:
        
        result = product

print (result)




















