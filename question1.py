a=[]

list=['helo','python','is','a','programming','language']
print(list)
print(len(list))
print(list[0])

mid=int(0+len(list))/2
print(mid)
print(list[3])
'''mid=(len(list)-1)/2
print(mid)'''
print(list[5])

mixed_data_type=['mnnu','18','5.2','nothing','1618']
print(mixed_data_type)

it_companies=['fackbook','Google','Microsft','Apple','ibm','oracel','Amazone']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
mid=int(0+len(list))/2
print(mid)
print(it_companies[3])
print(it_companies[6])

it_companies[3]='pvt'
print(it_companies)
it_companies.append('one tick')
print(it_companies)

midcom=int(0+len(it_companies)/2)
it_companies.insert(midcom,'twitter')
print(it_companies)

it_companies[5]=it_companies[5].upper()
print(it_companies)

for i in range(0,len(it_companies)):
    it_companies[i]="#"+it_companies[i]
print(it_companies)

for i in it_companies:
    if i in it_companies:
        print("yes")

it_companies.sort()
print(it_companies)


it_companies.reverse()
print(it_companies)

print(it_companies[0:3])#slice
print(it_companies[4:8])
print(it_companies[2:5])

it_companies.remove('#oracel')
print(it_companies)
it_companies.pop(3)
print(it_companies)
it_companies.pop()
print(it_companies)

'''del it_companies'''


it_companies.clear()
print(it_companies)

#join the following list:
front_end=['HTML','CSS','React','Redux']
back_end=['Node','Express']
'''front_end.join(back_end)'''
list3= front_end+back_end
print(list3)











