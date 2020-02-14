nums=[1,2,3,2,22,43,12,42,21]



length=len(nums)

for i in range(length):
    couting=0
    for j in range(length-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            couting+=1
    if couting==0:
        break


print(nums)



