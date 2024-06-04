import streamlit as st
from io import BytesIO

# Streamlit application for uploading and displaying a text file
def main():
    st.title("TXT File Renderer")

    uploaded_file = st.file_uploader("Choose a TXT file", type="txt")

    if uploaded_file is not None:
        # Read and display the uploaded file
        content = uploaded_file.read().decode("utf-8")
        
        # Display the content using the same rendering method as in the Book class
        display_file_content(content)

def display_file_content(content):
    lines = content.split('\n')
    current_title = ""
    current_content = ""
    placeholders = {}
    
    # Extract titles and contents, assuming titles start with '#'
    for line in lines:
        if line.startswith('#'):
            if current_title:
                placeholders[current_title].markdown(f"## {current_title}\n{current_content}")
            current_title = line.strip('#').strip()
            current_content = ""
            if current_title not in placeholders:
                placeholders[current_title] = st.empty()
        else:
            current_content += line + '\n'
    
    if current_title:
        placeholders[current_title].markdown(f"## {current_title}\n{current_content}")

if __name__ == "__main__":
    main()
