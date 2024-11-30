object T6 {
  def findMaxElement(arr: Array[Int]): Int = {
    if (arr.isEmpty) {
      throw new IllegalArgumentException("arry is Empty")
    }

    var maxElement = arr(0)
    for (i <- 1 until arr.length) {
      if (arr(i) > maxElement) {
        maxElement = arr(i)
      }
    }

    maxElement
  }

  def main(args: Array[String]): Unit = {
    print("请输入整数数组（以空格分隔）: ")

    var X1 = scala.io.StdIn.readLine()
    val array = X1.split(" ").map(_.toInt)
    println(findMaxElement(array))
  }
}
