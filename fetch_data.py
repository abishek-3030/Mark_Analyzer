import pandas as pd

def get_data():
    # Replace with your file name if different
    df = pd.read_excel("student_marks.xlsx")
    return df