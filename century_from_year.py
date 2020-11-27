year = int(input("Enter year"))

if ( ( year >=1 ) and ( year <= 2021 )):

  if ( year % 100 != 0):

     century = ( year // 100 ) +1

  else:

    century = (year // 100)

  print(century)

else:

    print("There is no such century")
