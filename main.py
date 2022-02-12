a = []
li=list()
m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
for i in range(m):          # A for loop for row entries
    b =[]
    for j in range(n):      # A for loop for column entries
         b.append(int(input()))
    a.append(b)
li= list()

#checking horizontal
for i in range(0,m):
  for j in range(0,n-3):
    if(a[i][j]==a[i][j+1]==a[i][j+2]==a[i][j+3]):
      li.append(a[i][j])
#print(z);
print("Hello");
#checking vertical
for i in range(0,m-3):
  for j in range(0,n):
    if(a[i][j]==a[i+1][j]==a[i+2][j]==a[i+3][j]):
      li.append(a[i][j])
#print(z);
print("Hello");
#checking diagonalr
for i in range(0,m-3):
  for j in range(0,n-3):
    if(a[i][j]==a[i+1][j+1]==a[i+2][j+2]==a[i+3][j+3]):
      li.append(a[i][j])
#print(z);
print("Hello");
#checking diagonall
for i in range(0,m-3):
  for j in range(3,n):
    if(a[i][j]==a[i+1][j-1]==a[i+2][j-2]==a[i+3][j-3]):
      li.append(a[i][j])
#print(z);
print("Hello");
print(li)
li=list(set(li))
li.sort()
print(li)
print(li[0])