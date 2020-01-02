information={}
editing=True
info=["寄件人：","寄件人地址：","寄件人电话：","收件人：","收件人地址：","收件人电话："]
print('\t')
for a in range(0,6):
    information[info[a]]=input('\t'+info[a]+':')
print('\t_________________\n\t请确认信息：\n')

for x,y in information.items():
    print('\n\t'+x+':'+y)
print('\n')

while editing:
    item=input('''\t________________\n\t请输入需要修改的信息的序号：（如无需要，请按9）
    0 寄件人
    1 寄件人地址
    2 寄件人电话
    3 收件人
    4 收件人地址
    5 收件人电话
    \n\t''')
    z=int(item)
    if z==9:
        break
    elif z<=5 and z>=0:
        information[info[z]]=input('\t'+info[z]+':')
        print('\t_______________\n\t请确认您的信息：\n')
        for m,n in information.items():
            print('\n\t'+m+':'+n)
    
    else:
        print('\t_________________\n\t请仅输入一个序号')
    judge=input('\t___________________\n\t输入小写字母y继续修改，其他按键结束')

    if judge=="y":
        continue
    else:
        editing=False