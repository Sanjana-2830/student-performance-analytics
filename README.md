# Student Performance Analytics System

**Project type:** Python data-analysis mini project  
**Level:** Beginner  
**Technologies:** Python 3, Pandas, NumPy, CSV

## 1. Objective
This project reads student records from a CSV file and analyzes marks and attendance. It calculates total and average marks, assigns grades, identifies pass/fail results, compares subject performance, lists top students, and saves the processed results.

## 2. Dataset
`students.csv` contains 20 sample student records with these columns:
- `Student_ID`: unique student identifier
- `Name`: student name
- `Department`: department name
- `Python_Marks`, `AI_Marks`, `Database_Marks`: marks out of 100
- `Attendance`: attendance percentage

The names and marks are sample data created for this educational project.

## 3. Grading and pass rules
Grades are based on the average of the three subjects:
- A+: 90 and above
- A: 80–89.99
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- F: below 50

A student passes only when they score at least 40 in **each** subject.

## 4. Project files
- `main.py` — runs the analysis and displays the results
- `functions.py` — reusable calculation, grade and result functions; uses NumPy
- `students.csv` — input dataset with 20 records
- `requirements.txt` — required Python libraries
- `Project_Documentation.md` — report template/content for submission
- `student_analysis_results.csv` — generated after running `main.py`

## 5. Setup and run
Install Python 3.10 or newer, then open a terminal in this folder.

```bash
python -m pip install -r requirements.txt
python main.py
```

On some Windows installations, use `py main.py` instead of `python main.py`.

The program prints the dataset, student results, class summary, subject-wise summary, top 3 performers and students with attendance below 75%. It also creates `student_analysis_results.csv`.

## 6. Concepts demonstrated
Variables, data types, functions, loops, conditions, CSV file handling, Pandas DataFrames, filtering, sorting, and NumPy numerical calculations.

## 7. Limitations
The sample data is illustrative, not real institutional data. The program assumes marks are numeric and on a 0–100 scale. It does not use machine learning because the assignment does not require advanced ML.

## 8. Before submitting
1. Run the program and check the output.
2. Take screenshots of the terminal output and place them in your documentation if required.
3. Add your own name/student details to `Project_Documentation.md`.
4. Create a public GitHub repository named `student-performance-analytics` (or as instructed).
5. Upload all project files and verify they are visible.
6. Copy the repository URL into the EWB Google Form provided by your trainer. The form URL was not included in the assignment PDF, so obtain it from your trainer.
