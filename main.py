import streamlit as st

st.set_page_config(page_title="TXT File Renderer", page_icon="https://i.ibb.co/thgXZCr/0a408dc3580b4d60894d402907a5db1f-png-tplv-0es2k971ck-image.png", layout="wide")

def main():
    """
    Main function that handles the Streamlit application logic.
    """
    try:
        # Set the title of the Streamlit app
        st.title = "TXT File Renderer"  # Assign the title to the st.title attribute

        # Create a file uploader widget for users to upload a TXT file
        uploaded_file = st.file_uploader("Choose a TXT file", type="txt")

        # Check if a file has been uploaded
        if uploaded_file is not None:
            # Read and decode the uploaded file content
            content = uploaded_file.read().decode("utf-8")

            # Check if the content is not empty
            if content:
                # Display the file content using the display_file_content function
                display_file_content(content)
            else:
                # Display an error message if the file is empty
                st.error("Empty file uploaded")
    except Exception as e:
        # Display an error message if an exception occurs
        st.error(title="Error", message=f"An error occurred: {e}")

def display_file_content(content):
    try:
        lines = content.split('\n')
        current_title = ""
        current_content = ""
        placeholders = {}
        
        # Extract titles and contents, assuming titles start with '#'
        for line in lines:
            if line.startswith('#'):
                if current_title:
                    if current_title in placeholders:
                        placeholders[current_title].markdown(f"## {current_title}\n{current_content}")
                    else:
                        raise KeyError(f"Title '{current_title}' not found in placeholders")
                current_title = line.strip('#').strip()
                current_content = ""
                if current_title not in placeholders:
                    placeholders[current_title] = st.empty()
            else:
                current_content += line + '\n'
        
        if current_title:
            if current_title in placeholders:
                placeholders[current_title].markdown(f"## {current_title}\n{current_content}")
            else:
                raise KeyError(f"Title '{current_title}' not found in placeholders")
    except Exception as e:
        st.error(title="Error", message=f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(title="Error", message=f"An error occurred: {e}")
