a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

result=[]

for i in range(2):
    row=[]

    for j in range(2):
        row.append(a[i][j]+b[i][j])

    result.append(row)

print(result)
