def run():

    # Utility methods
    def extract_column_bits(li, col):
        # Collect the bits from selected column
        return list(map(lambda bin_num: int(bin_num[col]), li))

    def most_common(li, comparator):
        zeros = li.count(0)
        ones = li.count(1)
        return comparator(ones, zeros)

    # Calculates the Oxygen generator- and CO2 scrubber ratings
    def calc_rating(comparator):
        picked = binary_numbers
        bit = 0
        while len(picked) > 1:
            bits = extract_column_bits(picked, bit)
            mc = most_common(bits, comparator)
            picked = list(filter(lambda num: num[bit] == mc, picked))
            bit += 1
        return int(picked[0], 2)

    # Parse input
    with open("day3_input.txt") as f:
        binary_numbers = f.read().split("\n")

    # Part 1
    gamma = ""
    epsilon = ""
    for column in [
        extract_column_bits(binary_numbers, i) for i in range(len(binary_numbers[0]))
    ]:
        mc = most_common(column, lambda a, b: ("1", "0") if a > b else ("0", "1"))
        gamma += mc[0]
        epsilon += mc[1]
    print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")

    # Part 2
    ogr = calc_rating(lambda a, b: "1" if a >= b else "0")
    cosr = calc_rating(lambda a, b: "0" if a >= b else "1")
    print(f"Part 2: {ogr * cosr}")


if __name__ == "__main__":
    run()
