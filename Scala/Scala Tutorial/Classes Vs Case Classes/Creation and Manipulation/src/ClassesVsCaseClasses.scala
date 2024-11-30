object ClassesVsCaseClasses {
  val aliceAccount = new BankAccount
  aliceAccount.deposit(100)
  val c3 = Note("C", "quarter", 3)/*create a c3 note with a quarter duration*/

  def main(args: Array[String]): Unit = {
    println(aliceAccount.withdraw(10))
    println(c3.name)
  }
}