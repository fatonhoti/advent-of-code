UNMARKED = False
MARKED = True


class Board:
    def __init__(self, board):
        self.board = board
        self.won = False

    def update(self, number):
        for cell in self.board:
            if cell[0] == number:
                cell[1] = MARKED

    def calculate_score(self):
        score = 0
        for num, state in self.board:
            if state is UNMARKED:
                score += num
        return score

    def has_won(self):
        if self.all_marked("horizontals", self.board) or self.all_marked(
            "verticals", self.board
        ):
            return True
        return False

    def all_marked(self, orientation, board):
        if orientation == "horizontals":
            for row in range(1, 6):
                if self.row_marked(row, board):
                    return True
        elif orientation == "verticals":
            for col in range(1, 6):
                if self.column_marked(col, board):
                    return True
        else:
            raise ValueError(f"Unknown orientation '{orientation}' given.")
        return False

    def row_marked(self, row, board):
        # Extract the row
        r = board[5 * (row - 1) : 5 * (row - 1) + 5]
        if all(list(map(lambda el: el[1], r))):
            # The whole row is marked!
            return True
        return False

    def column_marked(self, col, board):
        # Extract the column
        r = [board[(col - 1) + 5 * i] for i in range(5)]
        if all(list(map(lambda el: el[1], r))):
            # The whole column is marked!
            return True
        return False

    def print(self):
        for i, el in enumerate(self.board):
            if i % 5 == 0:
                print()
            print(el, end=" ")
        print()


def run():

    # Parse input
    with open("day4_input.txt") as f:
        # Extract the numbers to be drawn
        numbers_to_be_drawn = [int(x) for x in f.readline().split(",")]
        f.readline()

        # Create the bingo boards
        boards = []
        board = []
        for line in f:
            if line == "\n":
                newBoard = Board(board)
                boards.append(newBoard)
                board = []
                continue
            row = list(
                map(
                    lambda num: [int(num), False],
                    filter(lambda s: s != "", line.split()),
                )
            )
            board += row

    # Part 1 and 2
    first_score = None
    for drawn_number in numbers_to_be_drawn:
        for board in boards:
            if board.won:
                continue

            # Mark the number on the board
            board.update(drawn_number)

            # Check if the board won
            if board.has_won():
                # Mark it as done
                board.won = True
                if first_score is None:
                    # This board is the very first winner!
                    first_score = board.calculate_score() * drawn_number
                else:
                    second_score = board.calculate_score() * drawn_number

    print(f"Part 1: {first_score}")
    print(f"Part 2: {second_score}")


if __name__ == "__main__":
    run()
