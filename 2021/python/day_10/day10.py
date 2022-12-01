def run():

    # Parse input
    with open("day10_input.txt") as f:
        chunks = [chunk.strip() for chunk in f.readlines()]
        opened = {"(", "[", "{", "<"}
        opposite = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">",
        }
        points_part1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
        points_part2 = {")": 1, "]": 2, "}": 3, ">": 4}

    # Part 1
    corrupted = {")": 0, "]": 0, "}": 0, ">": 0}
    non_corrupted_chunks = []
    for chunk in chunks:
        stack = []
        chunk_corrupted = False
        pointer = 0
        while pointer < len(chunk):
            char = chunk[pointer]
            # Keep pushing to the stack until a closing character is met
            if char in opened:
                # We found an opening character
                stack.append(char)
                pointer += 1
            else:
                # We found a closing character
                left = stack.pop()  # Pop an opening character
                if not (opposite[left] == char):
                    # Open and close did not match => corrupt chunk
                    corrupted[char] += 1
                    chunk_corrupted = True
                    break
                pointer += 1
        if not chunk_corrupted:
            # Save the non-corrupted but incomplete chunks for part 2
            non_corrupted_chunks.append(chunk)

    # Calculate the total syntax error
    part1 = sum(points_part1[k] * v for k, v in corrupted.items())
    print(f"Part 1: {part1}")

    # Part 2
    lines = []
    for chunk in non_corrupted_chunks:
        stack = []
        pointer = 0
        for char in chunk:
            if char in opened:
                stack.append(char)
            else:
                stack.pop()

        # The remaining characters in the stack will be
        # the left characters with no right partner.
        # Generate the matching right partners in the correct order.
        line = "".join([opposite[left] for left in reversed(stack)])
        lines.append(line)

    # Calculate the scores
    scores = []
    for line in lines:
        total_score = 0
        for character in line:
            total_score = (total_score * 5) + points_part2[character]
        scores.append(total_score)
    part2 = sorted(scores)[(len(scores) - 1) // 2]
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
