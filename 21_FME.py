  from Bio.SubsMat.MatrixInfo import blosum62 as blosum

def middleColumn(s, t,Table, cost):

    dp = [[i * j * cost for j in xrange(-1, 1)] for i in range(len(s) + 1)]
    dp[0][1] = cost
    backtrack = [0] * (len(s) + 1)
    for j in range(1, len(t) / 2 + 1):
        for i in range(0, len(s) + 1):
            if(i == 0):
                dp[i][1] = -j * cost
            else:
                if (s[i - 1], t[j - 1]) in Table:
                    addcost = Table[(s[i - 1], t[j - 1])]
                else:
                    addcost = Table[(tuple(reversed((s[i - 1], t[j - 1]))))]
                score = [dp[i - 1][0] + addcost, dp[i][0] - cost, dp[i - 1][1] - cost]
                dp[i][1] = max(score)
                backtrack[i] = score.index(dp[i][1])
        if(j != len(t) / 2):
            dp = [[row[1]] * 2 for row in dp]

    return [row[1] for row in dp], backtrack

def middleEdge(v, w, cost, Table):
    rev_x=v[::-1]
    rev_y=w[::-1]
    arr=middleColumn(v, w, Table, cost)
    source_to_middle = arr[0]
    arr=middleColumn(rev_x, rev_y + ['', '$'][len(w) % 2 == 1 and len(w) > 1], Table, cost)
    middle_to_sink=arr[0][::-1]
    backtrack=arr[1]
    scores = map(sum, zip(source_to_middle, middle_to_sink))
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w) / 2 + 1)
    else:
        next_node = [(max_middle + 1, len(w) / 2 + 1), (max_middle, len(w) / 2 + 1), (max_middle + 1, len(w) / 2), ][backtrack[max_middle]]

    return (max_middle, len(w) / 2), next_node


def importdata():
    a=raw_input()
    b=raw_input()
    return a,b

string1,string2=importdata()
penalty=5
Table=blosum
middle = middleEdge(string1, string2, penalty,Table)
print(' '.join(map(str, middle)))
