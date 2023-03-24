import random
import copy

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
    """Calculates the points for a word from the points for each letter"""
    word_to_evaluate =  word_to_evaluate.upper()

    point_total = 0
    for letter in word_to_evaluate:
        point_total += letter_points[letter]

    return point_total


def create_rack(bag: dict, seed: int = 0) -> list:
    """Create a game rack of 7 random letters, distributed via the game bag"""
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


def is_valid_word(word: str, rack: list) -> bool:
    """checks to see if a word can be made out of letters in a list"""
    test_rack = copy.deepcopy(rack)
    for letter in word:
        if letter.upper() not in test_rack:
            return False
        test_rack.remove(letter.upper())
    return True
        

def get_valid_words_in_rack(rack: list) -> dict:
    """returns all the words that can be made out of letters in a game rack searching from dictionary.txt"""
    valid_words = {"Length 1": [], "Length 2": [], "Length 3": [], "Length 4": [], "Length 5": [], "Length 6": [], "Length 7": []}
    with open("dictionary.txt", mode="r", encoding="utf-8") as dictionary:
        for word in dictionary:
            if is_valid_word(word.strip(), rack):
                valid_words[f"Length {len(word)}"].append(word.strip())
    return valid_words


def find_longest_valid_word(rack: list) -> dict:
    """Find the longest valid word in a game rack out of the valid words"""
    valid_words = get_valid_words_in_rack(rack)
    for i in range(7, 0, -1):
        if valid_words[f"Length {i}"]:
            return {'word_length': i, 'words': valid_words[f"Length {i}"]}
        valid_words = get_valid_words_in_rack(rack)


def highest_word_score_with_triple_letter(word_to_evaluate: str) -> dict:
    """Calculates the best score a word can have depending on which letter is triple scored"""
    word_to_evaluate =  word_to_evaluate.upper()
    point_total = word_points(word_to_evaluate)
    best_total_with_triple_letter = {'word_score': 0, "best_triple_letters": []}

    for letter in word_to_evaluate:
        points_with_triple_letter = point_total + (2 * letter_points[letter])
        if points_with_triple_letter > best_total_with_triple_letter["word_score"]:
            best_total_with_triple_letter["word_score"] = points_with_triple_letter
            best_total_with_triple_letter["best_triple_letters"] = [letter]

        elif points_with_triple_letter == best_total_with_triple_letter["word_score"]:
            if letter not in best_total_with_triple_letter["best_triple_letters"]:
                best_total_with_triple_letter["best_triple_letters"].append(letter)
    return best_total_with_triple_letter


def find_highest_scoring_word(rack: list, include_triple_letter: bool = True) -> dict:
    """Returns a dict with the highest possible word score, along with the words, including triple letters if desired"""
    valid_words = get_valid_words_in_rack(rack)
    highest_scorers = {"word_score": 0, "words": []}
    for word_length in valid_words.values():
        for word in word_length:
            if include_triple_letter:
                score_and_triple_letters = highest_word_score_with_triple_letter(word)
                score = score_and_triple_letters['word_score']
                if score > highest_scorers["word_score"]:
                    highest_scorers["word_score"] = score
                    highest_scorers['words'] = [{"word": word, "best_triple_letters": score_and_triple_letters['best_triple_letters']}]
                elif score == highest_scorers["word_score"]:
                    highest_scorers['words'].append({"word": word, "best_triple_letters": score_and_triple_letters['best_triple_letters']})
            else:
                score = word_points(word)
                if score > highest_scorers["word_score"]:
                    highest_scorers["word_score"] = score
                    highest_scorers['words'] = [word]
                elif score == highest_scorers["word_score"]:
                    highest_scorers['words'].append(word)
    return highest_scorers

if __name__ == "__main__":
    rack = create_rack(bag)
    words = get_valid_words_in_rack(rack)
    print(find_longest_valid_word(rack))
    print(find_highest_scoring_word(rack, False))
    print(find_highest_scoring_word(rack, True))

