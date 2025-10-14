fun main() {
  var name="irzan"
  var x = 15
  var y = 51.5
  var z: Double; var z1: Double
  z = x + y
  z1 = z + x *y 
  println("Hello world")
  println("This is the second line ")
  one()
  two()
  println("Back to main function")
  printval(name)
  name="ratih"
  printval(name)
  println("value of x " + x)
  println("value of y " + y)
  println("value of z " + z)
  println("variable name " + name[0]  + name[2])
  printString(name)
  name="mochammad irzan"
  printString(name)
  name="ratih dyah kusumastuti"
  printString(name)
  name="raditya aulia satyabudhi irzan"
  printString(name)
  println(name.indexOf("raditya"))
  println(name.indexOf("sanny"))

}
fun one(){
  println("This is function one()")
}
fun two(){
  println("This is function two()")
}
fun printval(val1: Any){
  println("value of variable is " + val1)
}
fun printString(val1: String){
  println("value : " + val1)
  println("length of string " + val1.length)
}
