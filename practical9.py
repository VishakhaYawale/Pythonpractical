#creating a list
print("Empty List")
demo_list=[]
print("demo_list:",demo_list)
print()

#Adding elements to list
demo_list.append('N')
demo_list.append('A')
demo_list.append('P')
demo_list.append('U')
print("After Adding elements to the list:")
print("demo_list:",demo_list)
print()

#Deleting elements from the list
del(demo_list[3])
print("After Deleting element from list:")
print("demo_list:",demo_list)
print()

#Sorting element from the list
demo_list.sort()
print("After Sorting element to the list:")
print("demo_list:",demo_list)
print()

#Reversing elements from the list
demo_list.reverse()
print("After reversing the elements:")
print("demo_list:",demo_list)
print()

#Counting the elements in the list
print("No of elements:",len(demo_list))

