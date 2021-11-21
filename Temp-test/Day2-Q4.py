department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = '456789.12456'
COURSE_FEES_Python = 1234.3456

print(type(department1))
print(type(depart1_m))
print(type(COURSE_FEES_SEC))

s = 'i am %s,age %d' %('cai',18)

# SEC = 'department1 name:%-10s Manager:%-10s Course:%-10s' % (department1,depart1_m,COURSE_FEES_SEC)
# Python = 'department1 name:%-10s Manager:%-10s Course:%-10.2f' % (department2,depart2_m,COURSE_FEES_Python)
# line1 = 'department1 name:%s Manager:%s Course:%s' % (department1,depart1_m,COURSE_FEES_SEC)
# print(SEC)
# print(Python)

# int1 = int(COURSE_FEES_SEC)
# print(type(int1))
# print(int1)

str1 = "10.12"

int1 = int(str1)
print(type(int1))
print(int1)