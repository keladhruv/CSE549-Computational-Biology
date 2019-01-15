from Bio.SubsMat.MatrixInfo import blosum62 as blosum


def align(s, t, Table, gp, ep):
    data1=[[]]
    m1=[[]]
    n1=[[]]
    data2=[[]]
    m2=[[]]
    n2=[[]]
    b=s
    a=t
    for i in range(len(b) + 1):

        for j in range(len(a)+1):
            data1[i].append(0)
            m1[i].append(0)
            n1[i].append(0)
            data2[i].append(0)
            m2[i].append(0)
            n2[i].append(0)
        if i == len(b):
            break
        data1.append([])
        m1.append([])
        n1.append([])
        data2.append([])
        m2.append([])
        n2.append([])

    for i in range(1, len(s) + 1):
        m1[i][0] = -1000
        n1[i][0] = -1000

    for j in range(1, len(t) + 1):
        m1[0][j] = -1000
        n1[0][j] = -1000

    for i in range(1, len(s) + 1):
        data1[i][0] = gp + ep * (i - 1)

    for j in range(1, len(t) + 1):
        data1[0][j] = gp + ep * (j - 1)


    #discussed this with a classmate and then  wrote it on my own.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):

            if  (a[j - 1], b[i - 1]) in Table:
                addcost = Table[(a[j - 1], b[i - 1])]
            else:
                addcost = Table[(tuple(reversed((a[j - 1], b[i - 1]))))]

            costm1 = [data1[i - 1][j] + gp,m1[i - 1][j] + ep]
            m1[i][j] = max(costm1)
            m2[i][j] = costm1.index(m1[i][j])
            costn1 = [data1[i][j - 1] + gp,n1[i][j - 1] + ep]
            n1[i][j] = max(costn1)
            n2[i][j] = costn1.index(n1[i][j])

            costM = [data1[i - 1][j - 1] + addcost, m1[i][j],n1[i][j]]
            data1[i][j] = max(costM)
            data2[i][j] = costM.index(data1[i][j])


    pat_2=b
    pat_1=a
    scores = [m1[i][j], n1[i][j], data1[i][j]]
    max_score = max([m1[i][j], n1[i][j], data1[i][j]])
    path = scores.index(max_score)
    i, j = len(b), len(a)

    while i > 0 and j > 0:
        if path == 0:
            if m2[i][j] == 0:
                path = 2
            i = i-1
            pat_1 = pat_1[:j] + '-' + pat_1[j:]

        elif path == 1:
            if n2[i][j] == 0:
                path = 2
            j = j-1
            pat_2 = pat_2[:i] + '-' + pat_2[i:]

        elif path == 2:
            if data2[i][j] == 1:
                path = 0
            elif data2[i][j] == 2:
                path = 1
            else:
                i = i - 1
                j = j - 1

    for remaining in range(i):
        pat_1 = pat_1[:0] + '-' + pat_1[0:]
    for remaining in range(j):
        pat_2 = pat_2[:0] + '-' + pat_2[0:]

    return str(max_score), pat_2, pat_1


def readFile(path, no_id=True):
    ids = []
    seqs = []

    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    return seqs


def importdata():
    a=raw_input()
    b=raw_input()
    return a,b

Table = blosum
string1,string2=importdata()


alignment = align(string1, string2, Table, -11, -1)
for row in alignment:
    print row
