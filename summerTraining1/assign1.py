def GetInformation():
    Name = input('What is your name? ')
    Dept = input('What is your Dept? ')
    Degr = input('What is your Degree? ')
    return Name,Dept,Degr

Name, Dept, Degr = GetInformation()
Grade = ''
if int(Degr) >= 90: 
    Grade = 'Excellent'
elif int(Degr) >= 80: 
    Grade = 'Very Good'
elif int(Degr) >= 70: 
    Grade = 'Good'
elif int(Degr) >= 60: 
    Grade = 'Passed'
else:
    Grade = 'Failed'
print("Hello {0}, Your department is {1} and your degree is {2}".format(Name, Dept, Grade))
