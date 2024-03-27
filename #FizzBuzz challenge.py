#FizzBuzz challenge
#print numbers 1-100.
#If divisible by 3, print Fizz; by 5, print Buzz
#divisible by both, print FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")    
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)    