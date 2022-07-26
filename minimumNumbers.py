# def minimumNumbers(num, k):
#     list_nums = [b for b in range(1,num+1)]
#     print(list_nums)
#     for i in list_nums:
#         d = [int(c) for c in str(i)]
#         print(d)
#         nine_set = []
#         for i in d:
#             if i == 9:
#                 nine_set.append(d)
#             elif d[-1] == 9:
#                 nine_set.append(d)
#                 return nine_set

# print(minimumNumbers(58, 9))


def minimumNumbers( num, k):
    """
    :type num: int
    :type k: int
    :rtype: int
    """
    if num == 0 :
        return 0

    for i in range(1, 11):
        if (num-i*k) % 10 == 0 and i*k <= num:
            print(num)
            return i
    return -1
print(minimumNumbers(80, 2))