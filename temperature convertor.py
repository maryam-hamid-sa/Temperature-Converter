# temperature conversion
temperature = float(input("Enter temperature value: "))
unit = str(input("Convert to Celsius or Fahrenheit(C/F): "))
 
if unit == "C" or unit == "c":
    print("Temperature in Celsius:", (temperature - 32) * (5 / 9), "C")
elif unit == "F" or unit == "f":
    print("Temperature in Fahrenheit:", (temperature * (9 / 5)) + 32, "F")
else:
    print("not the required scale")
