# Q10: Student grade calculator

total = 0
below_35 = False
for i in range(1, 6):
    while True:
        m = float(input(f"Marks of subject {i} (0-100): "))
        if 0 <= m <= 100:
            break
        print("Invalid marks, try again.")
    total += m
    if m < 35:
        below_35 = True
percentage = total / 5
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"
print("Total:", total, "| Percentage:", percentage, "| Grade:", grade)
if below_35:
    print("Warning: at least one subject is below 35.")

# ---------------- Level 3 ----------------
