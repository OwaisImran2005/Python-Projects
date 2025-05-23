

c: int = 299792458  

def main():
    mass: float = float(input("Enter mass in kilos: "))
    energy: float = mass * (c ** 2)

    print(f"m =  {mass} kg")
    print(f"C =  {c} m/s")
    
    print("Energy = " ,energy , "joules")

if __name__ == '__main__':
    main()



