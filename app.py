import streamlit as st
from search_helper import search_collection

def search_interface(query):
    # Calls the backend function and returns the results
    return search_collection(query)

def main():
    # Set the title of the app
    st.markdown("# Telugu Proverbs Search")

    # Create a text input for the search query
    query = st.text_input("Enter your search query:", placeholder="Type something...")

    # When the Search button is clicked, call the search function
    if st.button("Search"):
        # Get the search results from the backend function
        results = search_interface(query)
        
        # Optionally, if results is not a string, convert it to one
        if not isinstance(results, str):
            results = str(results)
        
        # Display the search results in a text area
        st.text_area("Search Results", value=results, height=200)
