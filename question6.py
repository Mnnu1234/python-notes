#set the dicitionary
it_companies= {'facebook','google','Microsoft','IBM','oracel','Amazone'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
#find len of it_companies
print(len(it_companies))
#add twitter to it_companies
it_companies.add('twitter')
print(it_companies)
#insert multiple it_companies from set it_companies
it_companies.update({'linux','utube','insta','it'})
print("after inserting multiple values:",it_companies)
#remove one of the companies
it_companies.remove('it')
print("after removing one of the it_companies",it_companies)
#diference between remove and discard
it_companies.discard('twitter')
print(it_companies)
#join A and B
join=A.union(B)
print("after joining A and B",join)
#find A intersection B
intersection=A.intersection(B)
print("after intersection A and B",intersection)
#is A subset B
subset=A.issubset(B)
print("A is subset of B",subset)
#are A and B disjoint sets
disjoint=A.isdisjoint(B)
print("Are a is disjoint of B",disjoint)
#join A with B and B with A
t1=A.union(B)
t2=B.union(A)
print("A with B:",t1)
print("B with A:",t2)
#symmetric difference btwn A and B
symm=A.symmetric_difference(B)
print(B)
# delete the set completely
del(A)
'''print(A)'''
#convert ages to set and compare length of list and set
new_age=set(age)
print("length of age list",len(age))
print("length of age set",len(new_age))
#compare len
if len(age)>len(new_age):
    print("length of age in list bigger by",len(age)-len(new_age))
else:
    print("length of age in dic is bigger than",len(new_age)-len(age))
#explain difference btwn the following data types:list tuple,string and set
string="\t\t**STRING**\n\ni.string is immutable.\nni.string are written in single or double quotes\nExample:-name='mnnu'"

lis1="\t\t**LIST**\n\ni.list is mutable.\nii.list consume more memory\niii.list are written between square brackets[].\nExample:-[1,2,3,3,4]"

tupl="\t\t**TUPLE**\n\ni.tuple is immutable.\nni.tuple consume less space the list\niii.tuple are written between paranthesis brackets().\nExample:-(1,2,3,4)"

set1="\t\t**SETS**\n\ni.Set are immutable.\nii.list consume less space\niii.sets are written between cruly braces {}.\nExample:-{1,2,3,3,4}"

total=[string,lis1,tupl,set1]
for i in range(4):
    print("\n")
    print(total[i],end="")
    print("\n")
    for j in range(10):
        print("------",end="")