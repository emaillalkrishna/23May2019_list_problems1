# # Python program to find sum of elements in list
# total = 0
#
# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # Iterate each element in list and add them in variale total
# for ele in range(0, len(list1)):
#     total = total + list1[ele]
#
# # printing total value
# print("Sum of all elements in given list: ", total)

# ----------------------------------------------

# # Python program to find sum of elements in list
# total = 0
# ele = 0
#
# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # Iterate each element in list and add them in variale total
# while (ele < len(list1)):
#     total = total + list1[ele]
#     ele += 1
#
# # printing total value
# print("Sum of all elements in given list: ", total)

# ----------------------------------------------

# # Python program to find sum of all elements in list using recursion
# # # creating a list
# list1 = [11, 5, 17, 18, 23]
#
#
# # creating sum_list function
# def sumOfList(list, size):
#
#
#     if (size == 0):
#         return 0
#     else:
#         return list[size - 1] + sumOfList(list, size - 1)
#
#     # Driver code
# total = sumOfList(list1, len(list1))
#
# print("Sum of all elements in given list: ", total)

# -----------------------------------------------------

# Python program to find sum of elements in list

# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # using sum() function
# total = sum(list1)
#
# # printing total value
# print("Sum of all elements in given list: ", total)
