class Animal(
    private var name: String,
    private var sound: String
) {

  def makeSound(): Unit = {
    println(s"$name's sound is: $sound")
  }

  def setName(newName: String): Unit = {
    name = newName
  }

  def setSound(newSound: String): Unit = {
    sound = newSound

  }
}
