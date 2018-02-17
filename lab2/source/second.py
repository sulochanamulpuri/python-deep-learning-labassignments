n = int(input("Number of contacts : "))
contacts = []
dummydict = {}
for i in range(n) :
    dummydict["name"] = input("Enter name ")
    dummydict["number"] = input("Enter number ")
    dummydict["email"] = input("Enter email ")
    contacts.append(dummydict.copy())
print(contacts)
def choice() :
    x = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
    return x

if choice()=='a':
    name = str(input("Enter the name: "))
    for a in contacts:
        if a['name'] == name:
            print(a)
if choice()=='b':
    num = str(input("Enter the number: "))
    for a in contacts:
        if a['number'] == num:
            print(a)
if choice()=='c':
    name = str(input("Enter the name: "))
    number = int(input("Enter the number: "))
    for index,a in enumerate(contacts):
        if a['name'] == name:
            contacts[index]['number']=number
    print(contacts)
if choice()=='d' :
    exit()