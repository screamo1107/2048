from game_logic import *
import unittest


class Test2048(unittest.TestCase):
    def test_number_by_index_1(self):
        self.assertEqual(get_number_from_index(0, 0), 1)

    def test_number_by_index_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_number_by_index_3(self):
        self.assertEqual(get_number_from_index(0, 3), 4)

    def test_number_by_index_4(self):
        self.assertEqual(get_number_from_index(3, 0), 13)

    def test_empty_list_1(self):
        lst_given = [[2, 2, 2, 0], [0, 2, 0, 2], [0, 2, 0, 0], [2, 2, 2, 2]]
        lst_expected = [4, 5, 7, 9, 11, 12]
        self.assertEqual(get_empty_list(lst_given), lst_expected)

    def test_empty_list_2(self):
        lst_given = [[0, 2, 2, 2], [2, 2, 0, 0], [0, 0, 0, 0], [2, 2, 2, 0]]
        lst_expected = [1, 7, 8, 9, 10, 11, 12, 16]
        self.assertEqual(get_empty_list(lst_given), lst_expected)

    def test_index_by_number_1(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_index_by_number_2(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_is_zero_in_mas_1(self):
        mas = [
            [2, 2, 2, 2],
            [2, 0, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_is_zero_in_mas_2(self):
        mas = [
            [0, 2, 2, 2],
            [2, 0, 2, 2],
            [2, 2, 0, 2],
            [2, 2, 2, 0]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_is_zero_in_mas_3(self):
        mas = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_move_left_1(self):
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), expected)

    def test_move_left_2(self):
        mas = [
            [2, 2, 0, 0],
            [4, 0, 4, 0],
            [8, 0, 0, 8],
            [16, 2, 0, 16]
        ]
        expected = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [16, 0, 0, 0],
            [16, 2, 16, 0]
        ]
        self.assertEqual(move_left(mas), expected)

    def test_move_left_3(self):
        mas = [
            [0, 2, 2, 0],
            [0, 0, 4, 4],
            [8, 0, 8, 8],
            [0, 2, 16, 16]
        ]
        expected = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [16, 8, 0, 0],
            [2, 32, 0, 0]
        ]
        self.assertEqual(move_left(mas), expected)

    def test_move_left_4(self):
        mas = [
            [4, 2, 2, 4],
            [2, 2, 4, 4],
            [2, 4, 8, 32],
            [0, 2, 4, 16]
        ]
        expected = [
            [4, 4, 4, 0],
            [4, 8, 0, 0],
            [2, 4, 8, 32],
            [2, 4, 16, 0]
        ]
        self.assertEqual(move_left(mas), expected)
