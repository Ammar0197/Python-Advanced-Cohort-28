import os
from datetime import datetime

# Custom Exception
class DuplicateVisitorError(Exception):
    """Raised when the visitor is the same as the last one in the file."""
    pass

def add_visitor(filename="Visitor.txt"):
    try:
        visitor_name = input("Enter visitor's name: ").strip()
        last_visitor = None

        # If file exists, read last line
        if os.path.exists(filename):
            with open(filename, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    # Extract only the name part before the timestamp
                    last_visitor = last_line.split(" - ")[0]

        # Check for duplicate
        if last_visitor and visitor_name.lower() == last_visitor.lower():
            raise DuplicateVisitorError(f"Visitor '{visitor_name}' is already the last entry!")

        # Append visitor with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as file:
            file.write(f"{visitor_name} - {timestamp}\n")

        print(f"Visitor '{visitor_name}' added successfully.")

    except DuplicateVisitorError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "_main_":
    add_visitor()