input = open("input.txt", "r")
calories = [
  sum([int(cal) for cal in calorie.split("\n")])
  for calorie in input.read().split("\n\n")
]
top_calories = sorted(calories, reverse=True)
print(sum(top_calories[0:3]))

