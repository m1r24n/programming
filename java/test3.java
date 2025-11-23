public void main(String[] args){
    int i;
    float f1;
    if(args.length == 0){
        IO.println("where is the number ?");
    } else{
        IO.println(args[0]);
        f1 = Float.parseFloat(args[0]);
        IO.println(f1 + "^2 = " + Math.pow(f1,2));
    }
}