## start
number: int = int(input("Enter another integer: "));
if number % 3 == 0 and number % 5 == 0:
    print ("Buzz Fizz");
elif number % 3 == 0:
    print ("Buzz");
elif number % 5 == 0:
    print ("Fizz");
else:
    print("Not divisible by 3 or 5");
## End