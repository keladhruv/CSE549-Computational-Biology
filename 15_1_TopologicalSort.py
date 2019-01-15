#Python
def importData():
    file = open('test.txt', 'r')
    m=file.readlines()
    list=[]
    graph={}
    for i in m:
        i=i.strip()
        node,vertex=i.split("->")
        vertexList=vertex.split(",")
        node=node.strip()
        graph[node]=[]

        for k in vertexList:
            k=k.strip()
            graph[node].append(k)

        for node in graph.keys():
            for val in graph[node]:
                if val not in graph:
                    graph[val]={}


    return graph

def order(node, visit, stack):
    visit[node]=True

    for i in graph[node]:
        if visit[i] == None:
            order(i,visit,stack)
    stack.append(node)

def topo(graph):

    visit={}
    for node in graph:
        visit[node]=None

    stack=[]
    for node in graph:
        if visit[node] == None:
            order(node,visit,stack)

    return stack

def output(stack):
    file = open("output.txt", "w+")
    file.write(', '.join(stack[::-1]))
    file.close()


graph=importData()
stack=topo(graph)
output(stack)

