mylist = ["A", "B" , "C", 1]

print("Print the first list element :  %s " % mylist[0])

print("Print the last element, Negative values starts the list from the end : %s "  % mylist[-1])

print("Sublist - first and second element : %s "  % mylist[0:2])

# Add elements to the list
mylist.append("D")

# Print the content of the list
for element in mylist:
    print(element)
    
    
list1 = ["A", "B" , "C"]
list2 = ["A", "X" , "D", 1, 2, 4]
print(len(list1))
print(len(list2))


difference = list(set(list1).difference(set(list2))) 

print ("Difference between two lists %s " % difference) 

listOfNumbers = ["1","2","3","4"]
listOfNumbers = map(int, listOfNumbers) 
print listOfNumbers



