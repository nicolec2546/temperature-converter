print("Welcome to Temperature Converter, a lightweight utillity for convertering temperatures.")

#Create variables for the unit that is being converted and the temperature
unit = input("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature you want converted: "))

#Function that converts C to F
def c_to_f(temp_c):
    converted_c = temp_c * (9/5 + 32)
    return converted_c
#Function that converts F to C
def f_to_c(temp_f):
    converted_f = (temp_f - 32) * (5/9)
    return converted_f

#Function that converts K to F
def k_to_f(temp_k):
    converted_k = (temp_k - 273.15) * 9/5 + 32
    return converted_k

#Function that converts F to K
def f_to_k(temp_f2):
    converted_f2 = (temp_f2 - 32) * 5/9 + 273.15
    return converted_f2


#Main function that uses conditionals to decide which convert function to select
def main():
    if(unit == "C"):
        celsius_to_fahrenheit = c_to_f(value)
        return celsius_to_fahrenheit
    elif(unit == "F"):
       if(unit = "K")
        fahrenheit_to_celsius = f_to_c(value)
        return fahrenheit_to_celsius
       else
        kelvin_to_fahrenheit = k_to_f(value)
        return kelvin_to_fahrenheit
    elif(unit == "K")
        fahrenheit_to_kelvin = f_to_k
        return fahrenheit_to_kelvin
    else:
        warning = "Please enter C, F, or K to specify the unit: " 
        return warning


#Print results
result = main()
print("Your value is: " + str(result))