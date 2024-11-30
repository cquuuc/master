class Employee(
    private var name: String,
    private var age: Int,
    private var position: String
) {

  // 显示员工详细信息的方法
  def getDetails(): Unit = {
    println(s"name: $name")
    println(s"age: $age")
    println(s"position: $position")
  }

  // 设置姓名
  def setName(newName: String): Unit = {
    name = newName
  }

  // 设置年龄
  def setAge(newAge: Int): Unit = {
    if (newAge >= 0) {
      age = newAge
    } else {
      println("age can't <0")
    }
  }

  // 设置职务
  def setPosition(newPosition: String): Unit = {
    position = newPosition
  }

}
