class Triangle(
    private val side1: Double,
    private val side2: Double,
    private val side3: Double
) {

  // 检查三角形是否为等边三角形
  def isEquilateral: Boolean = {
    side1 == side2 && side2 == side3
  }

  // 显示三角形的边长
  def displaySides(): Unit = {
    println(s"side1: $side1, side2: $side2, side3: $side3")
  }
}
