object T9 {
  def isPerfectSquare(num: Int): Boolean = {
    var i = 1
    var square = 1

    while (square <= num) {
      if (square == num) {
        return true
      }
      i += 1
      square = i * i
    }

    false
  }

  def main(args: Array[String]): Unit = {
    var X1 = scala.io.StdIn.readInt()
    println(isPerfectSquare(X1))
  }
}
