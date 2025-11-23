public void main(){
    int age;
    String name="irzan";
    double v1;
    v1 = 1.0 / 3.0;
    name = IO.readln("What is your name ");
    age = Integer.parseInt(IO.readln("Enter your age "));
    IO.println("your name is " + name);
    IO.println("In 10 years you will be " + (age + 10));
    IO.println("value of v1 " + v1);
    IO.println("value of v1 %5.2f, age is %5d".formatted(v1,age));
}
