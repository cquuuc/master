// 定义 Person 类
class Person(
    private var name: String,
    private var age: Int,
    private var country: String
) {

  // 获取姓名
  def getName: String = name

  // 设置姓名
  def setName(newName: String): Unit = {
    name = newName
  }

  // 获取年龄
  def getAge: Int = age

  // 设置年龄
  def setAge(newAge: Int): Unit = {
    if (newAge >= 0) {
      age = newAge
    } else {
      println("age cant <0")
    }
  }

  // 获取国家
  def getCountry: String = country

  // 设置国家
  def setCountry(newCountry: String): Unit = {
    country = newCountry
  }

  // 打印 Person 信息
  def Info(): Unit = {
    println(s"name: $name, age: $age, country: $country")
  }
}

// // 测试 Person 类
// object Main1 extends App {

// }
