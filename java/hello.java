/**
 * This program displays a greeting for the reader.
 */
void main() {
    String greeting = "Welcome to Core Java!";
    int n,a,b,c, i;
    IO.println(greeting);
    n = greeting.length();
    IO.println("=".repeat(greeting.length()));
    IO.println("length of " + greeting + " is " + n);
    a = 10; 
    b = 50;
    c = a + b;
    IO.println("value of a " + a);
    IO.println("value of b " + b);
    IO.println("value of c " + c);
    for(i=0;i<=n;i++){
        IO.println("#".repeat(i) + "-".repeat(n - i));
    }
    IO.println("value of pi " + Math.PI);
}