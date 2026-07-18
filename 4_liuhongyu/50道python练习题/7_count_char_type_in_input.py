"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
def count_char_type_in_input(s):
    letter_num = 0
    space_num = 0
    digit_num = 0
    other_num = 0
    for i in s:
        if i.isalpha():
            letter_num += 1
        elif i.isspace():
            space_num += 1
        elif i.isdigit():
            digit_num += 1
        else:
            other_num += 1
    print(f"{letter_num}个英文字母,{space_num}个空格,{digit_num}个数字,{other_num}个其他字符")
count_char_type_in_input("hello world 123 !@#")