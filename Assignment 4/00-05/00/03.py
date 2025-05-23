
def main():
     print("(1) Farenheit to Celsius ")
     print("(2) Celsius to Farenheit ")
     choice = input("Select your choice:  ")
     if choice =="1":
         farenheit = float(input("Enter temperature in Farenheit: "))
         calc = (farenheit - 32) * 5.0/9.0
         print("Temperature in Celsius is: ", calc,"°C")
     elif choice =="2":
         celsius = float(input("Enter temperature in Celsius: "))
         calc = (celsius * 9.0/5.0) + 32
         print("Temperature in Farenheit is: ", calc,"°F")

    
if __name__ == '__main__':
    main()