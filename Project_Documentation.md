# Project Documentation: Student Performance Analytics System

**Student Name:** [Sanjana]   
**Course:** Python with AI  
**Project Title:** Student Performance Analytics System

## 1. Objective
The objective is to create a beginner-friendly Python application that reads student data and turns marks and attendance into an understandable performance report. It helps identify strong performance, students who need support, and subject-level trends.

## 2. Technologies Used
- Python 3
- Pandas for reading CSV data and working with DataFrames
- NumPy for minimum, maximum and average calculations
- CSV for storing the student dataset

## 3. Dataset Description
The project uses `students.csv`, a sample dataset with 20 student records. Each record includes Student ID, Name, Department, marks in Python, AI and Database, and Attendance percentage. Each subject mark is out of 100.

## 4. Implementation
1. `main.py` loads `students.csv` using `pandas.read_csv()`.
2. The program displays the dataset and the number of records.
3. Functions in `functions.py` calculate total marks and average marks.
4. A grading function assigns a grade based on the average.
5. A pass/fail function checks each subject; a mark below 40 in any subject means Fail.
6. NumPy calculates minimum, maximum and average values.
7. A loop prints subject-wise summaries.
8. Pandas sorting identifies the top three students.
9. Pandas filtering identifies students with attendance below 75%.
10. The final DataFrame is saved as `student_analysis_results.csv`.

## 5. Grading Rule
- A+: average >= 90
- A: average >= 80 and below 90
- B: average >= 70 and below 80
- C: average >= 60 and below 70
- D: average >= 50 and below 60
- F: average below 50

**Pass condition:** at least 40 marks in every subject.

## 6. Key Features
- Reads and displays 20 student records.
- Calculates each student's total and average marks.
- Assigns grades and pass/fail status.
- Reports highest, lowest and class-average performance.
- Counts passed and failed students.
- Summarizes average, highest and lowest marks for each subject.
- Lists the top three students.
- Flags attendance below 75%.
- Exports the results to a new CSV file.

## 7. Output / Screenshots
Run `python main.py` and take screenshots of:
1. Dataset overview.
2. Student results and grades.
3. Class performance and subject-wise summaries.
4. Top performers and attendance alerts.

Insert the screenshots here before final submission.

## 8. Final Outcome
The project demonstrates how Python, Pandas and NumPy can be used to analyze student marks and attendance. It produces a readable report and a processed CSV file that can be opened in spreadsheet software.

## 9. Challenges and Learning
**Example points to personalize after testing:**
- Learned how to load a CSV file into a Pandas DataFrame.
- Practiced functions, conditions and loops.
- Learned to use NumPy for numerical summaries.
- Used sorting and filtering to find top performers and low-attendance students.
- Learned to export analyzed data to a new CSV file.

Replace or edit these points to reflect the challenges you personally encountered.

## 10. GitHub Repository
**Repository URL:** [Paste your GitHub repository URL here after uploading]

## 11. Testing Checklist
- [ ] Installed dependencies from `requirements.txt`
- [ ] Ran `python main.py` successfully
- [ ] Checked that `student_analysis_results.csv` was created
- [ ] Added screenshots
- [ ] Added student name and ID
- [ ] Uploaded code, dataset, README and documentation to GitHub
- [ ] Verified repository visibility
- [ ] Submitted repository URL through the trainer's Google Form
