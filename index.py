# Task1 Take a list of dictionary{Name: ,age: ,citize: }
#  check whether that person is eligible for vote or not and also check the citizen.
# if both conditions are True add { eligible: True}
details=[{"name":"madhu","age":17,"citizen":"indian"},
         {"name":"srinivas","age":19,"citizen":"indian"}]
for i in range(0,len(details),1):
    if details[i]["age"]>18 and details[i]["citizen"]=="indian":
       details[i]["eligible"]=True
    else:
        details[i]["eligible"]=False    
print(details)


# Task2: Take a tuple of elements, print the unique elements in the new list
my_tuple=(1,4,3,55,55,6,6,43,23,45,9,9)
newlist=[]
for i in range(len(my_tuple)):
    number=my_tuple[i]
    if my_tuple.count(number)==1:
     newlist.append(number)
print(newlist)
