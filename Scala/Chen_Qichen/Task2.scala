// import org.scalatest.{FlatDpec,Matchers}

object Task2{

  def distance(a:Int,b:Int,c:Int,d:Int):Unit={
    
    var r=math.pow(a-c,2)+math.pow(b-d,2)
    var res=math.sqrt(r)
    print(res)
  }



  def main(args: Array[String]): Unit = {
  var X1 = scala.io.StdIn.readInt()
   var Y1 = scala.io.StdIn.readInt()
   var X2 = scala.io.StdIn.readInt()
   var Y2 = scala.io.StdIn.readInt()
   
    distance(X1,Y1,X2,Y2)
  }
}