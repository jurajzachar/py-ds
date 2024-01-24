import heapq

# '.' is free path and 'x' is unpassable obstacle
map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""


def parse_map(map=map):
    '''
    The function takes a map and returns a tuple of three elements:
      - A list of lines
      - The origin
      - The destination
    '''
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination


def is_valid(lines, position):
    '''
    To be valid, a position has to be inside the boundaries of the map and not an obstacle.
    '''
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    if lines[y][x] == "X":
        return False
    return True


def get_neighbors(lines, current):
    '''
    The function returns all the valid positions surrounding the current position.
    '''
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position


def get_shorter_paths(tentative, positions, through):
    '''
    yields positions for which the path that has through as its last step is shorter than the current known path.

    get_shorter_paths() has three parameters:

      - tentative is a dictionary mapping a position to the shortest known path.
      - positions is an iterable of positions to which you want to shorten the path.
      - through is the position through which, perhaps, a shorter path to the positions can be found.
    '''
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path


def find_path(map):
    '''
    You keep three pieces of data:

      - certain is the set of certain positions.
      - candidates is the heap of candidates.
      - tentative is a dictionary mapping nodes to the current shortest known path.

    A position is in certain if you can be certain that the shortest known path is the shortest possible path.
    If the destination is in the certain set, then the shortest known path to the destination is unquestionably the shortest
    possible path, and you can return this path.

    The heap of candidates is organized by the length of the shortest known path and is managed with the help of the
    functions in the Python heapq module. At each step, you look at the candidate with the shortest known path.
    This is where the heap is being popped with heappop(). There is no shorter path to this candidate—all other paths go
    through some other node in candidates, and all of these are longer. Because of that, the current candidate can be
    marked certain.

    You then look at all neighbors that have not been visited, and if going through the current node is an improvement,
    then you add them to the candidates heap using heappush()
    '''
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        raise ValueError("no path")


if __name__ == '__main__':
    print(parse_map())
