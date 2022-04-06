#This function takes a number and states whether it is an odd an even number
def Odd_or_even():
    print('This function accepts an integer and state whether it is an odd or and even number\n')
    while True:
        try:
            number = int(input('Enter an integer: \n'))
            break
        except:
            print("That's not a valid option!\n")

    
    if number%2==0:
        number=str(number)
        return "{} is an even number!".format(number)
    else:
        number=str(number)
        return "{} is an odd number!".format(number)
