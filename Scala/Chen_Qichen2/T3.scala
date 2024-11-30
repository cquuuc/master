import scala.io.StdIn

object T3 {
  def sumOfDigits(n: Int): Int = {
    var num = n
    var sum = 0

    while (num > 0) {
      sum += num % 10
      num = num / 10
    }

    return sum
  }

  def main(args: Array[String]): Unit = {
    print("请输入多个数字，以空格分隔：")
    val input = StdIn.readLine()
    val numbers = input.split(" ").map(_.toInt)

    // 计算所有数字的数字之和
    var totalSum = 0
    for (number <- numbers) {
      totalSum += sumOfDigits(number)
    }
    println(s"输入的数字中各位数字之和的总和为: $totalSum")
  }
}
