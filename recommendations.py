def generate_recommendations(df, subject_columns):
    df['Weakest Subject'] = df[subject_columns].idxmin(axis=1)
    recommendations = df.groupby('Weakest Subject')[df.columns[0]].apply(list)
    return recommendations