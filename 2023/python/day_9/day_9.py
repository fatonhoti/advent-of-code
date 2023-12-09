def calculate_differences(history, all_differences):
  diffs = []
  for i in range(len(history) - 1):
    diff = history[i + 1] - history[i]
    diffs.append(diff)

  if all(n == 0 for n in diffs):
    all_differences[-1].append(all_differences[-1][0])
    return all_differences

  all_differences.append(diffs)
  return calculate_differences(diffs, all_differences)

def extrapolate(differences, backwards=False):
  extrapolated_value = 0
  for i in range(len(differences) - 1, 0, -1):
    if backwards:
      extrapolated_value = differences[i - 1][0] - differences[i][0]
      differences[i - 1] = [extrapolated_value] + differences[i - 1]
    else:
      extrapolated_value = differences[i][-1] + differences[i - 1][-1]
      differences[i - 1].append(extrapolated_value)
  return extrapolated_value

def run():

  histories = []
  with open(f"day_9.txt", "r") as f:
    for history in f.readlines():
      histories.append([int(n) for n in history.split()])

  # Part 1 & 2
  for i, backwards in enumerate([False, True]):
    s = 0
    for history in histories:
      differences = calculate_differences(history, [])
      differences = [history] + differences
      extrapolated_value = extrapolate(differences, backwards=backwards)
      s += extrapolated_value
    print(f"Part {i + 1}: {s}")

if __name__ == "__main__":
    run()
