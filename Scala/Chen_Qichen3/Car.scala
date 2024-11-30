class Car(
    private var make: String,
    private var model: String,
    private var year: Int
) {

  def getInfo(): Unit = {
    println(s"make: $make")
    println(s"model: $model")
    println(s"year: $year")
  }

  def setMake(newMake: String): Unit = {
    make = newMake
  }

  def setModel(newModel: String): Unit = {
    model = newModel

  }

  def setYear(newYear: Int): Unit = {
    year = newYear
  }
}
