"""Student Performance Analytics System - beginner-friendly main program."""
import pandas as pd
from functions import SUBJECT_COLUMNS, calculate_total, calculate_average, assign_grade, get_result, numerical_summary

DATA_FILE = "students.csv"

def main():
    # 1. Load the CSV file into a Pandas DataFrame.
    try:
        data = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("Error: students.csv was not found. Keep it in the same folder as main.py.")
        return

    print("=" * 68)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 68)
    print("\n1. DATASET OVERVIEW")
    print("-" * 68)
    print(data.to_string(index=False))
    print(f"\nNumber of students: {len(data)}")
    print(f"Columns: {', '.join(data.columns)}")

    # 2. Calculate totals, averages, grades and pass/fail results.
    data["Total_Marks"] = data.apply(calculate_total, axis=1)
    data["Average_Marks"] = data.apply(calculate_average, axis=1).round(2)
    data["Grade"] = data["Average_Marks"].apply(assign_grade)
    data["Result"] = data.apply(get_result, axis=1)

    print("\n2. STUDENT RESULTS")
    print("-" * 68)
    result_columns = ["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result", "Attendance"]
    print(data[result_columns].to_string(index=False))

    # 3. Overall performance using NumPy.
    print("\n3. CLASS PERFORMANCE SUMMARY")
    print("-" * 68)
    summary = numerical_summary(data["Average_Marks"])
    print(f"Highest student average: {summary['maximum']:.2f}")
    print(f"Lowest student average : {summary['minimum']:.2f}")
    print(f"Class average          : {summary['average']:.2f}")
    print(f"Students passed        : {(data['Result'] == 'Pass').sum()}")
    print(f"Students failed        : {(data['Result'] == 'Fail').sum()}")
    print(f"Average attendance     : {data['Attendance'].mean():.2f}%")

    # 4. Subject-wise performance.
    print("\n4. SUBJECT-WISE PERFORMANCE")
    print("-" * 68)
    for subject in SUBJECT_COLUMNS:  # A loop visits each subject.
        subject_summary = numerical_summary(data[subject])
        print(f"{subject.replace('_Marks', ''):16} | Average: {subject_summary['average']:.2f}"
              f" | Highest: {subject_summary['maximum']:.0f}"
              f" | Lowest: {subject_summary['minimum']:.0f}")

    # 5. Top-performing students (top 3 by average marks).
    print("\n5. TOP 3 PERFORMING STUDENTS")
    print("-" * 68)
    top_students = data.sort_values(by="Average_Marks", ascending=False).head(3)
    print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))

    # 6. Attendance alert.
    print("\n6. ATTENDANCE ALERT (below 75%)")
    print("-" * 68)
    low_attendance = data[data["Attendance"] < 75]
    if low_attendance.empty:
        print("No students have attendance below 75%.")
    else:
        print(low_attendance[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    # 7. Save the processed results for easy review.
    output_file = "student_analysis_results.csv"
    data.to_csv(output_file, index=False)
    print(f"\nFull analysis saved to: {output_file}")
    print("\nProject completed successfully.")

if __name__ == "__main__":
    main()
