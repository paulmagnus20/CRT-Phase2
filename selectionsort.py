def Selectionsort(nums):
    n=len(nums)
    fixThisIndex=n-1
    while fixThisIndex>0:
        maxEleIndex=fixThisIndex
        
        for index in range(fixThisIndex):
            if nums[index]>nums[maxEleIndex]:
                maxEleIndex=index
                
        if maxEleIndex!= fixThisIndex:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[fixThisIndex]
            nums[fixThisIndex]=temp
        print(nums)
        fixThisIndex-=1
nums=[10,8,2,14,12,7]
print("Before sorting", nums)
Selectionsort(nums)
print("After Sorting", nums)