# Simple Database Management System

This project is a **Simple Database Management System** developed as part of **ASSIGNMENT #3** for the CENG113 Programming Basics course. The application is designed to perform file-based data operations using a customized query language.

## Features

The program supports the following types of queries:

1. **Create File**  
   Creates a new file with the specified structure.

2. **Delete File**  
   Deletes the specified file.

3. **Display Files**  
   Displays a list of existing files.

4. **Add Line**  
   Adds a new line to the specified file.

5. **Remove Lines**  
   Removes lines from the specified file that satisfy the given condition.

6. **Modify Lines**  
   Updates lines in the specified file that satisfy the given condition.

7. **Fetch Lines**  
   Queries specific lines and columns from a file based on the given condition.

8. **Invalid Query**  
   Returns an error message for invalid queries.

9. **Program Termination**  
   Allows the user to exit the program by entering "x".

## Usage Instructions

1. Run the program.
2. Enter queries following the syntax rules:
   - Refer to [Appendix A and B](#) for example queries and syntax details.
3. All valid queries are applied to the files, and the results are displayed on the screen.
4. You can terminate the program by entering "x".

## Technical Details

- The `os` module in Python is used for file management.
- All data is stored in files, and the state is preserved even when the program restarts.
- Files are saved with the **.hw3** extension.

## Evaluation Criteria

The program was assessed based on the following criteria:

| Feature        | Points |
|----------------|--------|
| Create         | 10     |
| Delete         | 10     |
| Display        | 10     |
| Add            | 15     |
| Remove         | 15     |
| Modify         | 15     |
| Fetch          | 15     |
| Invalid Query  | 10     |
| **Total**      | **100**|

## Example Usage

Below are some example queries and outputs:

