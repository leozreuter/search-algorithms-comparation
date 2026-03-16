from pyamaze import maze, agent
import astar, bfs

m = maze(500,500)
m.CreateMaze(loopPercent=50)

a = agent(m, filled=True, footprints=True, color="red")
b = agent(m, filled=True, footprints=True, color="yellow")


path_bfs = bfs.bfs(m,None)#b)
path_astar = astar.a_star(m,None)#a)

# agente que mostra caminho final
#a = agent(m, filled=True, footprints=True, color='green')
#b = agent(m, filled=True, footprints=True, color='blue')

#m.tracePath({a: path_bfs}, delay=1)
#m.tracePath({b: path_astar}, delay=1)

#m.run()