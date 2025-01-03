import org.scalatest.{FlatSpec, Matchers}

object StandardLibrary extends FlatSpec with Matchers {

  def optionMap(x: Option[Int]) : Option[Int]= {
    x.map(x => x + 1)/*map the x values to x + 1*/
  }

  def optionFilter(x: Option[Int]): Option[Int] = {
    x.filter(x => x % 2 == 0)/*filter the x values to return only even ones*/
  }

  def optionFlatMap(x: Option[Int]): Option[Int] = {
    x.flatMap(x => Some(x +1))/*use flatMap to return the option for x + 1*/
  }

  def main(args: Array[String]): Unit = {
    println(optionMap(Some(7)))
    println(optionMap(None))
    println(optionFilter(Some(5)))
    println(optionFilter(Some(6)))
    println(optionFlatMap(Some(4)))
    println(optionFlatMap(None))
  }

}