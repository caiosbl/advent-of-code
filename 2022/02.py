input = open("input.txt", "r")

plays_map = {"A": "X", "B": "Y", "C": "Z", "X": "A", "Y": "B", "Z": "C"}
play_set_winning = {"A": "Z", "B": "X", "C": "Y", "X": "C", "Y": "A", "Z": "B"}
play_set_lose = {
  "A": "Y",
  "B": "Z",
  "C": "X",
}
play_set_score = {
  "X": 1,
  "A": 1,
  "Y": 2,
  "B": 2,
  "Z": 3,
  "C": 3,
}


def get_play_score(play_1, play_2, extra_mode=False):
  p1 = 0
  p2 = 0

  if (extra_mode):
    if play_2 == "Y":
      play_2 = plays_map[play_1]
    elif play_2 == "X":
      play_2 = plays_map[play_set_winning[plays_map[play_1]]]
    else:
      play_2 = play_set_lose[play_1]

  p1 += play_set_score[play_1]
  p2 += play_set_score[play_2]

  withdraw = plays_map[play_1] == play_2
  p1_winner = play_set_winning[play_1] == play_2
  p2_winner = not withdraw and not p1_winner

  if (withdraw):
    p1 += 3
    p2 += 3
  else:
    p1 += 6 if p1_winner else 0
    p2 += 6 if p2_winner else 0

  return p2


play_set_list = [(play[0], play[2]) for play in input.read().split("\n")]

scores_default = [get_play_score(play[0], play[1]) for play in play_set_list]
scores_extra_mode = [
  get_play_score(play[0], play[1], extra_mode=True) for play in play_set_list
]

print(sum(scores_default))
print(sum(scores_extra_mode))
