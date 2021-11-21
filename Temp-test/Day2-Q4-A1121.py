department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = '456789.12456'
COURSE_FEES_Python = 1234.3456

print(type(department1))
print(type(depart1_m))
print(type(COURSE_FEES_SEC))


#字符串格式化要记得\s字符串 \d数字 \f浮点数 等要对应的上，不然会报错。 float()是直接将字符串转成浮点数调用。不然就只能切片来显示小数点，但这样是不完美的。
#旧字符串的对齐，-10s就是左对齐，10s默认是右对齐。010d就是数字左补零。 -6.2f就是左占6个位，2个小数点对齐。这个可以左右试试结果就知道，也不必要刻意记。
SEC = 'department1 name:%-10s Manager:%-10s Course:%-10.2f' % (department1,depart1_m,float(COURSE_FEES_SEC))
Python = 'department2 name:%-10s Manager:%-10s Course:%-10.2f' % (department2,depart2_m,COURSE_FEES_Python)


#新字符串格式化的方法。要点就是对齐方式和旧的不一样。
# （1）< （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐
# （2）取位数“{:4s}”、"{:.2f}"等]。 发现字符串默认是左对齐，数字是右对齐的。
SEC1 = 'department1 name:{:10s} Manager:{:10s} Course:{:<10.2f}'.format(department1,depart1_m,float(COURSE_FEES_SEC))
SEC2 = 'department1 name:{:10} Manager:{:10} Course:{:<10.2f}'.format(department2,depart2_m,COURSE_FEES_Python)
print(SEC1)
print(SEC2)
print(SEC)
print(Python)

#下面为fstring的格式方法，看起来的话相对更简介的语法。字符串是左对齐，数字是右对齐。
print(f'department1 name:{department1:10s} Manager:{depart1_m:10s} Course:{float(COURSE_FEES_SEC):<10.2f}')
print(f'department1 name:{department2:10s} Manager:{depart2_m:10s} Course:{COURSE_FEES_Python:<10.2f}')

# 1.print('{} and {}'.format('hello','world'))  # 默认左对齐
# hello and world
# 2.print('{:10s} and {:>10s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
# hello      and      world
# 3.print('{:^10s} and {:^10s}'.format('hello','world'))  # 取10位中间对齐
#   hello    and   world
# 4.print('{} is {:.2f}'.format(1.123,1.123))  # 取2位小数
# 1.123 is 1.12
# 5. print('{0} is {0:>10.2f}'.format(1.123))  # 取2位小数，右对齐，取10位
# 1.123 is       1.12
