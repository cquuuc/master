// import org.scalatest.{FlatDpec,Matchers}


object Task7{

def  fact(A: Int):Unit = {
  var res=1
  for (i <- 1 to A) {
      res=res*i
}
  print(res)


}



  def main(args: Array[String]): Unit = {
   var A1 = scala.io.StdIn.readInt()
   fact(A1)
  }
}