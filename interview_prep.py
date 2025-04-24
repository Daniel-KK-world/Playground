def get_factorial(num):
     factorial = 1 
     while num > 1:
          factorial *= num 
          num -= 1
          print(factorial) 

get_factorial(5)