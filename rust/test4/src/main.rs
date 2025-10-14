use std::io;

fn main() {
    
    println!("This is test4!");
    
    // println!("value of month[0] {}, and month[11] {}",month[0],month[11]);
    println!("enter a number "); 
    
    let mut index = String::new();
    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let mut index: usize = index
        .trim()
        .parse()
        .expect("Index entered was not a number");
    index = index - 1;
    fun1();
    fun2(index)

}

fn fun1(){
    println!("This is function one")
}
fn fun2(idx: usize){
    let idxdsp = idx + 1;
    let month = ["january","february", "march", "april","may","june","july","august","september","october","november","december"];
    println!("This is fun2");
    println!("you choose index {idxdsp}, and the value is {}",month[idx]);
}
