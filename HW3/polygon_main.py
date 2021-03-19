from HW3.polygon_children import Triangle, Square, Hexagon

tri = Triangle(3)
tri.input_sides()
tri.display_sides()
print(tri.get_area())

sqr = Square(4)
sqr.input_sides()
sqr.display_sides()
print(sqr.get_area())

hex = Hexagon(5)
hex.input_sides()
hex.display_sides()
print(hex.get_max_side())
