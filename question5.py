dic={}
dic['name']='jackey'
dic['color']='brown'
dic['breed']='biscuit'
dic['legs']='4'
dic['age']='2'
print(dic)

student={}
student['first_name']="jolly"
student['last_name']="suzi"
student['gender']="female"
student['age']="22"
student['martial_status']="unmarried"
student['skills']="mba pass"
student['country']="india"
student['city']= "faridabad"
student['address']="fkn,jchfvjcmchmh"
print(student)
print(len(student))
print(student['skills'])
print(type(student))
#add value
student['skills']=['css','python']
print(student)
print(student.keys())
print(student.values())
#dic to convert tuple
print(student.items())

student.pop('address')
student.popitem()
print(student)
#one more method
del student['skills']
print(student)

#delete one dicitonary
del student
print(student)


