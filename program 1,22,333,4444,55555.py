rows = 6
  # if you want user to enter a number , uncomment the below line
  # rows = unt(input('enter the number of rows'))
  # outer loop
for i in range(rows):
      # nested loop
      for j in range(i):
          # displaynumber
          print(i, end='')
      # new line after each row
      print('')
