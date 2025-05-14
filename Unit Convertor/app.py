import streamlit as st

def main():
    st.title("📏 UNIT CONVERTOR")
    st.write("***************")
    
    st.write("Select from the options below:")
    option = st.radio(
        "",
        ("(1) TEMPERATURE", "(2) LENGTH", "(3) SPEED", "(4) WEIGHT"),
        index=None
    )
    
    if option == "(1) TEMPERATURE":
        temp_option = st.radio(
            "Temperature Conversion:",
            ("(1) F to C", "(2) C to F"),
            index=None
        )
        
        if temp_option == "(1) F to C":
            f = st.number_input("Enter the temperature in Fahrenheit:")
            if f is not None:
                c = (f - 32) * 5/9
                st.success(f"The temperature in Celsius is {c:.2f} °C")
                
        elif temp_option == "(2) C to F":
            c = st.number_input("Enter the temperature in Celsius:")
            if c is not None:
                f = (c * 9/5) + 32
                st.success(f"The temperature in Fahrenheit is {f:.2f} °F")
    
    elif option == "(2) LENGTH":
        length_option = st.radio(
            "Length Conversion:",
            ("(1) M to KM", "(2) KM to M", "(3) M to CM", 
             "(4) CM to M", "(5) inch to CM", "(6) CM to inch"),
            index=None
        )
        
        if length_option == "(1) M to KM":
            m = st.number_input("Enter the length in Metres:")
            if m is not None:
                km = m / 1000
                st.success(f"The length in Kilometres is {km:.4f} km")
                
        elif length_option == "(2) KM to M":
            km = st.number_input("Enter the length in Kilometres:")
            if km is not None:
                m = km * 1000
                st.success(f"The length in Metres is {m:.2f} m")
                
        elif length_option == "(3) M to CM":
            m = st.number_input("Enter the length in Metres:")
            if m is not None:
                cm = m * 100
                st.success(f"The length in Centimetres is {cm:.2f} cm")
                
        elif length_option == "(4) CM to M":
            cm = st.number_input("Enter the length in Centimetres:")
            if cm is not None:
                m = cm / 100
                st.success(f"The length in Metres is {m:.2f} m")
                
        elif length_option == "(5) inch to CM":
            inch = st.number_input("Enter the length in Inches:")
            if inch is not None:
                cm = inch * 2.54
                st.success(f"The length in Centimetres is {cm:.2f} cm")
                
        elif length_option == "(6) CM to inch":
            cm = st.number_input("Enter the length in Centimetres:")
            if cm is not None:
                inch = cm / 2.54
                st.success(f"The length in Inches is {inch:.2f} inch")
    
    elif option == "(3) SPEED":
        speed_option = st.radio(
            "Speed Conversion:",
            ("(1) KM/H to M/S", "(2) M/S to KM/H"),
            index=None
        )
        
        if speed_option == "(1) KM/H to M/S":
            kmh = st.number_input("Enter the speed in KM/H:")
            if kmh is not None:
                ms = kmh / 3.6
                st.success(f"The speed in M/S is {ms:.2f} m/s")
                
        elif speed_option == "(2) M/S to KM/H":
            ms = st.number_input("Enter the speed in M/S:")
            if ms is not None:
                kmh = ms * 3.6
                st.success(f"The speed in KM/H is {kmh:.2f} km/h")
    
    elif option == "(4) WEIGHT":
        weight_option = st.radio(
            "Weight Conversion:",
            ("(1) KG to G", "(2) G to KG"),
            index=None
        )
        
        if weight_option == "(1) KG to G":
            kg = st.number_input("Enter the weight in Kilograms:")
            if kg is not None:
                g = kg * 1000
                st.success(f"The weight in Grams is {g:.2f} g")
                
        elif weight_option == "(2) G to KG":
            g = st.number_input("Enter the weight in Grams:")
            if g is not None:
                kg = g / 1000
                st.success(f"The weight in Kilograms is {kg:.4f} kg")

if __name__ == "__main__":
    main()
