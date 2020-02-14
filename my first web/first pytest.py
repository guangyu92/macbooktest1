import unittest
import os



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


class Circle():

    def __init__(self,radius,center):
        self.radius=radius
        self.center=center
    
    def printcircle(self):
        print('\tthe radius is '+str(self.radius)+
        '\n\tthe center is '+str(self.center))

circle_1=Circle(4,(2,4))
circle_1.printcircle()    

name=input('please enter your name: ')
tel=input('please enter your tel: ')

with open('first_write.txt','w') as file:
    file.write(name)
    file.write(tel)



    


    
