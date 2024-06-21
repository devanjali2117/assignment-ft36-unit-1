
def solve(N,M,arr):

    for j in range(M):
        column_sum=0
            for i in range(N):
            if arr[i][j]%2 !=0:
            column_sum+=arr[i][j]
print(column_sum)        