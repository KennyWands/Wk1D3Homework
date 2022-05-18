def return_10():
    return (10)

def add (x, y):
    return(x + y)

def subtract (x, y):
    return (x-y)

def multiply (x, y):
    return(x*y)

def divide (x, y):
    return(x/y)

def length_of_string(string):
    return len(string)

def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(x, y):
    num_x = int(x)
    num_y = int(y)
    return num_x + num_y

def number_to_full_month_name(number):
    off_by_1 = number-1
    months= ["January","Febuary","March",
    "April","May","June","July","August",
    "September","October","November","December"]
    return(months[off_by_1])

def number_to_short_month_name(number):
    off_by_1 = number-1
    months= ["January","Febuary","March",
    "April","May","June","July","August",
    "September","October","November","December"]
    short =(months[off_by_1])[0:3]
    return(short)

def volume_of_cube(side):
    return(side*side*side)

def reverse_string (string):
    return(string[::-1])

def fahrenheit_to_celsius(fah):
    return((fah-32)*0.5556)