class Polygon:

    def __init__(self, n_sides):
        self.n_sides = n_sides
        self.side_len = []

    def input_sides(self):
        '''
        get the side lengths from the user
        :return:
        '''
        self.side_len = []
        for i in range(self.n_sides):
            side = int(input('What is the length of side ' + str(i + 1)))
            self.side_len.append(side)

    def display_sides(self):
        '''
        display the side lengths of the polygon
        :return:
        '''
        print('The side lengths are respectively:', self.side_len)

    def get_area(self):
        '''
        return the area of the polygon
        :return:
        '''
        return

