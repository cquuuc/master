// import org.scalatest.{FlatDpec,Matchers}


object Task8{

def  fuc(N: Int):Unit = {
   
    var power = 1
    var exponent = 0

    while (power * 2 <= N) {
      power *= 2
      exponent += 1
    }

    print(s" 2^$exponent = $power < $N")

}



  def main(args: Array[String]): Unit = {
   var A1 = scala.io.StdIn.readInt()
   fuc(A1)
  }
}