fun main(){
    var score = 79.8
    var value = if (score > 90) "A" else if (score > 70) "B" else if (score > 55) "C" else if (score > 40) "D" else "E"
    println("score $score value is $value")
}