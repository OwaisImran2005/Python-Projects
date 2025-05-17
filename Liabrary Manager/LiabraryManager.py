import streamlit as st


if 'books' not in st.session_state:
    st.session_state.books = {}

st.title("📚 Personal Library Manager")


menu = st.sidebar.selectbox(
    "Menu Options",
    ["Add Book", "Remove Book", "Search Book", "View All Books", "Statistics", "Exit"]
)

if menu == "Add Book":
    st.header("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Book Title").lower()
        book_type = st.selectbox(
            "Book Type",
            ["Fiction", "Non-Fiction", "Science", "Biography", "Other"]
        )
        author = st.text_input("Author")
        year = st.text_input("Publication Year")
        read_status = st.radio("Have you read this book?", ("Yes", "No"))
        
        if st.form_submit_button("Add Book"):
            if title and author and year:
                st.session_state.books[title] = {
                    "type": book_type,
                    "author": author,
                    "year": year,
                    "read": read_status == "Yes"
                }
                st.success(f"Book '{title}' added successfully!!!")
            else:
                st.warning("Please fill in all fields")

elif menu == "Remove Book":
    st.header("🗑️ Remove a Book")
    title = st.text_input("Enter the book title to remove:").lower()
    
    if st.button("Remove Book"):
        if title in st.session_state.books:
            del st.session_state.books[title]
            st.success(f"Book '{title}' removed successfully!")
        else:
            st.error(f"Book '{title}' not found in the library.")

elif menu == "Search Book":
    st.header("🔍 Search for a Book")
    title = st.text_input("Enter the book title to search for:").lower()
    
    if st.button("Search"):
        if title in st.session_state.books:
            book = st.session_state.books[title]
            st.success("Book found:")
            st.write(f"**Title:** {title}")
            st.write(f"**Type:** {book['type']}")
            st.write(f"**Author:** {book['author']}")
            st.write(f"**Year:** {book['year']}")
            st.write(f"**Read:** {'Yes' if book['read'] else 'No'}")
        else:
            st.error(f"Book '{title}' not found in the library.")

elif menu == "View All Books":
    st.header("📖 All Books in Library")
    
    if not st.session_state.books:
        st.warning("The library is empty!")
    else:
        for title, details in st.session_state.books.items():
            st.subheader(title.title())
            st.write(f"**Type:** {details['type']}")
            st.write(f"**Author:** {details['author']}")
            st.write(f"**Year:** {details['year']}")
            st.write(f"**Read:** {'Yes' if details['read'] else 'No'}")
            st.write("---")

elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total_books = len(st.session_state.books)
    
    st.write(f"**Total books:** {total_books}")
    
    if total_books > 0:
        read_count = sum(1 for book in st.session_state.books.values() if book['read'])
        st.write(f"**Books read:** {read_count}")
        st.write(f"**Books unread:** {total_books - read_count}")
        
       
        types = {}
        for book in st.session_state.books.values():
            types[book['type']] = types.get(book['type'], 0) + 1
        
        st.write("\n**Books by type:**")
        for book_type, count in types.items():
            st.write(f"- {book_type}: {count}")

elif menu == "Exit":
    st.success("Exiting the library manager. Goodbye!")
    st.stop()