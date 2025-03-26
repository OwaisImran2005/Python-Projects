import streamlit as st
import random

def main():
    st.title("Number Guessing Game")
    
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 50)
        st.session_state.chances = 10
        st.session_state.guess_history = []
    
    choice = st.radio(
        "Select an option:",
        ("1. Start game", "2. Quit"),
        index=None
    )
    
    if choice == "1. Start game":
        st.write("\nGAME STARTED!")
        player_name = st.text_input("Enter your name: ")
        if player_name:
            name = player_name.upper()
            st.write(f"\nAlright {name}! The rules are simple:")
            st.write("- You have to guess the number between 1 and 50")
            st.write(f"- You have {st.session_state.chances} chances to guess the correct number")
            st.write("Good luck!")
            
            guess = st.number_input(
                "ENTER YOUR GUESS (1-50):",
                min_value=1,
                max_value=50,
                key="guess_input"
            )
            
            if st.button("Submit Guess", key="submit_button"):
                st.session_state.guess_history.append(guess)
                st.session_state.chances -= 1
                
                if guess == st.session_state.number:
                    st.success(f"CONGRATULATIONS! You Guessed The Correct Number in {10 - st.session_state.chances} Attempts.")
                    st.session_state.number = random.randint(1, 50)
                    st.session_state.chances = 10
                    st.session_state.guess_history = []
                elif guess < st.session_state.number:
                    st.warning(f"The number is greater than your guess. Try again! (You have {st.session_state.chances} chances left)")
                else:
                    st.warning(f"The number is smaller than your guess. Try again! (You have {st.session_state.chances} chances left)")
                
                if st.session_state.chances == 0:
                    st.error(f"Game over! The correct number was {st.session_state.number}.")
                    st.session_state.number = random.randint(1, 50)
                    st.session_state.chances = 10
                    st.session_state.guess_history = []
    
    elif choice == "2. Quit":
        st.write("Quitting game...")
        st.stop()

if __name__ == "__main__":
    main()