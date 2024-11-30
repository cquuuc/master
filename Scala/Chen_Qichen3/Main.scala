object Main extends App {
  // 创建 Rectangle 对象
  val rectangle2 = new Rectangle2(10.0, 5.0)

  // 显示矩形的详细信息
  rectangle2.displayDetails()

  // 调整矩形的大小
  rectangle2.resize(2.0) // 将矩形大小扩大 2 倍
  rectangle2.displayDetails()

  rectangle2.resize(0.5) // 将矩形大小缩小 0.5 倍
  rectangle2.displayDetails()

  rectangle2.resize(-1.0) // 测试无效的缩放因子
  print("\n")

  // 创建不同的 Triangle 对象
  val triangle1 = new Triangle(5.0, 5.0, 5.0) // 等边三角形
  val triangle2 = new Triangle(5.0, 4.0, 5.0) // 不是等边三角形

  // 显示三角形的边长并检查是否为等边三角形
  triangle1.displaySides()
  println(s"triangle1 is equilateral: ${triangle1.isEquilateral}")

  triangle2.displaySides()
  println(s"triangle2 is equilateral: ${triangle2.isEquilateral}")

  print("\n")

  val animal = new Animal("Dog", "woof,woof")
  animal.makeSound()
  animal.setName("Fox")
  animal.setSound("大楚兴,陈胜王")
  animal.makeSound()
  print("\n")

  val car = new Car("BMW", "X5", 2024)
  car.getInfo()
  car.setMake("UFO")
  car.setModel("Earth-10")
  car.setYear(4202)
  println("\nafter update:")
  car.getInfo()
  print("\n")

  // 创建 Employee 对象
  val employee = new Employee("Alice", 10, "CFO")

  // 显示员工详细信息
  employee.getDetails()

  // 修改员工信息
  employee.setName("Bob")
  employee.setAge(15)
  employee.setPosition("CEO")

  // 显示修改后的员工详细信息
  println("\naftef update:")
  employee.getDetails()

  print("\n")
  // 创建 BankAccount 对象
  val account = new BankAccount("123456789")

  // 测试存款
  account.deposit(1000.0)
  account.deposit(500.0)

  // 测试取款
  account.withdraw(200.0)
  account.withdraw(5500.0) // 超过余额的取款
  account.withdraw(-50.0) // 负数取款

  // 打印当前余额
  println(
    s"ACC: ${account.getAccountNumber}, Balance: ${account.getBalance}BYN."
  )

  print("\n")
  // 创建 Rectangle 对象
  val rectangle = new Rectangle(5.0, 3.0)
  println(s"RT's Area: ${rectangle.area}")

  // 创建 Circle 对象
  val circle = new Circle(2.0)
  println(s"circle's Area: ${circle.area}")

  print("\n")
  // 测试 factorial 方法
  val number = 5
  val result = MathUtils.factorial(number)
  println(s"$number! is: $result")

  // 测试负数情况
  try {
    val negativeResult = MathUtils.factorial(-1)
  } catch {
    case e: IllegalArgumentException => println(e.getMessage)
  }

  print("\n")
  // 创建 Student 对象
  val student = new Student("Jack", 20, "USA", "SSR")

  // 打印初始信息
  student.Info()

  // 修改属性
  student.setName("Bob")
  student.setAge(21)
  student.setCountry("Canada")
  student.setGrade("S")

  // 打印修改后的信息
  student.Info()

  print("\n")
  // 创建 Person 对象
  val person = new Person("Chirs", 25, "HK")

  // 打印初始信息
  person.Info()

  // 修改属性
  person.setName("Natasha")
  person.setAge(25)
  person.setCountry("RUS")

  // 打印修改后的信息
  person.Info()
}
