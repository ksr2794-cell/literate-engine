def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

scores = [95, 82, 75, 60]

for s in scores:
    print(f"Score: {s}, Grade: {calculate_grade(s)}")