object ComputingSquareRoot{

  def sqrt(x: Double) = {
    sqrtIter(1.0, x)
  }

  def sqrtIter (guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

  def improve(guess: Double, x: Double) = {
    (guess + x / guess) / 2//here we need to place an expression for evaluating a better guess
  }

  def isGoodEnough(guess: Double, x: Double) = {
    math.abs(guess * guess - x) < 0.001
  }

  def main(args: Array[String]): Unit = {
    println(sqrt(36))
    println(sqrt(255))
  }
}