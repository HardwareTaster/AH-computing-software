list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

target =int(input("enter number between 0 and 31 "))
found = "False"
low = 0
counter = 0
high = len(list)-1
while found == "False" and low<=high:
    middle = (high+low)//2
    if list[middle] == target:
        found = "True"
    elif list[middle] <target:
        low = middle+1
    else:
        high = middle -1
    counter+=1
    print (list[middle])
print(counter)