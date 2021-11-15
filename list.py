#LIST 

frnd = [ "ab", "bc", "cd"]
#print(frnd)
#accessing the elements of the list
#print(frnd[1])

#add a single element to the list
frnd.append("ef")
#print(frnd)

frnd.append("gh")
frnd.append("ij")
print(frnd)

#accessing a range of elements from a list
print(frnd[1:3])
print(frnd[1:])

#add to lists to together
l_num = [1,2,3]
#frnd.extend(l_num)

#to insert any element in between the list
frnd.insert(3, "sk")
print(frnd)

#to remove any element 
frnd.remove("sk")
print(frnd)

#to clear the whole list - frnd.clear()

#to find the index of any element present in the list
print(frnd.index("gh"))

#to count the occurence of any element in the list
print(frnd.count("ab"))

#to sort the list
frnd.sort()
print(frnd)

#to reverse a list
l_num.reverse()
print(l_num)

#to duplicate a list into another
frnd2 = frnd.copy()
print(frnd2)