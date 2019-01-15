#Python
def importData():
    file = open('test.txt', 'r')
    m=file.readlines()
    list=[]
    graph={}
    c=0
    w={}
    for i in m:
        i=i.strip()
        if c==0:
            src=i
            c+=1
            continue
        elif c==1:
            sink=i
            c+=1
            continue
        node, vertex = i.split("->")
        node=int(node)
        vertex, weight =vertex.split(":")
        vertex=int(vertex)
        weight=int(weight)
        if node not in graph:
            graph[node] = {}
        graph[node][vertex] = weight

    return int(src),int(sink),graph

def compute(curr, graph, source, sink, longest_path, longest_path_choice):
    if curr == sink:
        longest_path[sink] = 0
        return 0
    if curr in longest_path:
        return longest_path[curr]
    else:
        lp = float('-inf')
        lpc = None
        if curr not in graph:
            longest_path[curr] = float('-inf')
            longest_path_choice[curr] = None
            return float('-inf')
        for node in graph[curr]:
            res = graph[curr][node] + compute(node, graph, source, sink, longest_path, longest_path_choice)
            if res > lp:
                lp = res
                lpc = node
        longest_path_choice[curr] = lpc
        longest_path[curr] = lp
        return lp

def output(we,source, sink, lpc):
    out=[]
    out.append(source)
    while source != sink:
        source = lpc[source]
        out.append(source)

    file = open("output.txt", "w+")
    file.write(str(we)+"\n")
    file.write('->'.join(map(str, out)))
    file.close()

source,sink,graph=importData()
lp,lpc= {},{}
we=compute(source, graph, source, sink, lp, lpc)
print lpc
output(we,source, sink, lpc)
