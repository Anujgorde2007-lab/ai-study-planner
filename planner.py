subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("Subject name: ")
    difficulty = int(input("Difficulty (1-5): "))
    subjects.append((name, difficulty))

total_time = int(input("Total study hours available: "))

# Sort subjects by difficulty (higher first)
subjects.sort(key=lambda x: x[1], reverse=True)

plan = {}

total_difficulty = sum(d for _, d in subjects)

for name, difficulty in subjects:
    allocated_time = predict_time(difficulty)
    plan[name] = round(allocated_time, 2)

print("\n📅 Study Plan:")
for subject, time in plan.items():
    print(f"{subject}: {time} hours")
