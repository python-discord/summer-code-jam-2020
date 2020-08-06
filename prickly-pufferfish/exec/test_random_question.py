import return_random_question
import unittest
from functions import *


my_class = return_random_question.RandomQuestion()
random_question = my_class.question()
name = my_class.name()


class TestQuestion(unittest.TestCase):
    if name == 'add_to_zero.py':
        def test_add_to_zero(self):
            self.assertEqual(add_to_zero([]), False)
            self.assertEqual(add_to_zero([1]), False)
            self.assertEqual(add_to_zero([1, 2, 3]), False)
            self.assertEqual(add_to_zero([1, 2, 3, -2]), True)
    if name == 'anagram_of_palindrome.py':
        def test_anagram_of_palindrome(self):
            self.assertEqual(is_anagram_of_palindrome("a"), True)
            self.assertEqual(is_anagram_of_palindrome("ab"), False)
            self.assertEqual(is_anagram_of_palindrome("aab"), True)
            self.assertEqual(is_anagram_of_palindrome("arceaceb"), False)
            self.assertEqual(is_anagram_of_palindrome("arceace"), True)
    if name == 'coins.py':
        def test_coins(self):
            self.assertEqual(coins(1) == {1, 10}, True)
            self.assertEqual(coins(2) == {2, 11, 20}, True)
            self.assertEqual(coins(3) == {3, 12, 21, 30}, True)
            self.assertEqual(coins(4) == {4, 13, 22, 31, 40}, True)
            self.assertEqual(coins(10) == {10, 19, 28, 37, 46, 55,
                                          64, 73, 82, 91, 100}, True)
    if name == 'has_balanced_brackets.py':
        def test_has_balanced_brackets(self):
            self.assertTrue(has_balanced_brackets("<ok>"))
            self.assertTrue(has_balanced_brackets("<[ok]>"))
            self.assertTrue(has_balanced_brackets("<[{(yay)}]>"))
            self.assertTrue(has_balanced_brackets("No brackets here!"))
            self.assertFalse(has_balanced_brackets("(Oops!){"))
            self.assertFalse(has_balanced_brackets(">"))
            self.assertFalse(has_balanced_brackets("(This has {too many} ) closers. )"))
            self.assertFalse(has_balanced_brackets("<{Not Ok>}"))
    if name == 'make_change.py':
        def test_make_change(self):
            self.assertEqual(make_change(amount=4, denominations=[1, 2, 3]), 4)
            self.assertEqual(make_change(amount=20, denominations=[5, 10]), 3)
    if name == 'merge_ranges.py':
        def test_merge_ranges(self):
            self.assertEqual(merge_ranges([(3, 5), (4, 8), (10, 12), (9, 10),
                                         (0, 1)]), [(0, 1), (3, 8), (9, 12)])
            self.assertEqual(merge_ranges([(0, 3), (3, 5), (4, 8), (10, 12),
                                         (9, 10)]), [(0, 8), (9, 12)])
            self.assertEqual(merge_ranges([(0, 3), (3, 5)]), [(0, 5)])
            self.assertEqual(merge_ranges([(0, 3), (3, 5), (7, 8)]),
                                         [(0, 5), (7, 8)])
            self.assertEqual(merge_ranges([(1, 5), (2, 3)]), [(1, 5)])
    if name == 'stock-price.py':
        def test_stock_price(self):
            self.assertEqual(get_max_profit([10, 7, 5, 8, 11, 9]), 6)
            self.assertEqual(get_max_profit([10, 3]), -7)
            self.assertEqual(get_max_profit([1, 10, 7, 14, 2, 11]), 13)
            self.assertEqual(get_max_profit([11, 10, 9, 8, 2, 1]), -1)
            self.assertEqual(get_max_profit([11, 9, 5, 2, 2, 0]), 0)
            self.assertEqual(get_max_profit([1, 1, 1, 1, 1, 1]), 0)
    if name == 'valid_parenthesis_permutations.py':
        def test_valid_parens_perms(self):
            self.assertEqual(valid_parens_perms(1), ['()'])
            self.assertEqual(valid_parens_perms(2), ['(())', '()()'])
            self.assertEqual(valid_parens_perms(3), ['((()))', '(()())',
                                                     '(())()',
                                                     '()(())', '()()()'])
            self.assertEqual(valid_parens_perms(4), ['(((())))', '((()()))',
                                                     '((())())',
                                                     '((()))()',
                                                     '(()(()))', '(()()())',
                                                     '(()())()', '(())(())',
                                                     '(())()()', '()((()))',
                                                     '()(()())', '()(())()',
                                                     '()()(())', '()()()()'])
    if name == 'zig_zag.py':
        def test_zig_zag(self):
            self.assertEqual(zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6]), 4)
            self.assertEqual(zigzag([2, 3, 1, 0, 2]), 3)
            self.assertEqual(zigzag([1, 2, 3, 2, 1]), 3)
            self.assertEqual(zigzag([2, 3, 1, 4, 2]), 5)
            self.assertEqual(zigzag([1, 2, 0, 3, 2, 1, 3, 2, 4, 0]), 6)
            self.assertEqual(zigzag([1, 2]), 2)
            self.assertEqual(zigzag([1, 2, 1]), 3)
            self.assertEqual(zigzag([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
