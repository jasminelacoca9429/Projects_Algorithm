from HW3.polygon import Polygon


class Triangle(Polygon):

    def __init__(self, n_sides):
        super().__init__(n_sides)

    def input_sides(self):
        '''
        Return the list of sides only if the length of the longest side
        is less than the sum length of the other two sides, hence the
        triangle could be closed.
        '''
        self.side_len = []
        for i in range(self.n_sides):
            side = int(input('What is the length of side ' + str(i + 1) + '?'))
            self.side_len.append(side)
        if max(self.side_len) >= 0.5 * sum(self.side_len):
            raise ValueError ('These side lengths cannot make a triangle.')
        else:
            return self.side_len

    def get_area(self):
        '''According to triangle area formula. '''
        perimeter = 0
        sub_area = 1
        for i in self.side_len:
            perimeter += i
        sp = 0.5 * perimeter
        for j in self.side_len:
            sub_area *= (sp - j)
        area = (sub_area * sp) ** 0.5
        return f'The area of the square is {area}'


class Square(Polygon):

    def __init__(self, n_sides):
        super().__init__(n_sides)

    def input_sides(self):
        '''
        The lengths of side 2 to side 4 should be the same as side 1.
        Otherwise, exception raised.
        '''
        self.side_len = []
        ini_side = int(input('What is the length of the 1st side?'))
        self.side_len.append(ini_side)
        for i in range(1, self.n_sides):
            side = int(input('What is the length of side ' + str(i + 1) + '?'))
            if side not in self.side_len:
                raise ValueError('To make a square, lengths of all the sides should be equal!')
            else:
                self.side_len.append(side)

    def get_area(self):
        '''Double check if lengths of all sides are the same.'''
        pivot = self.side_len[0]
        for i in self.side_len[1:]:
            if i != pivot:
                raise ValueError('This is not a square!')
        area = pivot ** 2
        return f'The area of the square is {area}'


class Hexagon(Polygon):
    def __init__(self, n_sides):
        super().__init__(n_sides)

    def input_sides(self):
        '''
        Return the list of sides only if the length of the longest side
        is less than the sum length of the other four sides, hence the
        polygon could be closed.
        '''
        self.side_len = []
        for i in range(self.n_sides):
            side = int(input('What is the length of side ' + str(i + 1) + '?'))
            self.side_len.append(side)
        if max(self.side_len) >= 0.5 * sum(self.side_len):
            raise ValueError ('These side lengths cannot make a hexagon.')
        else:
            return self.side_len

    def get_max_side(self):
        max_side = max(self.side_len)
        return f'The maximum side fo the hexagon is {max_side}'
