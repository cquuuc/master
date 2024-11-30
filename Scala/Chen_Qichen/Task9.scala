// import org.scalatest.{FlatDpec,Matchers}


object Task9{

def  fuc(x: Int,y: Int):Unit = {
   
var distance:Double = x
    var day = 1
    while (distance < y) {
      distance = distance * 1.1 
      day += 1
    }

    println(s"$y km need $day days.")
  }




  def main(args: Array[String]): Unit = {
   var A1 = scala.io.StdIn.readInt()
   var A2 = scala.io.StdIn.readInt()
   fuc(A1,A2)
  }
}