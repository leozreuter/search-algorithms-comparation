from pyamaze import maze, agent
import astar, bfs

SIZE=25

explore = True if str(input("Acompanhar visualmente a exploração? (y,N)  ")).upper() == "Y" else False
loop    = True if str(input("Mapa tem loop? (y,N)  ")).upper() == "Y" else False

m = maze(SIZE,SIZE)
m.CreateMaze(loadMaze=f"maze-{SIZE}{"l" if loop else None}.csv")

# BFS Explore
b_explore = agent(m, filled=True, footprints=True, color="red") if explore else None
path_bfs, total_nodes_bfs, time_bfs = bfs.bfs(m, b_explore)

# A* Explore
a_explore = agent(m, filled=True, footprints=True, color="green") if explore else None
path_astar, total_nodes_astar, time_astar = astar.a_star(m,a_explore)

print("\n\n\tRESULTADOS")
print("--------------------")
print(f"MAZE size: {m.cols}x{m.rows}")
print("--------------------")
print(f"BFS path:       {[p for p  in path_bfs]}")
print(f"BFS lenght:     {len(path_bfs)}")
print(f"BFS nodes:      {total_nodes_bfs}")
print(f"BFS time:       {time_bfs:.6f}")
print("--------------------")
print(f"A-STAR path:    {[p for p in path_astar]}")
print(f"A-STAR lenght:  {len(path_astar)}")
print(f"A-STAR nodes:   {total_nodes_astar}")
print(f"A-STAR time:    {time_astar:.6f}")

if explore:
    b = agent(m, filled=not explore, footprints=True, color='dark')
    m.tracePath({b:path_bfs}, delay=20)

    a = agent(m, filled=not explore, footprints=True, color='blue')
    m.tracePath({a:path_astar}, delay=20)

    m.run()
