object ClassesVsCaseClasses{
  val aliceAccount = new BankAccount
  val bobAccount   = new BankAccount/*create a new BankAccount here*/

  val c3     = Note("c", "quarter", 3)
  val cThree = Note("c", "quarter", 3)/*create a new c3 note here with a quarter duration*/

  def main(args: Array[String]): Unit = {
    println(aliceAccount == bobAccount)
    print(c3 == cThree)
  }
}