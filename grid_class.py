import itertools as itr
import math


class GridSearch:
    def __init__(self, file_data) -> None:
        self.radius = 30
        self.grid_borders = {}
        self.filled_map = {}
        self.every_dot = []
        self.user_square = 0
        self.period_len = 0
        self.first_square_coords = 0
        self.closest_points = {}

        self.file_data = file_data


    def content_list(self, data):
        coord = {}
        for row in data:
            for n in ['x', 'y']:
                if row[n]:
                    coord.setdefault(row['FMID'], []).append(float(row[n]))
        return coord


    def min_max(self, coord):
        x_val, y_val = zip(*coord.values())
        return (min(x_val), max(x_val)), (min(y_val), max(y_val))

    def period_and_1square_points(self, points):
        return len(points), [0, 1, len(points), len(points)+1]

    def divide_into_parts(self, coord_min, coord_max, parts=7):
        tenth = (coord_max - coord_min) / parts
        return [coord_min + i * tenth for i in range(parts + 1)]

    def combine(self, x_list, y_list):
        return list(itr.product(x_list, y_list))


    def build_grid(self, combinations, first_sq_points, row_len):
        grid = {}
        c = 1

        def filler(sq_name, points, c):
            try:
                fin_point = combinations[points[0]], combinations[points[3]]
                grid.setdefault(sq_name, []).extend(fin_point)

                if points[3] + 1 < len(combinations):
                    new_sq_name = 'square' + str(c)
                    new_points = [i + 1 for i in points]
                    filler(new_sq_name, new_points, c + 1)
            except IndexError:
                pass

        filler('square0', first_sq_points, c)

        del_list = [i for i in range(row_len, len(grid), row_len)]
        for i in del_list:
            del grid['square' + str(i)]

        return grid


    def split_in_half(self, combinations):
        if len(combinations)%2==0:
            x = len(combinations)//2
            first_half = combinations[:x][0],  combinations[:x][-1]
            second_half = combinations[x:][0],  combinations[x:][-1]
            return first_half, second_half


    def is_point_inside(self, point, square):
        try:
            _min, _max = square[0], square[1]
            x, y = point[0], point[1]
            if _min[0] <= x <= _max[0] and _min[1] <= y <= _max[1]:
                return x, y
        except IndexError:
            pass

    def fill_grid(self, content, grid):
        filled_grid = {}
        for key, value in grid.items():
            for id, point in content.items():
                point_pos = self.is_point_inside(point, value)
                if point_pos:
                    filled_grid.setdefault(key, []).append((point_pos, id))
        return filled_grid



    def find_neighbours(self, sq_name, period_and_1square_points):
        square_number = int(sq_name.replace('square', ''))
        x = period_and_1square_points-1
        neighbour_indx = [
            square_number - x + 1, square_number + 1, square_number + x + 1,
            square_number - x, square_number, square_number + x,
            square_number - x - 1, square_number - 1, square_number + x - 1
        ]

        neibours = ['square'+str(i) for i in neighbour_indx if i>=0]
        return neibours

    def half_search(self, user):
        first_half, second_half = self.split_in_half(self.every_dot)
        half = len(self.filled_map) // 2

        if self.is_point_inside(user, first_half):
            search_field = dict(list(self.grid_borders.items())[:half])
            for key, value in search_field.items():
                if self.is_point_inside(user, value):
                    self.user_square = key
                    print(f'User position found in the first half, {self.user_square}')
        elif self.is_point_inside(user, second_half):
            search_field = dict(list(self.grid_borders.items())[half:])
            for key, value in search_field.items():
                if self.is_point_inside(user, value):
                    self.user_square = key
                    print(f'User position found in the second half, {self.user_square}')
        else:
            raise ValueError('User position is out of range!\nPlease, try again.')
        return self.user_square

    def radius_search(self, user):
        square_range = self.find_neighbours(self.user_square, self.period_len)
        position_list = {}

        for square in square_range:
            try:
                dots_list = self.filled_map[square]

                for dot in dots_list:
                    dot_id = dot[1]
                    dot_coord = dot[0]
                    x_1, x_2, y_1, y_2 = map(math.radians, [user[0], dot_coord[0], user[1], dot_coord[1]])

                    a = (math.sin((x_2 - x_1) / 2)) ** 2 + math.cos(x_1)
                    b = a * math.cos(x_2) * (math.sin((y_2 - y_1) / 2)) ** 2
                    distance = 2 * 3958.8 * math.asin(math.sqrt(b))

                    if round(distance, 2) <= self.radius:
                        position_list[dot_id] = dot_coord, round(distance, 2)
            except KeyError:
                pass
        self.closest_points = dict(sorted(position_list.items(), key=lambda val: val[1][1]))
        return self.closest_points


    def map_builder(self):
        coord = self.content_list(self.file_data)
        x_min_max, y_min_max = self.min_max(coord)
        border_x = self.divide_into_parts(*x_min_max)
        border_y = self.divide_into_parts(*y_min_max)
        self.every_dot = self.combine(border_x, border_y)
        self.period_len, self.first_square_coords = self.period_and_1square_points(border_x)
        self.grid_borders = self.build_grid(self.every_dot, self.first_square_coords, self.period_len)
        self.filled_map = self.fill_grid(coord, self.grid_borders)
        print('Сетка успешно построена!')
        return self.every_dot, self.period_len, self.first_square_coords, self.filled_map, self.grid_borders

    def search(self, user):
        self.user_square = self.half_search(user)
        self.closest_points = self.radius_search(user)
        return self.closest_points


if __name__ == '__main__':
    import server
    import time

    db = server.Database()
    db.open_database('Export.csv')
    file = db.data
    srch = GridSearch(file)
    start_time = time.time()  # Таймер1 старт
    srch.map_builder()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время создания сетки: {execution_time} секунд")

    while True:

        inp = input('for exit press 0, for search press 1\n')
        match inp:
            case '0':
                break
            case '1':
                user_pos = float(input('Enter X coord\n')), float(input('Enter Y coord\n1'))

                start_time = time.time()
                res = srch.search(user_pos)
                chk = 0
                for index, coordinates in res.items():
                    if coordinates[0]:
                        x = coordinates[0][0]
                        y = coordinates[0][1]
                        dist = coordinates[1]
                        print(f'{chk:<5} Индекс: {index} x: {x:<5}  y: {y:<5} Расстояние: {dist:<5} миль')
                        chk +=1

                end_time = time.time()
                execution_time = end_time - start_time

                print(f"Время перебора по сетке: {execution_time} секунд")