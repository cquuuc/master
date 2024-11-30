// import org.scalatest.{FlatDpec,Matchers}

import scala.io.StdIn._
object Task10{

def  fuc():Unit = {
   
    var maxElement = 0 // 初始化最大元素为0
    var count = 0 // 初始化等于最大元素的元素数量为0
    var input = 1 // 初始化输入值为0
    while (input != 0) // 当输入值为0时结束循环
     {
        input = readInt() // 读取用户输入的整数
        if (input > maxElement) { // 如果输入值大于当前最大元素
            maxElement = input // 更新最大元素为输入值
            count = 1 // 重置等于最大元素的元素数量为1
            } 
      else if (input == maxElement) { // 如果输入值等于最大元素
            count += 1 // 等于最大元素的元素数量加1
            }
    } 

    print(s"big input number is $maxElement has count:$count") // 输出等于最大元素的元素数量
  }




  def main(args: Array[String]): Unit = {
   fuc()
  }
}