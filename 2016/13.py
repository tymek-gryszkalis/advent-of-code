import sys, os
from collections import defaultdict

FAV_NUMBER = 1364
REACH = "31,39"
EMPTY_SYMBOL = "."
WALL_SYMBOL = "#"
WALL_LENGTH = 50

LINE_UP = "\033[F"

def is_wall(x, y):
    binary_number = bin((x * x + 3 * x + 2 * x * y + y + y * y) + FAV_NUMBER)[2:]
    number_of_ones = binary_number.count("1")
    if number_of_ones % 2 == 0:
        return False
    return True

matrix = [[EMPTY_SYMBOL for j in range(WALL_LENGTH)] for i in range(WALL_LENGTH)]

def print_matrix(final = False):
    to_print = ""
    for i in matrix:
        to_print += f"{' '.join(i)}\n"
    if not final:
        to_print += f"{LINE_UP * len(matrix)}"
    sys.stdout.write(to_print)
    
for y in range(WALL_LENGTH):
    for x in range(WALL_LENGTH):
        if is_wall(x, y):
            matrix[y][x] = WALL_SYMBOL

graph = defaultdict(lambda : [])
for y in range(WALL_LENGTH):
    for x in range(WALL_LENGTH):
        if matrix[y][x] == WALL_SYMBOL:
            continue
        if y - 1 >= 0 and matrix[y - 1][x] == EMPTY_SYMBOL:
            graph[f"{x},{y}"].append(f"{x},{y - 1}")
        if y + 1 < WALL_LENGTH and matrix[y + 1][x] == EMPTY_SYMBOL:
            graph[f"{x},{y}"].append(f"{x},{y + 1}")
        if x - 1 >= 0 and matrix[y][x - 1] == EMPTY_SYMBOL:
            graph[f"{x},{y}"].append(f"{x - 1},{y}")
        if x + 1 < WALL_LENGTH and matrix[y][x + 1] == EMPTY_SYMBOL:
            graph[f"{x},{y}"].append(f"{x + 1},{y}")

def get_from_pq(queue, dist):
    lowest_distance = 999999
    chosen_vertex = ""
    for i in queue:
        if dist[i] < lowest_distance:
            lowest_distance = dist[i]
            chosen_vertex = i
    if chosen_vertex == "":
        return -1
    return queue.index(chosen_vertex)

def dijkstra(source):
    dist = {}
    prev = {}
    q = []
    for vertex in graph:
        dist[vertex] = 999999
        prev[vertex] = -1
        q.append(vertex)
    dist[source] = 0

    while len(q) > 0:
        index = get_from_pq(q, dist)
        if index == -1:
            return dist, prev
        u = q.pop(index)
        for n in graph[u]:
            if n not in q:
                continue
            alt = dist[u] + 1
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
    return dist, prev

graph_analysis = dijkstra(REACH)
distances = graph_analysis[0]
previouses = graph_analysis[1]
print(distances["1,1"])