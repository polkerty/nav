# Intersections exist at random points in the grid.
# Buildings exist at random intersections, with NSWE designation for which side of the intersection. 


import random

random.seed('puffin')

NO_STREET_PROB = 0.1


def generate_plausible_identifier():
    length = random.random(5, 15)

    


def make_name(type):

    if type == 'street':
        pass




def gen_id(type):
    return type + '_' + str(random.random())[2:]

class Street:
    def __init__(self, name):
        self.name = name
        self.segments = []
        self.start = None
        self.end = None
        self.dir = None
        self.id = gen_id()

    def add_segment(self, segment):
        if self.dir is None:
            # This is the first segment in the street.
            self.segments.append(segment)
            self.start = segment.from_point
            self.end = segment.to_point
            self.dir = segment.dir
        elif segment.dir != self.dir:
            # This segment doesn't point the same way as ours. That's an error
            raise ValueError(f"Tried to append segment with dir {segment.dir} to street with dir {self.dir}")
        elif segment.to_point == self.start:
            # Segment slots in before the start of our current street
            # (impossible in our current world generation scheme, but might as well
            # be generic here)
            self.segments = [segment] + self.segments
            self.start = segment.from_point
        elif segment.from_point == self.end:
            # Segment slots in after the end of our current street.
            self.segments.append(segment)
            self.end = segment.to_point
        else:
            # We can only reach this point if the segment doesn't connect to the existing street. 
            raise ValueError(f"Segment ({segment.from_point, segment.to_point}) does not connect to street ({(self.start, self.end)})")            

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = gen_id()
        self.streets = []

    def add_street(self, street):
        self.streets.append(street)

    def find_linking_street(self, dir):
        for street in self.streets:
            if street.dir == dir:
                return street
        return None


class Attribute:
    def __init__(self, name, type, side, vertices):
        self.name = name
        self.type = type
        self.side = side
        self.vertices = vertices
        self.id = gen_id()

class Segment:
    def __init__(self, street, from_point, to_point, attributes, ):
        
        # Ensure the segments are ordered properly
        if to_point[0] < from_point[0] or \
            (to_point[0] == from_point[0] and to_point[1] < from_point[1]):
            (from_point, to_point) = (to_point, from_point)

        # normalized vector of the street. Used to ensure that,
        # for now, all of our streets consist of segments pointing the
        # same direction.
        self.dir = dir_of_points(from_point, to_point)
        self.street = street
        self.from_point = from_point
        self.to_point = to_point
        self.attributes = attributes 
        self.id = gen_id()

class Block:
    def __init__(self, vertices, segments, attributes):
        self.vertices = vertices
        self.segments = segments
        self.attributes = attributes
        self.id = gen_id()

def dir_of_points(a, b):
    (w, x), (y, z) = a, b
    return ((y - w)/abs(y - w), (z-x)/abs(z-x))


def generate_world(dim):
    # 1. Generate points on the lattice.
    point_map = []
    for row_index in range(dim):
        row = []
        for col_index in range(dim):
            row.append(Point(row_index, col_index))
        point_map.append(row)

    # 2. Fill in the gaps. We work block-by-block, since objects are 2D elements within a block.
    blocks = {}
    segments = {}
    attributes = {}
    streets = []

    for row in range(dim - 1):
        for col in range(dim - 1):
            # For now, assume blocks are laid out on a grid. 
            # Later on, without loss of generality, we might skew the coordinates of the grid,
            # so pay special attention to the (x, y) coordinates of each point.

            # Points are laid out clockwise from the top left corner,
            # to make traversing segments easy.
            vertices = [
                point_map[row][col], 
                point_map[row][col + 1], 
                point_map[row + 1][col + 1],
                point_map[row + 1][col],
            ]

            for a, b in zip(vertices, vertices[1:] + vertices[:1]):
                if random.random() < NO_STREET_PROB:
                    # There is no street between these two points. (We still consider the conjoined
                    # blocks separate, for simplicity.)
                    pass
                else:
                    # Is there a street through these two points? If not, make one. 
                    dir = dir_of_points(a, b)
                    street = a.find_linking_street(dir)
                    if street is None:
                        street = Street()
                        streets.append(street)

                    



    return point_map, blocks, segments, attributes, streets
    




def main():
    wo


if __name__ == '__main__':
    main()