def twoSum(nums, target):
    indexnum = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            current_sum = nums[i] + nums[j]
            if current_sum == target:
                indexnum.append(i)
                indexnum.append(j)
                return indexnum


user_input = input("Enter a list of number(seperated by spaces): ")
input_list = [int(n) for n in user_input.split()]
user_target = int(input("Enter the expected result number:"))
result = twoSum(input_list, user_target)

print(f"List: {input_list}")
print(f"target: {user_target}")
print(f"The index of sum up value: {result}")
