family=["devarajan" , "vasantha", "kalpana", "anand", "venkatesan", "sai", "praveen","anand"]
totest = ["extend", "sort", "reverse", "insert","remove","count","index","clear","pop","copy"]


print(family.index("anand"))
family.remove("anand")
print(family)
print(family.pop(4))
print(family)
family2=family.copy()
print(family2)
family.append("sai")
print(family)
family.insert(-2,"murali")
print(family)
family.extend(totest)
print(family)
family.count()
print(family)

family.