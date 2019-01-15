#Python2.7
def importdata():
    a=raw_input()
    b=raw_input()
    r=raw_input()
    return a,b,r

def hamming(a,b):
    l=len(a)
    dis=0
    i=0
    while i<l:
        if a[i] != b[i]:
            dis += 1
        i+=1
    return dis

def alignment(a,b,r):
    seqs = [a, b]
    for i in range(len(seqs)):
        num = 0
        for j in range(len(seqs[i]) - len(r)):
            str = seqs[i][j:j + len(r)]
            dis=hamming(str, r)
            if dis < 4:
                num =num + 1
        print num,

a,b,r=importdata()
alignment(a,b,r)

