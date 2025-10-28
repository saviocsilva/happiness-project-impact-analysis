import pandas as pd
import os

# --- CONFIGURATION ---
# The complete source files
COMPLETE_MAIN_SHEET_EXCEL = 'main_sheet (1).xlsx'
COMPLETE_STUDENT_ID_EXCEL = 'student_id.xlsx'

# Path to the assignments folder
ASSIGNMENTS_BASE_PATH = 'Assignments'
# Name for the final, rebuilt output file
OUTPUT_FILENAME = 'wide_sheet_FINAL_sorted.xlsx'
# --------------------

def build_wide_sheet_sorted():
    """
    Builds a new, complete wide_sheet from scratch and sorts the
    assignment columns alphabetically.
    """
    print("Building the final wide_sheet from scratch...")
    try:
        # Load the complete source files
        main_df = pd.read_excel(COMPLETE_MAIN_SHEET_EXCEL)
        student_id_df = pd.read_excel(COMPLETE_STUDENT_ID_EXCEL)
        print("Source files loaded successfully.")
    except Exception as e:
        print(f"ERROR: Could not read one of the source Excel files. Details: {e}")
        return

    # 1. Create the base of the new sheet from the student_id file
    final_wide_sheet = student_id_df[['student_id', 'Full name']].copy()
    print(f"Found {len(final_wide_sheet)} unique students to build the sheet.")

    # 2. Get a list of all unique assignments from the folder structure
    try:
        assignment_names = [name for name in os.listdir(ASSIGNMENTS_BASE_PATH) if os.path.isdir(os.path.join(ASSIGNMENTS_BASE_PATH, name))]
        print(f"Found {len(assignment_names)} unique assignments.")
    except FileNotFoundError:
        print(f"ERROR: The '{ASSIGNMENTS_BASE_PATH}' folder was not found.")
        return

    # 3. For each assignment, create a new column and check for submissions
    print("Checking submissions for each student and each assignment...")
    for assignment in assignment_names:
        submission_map = {}
        assignment_path = os.path.join(ASSIGNMENTS_BASE_PATH, assignment)
        if os.path.isdir(assignment_path):
            for dirpath, _, filenames in os.walk(assignment_path):
                for filename in filenames:
                    student_id_str = os.path.splitext(filename)[0]
                    if student_id_str.isdigit() and not filename.lower().endswith('.txt'):
                        submission_map[int(student_id_str)] = 1
        
        final_wide_sheet[assignment] = final_wide_sheet['student_id'].map(submission_map).fillna(0).astype(int)

    # --- NEW LOGIC TO SORT COLUMNS ---
    print("Sorting assignment columns alphabetically...")
    # Get the initial columns (student_id, Full name)
    info_columns = ['student_id', 'Full name']
    # Get all the assignment columns
    assignment_columns = [col for col in final_wide_sheet.columns if col not in info_columns]
    # Sort the assignment columns alphabetically
    sorted_assignment_columns = sorted(assignment_columns)
    # Recombine the columns in the new order
    final_wide_sheet = final_wide_sheet[info_columns + sorted_assignment_columns]
    
    # 4. Save the new wide sheet
    try:
        final_wide_sheet.sort_values(by='student_id', inplace=True)
        final_wide_sheet.to_excel(OUTPUT_FILENAME, index=False)
        print(f"\n--- Success! ---")
        print(f"A new, complete, and sorted wide sheet has been created and saved as '{OUTPUT_FILENAME}'")
    except Exception as e:
        print(f"ERROR: Could not save the new Excel file. Details: {e}")


if __name__ == '__main__':
    build_wide_sheet_sorted()