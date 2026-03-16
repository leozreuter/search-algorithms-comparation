from pyamaze import maze, agent
import time

def bfs(m:maze,a:agent|None=None):
    print("BFS rodando...")

    start_time = time.time()
    
    inicio = (m.rows, m.cols)
    destino = (1, 1)

    count_nos_abertos = 0

    came_from = {}
    nos_abertos = [inicio]
    nos_visitados = [inicio]

    while nos_abertos:

        current = nos_abertos.pop(0)

        if a:
            a.position = current
            m._win.update()
            time.sleep(0.001)

        if current == destino:
            break

        for direction in "ESNW":
           
            if m.maze_map[current][direction] == True:
                if direction == "E":
                    novo_no = (current[0], current[1] + 1)
                elif direction == "W":
                    novo_no = (current[0], current[1] - 1)
                elif direction == "N":
                    novo_no = (current[0] - 1, current[1])
                elif direction == "S":
                    novo_no = (current[0] + 1, current[1])

                count_nos_abertos = count_nos_abertos + 1

                #print(f"child: {novo_no}")

                if novo_no not in nos_visitados:

                    nos_abertos.append(novo_no)
                    nos_visitados.append(novo_no)

                    came_from[novo_no] = current


    path = {}
    cell = destino

    while cell != inicio:
        path[came_from[cell]] = cell
        cell = came_from[cell]

    end_time=time.time()

    return path, count_nos_abertos, end_time-start_time