print("\n") 
print("\n") 

print("UNIT CONVERTOR")    
print("***************")  
print("\n") 

print("Select from the options below : ")
print("\n")

print("(1) TEMPERATURE")
print("(2) LENGTH")
print("(3) SPEED")
print("(4) WEIGHT")

print("\n")
select1 = int(input("Enter your choice : "))
print("\n")
 


# Temperature Conversion
if select1 == 1:
        print("(1) F to C ")
        print("(2) C to F ")
        print("\n")
        select2 = int(input("Enter your choice : "))
        
        if select2 == 1:
            f = float(input("Enter the temperature in Fahrenheit : "))
            c = (f - 32) * 5/9
            print(f"The temperature in Celsius is {c} C")
        elif select2 == 2:
            c = float(input("Enter the temperature in Celsius : "))
            f = (c * 9/5) + 32
            print(f"The temperature in Fahrenheit is {f} F")
        else:
            print("Invalid choice!")



 # Length Conversion
elif select1 == 2:
    print("(1) M to KM ")
    print("(2) KM to M ")
    print("(3) M to CM ")
    print("(4) CM to M ")
    print("(5) inch to CM ")
    print("(6) CM to inch ")
    select2 = int(input("Enter your choice : "))
    
    if select2 == 1:
        m = float(input("Enter the length in Metres : "))
        km = m / 1000
        print(f"The length in Kilometres is {km} km")
    elif select2 == 2:
        km = float(input("Enter the length in Kilometres : "))
        m = km * 1000
        print(f"The length in Metres is {m} m")
    elif select2 == 3:
          m = float(input("Enter the length in Metres : "))
          cm = m * 100
          print(f"The length in Centimetres is {cm} cm")
    elif select2 == 4:
          cm = float(input("Enter the length in Centimetres : "))
          m = cm / 100
          print(f"The length in Metres is {m} m")
    elif select2 == 5:
          inch = float(input("Enter the length in Inches : "))
          cm = inch * 2.54
          print(f"The length in Centimetres is {cm} cm")

    elif select2 == 6:
          cm = float(input("Enter the length in Centimetres : "))
          inch = cm / 2.54
          print(f"The length in Inches is {inch} inch")
    else:
            print("Invalid choice!")





elif select1 == 3:
      print("(1) KM/H to M/S ")
      print("(2) M/S to KM/H ")
      select2 = int(input("Enter your choice : "))

      if select2 == 1:
         kmh = float(input("Enter the speed in KM/H : "))
         ms = kmh / 3.6
         print(f"The speed in M/S is {ms} m/s")

      elif select2 == 2:
            ms = float(input("Enter the speed in M/S : "))
            kmh = ms * 3.6
            print(f"The speed in KM/H is {kmh} km/h")
      else:
            print("Invalid choice!")


elif select1 == 4:
           print("(1) KG to G ")
           print("(2) G to KG ")
           select2 = int(input("Enter your choice : "))

           if select2 == 1:
               kg = float(input("Enter the weight in Kilograms : "))
               g = kg * 1000
               print(f"The weight in Grams is {g} g")

           elif select2 == 2:
                  g = float(input("Enter the weight in Grams : "))
                  kg = g / 1000
                  print(f"The weight in Kilograms is {kg} kg")
           else:
                  print("Invalid choice!")

else:
      print("Invalid choice!")
