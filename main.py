import streamlit as st

# Streamlit application for uploading and displaying a text file
def main():
    """
    Main function that handles the Streamlit application logic.
    """
    try:
        # Set the title of the Streamlit app
        st.title("TXT File Renderer")

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
    """
    Display the content of a text file with titles and sections.

    Args:
        content (str): The content of the text file.

    Raises:
        KeyError: If a title is not found in the placeholders.
    """
    try:
        lines = content.split('\n')
        current_title = ""
        current_content = ""
        placeholders = {}
        
        # Extract titles and contents, assuming titles start with '#'
        for line in lines:
            if line.startswith('#'):
                # If a title is found, display the current content and title
                if current_title:
                    if current_title in placeholders:
                        placeholders[current_title].markdown(f"## {current_title}\n{current_content}")
                    else:
                        raise KeyError(f"Title '{current_title}' not found in placeholders")
                
                # Update the current title and content
                current_title = line.strip('#').strip()
                current_content = ""
                if current_title not in placeholders:
                    placeholders[current_title] = st.empty()
            else:
                # Update the current content
                current_content += line + '\n'
        
        # Display the last title and content
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
