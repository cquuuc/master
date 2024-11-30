// import org.scalatest.{FlatDpec,Matchers}

object Task1{

  def Max(a:Int,b:Int,c:Int)={
   var res=a
   var A=(a-b)*(a-c)
   var B=(b-a)*(b-c)
   var C=(c-a)*(c-b)
   if (A>0) res=a
   if (B>0) res=b
   if (C>0) res=c
   print(res)
  }



  def main(args: Array[String]): Unit = {
   var A1 = scala.io.StdIn.readInt()
   var B1 = scala.io.StdIn.readInt()
   var C1 = scala.io.StdIn.readInt()
    
    Max(A1,B1,C1)
    
  }
}