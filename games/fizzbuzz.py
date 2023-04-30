

def fizz_buzz():

    # loop through numbers from 1 to 100
    for number in range(1, 101):
      
        fizz = number % 3
        buzz = number % 5

        if (fizz == 0) and (buzz == 0):
            # is divisable by both 3 and 5 then print FizzBuss
            print("FizzBuzz")
        elif fizz == 0:
            # is divisible by 3 then print Fizz
            print("Fizz")
        elif buzz == 0:
            # is divisable by 5 then print Buzz
            print("Buzz")
        else:
            print(f"{number}")
