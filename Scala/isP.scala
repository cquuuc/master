object isP {

  def isPrime(n: Int): Boolean = {
    if (n <= 1) false
    else if (n == 2) true
    else !(2 to (n - 1)).exists(x => n % x == 0)
  }

  def main(args: Array[String]): Unit = {
    var X1 = scala.io.StdIn.readInt()
    println(isPrime(X1))
  }
}
