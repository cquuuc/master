// MathUtils.scala
object MathUtils {

  // 计算给定数字的阶乘
  def factorial(n: Int): BigInt = {
    if (n < 0) {
      throw new IllegalArgumentException("! cant use num<0")
    } else if (n == 0) {
      1 // 0 的阶乘是 1
    } else {
      (1 to n).product // 计算 n 的阶乘
    }
  }
}
