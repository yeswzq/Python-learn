# >>> line = 'aaa bbb ccc;ddd   eee,fff'
# >>> re.split(r';',line)
# ['aaa bbb ccc', 'ddd\teee,fff']


# a='Beautiful, is; better*than\nugly'
# b = re.split(pattern='[,;*\n]',string=a)[-1]
# print(b)

import re           #导入了模块，原来是要有调用才会变成高亮。

sub_word2 = re.split(pattern='\W*' ,string=word)[4:8]
print(sub_word2)
