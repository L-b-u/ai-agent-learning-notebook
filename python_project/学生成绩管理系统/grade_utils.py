import threading


student_records = {}
record_lock = threading.Lock()

#检查成绩是否在有效范围
def check_valid_score(score, max_score):
    score = int(score)
    max_score = int(max_score)
    if score < 0 or score > max_score:
        raise ValueError()

#计算得分率 = 分数/满分 × 100%
def calc_percentage(score, max_score):
    score_rate = score / max_score
    return score_rate

#使用 with 追加写入 exam_records.txt
def save_record(record_info):
    with open('exam_records.txt', 'a',encoding="utf-8") as f:
        f.write(record_info + '\n')
    print('成绩记录已保存，文件自动关闭。')

#使用 with 读取全部成绩记录
def read_all_records():
    with open('exam_records.txt', 'r', encoding="utf-8") as f:
        records = f.readlines()
    return records

#列表推导式筛选达到优秀的学生
def get_excellent_students(score_dict, threshold):
    excellent_students = [
        name for name, subjects in score_dict.items()
        if sum(subjects.values()) / len(subjects) >= threshold
    ]
    return excellent_students

#生成器，yield 格式化成绩单字符串
def report_card_generator(student_list):
    for student in student_list:
        yield f"学生姓名：{student}\n{student_records[student]}"

#线程锁安全录入成绩
def input_score_thread_safe(student_name, subject, score):
    with record_lock:
        if student_name not in student_records:
            student_records[student_name] = {}
        student_records[student_name][subject] = score


#创建2个线程并发录入测试
def multi_thread_input_test():
    t1 = threading.Thread(target=input_score_thread_safe, args=("张三", "数学", 140))
    t2 = threading.Thread(target=input_score_thread_safe, args=("张三", "语文", 100))
    t3 = threading.Thread(target=input_score_thread_safe, args=("张三", "英语", 80))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    save_record(f"{student_records}")

if __name__ == '__main__':
    #多线程测试
    multi_thread_input_test()