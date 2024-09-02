# file_handling_assignment.py

def create_file():
    """
    Create a new text file and write initial content to it.
    """
    try:
        # Open 'my_file.txt' in write mode; this will create the file if it doesn't exist
        with open('my_file.txt', 'w') as file:
            # Write three lines of text to the file
            file.write("This is the first line of text.\n")
            file.write("Here's the second line with a number: 42\n")
            file.write("Finally, the third line is here.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File creation attempt finished.")

def read_file():
    """
    Read and display the contents of the text file.
    """
    try:
        # Open 'my_file.txt' in read mode
        with open('my_file.txt', 'r') as file:
            # Read all content
            content = file.read()
            # Print the content to the console
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File reading attempt finished.")

def append_to_file():
    """
    Append additional content to the text file.
    """
    try:
        # Open 'my_file.txt' in append mode
        with open('my_file.txt', 'a') as file:
            # Append three additional lines of text
            file.write("Appending a fourth line.\n")
            file.write("Here's a fifth line with a different message.\n")
            file.write("And a sixth line to wrap things up.\n")
        print("Additional content appended successfully.")
    except PermissionError:
        print("Error: You do not have permission to append to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File appending attempt finished.")

# Execute the functions in order
if __name__ == "__main__":
    create_file()     # Create the file and write initial content
    read_file()       # Read and display the file's content
    append_to_file()  # Append additional content to the file
    read_file()       # Read and display the file's content again to show appending
