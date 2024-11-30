// BankAccount.scala
class BankAccount(private val accountNumber: String) {
  // 初始余额为 0
  private var balance: Double = 1000.0

  // 存款方法
  def deposit(amount: Double): Unit = {
    if (amount > 0) {
      balance += amount
      println(s"Succ deposit: ${amount}BYN, Balance: ${balance} BYN.")
    } else {
      println("deposit must >0.")
    }
  }

  // 取款方法
  def withdraw(amount: Double): Unit = {
    if (amount > 0 && amount <= balance) {
      balance -= amount
      println(s"Succ withdraw: ${amount}BYN, Balance: ${balance}BYN.")
    } else if (amount > balance) {
      println("withdraw>Balance.")
    } else {
      println("withdraw must >0.")
    }
  }

  // 获取当前余额
  def getBalance: Double = balance

  // 获取账户号码
  def getAccountNumber: String = accountNumber
}
