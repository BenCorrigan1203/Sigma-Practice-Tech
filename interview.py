import random

letter_points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

bag = {
    'E':12,
    'A':9, 'I':9,
    'O':8,
    'N':6, 'R':6, 'T':6,
    'L':4, 'S':4,'U':4, 'D':4,
    'G':3,
    'B':2, 'C':2, 'M':2, 'P':2, 'F':2,
    'H':2, 'V':2, 'W':2, 'Y':2,
    'K':1, 'J':1, 'X':1, 'Q':1, 'Z':1
}

def word_points(word_to_evaluate: str) -> int:
    word_to_evaluate =  word_to_evaluate.upper()

    point_total = 0
    for letter in word_to_evaluate:
        point_total += letter_points[letter]

    return point_total


def create_rack(bag: dict, seed: int = 0) -> list:
    rack = []
    if seed != 0:
        random.seed(seed)
    alphabet = list(letter_points.keys())
    while len(rack) < 7:
        random_number = random.randint(0,25)
        potential_rack_letter = alphabet[random_number]

        if bag[potential_rack_letter] > 0:
            rack.append(alphabet[random_number])
            bag[potential_rack_letter] -= 1
    return rack


if __name__ == "__main__":
    print(bag)
    create_rack(bag, 123)
    print(bag)
