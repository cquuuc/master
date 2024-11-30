object T4 {
  def reverseStr(str: String): String = {
    return str.reverse
  }

  def main(args: Array[String]): Unit = {
    var X1 = scala.io.StdIn.readLine()
    println(reverseStr(X1))
  }

}
