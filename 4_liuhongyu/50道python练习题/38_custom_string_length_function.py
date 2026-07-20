"""
题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
"""
letter = input("请输入一个字符串：")
def custom_string_length(string):
    len_letter = len(string)
    return len_letter
def main():
    print(custom_string_length(letter))

if __name__ == '__main__':
    main()