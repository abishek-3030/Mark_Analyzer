import matplotlib.pyplot as plt
import seaborn as sns

def plot_subject_averages(subject_averages):
    plt.figure(figsize=(10,6))
    sns.barplot(x=subject_averages.index, y=subject_averages.values)
    plt.title("Subject-wise Average Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_heatmap(df, subject_columns):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[subject_columns], annot=True, cmap="YlGnBu", xticklabels=subject_columns, yticklabels=df.iloc[:,0])
    plt.title("Student Performance Heatmap")
    plt.tight_layout()
    plt.show()