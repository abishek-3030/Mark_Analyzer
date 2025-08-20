from fetch_data import get_data
from analysis import compute_statistics
from visualization import plot_subject_averages, plot_heatmap
from recommendations import generate_recommendations

# Step 1: Load data from Excel
df = get_data()

# Step 2: Analyze
df, top_students, subject_averages, subject_columns = compute_statistics(df)

# Step 3: Visualize
plot_subject_averages(subject_averages)
plot_heatmap(df, subject_columns)

# Step 4: Recommend
recommendations = generate_recommendations(df, subject_columns)

print("\n📌 Subject-wise Focus Recommendations:")
for subject, students in recommendations.items():
    print(f"➤ {subject}: {', '.join(students)}")