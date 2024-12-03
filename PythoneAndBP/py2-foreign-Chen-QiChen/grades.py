import os
import sys
import pandas as pd
from tabulate import tabulate


def readTxt(GroupsFile):
    # 初始化一个空的字典来存储数据
    data = {}

    # 读取文件
    with open(GroupsFile, "r") as file:
        lines = file.readlines()

        current_category = None
        for line in lines:
            line = line.strip()  # 去掉首尾空白字符
            if len(line) == 1:  # 如果是单个字母，表示新的类别
                current_category = line
                data[current_category] = {"students": [], "class": []}  # 初始化字典
            elif line:  # 否则是数据行
                items = line.split(",")
                if current_category:  # 确保当前类别已定义
                    if (
                        len(data[current_category]["students"]) == 0
                    ):  # 如果学生列表为空，添加学生
                        data[current_category]["students"] = items
                    else:  # 否则添加课程
                        data[current_category]["class"] = items
    return data


def fetch(GroupsFile, GradesFile):
    # 读取以逗号分隔的文本文件
    Grades = pd.read_csv(GradesFile, header=None)
    Groups = readTxt(GroupsFile)
    return {"Grades": Grades, "Groups": Groups}


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    # def average_grade(self):
    #     total_grades = sum([sum(grades) for grades in self.grades.values()])
    #     total_subjects = sum([len(grades) for grades in self.grades.values()])
    #     return total_grades / total_subjects if total_subjects > 0 else 0
    def average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_subjects = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_subjects if total_subjects > 0 else 0


class Management:
    def __init__(self):
        self.students = {}
        self.groups = {}  # 用于存储组的信息

    def set_groups(self, groups):
        self.groups = groups

    def add_grade(self, group_name, course_name, student_name, grade):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
        self.students[student_name].add_grade(course_name, grade)

    def generate_report(self, group_filter=None):
        report = {}
        all_courses = set()  # 用于存储所有课程
        for student in self.students.values():
            if group_filter:
                if student.name not in self.groups.get(group_filter, {}).get(
                    "students", []
                ):
                    continue
            report[student.name] = {
                "Grades": student.grades,
                "Average": student.average_grade(),
            }
            all_courses.update(student.grades.keys())  # 更新所有课程

        # 为每个学生的成绩填充缺失的课程
        for student in report:
            for course in all_courses:
                if course not in report[student]["Grades"]:
                    report[student]["Grades"][course] = ["-"]  # 设置为 ['-']
                    report[student]["Average"] = ["-"]

        return report

    # def print_report(self, group_filter=None):
    #     report = self.generate_report(group_filter)
    #     report_df = pd.DataFrame.from_dict(report, orient="index")
    #     print(report_df)
    # def print_report(self, group_filter=None):
    #     report = self.generate_report(group_filter)
    #     table = []
    #     for student, details in report.items():
    #         table.append([student, details["Grades"], f"{details['Average']:.2f}"])
    #     print(
    #         tabulate(table, headers=["Student", "Grades", "Average"], tablefmt="grid")
    #     )
    def print_report(self, group_filter=None):
        report = self.generate_report(group_filter)
        table = []
        headers = ["Student"]  # 初始化表头

        # 获取所有课程并添加到表头
        all_courses = set()
        for details in report.values():
            all_courses.update(details["Grades"].keys())
        headers.extend(sorted(all_courses))  # 添加课程到表头

        # 填充表格数据
        for student, details in report.items():
            row = [student]
            for course in sorted(all_courses):
                if course in details["Grades"]:
                    # 将成绩转换为字符串，去掉方括号
                    grade = details["Grades"][course]
                    row.append(grade[0] if grade != ["-"] else "-")  # 处理缺失课程
                else:
                    row.append("-")  # 添加缺失课程的占位符
            table.append(row)

        # 添加平均分列
        headers.append("Average")
        for i, row in enumerate(table):
            student = list(report.keys())[i]
            average = report[student]["Average"]

            # 判断是否有 '-' 的成绩
            has_negative = any(
                "-" in grades for grades in self.students[student].grades.values()
            )

            # 根据是否有 '-' 来设置平均分的输出
            if has_negative:
                row.append("N/A")  # 或者其他自定义字符串
            else:
                row.append(f"{average:.2f}" if average is not None else "N/A")

        # 打印组过滤器信息
        if group_filter:
            print(f"\nGroup Filter: {group_filter}:")

        print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        GroupsFile = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件
        GradesFile = os.path.join(script_dir, sys.argv[2])  # 使用相对路径加载字典文件
    except EOFError as e:
        GroupsFile = sys.argv[1]  # 使用相对路径加载字典文件
        GradesFile = sys.argv[2]  # 使用相对路径加载字典文件
    # 创建管理实例
    management = Management()
    # 设置组信息
    groups_data = fetch(GroupsFile, GradesFile)["Groups"]
    management.set_groups(groups_data)
    # 添加成绩数据
    for index, row in fetch(GroupsFile, GradesFile)["Grades"].iterrows():
        group = row[0]  # 根据你的数据结构获取相应的列
        course = row[1]
        student = row[2]
        grade = row[3]
        management.add_grade(group, course, student, grade)
    # 生成成绩报告
    management.print_report(group_filter="B")
    management.print_report(group_filter="T")
