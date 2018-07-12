# Exercise: Temperature Converter

Goal: create a program that can convert a temperature in fahrenheit, Celsius or Kelvin to the other two units.

- Try the bonus goals if you have extra time!

## Setup

- Fork and clone this repo to your computer. (or just clone)
- Write your code in `temp_converter.py`.
- Test your code by running the following the terminal...

```bash
$ python3 temp_converter.py
```

## Instructions

Ask the user for two inputs and store them in their own variables...

1.  A starting temperature value
2.  A temperature unit (e.g., f, C, K). Store each of those in a variable.

Define a `convert_temp` method that takes those two user inputs as arguments.

Inside the method, create a conditional statement that contains a block for each unit of temperature. It will look something like this...

```py
if temp_unit == "f":
  ...
elif temp_unit == "C":
  ...
else:
  ...
```

Each conditional block should convert the starting temperature to its equivalent value in the other two units (e.g., f should be converted to C and K).

- Conversion formulae: [http://www.csgnetwork.com/temp2conv.html](http://www.csgnetwork.com/temp2conv.html)
- Sample temperatures: 32f = 0C = 273.15K

Display the starting and converted values in the console.

- **NOTE:** You should only be displaying the starting and converted values for the temperature the user selected at the beginning.

```py
# User selected "f" at the start of the program. So the output is...
fahrenheit: ...
to Celsius: ...
to Kelvin: ...
```

Feel free to turn to your tablemates for help!

### Bonus 1

Store the starting and converted temperatures in a dictionary. When you print those values to the console, do it by accessing the values in the dictionary.

### Bonus 2

Keep the program running until the user decides to quit.

- **HINT:** Requires a `while` loop.
- When the program starts, the user should be prompted to enter a temperature OR quit the program.
- After the program displays the starting/converted temperatures, it should return to the initial user prompt.
