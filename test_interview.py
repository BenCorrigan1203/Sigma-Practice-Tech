from interview import letter_points, word_points, create_rack, is_valid_word

def test_for_points():

    assert letter_points['G'] == 2
    assert letter_points['E'] == 1
    assert letter_points['J'] == 8


def test_points_for_word_guardian():
    assert word_points("GUARDIAN") == 10


def test_points_for_word_dog():
    assert word_points("DOG") == 5


def test_for_lowercase_word():
    assert word_points("GUARdiAN") == 10


def test_rack_length(import_bag):
    assert len(create_rack(import_bag)) == 7


def test_bag_removal_B(import_bag):
    assert import_bag['B'] == 2
    create_rack(import_bag,123)
    assert import_bag['B'] == 1


def test_bag_removal(import_bag):
    assert import_bag['I'] == 9
    create_rack(import_bag,123)
    assert import_bag['I'] == 7


def test_valid_word_true(test_rack):
    assert is_valid_word("ball", test_rack) == True


def test_valid_word_removes_letters(test_rack):
    assert is_valid_word("balll", test_rack) == False


def test_valid_word_false(test_rack):
    assert is_valid_word("tree", test_rack) == False