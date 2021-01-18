def fizzbuzz():
    """
     Assignment 2.3

     Here is a classic coding interview challenge.  Write a Python program called fizzbuzz.py that prints each number from 1 to 100, each on its own line, but with the following modifications.

     -If the number is divisible by 3, print "Fizz" instead,
     -If the number is divisible by 5, print "Buzz" instead,
     -Or if the number is divisible by both 3 and 5, print "FizzBuzz" instead.
    """
    for count in range(1, 101):
        if count % 3 == 0:
            print("Fizz", end="")
        if count % 5 == 0:
            print("Buzz", end="")
        if count % 3 != 0 and count % 5 != 0:
            print(count, end="")
        print()

fizzbuzz()