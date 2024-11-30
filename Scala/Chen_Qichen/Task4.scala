// import org.scalatest.{FlatDpec,Matchers}

object Task4{
   def Price_Buy(yuans:Int,fengs:Int,num:Int):Unit={
    var One_pie=yuans*100+fengs
    var All_pies_price=One_pie * num
    var finally_yuans=All_pies_price/100
    var finally_fengs=All_pies_price%100
    print(s"buy $num pies need $finally_yuans yuans and $finally_fengs fengs ")

   }




  def main(args: Array[String]): Unit = {
      var X1 = scala.io.StdIn.readInt()
      var Y1 = scala.io.StdIn.readInt()
      var Z1 = scala.io.StdIn.readInt()
      Price_Buy(X1,Y1,Z1)
  }
}