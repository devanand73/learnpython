#create a new file and write to it append to file read a file and read/write

# employee_file = open("employees.txt" , "r")
# employee_file = open("employees.txt" , "w")
employee_file = open("employees.txt" , "a")
# employee_file = open("employees.txt" , "r+")
# print(employee_file.writable())
#employee_file.writelines("devarajan--senior manager \n vasantha--CEO \n Anand--manager \n kalpana-- human resource \n praveen--supervisor ")
# employee_file.write("vasantha--CEO \n")
# employee_file.write("Anand--manager \n")
# employee_file.write("kalpana-- human resource \n")
# employee_file.write("praveen--supervisor\n")
#employee_file.close()
#print(employee_file.read())
print(employee_file.write("sai suushman-- doctor"))