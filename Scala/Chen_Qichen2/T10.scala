object T10 {
  def isSortedAscending(lst: List[Int]): Boolean = {
    lst == lst.sorted
  }

  def main(args: Array[String]): Unit = {
    print("请输入整数数组（以空格分隔）: ")
    var X1 = scala.io.StdIn.readLine()
    val list = X1.split(" ").map(_.toInt).toList
    println(isSortedAscending(list))
  }
}
