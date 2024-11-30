object T8 {
  def iseven(num: Int): Boolean = {
    if (num % 2 == 0) true
    else false
  }

  def main(args: Array[String]): Unit = {
    var X1 = scala.io.StdIn.readInt()
    println(iseven(X1))
  }
}
