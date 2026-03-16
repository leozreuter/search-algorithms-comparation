from pyamaze import maze, agent
from queue import PriorityQueue
import time

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(m:maze,b:agent|None=None):
    print("A-Star rodando...")
    
    start_time = time.time()

    start = (m.rows, m.cols)
    goal = (1, 1)

    count_nos_abertos = 0

    open_set = PriorityQueue()
    open_set.put((0, start))

    came_from = {}

    g_score = {cell: float("inf") for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float("inf") for cell in m.grid}
    f_score[start] = h(start, goal)

    while not open_set.empty():

        current = open_set.get()[1]

        if b:
            b.position = current
            m._win.update()
            time.sleep(0.001)

        if current == goal:
            break

        for direction in "ESNW":

            if m.maze_map[current][direction] == True:

                if direction == "E":
                    child = (current[0], current[1] + 1)
                elif direction == "W":
                    child = (current[0], current[1] - 1)
                elif direction == "N":
                    child = (current[0] - 1, current[1])
                elif direction == "S":
                    child = (current[0] + 1, current[1])

                count_nos_abertos = count_nos_abertos + 1

                temp_g = g_score[current] + 1

                if temp_g < g_score[child]:

                    came_from[child] = current
                    g_score[child] = temp_g
                    f_score[child] = temp_g + h(child, goal)

                    open_set.put((f_score[child], child))

    path = {}
    cell = goal

    while cell != start:
        path[came_from[cell]] = cell
        cell = came_from[cell]
    
    end_time = time.time()

    return path, count_nos_abertos, end_time-start_time