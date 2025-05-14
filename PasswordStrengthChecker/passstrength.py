
import re
import streamlit as st

def check_password_strength(password):
    score = 0
    
    if len(password) < 8:
        st.error("❌ Password should be more than 8 characters")
        return
    elif 8 <= len(password) <= 16:
        score += 1
    else:
        score += 2
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        st.warning("⚠️ Missing uppercase letter (A-Z)")
    
    if re.search(r"[0-9]", password):
        score += 1
    else:
        st.warning("⚠️ Missing number (0-9)")
    
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 2
    else:
        st.warning("⚠️ Missing special character (!@#$...)")
    
    if score >= 5:
        st.success("✅ Excellent! Strong password 🔒")
    elif score == 4:
        st.warning("🟢 Good password, but could be stronger")
    elif score == 3:
        st.warning("🟡 Fair password - add more complexity")
    else:
        st.error("🔴 Weak password - needs improvement")

def main():
    st.title("🔐 Password Strength Checker")
    st.write("Type your password to see its strength:")
    
    password = st.text_input("Password:", 
                           type="password",
                           key="pwd_input",
                           placeholder="Type here...")
    
    if password:
        check_password_strength(password)
        
    st.write("\n")
    st.caption("💡 Tip: Use a mix of uppercase, numbers, and special characters")

if __name__ == "__main__":
    main()