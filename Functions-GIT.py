#4.13.3: Greetings
#Jacob Shoup 2/6/19


print("")
name = input("( o‿o) Hey what is your name: ")

def greeting():
    print("(o‿o) Hi there non-gender specific person, what is your " + name + "?")
    print("(OヮO) Nice to meet you!")

greeting()


# 4.13.3: Functions and Variables
# Jacob Shoup
# 2.14.19

x = 410

def print_something():
    x = 13
    print(x)

print_something()
print(x)


# 4.13.5: Functions & Variables - Part 2
# Jacob Shoup
# 2.14.19

my_variable = 69.420

def something():
    print(my_variable + 10)

something()



# 4.13.6: Functions & Variables, Part 3
# Jacob Shoup
# 2.18.19


def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + 'Hello World')

# 4.14.4: Name and Age
# Jacob Shoup
# 2.18.19

def name_and_age(name, age):
    print('Hi, my name is ', name, ' and I am ', str(age), ' years old.')

name_and_age('Jacob Shoup', 18)
name_and_age('Dave', 19)
name_and_age('Steve', 69)

# 4.14.5: Default Parameter Values
# Jacob Shoup
# 2.19.19

def print_two_numbers(x, y = 20):
    print('First number: ',  str(x))
    print('Second_number: ' + str(y))

print_two_numbers(5, 67)
print_two_numbers(23)

# 4.14.7: Print Multiple Times
# Mr. Lange
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hello Computer scientist', 4)




# 4.14.7: Print Multiple Times
# Mr. Lange
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hello Computer scientist', 4)


# 4.16.3: Enter a number
# Jacob Shoup
# 2.20.19


# 4.16.6: Temperature Converter
# Mr. Lange
# 2.20.19

try:
    my_number = int(input('Enter and integer: '))
    print('Your number: ' + str(my_number))

except ValueError:
    print('That was not an integer you degenerate')


def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) / 1.8

try:
    c = float(input('Enter a temp in C: '))
    print('In F:', round(celcius_to_fahrenheit(c), 2))

    f = float(input('Enter a temp in F: '))
    print('In C:', round(fahrenheit_to_celcius(f), 2))

except ValueError:
    print('You need to enter a float moron')