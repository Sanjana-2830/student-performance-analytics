"""Reusable functions for the Student Performance Analytics System."""
import numpy as np

SUBJECT_COLUMNS = ["Python_Marks", "AI_Marks", "Database_Marks"]

def calculate_total(row):
    """Return total marks across the three subjects."""
    return sum(row[subject] for subject in SUBJECT_COLUMNS)

def calculate_average(row):
    """Return average marks across the three subjects."""
    return calculate_total(row) / len(SUBJECT_COLUMNS)

def assign_grade(average):
    """Assign a grade using the project's grading rules."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def get_result(row):
    """A student passes only if every subject mark is at least 40."""
    for subject in SUBJECT_COLUMNS:
        if row[subject] < 40:
            return "Fail"
    return "Pass"

def numerical_summary(values):
    """Use NumPy to calculate minimum, maximum and mean."""
    numbers = np.array(values, dtype=float)
    return {
        "minimum": float(np.min(numbers)),
        "maximum": float(np.max(numbers)),
        "average": float(np.mean(numbers))
    }
