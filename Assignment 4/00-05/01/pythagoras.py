import math 

def main():
    
    P: float = float(input("Enter the value of P: "))
    B: float = float(input("Enter the value of B: "))

    
    H: float = math.sqrt(P**2 + B**2)
    print("The length of H  is: " + str(H))


if __name__ == '__main__':
    main()