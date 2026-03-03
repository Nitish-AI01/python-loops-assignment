import numpy as np

# ==========================================
# TASK 1 — Generate and Inspect Data
# ==========================================

np.random.seed(42)

# Generate 5x4 array (5 students, 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))

print("Scores:\n", scores)

# 1. Score of 3rd student in 2nd subject
print("\n3rd student, 2nd subject:", scores[2, 1])

# 2. All scores of the last 2 students
print("\nLast 2 students (all subjects):\n", scores[-2:, :])

# 3. All scores for first 3 students in subjects 2 and 3
print("\nFirst 3 students, subjects 2 & 3:\n", scores[:3, 1:3])


# ==========================================
# TASK 2 — Analyze with Broadcasting
# ==========================================

# Column-wise mean (per subject)
column_means = np.round(np.mean(scores, axis=0), 2)
print("\nColumn-wise means:", column_means)

# Add curve (broadcasting)
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.minimum(curved_scores, 100)

print("\nCurved Scores:\n", curved_scores)

# Row-wise max (best subject per student)
row_max = np.max(curved_scores, axis=1)
print("\nRow-wise max (best per student):", row_max)


# ==========================================
# TASK 3 — Normalize and Identify
# ==========================================

# Min-max normalization per row
row_min = np.min(curved_scores, axis=1, keepdims=True)
row_max = np.max(curved_scores, axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)

print("\nNormalized Scores:\n", normalized)

# Find index of single highest value in entire normalized array
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nIndex of highest normalized value (row, col):", max_index)

# Extract all curved scores strictly above 90
above_90 = curved_scores[curved_scores > 90]
print("\nCurved scores above 90:", above_90)
