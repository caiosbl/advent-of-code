input = open("input.txt", "r")


def get_priority(char):
  char_position = ord(char)
  # 38 is 65 (Ascii position of A) - 27 (Puzzle position of A)
  # 96 is 97 (Ascii position of a) - 1 (Puzzle position of a)
  return char_position - 38 if char_position < 97 else char_position - 96


def get_common_item_type(item_1, item_2, item_3=None):
  if (item_3 is None):
    item_3 = item_1
  return (set(item_1) & set(item_2) & set(item_3)).pop()


rucksacks = input.read().split("\n")
rucksacks_items = [(rucksack[:len(rucksack) // 2],
                    rucksack[len(rucksack) // 2:]) for rucksack in rucksacks]

rucksacks_priority = [
  get_priority(get_common_item_type(item_1, item_2))
  for (item_1, item_2) in rucksacks_items
]

rucksacks_groups = [
  (rucksacks[i], rucksacks[i + 1], rucksacks[i + 2])
  for i in [index + 3 for index in range(-3,
                                         len(rucksacks) - 3, 3)]
]

rucksacks_badges_priorities = [
  get_priority(get_common_item_type(item_1, item_2, item_3))
  for item_1, item_2, item_3 in rucksacks_groups
]

runsack_priorities_sum = sum(rucksacks_priority)
rucksacks_badges_priorities_sum = sum(rucksacks_badges_priorities)

print(runsack_priorities_sum, rucksacks_badges_priorities_sum)
