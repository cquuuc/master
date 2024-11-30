// import org.scalatest.{FlatDpec,Matchers}

object Task3{

def scool(startTimeHour:Int,startTimeMinute:Int,lesson: Int): Unit = {
    val lTime = 45
    val shortBreakDuration = 5
    val longBreakDuration = 15

    val totalDuration = lTime + (lesson - 1) / 2 * (shortBreakDuration + longBreakDuration) + (lesson - 1) % 2 * shortBreakDuration

    // val startTimeHour = 9
    // val startTimeMinute = 0

    val totalMinutes = startTimeHour * 60 + startTimeMinute + totalDuration
    val endTimeHour = totalMinutes / 60
    val endTimeMinute = totalMinutes % 60

    println(s"Lesson $lesson ends at: $endTimeHour:$endTimeMinute")
}



  def main(args: Array[String]): Unit = {
    
   var X1 = scala.io.StdIn.readInt()
   var Y1 = scala.io.StdIn.readInt()
   var Z1 = scala.io.StdIn.readInt()

    scool(X1,Y1,Z1)  
    // scool(9,0,5)  
  }
}