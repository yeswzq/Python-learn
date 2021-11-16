department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

#旧字符串格式
line1 = 'Department1 name:%-10s  Manager:%-10s COURSE_FEES:%-10.2f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2 name:%-10s  Manager:%-10s COURSE_FEES:%-10.2f The End!' % (department2,depart2_m,COURSE_FEES_Python)

#新字符格式串
#line3 = 'Department1 name:{0:<10} Manager:{0:<10} COURSE_FEES:{2:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
#line4 = 'Department1 name:{0:<10} Manager:{0:<10} COURSE_FEES:{2:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)


length = len(line1)
print('=' * length)
print(line1)
print(line2)
print('=' * length)
