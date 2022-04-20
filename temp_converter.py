banana = {
    1: "",
    2: ""
}


def convert_temp(unit, val):
    if unit == "c":
        banana[1] = ("Fahrenheit: " + str((val*9/5)+32))
        banana[2] = ("Kelvin: " + str(val + 273.15))
    elif unit == "k":
        banana[1] = ("Celsius: " + str(val - 273.15))
        banana[2] = ("Fahrenheit: " + str(((val-273.15)*9/5)+32))
    elif unit == "f":
        banana[1] = ("Kelvin: " + str(((val-32)*5/9)+273.15))
        banana[2] = ("Celsius: " + str((val-32)*5/9))


unit = input("Enter Unit type: ")
value = input("Enter Value: ")
convert_temp(unit, int(value))

print(banana)
