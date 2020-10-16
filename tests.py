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

    def test_index_by_number_1(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_index_by_number_2(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_index_by_number_3(self):
        self.assertEqual(get_index_from_number(4), (0, 3))

    def test_index_by_number_4(self):
        self.assertEqual(get_index_from_number(13), (3, 0))

    def test_empty_list_1(self):
        lst_given = [[2, 2, 2, 0], [0, 2, 0, 2], [0, 2, 0, 0], [2, 2, 2, 2]]
        lst_expected = [4, 5, 7, 9, 11, 12]
        self.assertEqual(get_empty_list(lst_given), lst_expected)

    def test_empty_list_2(self):
        lst_given = [[0, 2, 2, 2], [2, 2, 0, 0], [0, 0, 0, 0], [2, 2, 2, 0]]
        lst_expected = [1, 7, 8, 9, 10, 11, 12, 16]
        self.assertEqual(get_empty_list(lst_given), lst_expected)

    def test_empty_list_3(self):
        lst_given = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 0]]
        lst_expected = [16]
        self.assertEqual(get_empty_list(lst_given), lst_expected)

    def test_empty_list_4(self):
        lst_given = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
        lst_expected = []
        self.assertEqual(get_empty_list(lst_given), lst_expected)

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
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_is_zero_in_mas_4(self):
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

    def test_move_right_1(self):
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
        self.assertEqual(move_right(mas), expected)

    def test_move_right_2(self):
        mas = [
            [2, 2, 0, 0],
            [4, 0, 4, 0],
            [8, 0, 0, 8],
            [16, 2, 0, 16]
        ]
        expected = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 0, 16],
            [0, 16, 2, 16]
        ]
        self.assertEqual(move_right(mas), expected)

    def test_move_right_3(self):
        mas = [
            [0, 2, 2, 0],
            [0, 0, 4, 4],
            [8, 0, 8, 8],
            [0, 2, 16, 16]
        ]
        expected = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 8, 16],
            [0, 0, 2, 32]
        ]
        self.assertEqual(move_right(mas), expected)

    def test_move_right_4(self):
        mas = [
            [4, 2, 2, 4],
            [2, 2, 4, 4],
            [2, 4, 8, 32],
            [0, 2, 4, 16]
        ]
        expected = [
            [0, 4, 4, 4],
            [0, 0, 4, 8],
            [2, 4, 8, 32],
            [0, 2, 4, 16]
        ]
        self.assertEqual(move_right(mas), expected)

    def test_move_up_1(self):
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
        self.assertEqual(move_up(mas), expected)

    def test_move_up_2(self):
        mas = [
            [2, 2, 0, 0],
            [4, 0, 4, 0],
            [8, 0, 0, 8],
            [16, 2, 0, 16]
        ]
        expected = [
            [2, 4, 4, 8],
            [4, 0, 0, 16],
            [8, 0, 0, 0],
            [16, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), expected)

    def test_move_up_3(self):
        mas = [
            [2, 2, 2, 0],
            [2, 4, 8, 4],
            [4, 0, 8, 4],
            [4, 2, 2, 16]
        ]
        expected = [
            [4, 2, 2, 8],
            [8, 4, 16, 16],
            [0, 2, 2, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), expected)

    def test_move_up_4(self):
        mas = [
            [0, 2, 4, 4],
            [0, 2, 4, 4],
            [0, 4, 4, 0],
            [2, 0, 4, 16]
        ]
        expected = [
            [2, 4, 8, 8],
            [0, 4, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), expected)

    def test_move_down_1(self):
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
        self.assertEqual(move_down(mas), expected)

    def test_move_down_2(self):
        mas = [
            [2, 2, 0, 0],
            [4, 0, 4, 0],
            [8, 0, 0, 8],
            [16, 2, 0, 16]
        ]
        expected = [
            [2, 0, 0, 0],
            [4, 0, 0, 0],
            [8, 0, 0, 8],
            [16, 4, 4, 16]
        ]
        self.assertEqual(move_down(mas), expected)

    def test_move_down_3(self):
        mas = [
            [2, 2, 2, 0],
            [2, 4, 8, 4],
            [4, 0, 8, 4],
            [4, 2, 2, 16]
        ]
        expected = [
            [0, 0, 0, 0],
            [0, 2, 2, 0],
            [4, 4, 16, 8],
            [8, 2, 2, 16]
        ]
        self.assertEqual(move_down(mas), expected)

    def test_move_down_4(self):
        mas = [
            [0, 2, 4, 4],
            [0, 2, 4, 4],
            [0, 4, 4, 0],
            [2, 0, 4, 16]
        ]
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 4, 8, 8],
            [2, 4, 8, 16]
        ]
        self.assertEqual(move_down(mas), expected)

    def test_can_move_1(self):
        mas = [
            [4, 2, 4, 4],
            [8, 0, 4, 4],
            [2, 4, 4, 2],
            [2, 8, 4, 16]
        ]
        self.assertEqual(can_move(mas), True)

    def test_can_move_2(self):
        mas = [
            [4, 2, 4, 4],
            [8, 16, 4, 4],
            [2, 4, 4, 2],
            [2, 8, 4, 16]
        ]
        self.assertEqual(can_move(mas), True)

    @unittest.skip
    def test_can_move_3(self):
        mas = [
            [4, 2, 32, 4],
            [8, 16, 2, 4],
            [16, 2, 4, 2],
            [32, 8, 4, 2]
        ]
        self.assertEqual(can_move(mas), True)

    def test_can_move_4(self):
        mas = [
            [4, 2, 32, 2],
            [8, 16, 2, 4],
            [2, 2, 4, 2],
            [32, 8, 2, 2]
        ]
        self.assertEqual(can_move(mas), True)

    def test_can_move_5(self):
        mas = [
            [4, 2, 32, 2],
            [8, 16, 2, 4],
            [16, 2, 8, 32],
            [32, 8, 4, 16]
        ]
        self.assertEqual(can_move(mas), False)
