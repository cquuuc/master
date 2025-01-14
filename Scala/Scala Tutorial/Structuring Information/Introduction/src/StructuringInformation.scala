object StructuringInformation{
  case class Note(name: String, duration: String, octave: Int)

  def setUpC3Note(): Note = {
    Note("C", "Quarter", 3)
  }

  def main(args: Array[String]): Unit = {
    val note = setUpC3Note()
    println("Name: " + note.name)
    println("duration: " + note.duration)
    println("octave: " + note.octave)
  }
}