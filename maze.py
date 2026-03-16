from pyamaze import maze, agent
import astar, bfs

m = maze(60,60)
LOOP_PERCENT = 90

explore = True if str(input("Acompanhar visualmente a exploração? (y,N)  ")).upper() == "Y" else False

m.CreateMaze(loopPercent=LOOP_PERCENT)

# BFS Explore
b_explore = agent(m, filled=True, footprints=True, color="red") if explore else None
# A* Explore
a_explore = agent(m, filled=True, footprints=True, color="green") if explore else None


# BFS 
path_bfs, total_nodes_bfs, time_bfs = bfs.bfs(m, b_explore)

# A*
path_astar, total_nodes_astar, time_astar = astar.a_star(m,a_explore)

print("\n\n\tRESULTADOS")
print("--------------------")
print(f"MAZE size: {m.cols}x{m.rows}")
print(f"MAZE loop: {LOOP_PERCENT}")
print("--------------------")
print(f"BFS lenght:     {len(path_bfs)}")
print(f"BFS nodes:      {total_nodes_bfs}")
print(f"BFS time:       {time_bfs:.6f}")
print("--------------------")
print(f"A-STAR lenght:  {len(path_astar)}")
print(f"A-STAR nodes:   {total_nodes_astar}")
print(f"A-STAR time:    {time_astar:.6f}")

if explore:
    b = agent(m, filled=not explore, footprints=True, color='dark')
    m.tracePath({b:path_bfs}, delay=20)

    a = agent(m, filled=not explore, footprints=True, color='blue')
    m.tracePath({a:path_astar}, delay=20)

    m.run()