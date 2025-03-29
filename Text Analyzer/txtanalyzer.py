import streamlit as st

st.title("Text Analysis Tool")
st.write("*******************")

text = st.text_area("TYPE A PARAGRAPH:")

if text:
    st.write("\nTotal Words in the paragraph:", len(text.split()))
    st.write("Total Characters in the paragraph:", len(text))
    st.write("Number of vowels in the paragraph:", len([char for char in text if char.lower() in 'aeiou']))
    st.write("Number of consonants in the paragraph:", len([char for char in text if char.isalpha() and char.lower() not in 'aeiou']))

    word = st.text_input("\nType a word to know how many times it appears in the paragraph:")
    if word:
        st.write(f"The word '{word}' appears", text.lower().count(word.lower()), "times in the paragraph.")

    st.title("\nWord Replacement:")
    replace = st.text_input("Enter the word you want to replace:")
    replace_with = st.text_input("Enter the word you want to replace with:")
    if replace and replace_with:
        st.title("\nParagraph after replacing the word:")
        st.write("************************************")
        st.write(text.replace(replace, replace_with))

    st.title("\nParagraph in uppercase:")
    st.write(text.upper())

    st.title("\nParagraph in lowercase:")
    st.write(text.lower())

    if len(text.split()) > 0:
        avg_length = sum(len(word) for word in text.split()) / len(text.split())
        st.write("\n\nAverage word length:", round(avg_length, 2))