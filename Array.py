import numpy as np

def Array_1(nums):
    def Arr_1():
        result=[]
        if len(nums)<0:
            return 0
        else:
            for i in nums:
                result.append(i / 5)
        return np.array(result, dtype=float)
    return Arr_1


def Array_2(nums):
    def Arr_2():
        result=[]
        if len(nums)<0:
            return 'В данном списке значений числа нет'
        else:
            for i in nums:
                result.append(i / 5)
        return result
    
    my_list = Arr_2()
    
    if len(my_list) > 0:
        res = np.array(my_list, dtype=float)
        return res
    else:
        return 'В данном списке значений числа нет'


nums = []
for i in range(10):
    nums.append(float(input('Введите значение: ')))

print(Array_1(nums)())

print(Array_2(nums))
