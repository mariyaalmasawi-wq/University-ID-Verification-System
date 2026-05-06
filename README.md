🎓 University ID Verification System
A Python program that validates university ID numbers using regular expressions.
The system extracts valid IDs from user‑entered sentences, removes duplicates, and checks whether each ID follows the correct format (starting with 44, 45, or 46 and followed by 7 digits).

Note: This project was written in simple English to make it easy for learners to understand.
----------------------------------------------
🚀 Features
Validates university ID numbers using a precise regex pattern

Accepts full sentences, not just numbers

Extracts only the correct ID even if multiple numbers appear

Removes duplicate inputs using a set()

Separates logic into a module file and a main file for clarity
---------------------------------------------
🧠 How It Works
The module file contains two functions:

match() → checks if the phrase contains a valid ID

matching_parts() → extracts the ID from the phrase

The main file collects user input until “done” is entered

Each phrase is validated and the extracted ID is displayed
----------------------------------------------
📂 File Structure
University-ID-Verification-System/
│
├── id_validator_module.py     # Regex functions
├── id_verification_main.py    # Main program (user interaction)
└── README.md
----------------------------------------------
▶️ How to Run
Make sure Python is installed

Run the main file: python id_verification_main.py
----------------------------------------------
🧪 Example Output
Input: my name is sara and my ID is 451220890
Valid: Yes
Extracted ID: 451220890
