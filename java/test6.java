public void main(){
    int choice;
    String name="irzan";
    name = IO.readln("What is your name ");
    choice = Integer.parseInt(IO.readln("what is your choice (1 - 5) "));
    switch(choice){
        case 1 ->  {
            IO.println("Hi %s, your choice is %d".formatted(name,choice));
            IO.println("this is choice 1");
        }
        case 2 -> IO.println("Hi %s, your choice is %d".formatted(name,choice));
        default -> IO.println("your choice %d. which is not defined".formatted(choice));
    }
}
