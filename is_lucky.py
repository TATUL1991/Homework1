number = int(input("Enter"))

if ( number >= 10 ) and ( number <=  99999999 ):

    list,list1 = [], []

    i, j, sum = 0, 0, 0

    while number > 0:

        sum = sum + int(number % 10)

        list.append(int(number % 10))

        i += 1

        j =  int( i/2 )

        if (int(i) % 2 == 0):

         list1 = list[j:]

         sum1 = 0

         for elem in list1:

             sum1 = sum1 + elem

             sum2 = sum - sum1

        number = (number - (number % 10 ))/10

    if ( sum1 == sum2 ):

        print("YES")

    else:

        print("NO")







