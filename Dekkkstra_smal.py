import time
# from guppy import hpy
start_time = time.clock()
graph = {'a':{'b':3,'c':3},'b':{'c':1,'d':2,'f':3,'g':3,'h':3},'c':{'d':2,'f':3,'g':3,'h':3},'d':{'f':1,'g':1,'h':1},'e':{'f':1,'g':1,'h':1},'f':{'i':3,'j':3,'k':3,'g':1},'g':{'i':3,'j':3,'k':3,'h':1},'h':{'i':3,'j':3,'k':3},'i':{'l':3,'m':3,'n':3,'j':1},'j':{'l':3,'m':3,'n':3,'k':1},'k':{'l':3,'m':3,'n':3},'l':{'k':9999},'m':{'k':9999},'n':{'k':9999}}

mark = {'a':25,'b':20,'c':28,'d':20,'e':25,'f':19,'g':24,'h':28,'i':16,'j':23,'k':29,'l':28,'m':23,'n':28}
completedtaskas = ['b']
teamMarkers={'a':0,'b':1,'c':1,'d':11,'e':11,'f':2,'g':2,'h':2,'i':3,'j':3,'k':3,'l':4,'m':4,'n':4}
a1=completedtaskas[-1]


def edumap(graph,start,goal, previousTaskResult, minMarkWeight,maxMarkWeight,mark,completedtaskas):
    shortest_distance={}
    predecessor={} #Предшествующая вершина
    unseenNodes = graph #граф непосещенных вершин
    infinity = 999999
    path=[]
    print(previousTaskResult, minMarkWeight)
    marks = {}  # Массив оценок за пройденные задания
    if previousTaskResult < 0.6:
        thisTeamAgain = 1
        subTeam = 0
    elif previousTaskResult > 0.6 and previousTaskResult < 0.9 and minMarkWeight > 0.82:
        subTeam = 1
        thisTeamAgain = 0
    else:
        thisTeamAgain = 0
        subTeam = 0
    print(thisTeamAgain, subTeam)
    for node in unseenNodes:
        shortest_distance[node] = infinity #массив с кротчайшим путем от точки start в любую другую точку
    print('a',unseenNodes)
    shortest_distance[start] = 0 #из точки х в точку х путь равено 0
    print(shortest_distance)
    while unseenNodes: #пока есть непосещенные ноды в графе
        minNode = None #минимальный все ноды = 0
        # print('**')
        # print(unseenNodes)
        for node in unseenNodes: #для каждой ноды в графе
            # print('Текущая нода', node)
            # print('minNode', minNode)
            if minNode is None:
                minNode = node #если ноль берет значение начальной ноды
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
            # print ('minNode после цикла', minNode)
            # print(shortest_distance)
            # print(unseenNodes)
            # print('****')



        for childNode, weight in graph[minNode].items(): # weight - путь, childNode - ноды
            # print('childNode', childNode, 'weight', weight)
            # print('mark[childNode]/30',mark[childNode]/30)
            # print(childNode)
            if  (minMarkWeight<mark[childNode]/30<maxMarkWeight) and not childNode in completedtaskas:
                print('!!!!!!!!',mark[childNode]/30,str(teamMarkers[minNode])+'1')
                # print(teamMarkers[minNode], teamMarkers[completedtaskas[-1]],minNode,childNode,start)
                # print(str(teamMarkers[minNode]),str(teamMarkers[completedtaskas[-1]])+'1')
                if (weight + shortest_distance[minNode]< shortest_distance[childNode]) or (thisTeamAgain == 1 and teamMarkers[minNode] == teamMarkers[completedtaskas[-1]] and childNode != start) or (subTeam == 1 and str(teamMarkers[minNode]) == str(teamMarkers[completedtaskas[-1]])+'1' and childNode != start) :
                    shortest_distance[childNode]=weight+shortest_distance[minNode]
                    predecessor[childNode]=minNode #записанный путь
                    # print('текущий предцессор',predecessor)
                    print('путь из',minNode,'в',childNode,shortest_distance[childNode])
                    if thisTeamAgain == 1 and teamMarkers[minNode] == teamMarkers[completedtaskas[-1]] and childNode != start:
                        shortest_distance[childNode]=-1
                        thisTeamAgain=0
                        print('Сработал переход к заданию данной темы',shortest_distance[childNode],shortest_distance)
                    if (subTeam == 1 and str(teamMarkers[minNode]) == str(teamMarkers[completedtaskas[-1]])+'1' and childNode != start):
                        shortest_distance[childNode]=0
                        subTeam = 0
                        print('Сработал переход к субзаданию данной темы',childNode,shortest_distance[childNode],shortest_distance)
        print('кратчайший путь',shortest_distance)
        print('******')
        unseenNodes.pop(minNode) #Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент

    currentNode = goal
    # print('текущая нода',currentNode)
    # print('predecessor', predecessor)
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
            print('!!!текущая нода', currentNode)
        except KeyError:
            print('Path to reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal]!=infinity:
        print('Shortest distance is'+ str(shortest_distance[goal]))
        print('And the path is '+str(path))

edumap(graph, 'b','l',0.4,0.6,1,mark,completedtaskas)
print (time.clock() - start_time, "seconds")
