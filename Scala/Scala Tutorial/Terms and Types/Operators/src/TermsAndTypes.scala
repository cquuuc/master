object TermsAndTypes {

  def staticTyping(): Range.Inclusive =
    1 to 10

  def main(args: Array[String]): Unit = {
    println(staticTyping())
  }
}