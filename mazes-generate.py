from pyamaze import maze, agent

m500 = maze(500,500)
m1000 = maze(1000,1000)

m500.CreateMaze(saveMaze=True)
m500.CreateMaze(loopPercent=100, saveMaze=True)
m1000.CreateMaze(loopPercent=100, saveMaze=True)
m1000.CreateMaze(saveMaze=True)