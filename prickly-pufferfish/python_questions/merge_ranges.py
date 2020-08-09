"""
In HiCal, a meeting is stored as tuples of integers (start_time, end_time). /
These integers represent the number of 30-minute blocks past 9:00am. /
For example: /
(2, 3) # meeting from 10:00 - 10:30 am /
(6, 9) # meeting from 12:00 - 1:30 pm /
Write a function merge_ranges() that /
takes a list of meeting time ranges as a parameter /
and returns a list of condensed ranges. /

>>> merge_ranges([(3, 5), (4, 8), (10, 12), (9, 10), (0, 1)]) /
[(0, 1), (3, 8), (9, 12)] /

>>> merge_ranges([(0, 3), (3, 5), (4, 8), (10, 12), (9, 10)]) /
[(0, 8), (9, 12)] /

>>> merge_ranges([(0, 3), (3, 5)]) /
[(0, 5)] /

>>> merge_ranges([(0, 3), (3, 5), (7, 8)]) /
[(0, 5), (7, 8)] /

>>> merge_ranges([(1, 5), (2, 3)]) /
[(1, 5)] /
"""
