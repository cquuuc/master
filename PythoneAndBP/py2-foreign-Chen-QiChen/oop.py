class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Task: {self.name}, Description: {self.description}"


class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []

    def _add(self, task):
        """添加任务到项目中"""
        self.tasks.append(task)

    def _delete(self, task_name):
        """根据任务名称删除任务"""
        initial_count = len(self.tasks)
        self.tasks = list(filter(lambda task: task.name != task_name, self.tasks))
        if len(self.tasks) < initial_count:
            return f"Task '{task_name}' has been removed."
        return f"Task '{task_name}' not found."

    def _info(self):
        """显示所有任务"""
        if not self.tasks:
            return "No tasks in this project."
        return "\n".join(str(task) for task in self.tasks)

    @property
    def task_count(self):
        """获取项目中的任务总数"""
        return len(self.tasks)

    def __str__(self):
        return f"Project: {self.project_name}, Total Tasks: {self.task_count}"


# 演示类的使用
if __name__ == "__main__":
    # 创建项目
    project = Project("Website Development")

    # 创建任务
    task1 = Task("Design", "description1")
    task2 = Task("Development", "description2")
    task3 = Task("Testing", "description3")

    # 添加任务到项目
    project._add(task1)
    project._add(task2)
    project._add(task3)

    # 显示项目和任务
    print(project)
    print(project._info())

    # 删除一个任务
    print(project._delete("Development"))

    # 再次显示项目和任务
    print(project)
    print(project._info())
