class Student(
    name: String,
    age: Int,
    country: String,
    private var grade: String
) extends Person(name, age, country) {
  def getGrade: String = grade
  def setGrade(newGrade: String): Unit = {
    grade = newGrade
  }
  override def Info(): Unit = {
    super.Info()
    println(s"Grade: $grade")
  }
}
