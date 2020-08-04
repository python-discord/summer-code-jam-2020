"""
A sequence of integers is called a zigzag sequence if each of its
elements is either strictly less than both neighbors
or strictly greater than both neighbors.
For example, the sequence
4 2 3 1 5 3 is a zigzag, but 7 3 5 5 2 and 3 8 6 4 5 aren't.

For a given array of
integers return the length of
its longest contiguous sub-array that is a zigzag sequence.

Example

For a = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6], the output should be
zigzag(a) = 4.

The longest zigzag sub-arrays are[5, 3, 5, 3]
and [3, 2, 8, 6] and they both have length 4.

Input/Output

[time limit] 4000ms(py)
[input] array.integer a

Guaranteed constraints:
2 <= a.length <= 25,
0 <= a[i] <= 100.

[output] integer
"""


def zigzag(a):
    """
    >> > zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6])
    4

    >> > zigzag([2, 3, 1, 0, 2])
    3

    >> > zigzag([1, 2, 3, 2, 1])
    3

    >> > zigzag([2, 3, 1, 4, 2])
    5

    >> > zigzag([1, 2, 0, 3, 2, 1, 3, 2, 4, 0])
    6

    >> > zigzag([1, 2])
    2

    >> > zigzag([1, 2, 1])
    3

    >> > zigzag([1, 1])
    1

    """
