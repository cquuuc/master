object T7 {

  def power(base: Double, exponent: Int): Double = {
    if (exponent == 0) {
      return 1
    } else if (exponent % 2 == 0) {
      val halfPower = power(base, exponent / 2)
      return halfPower * halfPower
    } else {
      if (exponent > 0) {
        return base * power(base, exponent - 1)
      } else {
        return (1 / base) * power(base, exponent + 1)
      }
    }
  }

  def main(args: Array[String]): Unit = {
    var base = scala.io.StdIn.readInt()
    var x = scala.io.StdIn.readInt()
    println(power(base, x))
  }

}
