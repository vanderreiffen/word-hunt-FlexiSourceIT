import argparse
from collections import defaultdict


class WordHunt:

    _words_to_find = []
    _word_grid = []
    _word_coords = defaultdict(list)

    def __init__(self, filename):
        self.R = None
        self.C = None
        self._filename = filename
        # 4 directions to search
        self.dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.get_grid()

    def get_grid(self):
        has_newline = False
        with open(self._filename, "r") as pzl_file:
            for line in pzl_file.readlines():
                if not line.strip():
                    has_newline = True
                else:
                    if has_newline:
                        self._words_to_find.append(line.strip().upper())
                    else:
                        self._word_grid.append(
                            [letter for letter in line.strip().upper()]
                        )

    # This function searches in all 8-direction
    # from point(row, col) in grid[][]
    def search2D(self, grid, row, col, word):

        # If first character of word doesn't match
        # with the given starting point in grid.
        if grid[row][col] != word[0]:
            return False

        # Search word in all 4 directions
        # starting from (row, col)
        for x, y in self.dir:

            # Initialize starting point
            # for current direction
            rd, cd = row + x, col + y
            flag = True

            # First character is already checked,
            # match remaining characters
            start_loc = f"({col+1},{row+1})"
            for k in range(1, len(word)):
                # If out of bound or not matched, break
                if 0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]:
                    if k == len(word) - 1:
                        end_loc = f"({cd+1},{rd+1})"
                    # Moving in particular direction
                    rd += x
                    cd += y

                else:
                    flag = False
                    break

            # If all character matched, then
            # value of flag must be false
            if flag and start_loc and end_loc:
                self._word_coords[word].extend([start_loc, end_loc])
                return True
        return False

    # Searches given word in a given matrix
    # in all 8 directions
    def patternSearch(self):

        grid = self._word_grid
        # Rows and columns in given grid
        self.R = len(grid)
        self.C = len(grid[0])

        # Consider every point as starting point
        # and search given word
        for word in self._words_to_find:
            for row in range(self.R):
                for col in range(self.C):
                    if not (word in self._word_coords):
                        if self.search2D(grid, row, col, word):
                            print(
                                f"{word} {self._word_coords[word][0]} {self._word_coords[word][1]}"
                            )
        print("\n####")
        self.print_results()

    def print_results(self):
        print("printing to text file '{}.out'".format(self._filename[:-4]))
        with open(self._filename[:-4] + ".out", "w") as file_ln:
            for word in self._words_to_find:
                if word in self._word_coords:
                    file_ln.write(
                        f"{word} {self._word_coords[word][0]} {self._word_coords[word][1]}\n"
                    )
                else:
                    file_ln.write(f"{word} not found")


# Driver Code
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file", required=True, action="store", help="Puzzle File", dest="filename"
    )
    args = parser.parse_args()

    wordhunt = WordHunt(args.filename)

    print("Finding words...\n")
    wordhunt.patternSearch()

    print("Done...")
