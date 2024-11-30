// import org.scalatest.{FlatDpec,Matchers}

object Task5{

   def run(inc:Int,dec:Int,Length:Int):Unit={


      var h=0
      var days=1
      var finally_days=0
      while (h<Length)
      {

         h=inc+h
         if(h>Length){
            finally_days=days
         }

         days=days+1
         h=h-dec
      }
         print(finally_days)
   }



  def main(args: Array[String]): Unit = {
      var X1 = scala.io.StdIn.readInt()
      var Y1 = scala.io.StdIn.readInt()
      var Z1 = scala.io.StdIn.readInt()
      run(X1,Y1,Z1)
  }
}