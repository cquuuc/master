object ImperativeProgramming{
  def factorial(n: Int): Int = {
    var result = 1/*insert the initial resul value*/
    var i      = 1/*insert the initial i value*/
    while (i <= n) {
      result = result * i
      i = i + 1
    }
    result
  }

  def main(args: Array[String]): Unit = {
    println(factorial(5))
    println(factorial(11))
    println(factorial(15))
  }
}
