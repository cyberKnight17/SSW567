import unittest


def classify_triangle(a, b, c):
    if a + b > c and a + c > b:
        # intentional bug it should be  "if a + b > c and a + c > b and b + c > a:"
        if a == b and b == c:
            return 'Equilateral'
        if a == b and b != c or a == c and c != b:
            # intentional bug it should be  "if a == b and b != c or a == c and c != b or b == c and c != a:"
            return 'Isosceles'
        if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            return 'Right'
        else:
            return 'Scalene'
    else:
        return 'Not a triangle'


def run_classify_triangle(a, b, c):
    print('classify_triangle(', a, ',', b, ',', c, ')=', classify_triangle(a, b, c), sep="")


class TestTriangles(unittest.TestCase):
    def test_set1_not_a_triangle(self):
        self.assertEqual(classify_triangle(0, 0, 0),'Not a triangle', '0, 0, 0 is not a triangle')
        self.assertEqual(classify_triangle(1, 1, 2), 'Not a triangle', '1, 1, 2 is not a triangle')
        self.assertEqual(classify_triangle(1, 2, 9), 'Not a triangle', '1, 2, 9 is not a triangle')
        self.assertEqual(classify_triangle(1000, 2, 9), 'Not a triangle', '1000, 2, 9 is not a triangle')  # found bug

    def test_set2_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1, 1, 1 is an Equilateral')
        self.assertEqual(classify_triangle(2000, 2000, 2000), 'Equilateral', '2000, 2000, 2000 is an equilateral '
                                                                             'triangle')
        self.assertEqual(classify_triangle(0.83, 0.83, 0.83), 'Equilateral', '0.83, 0.83, 0.83 is an equilateral '
                                                                             'triangle')

    def test_set3_iosceles(self):
        self.assertEqual(classify_triangle(3, 3, 2), 'Isosceles', '3, 3, 2 is an iosceles triangle')
        self.assertEqual(classify_triangle(100, 100, 97), 'Isosceles', '100, 100, 97 is an iosceles triangle')
        self.assertEqual(classify_triangle(0.77, 0.77, 0.53), 'Isosceles', '0.77, 0.77, 0.53 is an iosceles triangle')
        self.assertEqual(classify_triangle(77, 88, 88), 'Isosceles', '77, 88, 88 is an iosceles triangle')  # found bug

    def test_set4_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3, 4, 4 is a right triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5, 12, 13 is a right triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5, 12, 13 is a right triangle')

    def test_set5_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene', '3, 3, 2 is an scalene')
        self.assertEqual(classify_triangle(5, 8, 7), 'Scalene', '3, 3, 2 is an scalene')
        self.assertEqual(classify_triangle(9, 10, 12), 'Scalene', '3, 3, 2 is an scalene')

    def test_set6(self):
        self.assertEqual(classify_triangle(1, 2, 100), 'Not a triangle', '1, 2, 100 should not be a triangle')
        self.assertEqual(classify_triangle(100, 100, 100), 'Equilateral', '100, 100, 100 should be an equilateral '
                                                                          'triangle')
        self.assertEqual(classify_triangle(76, 76, 37), 'Isosceles', '76, 76, 37 should be an isosceles triangle')
        self.assertEqual(classify_triangle(20, 99, 101), 'Right', '20, 99, 101 should be a right triangle')
        self.assertEqual(classify_triangle(20, 99, 100), 'Scalene', '76, 76, 37 should be a scalene triangle')

    def test_set7_equal(self):
        self.assertEqual(classify_triangle(1, 2, 100), 'Not a triangle', '1, 2, 100 should not be a triangle')
        self.assertEqual(classify_triangle(100, 100, 100), 'Equilateral', '100, 100, 100 should be an equilateral '
                                                                          'triangle')
        self.assertEqual(classify_triangle(76, 76, 37), 'Isosceles', '76, 76, 37 should be an isosceles triangle')
        self.assertEqual(classify_triangle(20, 99, 101), 'Right', '20, 99, 101 should be a right triangle')
        self.assertEqual(classify_triangle(20, 99, 100), 'Scalene', '76, 76, 37 should be a scalene triangle')

    def test_set7_notequal(self):
        self.assertNotEqual(classify_triangle(1, 2, 100), 'Right', '1, 2, 100 should not be a triangle')
        self.assertNotEqual(classify_triangle(100, 100, 100), 'Right', '100, 100, 100 should be an equilateral '
                                                                          'triangle')
        self.assertNotEqual(classify_triangle(76, 76, 37), 'Right', '76, 76, 37 should be an isosceles triangle')
        self.assertNotEqual(classify_triangle(20, 99, 101), 'Not a triangle', '20, 99, 101 should be a right triangle')
        self.assertNotEqual(classify_triangle(20, 99, 100), 'Not a triangle', '76, 76, 37 should be a scalene triangle')


if __name__ == '__main__':
    run_classify_triangle(0, 0, 1)
    run_classify_triangle(77, 77, 77)
    run_classify_triangle(888, 888, 777)
    run_classify_triangle(21, 220, 221)
    run_classify_triangle(21, 220, 223)

    unittest.main(exit=False)