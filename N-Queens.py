from itertools import permutations


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


def getSlope(obj1, obj2):
    return (obj1.column - obj2.column) / (obj1.row - obj2.row)


def check_if_pos_valid(queens_pos):
    for i, queen in enumerate(queens_pos):
        for j, temp_queen in enumerate(queens_pos):
            if i != j and (queen.row == temp_queen.row or
                           queen.column == temp_queen.column or
                           getSlope(queen, temp_queen) == 1 or
                           getSlope(queen, temp_queen) == -1):
                return False
    return True


def generate_the_array(num):
    vals = [i for i in range(num)]
    temp_found = []
    for j in list(permutations(vals, num)):
        temp = []
        for i in range(len(j)):
            temp.append(Position(i, j[i]))
        if check_if_pos_valid(temp) and j not in temp_found:
            temp_found.append(["".join(["." if column != j[row] else "Q" for column in range(num)]) for row in range(num)])
    return temp_found


print(check_if_pos_valid([Position(0, 3),
                          Position(1, 6),
                          Position(2, 2),
                          Position(3, 7),
                          Position(4, 1),
                          Position(5, 4),
                          Position(6, 0),
                          Position(7, 5)]))

generate_the_array(4)
