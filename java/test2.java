void main(String[] args){
    int i;
    IO.println("hello world");
    IO.println("length of array " + args.length);
    for(i=0;i<args.length;i++){
        IO.println("arg " + i + " is " + args[i]);
    }
}