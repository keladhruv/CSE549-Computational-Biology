def solution(a,b):
    l1,l2=len(a),len(b)
    DP = [[0 for j in range(l2 + 2)] for i in range(l1 + 2)]
    counts = [[0 for j in range(l2 + 2)] for i in range(l1 + 2)]

    for i in range( l1 + 1):
        DP[i][0] = i
        counts[i][0]=1

    for j in range(l2 + 1):
        DP[0][j] = j
        counts[j][0] = 1

    for i in range(1,l1+1):
        for j in range(1,l2+1):
            value = [0, 0, 0]
            if a[i-1]==b[j-1]:
                value[0]=(DP[i-1][j-1])
            else:
                value[0]=(DP[i - 1][j - 1] + 1)
            value[1]=(DP[i - 1][j] + 1)
            value[2]=(DP[i][j - 1] + 1)
            DP[i][j]=min(value)
            if DP[i][j]==value[0]:
                counts[i][j] += counts[i - 1][j - 1]
            if DP[i][j]==value[1]:
                counts[i][j] += counts[i - 1][j]
            if DP[i][j]==value[2]:
                counts[i][j] += counts[i][j - 1]
            counts[i][j] = counts[i][j] % 134217727

    return counts[l1][l2]






def importdata():
    a=raw_input()
    b=raw_input()
    return a,b

string1,string2=importdata()
#string1,string2="PLEASANTLY", "MEANLY"
data=solution(string1,string2)
print data