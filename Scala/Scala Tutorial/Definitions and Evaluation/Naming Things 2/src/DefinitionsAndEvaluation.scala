object DefinitionsAndEvaluation {

  def square(x: Double): Double = {
    x * x
  }

  def area(radius: Double): Double = {
    Math.PI * square(x = radius)
  }

  def main(args: Array[String]): Unit = {
    println(area(10))
  }
}