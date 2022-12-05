input = open("input.txt", "r")


def get_pair_range(pair):
  [assignment1, assignment2] = pair.split(",")
  [range1_start, range1_end] = assignment1.split("-")
  [range2_start, range2_end] = assignment2.split("-")

  return (set(range(int(range1_start),
                    int(range1_end) + 1)),
          set(range(int(range2_start),
                    int(range2_end) + 1)))


pairs = [get_pair_range(pair) for pair in input.read().split("\n")]

fully_contained_pairs = [
  pair for pair in pairs if pair[0] <= pair[1] or pair[1] <= pair[0]
]

pairs_with_intersection = [
  pair for pair in pairs if len(pair[0] & pair[1]) > 0
]

print(len(fully_contained_pairs))
print(len(pairs_with_intersection))
