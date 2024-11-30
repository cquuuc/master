// import org.scalatest.{FlatDpec,Matchers}


object Task6{

def sort(A: Int, B: Int):Unit = {

   for (i <-A to B by -1) {
            (i % 2) match {
            case 1 => print(i,'\n')
            case 0 =>
        }
    
}
   
   
   

}



  def main(args: Array[String]): Unit = {
   var A1 = scala.io.StdIn.readInt()
   var B1 = scala.io.StdIn.readInt()

   sort(A1,B1)
  }
}