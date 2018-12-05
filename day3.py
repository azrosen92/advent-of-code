def size_of_overlapping(input_list):
    stored_boxes = {}
    left_right_edges = []

    for line in input_list:
        box_id, rest = line.split(' @ ')
        position, size = rest.split(':')

        x, y = position.split(',')
        width, height = [int(dimension) for dimension in size.strip().split('x')]

        stored_boxes[box_id] = {
            'x': int(x),
            'y': int(y),
            'width': int(width),
            'height': int(height),
        }

        left_right_edges.extend([(x, box_id, 'start'), (x + width, box_id, 'end')])

    edge_stack = [] 
    for x_coord, box_id, state in sorted(left_right_edges, lambda x: x[0]):
        if state == 'start':
            edge_stack.append(stored_boxes[box_id])
        else:
            last_edge = edge_stack.pop()
            if last_edge and last_edge['

                     

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        inputs = [line.strip() for line in f.readlines()]

