def get_profile(first_name,second_name,**info):
    profile={}
    profile["first_name"]=first_name
    profile['second_name']=second_name

    for key,value in info.items():
        profile[key]=value
    return profile

user_info=get_profile("underwood","frank",sex='man',weight='180',height='175',hobby='play')

for x,y in user_info.items():
    print('\n\t'+str(x)+':'+str(y))
