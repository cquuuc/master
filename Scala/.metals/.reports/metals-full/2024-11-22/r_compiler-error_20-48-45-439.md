file:///C:/Users/ROG/Desktop/Scala/Task2/Test.scala
### java.lang.AssertionError: assertion failed: position error, parent span does not contain child span
parent      = new User(n = _root_.scala.Predef.???) # -1,
parent span = <913..950>,
child       = n = _root_.scala.Predef.??? # -1,
child span  = [922..923..952]

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
offset: 927
uri: file:///C:/Users/ROG/Desktop/Scala/Task2/Test.scala
text:
```scala
// object Whatever {
//   def speak(something: String)(implicit nice: String) = {
//     println(s"$something $nice")
//   }
// }

// implicit val nice = "the walrus"
// println {
//   Whatever.speak("I am")
// }
// println {
//   Whatever.speak("I like")("catfood")
// }
// trait Diva {
//   var attitude = "subjective"
// }
// var arianaGrand = new Diva
// println(arianaGrande.attitude)
// val s = "(888) 333-4444"
// // s.replace("x", "[0-9]")
// s.replaceAll("[0-9]", "x")
// // a = s.replace("[0-9]", "x")
// println(s.replaceAll("[0-9]", "x"))

// class Complex(real:Double,imaginary:Double){
// def re()=real
// def im()=imaginary
// }
// def sad = "meow"
// val catCry = sad
// println(catCry())
import java.util.Arrays
// val arr = Array(2, 3, 4)
// println(arr)
// arr.update(1, 5)
// println(Arrays.toString(arr))
class User(n:String){
val name:String=n
}
var u=new User(n="Fr@@ankl”)
println(u.name)

```



#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:8)
	dotty.tools.dotc.ast.Positioned.check$1(Positioned.scala:175)
	dotty.tools.dotc.ast.Positioned.check$1$$anonfun$3(Positioned.scala:205)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.immutable.List.foreach(List.scala:334)
	dotty.tools.dotc.ast.Positioned.check$1(Positioned.scala:205)
	dotty.tools.dotc.ast.Positioned.checkPos(Positioned.scala:226)
	dotty.tools.dotc.ast.Positioned.check$1(Positioned.scala:200)
	dotty.tools.dotc.ast.Positioned.checkPos(Positioned.scala:226)
	dotty.tools.dotc.ast.Positioned.check$1(Positioned.scala:200)
	dotty.tools.dotc.ast.Positioned.check$1$$anonfun$3(Positioned.scala:205)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.immutable.List.foreach(List.scala:334)
	dotty.tools.dotc.ast.Positioned.check$1(Positioned.scala:205)
	dotty.tools.dotc.ast.Positioned.checkPos(Positioned.scala:226)
	dotty.tools.dotc.parsing.Parser.parse$$anonfun$1(ParserPhase.scala:39)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	dotty.tools.dotc.core.Phases$Phase.monitor(Phases.scala:458)
	dotty.tools.dotc.parsing.Parser.parse(ParserPhase.scala:40)
	dotty.tools.dotc.parsing.Parser.$anonfun$2(ParserPhase.scala:52)
	scala.collection.Iterator$$anon$6.hasNext(Iterator.scala:479)
	scala.collection.Iterator$$anon$9.hasNext(Iterator.scala:583)
	scala.collection.immutable.List.prependedAll(List.scala:152)
	scala.collection.immutable.List$.from(List.scala:685)
	scala.collection.immutable.List$.from(List.scala:682)
	scala.collection.IterableOps$WithFilter.map(Iterable.scala:900)
	dotty.tools.dotc.parsing.Parser.runOn(ParserPhase.scala:51)
	dotty.tools.dotc.Run.runPhases$1$$anonfun$1(Run.scala:315)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.ArrayOps$.foreach$extension(ArrayOps.scala:1323)
	dotty.tools.dotc.Run.runPhases$1(Run.scala:308)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1(Run.scala:349)
	dotty.tools.dotc.Run.compileUnits$$anonfun$adapted$1(Run.scala:358)
	dotty.tools.dotc.util.Stats$.maybeMonitored(Stats.scala:69)
	dotty.tools.dotc.Run.compileUnits(Run.scala:358)
	dotty.tools.dotc.Run.compileSources(Run.scala:261)
	dotty.tools.dotc.interactive.InteractiveDriver.run(InteractiveDriver.scala:161)
	dotty.tools.pc.MetalsDriver.run(MetalsDriver.scala:45)
	dotty.tools.pc.WithCompilationUnit.<init>(WithCompilationUnit.scala:31)
	dotty.tools.pc.WithSymbolSearchCollector.<init>(PcCollector.scala:334)
	dotty.tools.pc.PcDocumentHighlightProvider.<init>(PcDocumentHighlightProvider.scala:17)
	dotty.tools.pc.ScalaPresentationCompiler.documentHighlight$$anonfun$1(ScalaPresentationCompiler.scala:178)
```
#### Short summary: 

java.lang.AssertionError: assertion failed: position error, parent span does not contain child span
parent      = new User(n = _root_.scala.Predef.???) # -1,
parent span = <913..950>,
child       = n = _root_.scala.Predef.??? # -1,
child span  = [922..923..952]