information={}
editing=True
info=['寄件人','寄件人电话','收件人','收件人电话']

for i in range(0,4):
    information[info[i]]=input('\t'+info[i]+':')
print('\t______________\n\t请确认信息:\n')

for x,y in information.items():
    print('\n\t'+x+':'+y)
print('\n')

while editing:
    item=input('''\t________________\n\t请输入需要修改的信息的序号：（如无需要，请按9）
    0 寄件人
    1 寄件人电话
    2 收件人
    3 收件人电话
    \n\t''')
    m=int(item)
    if m==9:
        break
    elif m>=0 and m<=4:
        information[info[m]]=input('\t'+info[m]+':')
        print('\t_______________\n\t请确认您的信息：\n')
        for a,s in information.items():
             print('\n\t'+a+':'+s)
    else:
        print('\t_________________\n\t请仅输入一个序号')
    judge=input('\t___________________\n\t输入小写字母y继续修改，其他按键结束')
    
    if judge=="y":
        continue
    else:
        editing=False