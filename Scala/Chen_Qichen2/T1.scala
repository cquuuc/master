object T1 {

  def factorial(num: Int): Int = {
    if (num == 0) 1
    else num * factorial(num - 1)
  }

  def main(args: Array[String]): Unit = {
    var X1 = scala.io.StdIn.readInt()
    println(factorial(X1))
  }
}
