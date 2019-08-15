#1 max of 2 numbers
def max(a,b):
    if a < b :
        print(b)
    else:
        print(a)

#2 fizz_buzz algorythm
def fizz_buzz(input):
    x = int(input)
    y = x % 3
    z = x % 5
    result = ""
    if y == 0 :
        result += "Fizz" 
    if z == 0 :
        result += "Buzz"
    if not z == 0 and not y ==0:
        result += str(input)
    return result

#3 speed check
def speed_check(input):
    if 0 < input < 120 : 
        print(f"{input}km/h. Ok speed! :)")
    elif 121 < input < 149:
        print(f"{input}km/h. You've exceeded the speed limit. You should slow down!")
    elif 150 < input:
        print(f"{input}km/h! You are commiting a crime! SLOW DOWN!!!")
    else:
        print("Invalid speed... Or is it driving in reverse?")

