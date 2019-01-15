#Python
#Referred geeks for geeks 
def input():
    file = open('test.txt', 'r')
    m=file.readlines()
    a = raw_input()
    b = raw_input()

    return a,b,len(a),len(b)

def edit(s1,s2,l1,l2,arr):
    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0:
                arr[i][j] = j
            elif j == 0:
                arr[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = 1 + min(arr[i][j-1],arr[i-1][j],arr[i-1][j-1])
    return arr[l1][l2]

s1,s2,l1,l2=input()
arr = [[0 for x in range(l2+1)] for x in range(l1+1)]
distance=edit(s1,s2,l1,l2,arr)
print distance

