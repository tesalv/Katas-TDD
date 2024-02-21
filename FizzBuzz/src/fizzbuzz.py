"""
Write a program that prints one line for each number from 1 to 100
Usually just print the number itself.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number
For numbers which are multiples of both three and five print "FizzBuzz" instead of the number

"""
def process(number):
    if number % 3 ==0 and number % 5 == 0: 
        return "FizzBuzz"
    elif number % 3 ==0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return number
