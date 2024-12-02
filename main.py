def find_next_square(sq):
    sq = sq ** 0.5 # sq root is a digit * 1/2
    if sq.is_integer(): # checking if digit is int
        return (sq + 1) ** 2 # returning next square
    else:
        return -1
