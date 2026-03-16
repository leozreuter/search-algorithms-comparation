from pyamaze import maze, agent
import copy
import astar, bfs

rows = 10
cols = 10

m = maze(rows,cols)
m_bfs = maze(rows,cols)
m_star = maze(rows,cols)

m.CreateMaze(loopPercent=50, loadMaze="maze--2026-03-15--21-33-14.csv")
mapa = copy.deepcopy(m.maze_map)

m_bfs.maze_map = mapa
m_star.maze_map = mapa

#a = agent(m_star, filled=True, footprints=True, color="red")
#b = agent(m_bfs, filled=True, footprints=True, color="yellow")


path_bfs = bfs.bfs(m_bfs,None)#b)
path_astar = astar.a_star(m_star,None)#a)

# agente que mostra caminho final
a = agent(m_star, filled=True, footprints=True, color='green')
b = agent(m_bfs, filled=True, footprints=True, color='blue')

m_star.tracePath({a: path_astar}, delay=1)
m_bfs.tracePath({b: path_bfs}, delay=1)

m.run()
m_bfs.run()
m_star.run()