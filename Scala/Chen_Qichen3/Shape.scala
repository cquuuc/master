abstract class Shape {
  // 抽象方法，用于计算面积
  def area: Double
}

// Rectangle 类，继承自 Shape
class Rectangle(private val w: Double, private val h: Double) extends Shape {
  // 实现 area 方法
  override def area: Double = w * h
}

// Circle 类，继承自 Shape
class Circle(private val r: Double) extends Shape {
  // 实现 area 方法
  override def area: Double = 3.14 * r * r
}
