"""
Author: Sanyoung Yoon
Assignment: #1
"""

gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # bool

# workout_stats is a dictionary: {str: tuple(int, int, int)}
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 50),
    "Taylor": (25, 55, 35)
}

names = ["Alex", "Jamie", "Taylor"]

for name in names:
    total = sum(workout_stats[name])
    workout_stats[name + "_Total"] = total

# workout_list is a 2D list (nested list)
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"])
]

print("Yoga and Running (all friends):")
for row in workout_list:
    print(row[:2])

print("\nWeightlifting (last two friends):")
print(workout_list[1][2])
print(workout_list[2][2])

for n in names:
    if workout_stats[n + "_Total"] >= 120:
        print("Great job staying active, " + n + "!")

name = input("\nEnter friend's name: ")

if name in workout_stats:
    print("Workout minutes:", workout_stats[name])
    print("Total minutes:", workout_stats[name + "_Total"])
else:
    print("Friend", name, "not found in the records.")

totals = [
    workout_stats["Alex_Total"],
    workout_stats["Jamie_Total"],
    workout_stats["Taylor_Total"]
]

highest_value = max(totals)
lowest_value = min(totals)

if workout_stats["Alex_Total"] == highest_value:
    print("Friend with highest total workout minutes: Alex")
elif workout_stats["Jamie_Total"] == highest_value:
    print("Friend with highest total workout minutes: Jamie")
else:
    print("Friend with highest total workout minutes: Taylor")

if workout_stats["Alex_Total"] == lowest_value:
    print("Friend with lowest total workout minutes: Alex")
elif workout_stats["Jamie_Total"] == lowest_value:
    print("Friend with lowest total workout minutes: Jamie")
else:
    print("Friend with lowest total workout minutes: Taylor")