# -*-coding:gbk-*-
import re

reg_if_condition = re.compile(r'(if.+?;|else if.+?;|else.+?;)')

if __name__ == '__main__':
    l = "if((x1&0x0f)/0x01==0)y=@029e;" \
        "else if((x1&0x0f)/0x01==1)y=@029f;" \
        "else if((x1&0x0f)/0x01==2)y=@02a0;" \
        "else if((x1&0x0f)/0x01==3)y=@02a1;" \
        "else if((x1&0x0f)/0x01==4)y=@02a2;" \
        "else if((x1&0x0f)/0x01==5)y=@02a3;" \
        "else if((x1&0x0f)/0x01==6)y=@0290;" \
        "else if((x1&0x0f)/0x01==7)y=@0127;" \
        "else y=@029e; "

    if 'if' in l:
        l = str.replace(l,'else if','elif')
        reg_if_condition = re.compile(r'if\((?P<condition>.+?)\)(?=y)(?P<other>.+?);')
        def if_sub(match):
            return 'if ' + match.group('condition') + ':\n        ' + match.group('other') + '\n    '
        if_cases = reg_if_condition.sub(if_sub, l)

        reg_elseif_condition = re.compile(r'else')

        else_execution = reg_elseif_condition.sub(r'else:\n        ',if_cases)
        else_execution = else_execution.replace(';','\n')
        def print_sub(match):
            return "'" + match.group('out_str') + "'"
        reg_y_str = re.compile(r'(?<=y=)(?P<out_str>.+?)(?=\n)')
        y_execution = reg_y_str.sub(print_sub,else_execution)
        final_fun = 'def func(x1):\n    '+ y_execution + 'return y'
        print(final_fun)
        y = None
        exec(final_fun)
        print(y)
#     l1 = '''
# def func(x1):
# 	if (x1&0x0f)/0x01==0:
# 		y='@029e'
# 	elif (x1&0x0f)/0x01==1:
# 		y='@029f'
# 	elif (x1&0x0f)/0x01==2:
# 		y='@02a0'
# 	elif (x1&0x0f)/0x01==3:
# 		y='@02a1'
# 	elif (x1&0x0f)/0x01==4:
# 		y='@02a2'
# 	elif (x1&0x0f)/0x01==5:
# 		y='@02a3'
# 	elif (x1&0x0f)/0x01==6:
# 		y='@0290'
# 	elif (x1&0x0f)/0x01==7:
# 		y='@0127'
# 	else:
# 	    y='@029e'
# 	return y
# print(func(0x01))
# out = func(0x01)
# '''
#     # out = reg_if_condition.findall(l)
#     print(exec(l1))
#     print(out)
#     # for i in out:
#     #     print(i)
