class Square:
    side = 4
    def calculate_area_sq(self):
        return self.side * self.side

class Triangle:
    base = 5
    height = 4
    def calculate_area_tri(self):
        return 0.5 * self.base * self.height

sq = Square()
tri = Triangle()
print("Area of square: ", sq.calculate_area_sq())
print("Area of triangle: ", tri.calculate_area_tri())