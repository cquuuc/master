import org.scalatest.{FlatSpec, Matchers}
object ListAnyFuc extends FlatSpec with Matchers {

  def optionMap(x: Option[Int]): Option[Int] = {
    x.map(x => x + 1)
  }

  def optionFilter(x: Option[Int]): Option[Int] = {
    x.filter(x => x % 2 == 0)
  }

  def optionFlatMap(x: Option[Int]): Option[Int] = {
    x.flatMap(x => Some(x + 1))
  }

  def main(args: Array[String]): Unit = {
    println(optionMap(Some(7)))
  }
}
