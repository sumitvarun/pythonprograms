List= [[100,200],[300,400],[500,600],[700,800],[900,1000]]
sum1=0;
for i in range(5):
    print("Index:",i)
    for j in range(2):
        print(" InnerIndex:",j,"=",List[i][j])
        print(sum(List[i]))
        sum1=sum1+List[i][j]

print(sum1)
