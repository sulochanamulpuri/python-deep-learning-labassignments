d = {'python': 30 , 'c': 20 ,'java': 50}
X=int(input("enter lower range:"))
Y=int(input("enter upper range"))
lister=[]
for key, value in d.items():
    if value in range(X,Y+1):
        lister.append(key)
print("you can purchase books : " , lister)