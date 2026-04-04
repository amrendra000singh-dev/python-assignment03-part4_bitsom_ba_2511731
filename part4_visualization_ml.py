import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

load data set....
import panda as pd

csv_path = 'students.csv'
df = pd.read_csv('students.csv')
df.head()
# 1. Show first 5 rows
print('First 5 rows:')
print(df.head(),

# 2. Shape and data types
print('Shape:', df.shape)
print('\nData types:')
print(df.dtypes),

# 3. Summary statistics for numeric columns
print('Summary statistics:')
print(df.describe(),)
# 4. Count of students who passed and failed
print('Passed/Failed counts:')
print(df['passed'].value_counts(),

# 5. Average score per subject for passing and failing students
subject_cols = ['math', 'science', 'english', 'history', 'pe']
print('Average scores for passing students:')
print(df[df['passed'] == 1][subject_cols].mean(),
print('Average scores for failing students:')
print(df[df['passed'] == 0][subject_cols].mean(), 

# 6. Student with highest overall average across all 5 subjects
# Add avg_score column for later visualization

df['avg_score'] = df[subject_cols].mean(axis=1)
best_student = df.loc[df['avg_score'].idxmax()]
print('Student with highest overall average:')
print(best_student[['name', 'avg_score']], 

# Task 2: Data visualization with Matplotlib

# Plot 1: Bar chart of average score per subject

subject_means = df[subject_cols].mean()
plt.figure(figsize=(8, 5))
plt.bar(subject_means.index, subject_means.values, color='skyblue', edgecolor='black')
plt.title('Average Score per Subject')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('plot1_bar.png', bbox_inches='tight')
plt.show()
plt.close()

# Plot 2: Histogram of math scores
math_mean = df['math'].mean()
plt.figure(figsize=(8, 5))
plt.hist(df['math'], bins=5, color='salmon', edgecolor='black')
plt.axvline(math_mean, color='blue', linestyle='--', linewidth=2, label=f'Mean = {math_mean:.2f}')
plt.title('Distribution of Math Scores')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('plot2_histogram.png', bbox_inches='tight')
plt.show()
plt.close()

# Plot 3: Scatter plot of study hours vs avg_score
pass_df = df[df['passed'] == 1]
fail_df = df[df['passed'] == 0]
plt.figure(figsize=(8, 5))
plt.scatter(pass_df['study_hours_per_day'], pass_df['avg_score'], color='green', label='Pass', s=80, alpha=0.7, edgecolor='black')
plt.scatter(fail_df['study_hours_per_day'], fail_df['avg_score'], color='red', label='Fail', s=80, alpha=0.7, edgecolor='black')
plt.title('Study Hours per Day vs Average Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Average Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('plot3_scatter.png', bbox_inches='tight')
plt.show()
plt.close()

# Plot 4: Box plot of attendance percentage for pass vs fail students
pass_attendance = pass_df['attendance_pct'].tolist()
fail_attendance = fail_df['attendance_pct'].tolist()
plt.figure(figsize=(8, 5))
plt.boxplot([pass_attendance, fail_attendance], labels=['Pass', 'Fail'])
plt.title('Attendance Percentage for Pass vs Fail Students')
plt.xlabel('Outcome')
plt.ylabel('Attendance Percentage')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('plot4_box.png', bbox_inches='tight')
plt.show()
plt.close()

# Plot 5: Line plot of math and science scores for each student
plt.figure(figsize=(12, 6))
plt.plot(df['name'], df['math'], marker='o', linestyle='-', label='Math')
plt.plot(df['name'], df['science'], marker='s', linestyle='--', label='Science')
plt.title('Math and Science Scores by Student')
plt.xlabel('Student Name')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('plot5_line.png', bbox_inches='tight')
plt.show()
plt.close()

# Task 3: Seaborn visualizations

# Seaborn bar plots: average math and science score split by passed
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
sns.barplot(data=df, x='passed', y='math', ax=ax1, palette='Blues_d')
ax1.set_title('Average Math Score by Pass/Fail')
ax1.set_xlabel('Passed')
ax1.set_ylabel('Average Math Score')
sns.barplot(data=df, x='passed', y='science', ax=ax2, palette='Greens_d')
ax2.set_title('Average Science Score by Pass/Fail')
ax2.set_xlabel('Passed')
ax2.set_ylabel('Average Science Score')
plt.suptitle('Average Scores by Subject and Pass/Fail')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('plot6_seaborn_bars.png', bbox_inches='tight')
plt.show()
plt.close()

# Seaborn scatter plot with regression lines
plt.figure(figsize=(8, 6))
sns.scatterplot(data=pass_df, x='attendance_pct', y='avg_score', color='green', label='Pass')
sns.scatterplot(data=fail_df, x='attendance_pct', y='avg_score', color='red', label='Fail')
sns.regplot(data=pass_df, x='attendance_pct', y='avg_score', scatter=False, color='green', label='Pass Trend')
sns.regplot(data=fail_df, x='attendance_pct', y='avg_score', scatter=False, color='red', label='Fail Trend')
plt.title('Attendance Percentage vs Average Score by Pass/Fail')
plt.xlabel('Attendance Percentage')
plt.ylabel('Average Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('plot7_seaborn_scatter.png', bbox_inches='tight')
plt.show()
plt.close()
please find out details below........
   ------------------------------------------------
               ----------------------------------------------------------------------
# Comparing Seaborn and Matplotlib
# Seaborn makes it easier to build statistical plots with fewer lines of code,
# especially when plotting grouped data and adding regression lines. Matplotlib
# still gives more fine-grained control, but it often requires more manual setup
# for appearance and layout details.

# Task 4: Machine Learning with scikit-learn
               
feature_cols = ['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']
X = df[feature_cols]
y = df['passed']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train logistic regression
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)
train_accuracy = model.score(X_train_scaled, y_train)
print('Training accuracy:', f'{train_accuracy:.2f}', end='\n\n')

# Evaluate on test set
y_pred = model.predict(X_test_scaled)
test_accuracy = model.score(X_test_scaled, y_test)
print('Test accuracy:', f'{test_accuracy:.2f}', end='\n\n')

print('Test set predictions:')
for idx, actual, predicted in zip(X_test.index, y_test, y_pred):
    name = df.loc[idx, 'name']
    result = '✅ correct' if actual == predicted else '❌ wrong'
    print(f'{name}: actual={actual}, predicted={predicted} -> {result}')
print()

# Feature importance
coefficients = model.coef_[0]
feature_importance = sorted(zip(feature_cols, coefficients), key=lambda x: abs(x[1]), reverse=True)
print('Feature importance (sorted by absolute coefficient):')
for feature, coef in feature_importance:
    direction = 'Pass' if coef > 0 else 'Fail'
    print(f'{feature}: {coef:.4f} ({direction})')
print()

# Plot feature coefficients
features_sorted = [feature for feature, _ in feature_importance]
coefs_sorted = [coef for _, coef in feature_importance]
colors = ['green' if coef > 0 else 'red' for coef in coefs_sorted]
plt.figure(figsize=(10, 6))
plt.barh(features_sorted, coefs_sorted, color=colors)
plt.title('Logistic Regression Feature Coefficients')
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.savefig('plot8_feature_coefficients.png', bbox_inches='tight')
plt.show()
plt.close()

# Bonus: Predict for a new student
new_student = [[75, 70, 68, 65, 80, 82, 3.2]]
new_student_scaled = scaler.transform(new_student)
prediction = model.predict(new_student_scaled)[0]
probabilities = model.predict_proba(new_student_scaled)[0]
result_text = 'Pass' if prediction == 1 else 'Fail'
print('New student prediction:')
print(f'Predicted label: {prediction} ({result_text})')
print(f'Probability [Fail, Pass]: {probabilities.tolist()}')
