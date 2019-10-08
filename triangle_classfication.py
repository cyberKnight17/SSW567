def classify_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return 'Equilateral'
        if a == b and b != c or a == c and c != b or b == c and c != a:
            return 'Isosceles'
        if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            return 'Right'
        else:
            return 'Scalene'
    else:
        return 'Not a triangle'
