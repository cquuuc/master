object LexicalScopes {
  def scopeRules(): Unit = {
    val x = 0

    def Sum(y: Int) = y + 1

    val result = {
      val x = Sum(3)
      x * x
    } + x

    println(result)
  }

  def main(args: Array[String]): Unit = {
    scopeRules()
  }
}