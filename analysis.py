def compute_statistics(df):
    subject_columns = df.columns[1:]  # Assuming 1st column is student name
    df['Total Marks'] = df[subject_columns].sum(axis=1)
    df['Average Marks'] = df[subject_columns].mean(axis=1)
    top_students = df.sort_values(by='Total Marks', ascending=False).head(5)
    subject_averages = df[subject_columns].mean().sort_values(ascending=False)
    return df, top_students, subject_averages, subject_columns