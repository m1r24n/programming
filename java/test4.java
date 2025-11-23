public void main(String[] args) {
    IO.println("test4 ");
    if(args.length == 0){
        IO.println("Arguments was not given");
    }else{
        int i, n;
        String data1="""
                This is the first line
                this is the second line
                this is the third line
                this is the fourth line
                """;
        n = args.length;
        IO.println("arguments are given");
        for(i=0;i<n;i++){
            IO.println("arg["+i+"] : " + args[i]);
        }
        IO.println(data1);
    }
}
