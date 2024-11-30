// Resizable.scala
trait Resizable {
  def resize(factor: Double): Unit
}

class Rectangle2(private var width: Double, private var height: Double)
    extends Resizable {
  def getWidth: Double = width
  def getHeight: Double = height
  // resize
  override def resize(factor: Double): Unit = {
    if (factor > 0) {
      width *= factor
      height *= factor
      println(s"Newwidth: $width, Newheight: $height")
    } else {
      println("factor must  >0")
    }
  }
  def displayDetails(): Unit = {
    println(s"width: $width, height: $height")
  }
}
