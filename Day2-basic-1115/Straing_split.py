#时间2021-11-15 Day2作业-正则切片 第2题
#现在有个字符串word = " scallywag"，创建一个变量sub_word，通过切片的方式获得字符串"ally"，将字符串的内容赋予sub_word。

# >>> line = 'aaa bbb ccc;ddd   eee,fff'
# >>> re.split(r';',line)
# ['aaa bbb ccc', 'ddd\teee,fff']


# a='Beautiful, is; better*than\nugly'
# b = re.split(pattern='[,;*\n]',string=a)[-1]
# print(b)

#['', '', 's', 'c', 'a', 'l', 'l', 'y', 'w', 'a', 'g', '']
import re

word = " scallywag"
sub_word = word[3:7]
print(sub_word)
print(word[3:7])

sub_word1 = re.split(pattern='\W*' ,string=word)[4:5]
print(sub_word1)
