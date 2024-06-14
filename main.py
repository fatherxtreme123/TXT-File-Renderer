import streamlit as st

st.set_page_config(page_title="TXT File Renderer", page_icon="https://i.ibb.co/thgXZCr/0a408dc3580b4d60894d402907a5db1f-png-tplv-0es2k971ck-image.png", layout="wide")

def main():
    """
    Main function that handles the Streamlit application logic.
    """
    try:
        # Set the title of the Streamlit app
        st.title("TXT File Renderer")

        # Create a file uploader widget for users to upload a TXT file
        uploaded_file = st.file_uploader(
            "Choose a TXT file",  # Label for the file uploader
            type="txt"  # Type of file to upload
        )

        # Check if a file has been uploaded
        if uploaded_file is not None:
            # Read and decode the uploaded file content
            content = uploaded_file.read().decode("utf-8")

            # Check if the content is not empty
            if content:
                display_file_content(content)  # Display the file content
            else:
                st.error("Empty file uploaded")  # Display an error for empty file
    except FileNotFoundError:
        st.error("File not found")  # Display an error for file not found
    except UnicodeDecodeError:
        st.error("Failed to decode file content")  # Display an error for decoding error
    except Exception as e:
        st.error(title="Error", message=f"An error occurred: {e}")  # Display a general error message

def display_file_content(content):
    """
    Display the content of a TXT file with titles.

    Args:
        content (str): The content of the TXT file.

    Raises:
        FileNotFoundError: If the file is not found.
        UnicodeDecodeError: If the file content fails to decode.
        KeyError: If a title is not found in the placeholders.
        ValueError: If a content line is encountered before a title.
    """
    try:
        lines = content.split('\n')
        current_title = ""
        current_content = ""
        placeholders = {}
        
        # Iterate through the lines of the content
        for line in lines:
            if line.startswith('#'):
                # If a title line is encountered
                
                # If there is a current title, display its content
                if current_title:
                    if current_title in placeholders:
                        placeholders[current_title].markdown(f"## {current_title}\n{current_content}")
                    else:
                        raise KeyError(f"Title '{current_title}' not found in placeholders")
                
                # Set the current title and reset the content
                current_title = line.strip('#').strip()
                current_content = ""
                
                # Add an empty placeholder for the current title
                if current_title not in placeholders:
                    placeholders[current_title] = st.empty()
            else:
                # If a content line is encountered
                
                # If there is a current title, add the line to the content
                if current_title:
                    current_content += line + '\n'
                else:
                    # If there is no current title, raise a ValueError
                    raise ValueError("Encountered content line before a title")
        
        # If there is a current title, display its content
        if current_title:
            if current_title in placeholders:
                placeholders[current_title].markdown(f"## {current_title}\n{current_content}")
            else:
                raise KeyError(f"Title '{current_title}' not found in placeholders")
    
    # Handle exceptions
    except FileNotFoundError:
        st.error("File not found")
    except UnicodeDecodeError:
        st.error("Failed to decode file content")
    except (KeyError, ValueError) as e:
        st.error(title="Error", message=f"An error occurred: {e}")


# This block of code runs the main function if the script is run directly
if __name__ == "__main__":
    """
    This block handles the main execution of the script.
    It runs the main function and catches any exceptions that may occur.
    """
    try:
        # Run the main function
        main()
    except FileNotFoundError:
        """
        If a FileNotFoundError occurs, display an error message.
        """
        st.error("File not found")
    except UnicodeDecodeError:
        """
        If a UnicodeDecodeError occurs, display an error message.
        """
        st.error("Failed to decode file content")
    except (KeyError, ValueError) as e:
        """
        If a KeyError or ValueError occurs, display an error message.
        """
        st.error(title="Error", message=f"An error occurred: {e}")
    except Exception as e:
        """
        If any other exception occurs, display an error message.
        """
        st.error(title="Error", message=f"An unexpected error occurred: {e}")
