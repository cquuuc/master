object LexicalScopes {
  def objectScopes(): Int = {
    object Foo {
      val x = 1
    }

    object Bar {
      val x = 2
    }

    object Baz {
      val y = Bar.x + Foo.x
    }

    Baz.y
  }

  def main(args: Array[String]): Unit = {
    println(objectScopes())
  }
}