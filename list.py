family=["devarajan" , "vasantha", "kalpana", "anand", "venkatesan", "sai", "praveen"]
totest = ["extend", "sort", "reverse", "insert","remove","count","index","clear","pop","copy"]
print("#list reverse function reverses order of the list#####")
totest.reverse()
print(totest)
########################
print("count function to count occurance of an element returns integer(1,2 etc")
print(family.count("anand"))
print("#sort list elements in ascending order")
family.sort()
print(family)
print(""##returns index of the given list value")
#family.index("sai")
##"extend function that combines elements in 2 lists")
family.extend(totest)
print(family)
#print("#reverse list elements order")
family.reverse()
print(family)
#print("# insert new value to existing list")
family.insert(4,"murali")
print(family)
print(""####remove a value from list")
print(totest.remove("copy")
print(family.count("praveen"))
print("###pop function removes last element from list")
totest.pop()
print(totest)
#print("###copy to create a duplicate of a list")
totest2 = totest.copy()
print(totest2)