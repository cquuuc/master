object T5 {
  def isPalindrome(inputString: String): Boolean = {
    val cleanString = inputString.toLowerCase().replaceAll("[^a-zA-Z0-9]", "")
    cleanString == cleanString.reverse
  }

  def main(args: Array[String]): Unit = {
    print("请输入一个字符串: ")
    var X1 = scala.io.StdIn.readLine()
    println(isPalindrome(X1))
  }
}
