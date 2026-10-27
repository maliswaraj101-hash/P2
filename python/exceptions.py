try:
    a = 5/0
except ZeroDivisionError as e:
    print(f"Error : {e}")
    

try:
    a = 5/0
except :
    print("Error")

try:
    # code
    print("code")
except KeyError:
    print("got a keyError")
except TypeError:
    print("got a type Errro")
    
def color_checker(color : str):
    if color not in ["red" , "blue" , "green"]:
        raise ValueError("Color not present")

color_checker("yellow")


class CustomException(Exception):
    pass


a = 5

if a != 6:
    raise CustomException("This is custom exception")