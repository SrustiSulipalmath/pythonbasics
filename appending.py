from Functions import employee_file

employee_file=open("employees.txt","a")
employee_file.write("Toby-Human resources")
employee_file.write("\nkelly-customerservice")
employee_file.close()