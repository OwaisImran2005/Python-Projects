

Inches_In_Foot: int = 12  

def main():
    feet: float = float(input("Enter number of feet: "))  
    inches: float = feet * Inches_In_Foot  
    print(f"{inches} inches in {feet} feet")
    
    
if __name__ == '__main__':
    main()