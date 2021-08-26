class SudokuSolver:

    def __init__(self, str):
        self._str = str
        self._puzzle = self.generate_list(self._str)
        self._stack = []
        self._last_value = None
        self._solved = False
        self.display_puzzle()
        print()
        # print(self._puzzle)

    def generate_list(self, str):
        """
        Turns the provided string into a list of lists for grid representation.
        :param str: self._str
        :return: list of lists of sudoku data
        """
        sudoku_puzzle = []
        for _ in range(9):
            row = []
            for num in str:
                if num != '/':
                    row.append(int(num))
                if num == '/':
                    str = str[10:]
                    break
            sudoku_puzzle.append(row)  # appends the last row since it has no '/'
        return sudoku_puzzle

    def get_list(self):
        return self._puzzle

    def display_puzzle(self):
        """
        Displays puzzle in output for easy viewing.
        :return: None
        """
        puzzle = self._puzzle
        for row in range(9):
            if row % 3 == 0 and row != 0:
                print('----+-----+----')
            for col in range(1, 10):
                if col != 9:
                    print(puzzle[row][col-1], end='')
                    if col % 3 == 0:  # vertical columsn for visuals
                        print(' | ', end='')
                else:
                    print(puzzle[row][col-1])

    def solve(self):
        """
        Solves the sudoku puzzle using a backtracking algorithm.
        :return: None
        """
        next_coord = self.find_next()
        while not self._solved:
            next_num = self.solve_next(next_coord)
            if next_num == 0:
                next_coord = self._stack.pop()
            else:
                next_coord = self.find_next()

    def solve_next(self, coord):
        """
        Solves next position.
        :param coord: grid position to be solved
        :return:
        """
        puzzle = self._puzzle
        row, col = coord
        puzzle[row][col] = self.find_valid(coord)
        if puzzle[row][col] != 0:  # if a valid number was found
            self._stack.append(coord)  # keeps of stack of all cells solved
            next_coord = self.find_next()
            if not next_coord:
                self._solved = True
        return puzzle[row][col]

    def slow_solve(self):
        """
        Used in GUI to solve slower than method above (step by step).
        :return:
        """
        if self._solved == False:
            puzzle = self._puzzle
            if self._last_value == 0:
                next_coord = self._stack.pop()
            else:
                next_coord = self.find_next()
                if not next_coord:
                    self._solved = True
                    return
            row, col = next_coord
            puzzle[row][col] = self.find_valid(next_coord)
            if puzzle[row][col] != 0:
                self._stack.append(next_coord)
            self._last_value = puzzle[row][col]

    def find_next(self):
        """
        Returns the next cell that is empty (0) or cell to revisit, whichever comes first.
        :return: (row, col) tuple of next empty cell
        """
        for row in range(9):
            for col in range(9):
                if self._puzzle[row][col] == 0:
                    return (row, col)
        return False

    def find_valid(self, coord):
        """
        Finds the next valid input possible for a cell.
        :param coord: tuple of (row, column) where cell is cloated
        :return: The next valid number for the cell, or 0 if no other numbers are valid.
        """
        row, col = coord
        num = self._puzzle[row][col] + 1
        while num < 10:
            # Checks if number satisfies the row, column, and square rules (no repeats) of Sudoku
            if self.check_row(num, row) and self.check_column(num, col) and self.check_square(num, row, col):
                return num
            else:
                num += 1
        # If all numbers 1-9 are checked and no numbers are valid, return 0
        return 0

    def check_row(self, num, row):
        """
        Verifies that number is not already present in the row.
        :param num: number being checked
        :param row: row being scanned
        :return: True is num is valid, False otherwise.
        """
        if num in self._puzzle[row]:
            return False
        return True

    def check_column(self, num, col):
        """
        Verifies that number is not already present in the column.
        :param num: number being checked
        :param col: column being scanned
        :return: True is num is valid, False otherwise.
        """
        for row in range(9):
            if self._puzzle[row][col] == num:
                return False
        return True

    def check_square(self, num, row, col):
        """
        Verified that number is not already present in the box. Identifies square (not cell) rows and columns. Rows
        and columns range from 0-2. For example, square 0 would be in grid_row 0 and grid_column 0, square 3 would
        be in grid_row 1 and grid_column 0. Layout is as follows:

        0 1 2
        3 4 5
        6 7 8

        :param num: number being checked
        :param row: row the number is in
        :param col: column the number is in
        :return: True if num is valid, False otherwise.
        """
        box = self.identify_box(row, col)
        grid_row = int(box/3)
        grid_col = box%3

        # Python list comprehension to isolate only cells inside square.
        numbers_in_box = [num for row in self._puzzle[grid_row*3:grid_row*3+3]
                          for num in row[grid_col*3:grid_col*3+3]]

        if num in numbers_in_box:
            return False
        return True

    def identify_box(self, row, col):
        """
        Determines which square the cell is in.
        :param row: row coordinate of cell
        :param col: column coordinate of cell
        :return: square number 1-9
        """
        if row < 3:
            if col < 3:
                return 0
            elif col < 6:
                return 1
            elif col < 9:
                return 2
        elif row < 6:
            if col < 3:
                return 3
            elif col < 6:
                return 4
            elif col < 9:
                return 5
        elif row < 9:
            if col < 3:
                return 6
            elif col < 6:
                return 7
            elif col < 9:
                return 8


def main():
    # s_string = "400003510/300092806/819040000/002009180/708300050/041087900/060730205/070205000/200900031"
    # s_string2 = "000890040/000002008/508040200/093274610/150060784/674000923/029085000/761400850/080026390"
    s_string3 = "438209061/206008040/001036270/000052400/080900020/320040680/000701802/792600000/005000706"
    s = SudokuSolver(s_string3)
    s.solve()
    s.display_puzzle()

if __name__ == '__main__':
    main()