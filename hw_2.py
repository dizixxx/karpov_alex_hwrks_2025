"""__________________________num 1__________________________"""

# def fubb(n):
#     if n == 0: return 1
#     if n == 1: return 1
#     if n > 1:
#         return fubb(n - 1) + fubb(n - 2)


"""-----------------"""


# n = int(input())
# fib_list = [1, 1]
# for i in range(n):
#     fib_list += [fib_list[-1] + fib_list[-2]]
    
# print(fib_list[-1])


"""__________________________num 2__________________________"""


# def is_correct_brackets_seq(str: str) -> bool:
#     stack = []
#     for char in str:
#         if char == "(": stack.append("(")
#         if char == ")": 
#             try:
#                 stack.pop()
#             except IndexError:
#                 return False
#     return not stack

# string = input()
# print(is_correct_brackets_seq(string))


"""__________________________num 3__________________________"""
# def plus_one(lst: list) -> list:
#     string = "".join([str(char) for char in lst])
#     res_lst = [char for char in str(int(string) + 1)]
#     return res_lst


# lst = map(int, input().split())
# print(plus_one(lst))


"""__________________________num 4__________________________"""


# def unique(string: str) -> dict:
#     chars_dict = {}
#     for char in string:
#         chars_dict[char] = 1 + chars_dict.get(char, 0)
#     return chars_dict


# string = input()
# print(unique(string))


"""__________________________num 5__________________________"""

# def two_sum(lst: list, num: int) -> tuple:
#     not_enough_sum = {}
#     for index, value in enumerate(lst):
#         not_enough_sum[index] = num - value
#         for search_index in not_enough_sum.keys():
#             if search_index != index:
#                 if (not_enough_sum[search_index] + not_enough_sum[index] == num):
#                     return (search_index, index)

# lst = [4, 5, 9, 5]
# num = 10 

# print(two_sum(lst, num))


"""__________________________num 6__________________________"""

# def format_number(number: float) -> str:
#     rounded = round(number, 3)
    
#     int_part = int(rounded)
#     fract_part = round(rounded - int_part, 3)
    
#     formatted_int = f"{int_part:,}".replace(',', ' ')
#     fract_str = f"{fract_part:.3f}".split('.')[1].lstrip('0')
#     if fract_str == "": fract_str = "0"
    
#     formatted_fractional = f". {fract_str:0<3}"
#     res_string = f"{formatted_int}{formatted_fractional}"
    
#     return f"{res_string:*^30}"

# number = float(input())
# print(format_number(number))