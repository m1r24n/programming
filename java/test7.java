import java.lang.reflect.Array;

void main(){
    int[] v1={1,2,3,4,5,6,7,8,9,10};
    int[] v2;
    IO.println("length of array %d ".formatted(v1.length)); 
    for(int x : v1){
        IO.println("v1: value %d".formatted(x));
    }
    v2 = v1;
    // v2 = Arrays.copyOf(v1,v1.length);
     for(int x : v2){
        IO.println("v2 value %d".formatted(x));
    }
    v1[3]=-15;
    for(int x : v1){
        IO.println("v1: value %d".formatted(x));
    }

    for(int x : v2){
        IO.println("v2 value %d".formatted(x));
    }

}