use std::io;
fn main() {
    // println!("this is program test3");
    // let x1 = [ 10, 11,12,13,14,15];
    // let l = x1.len();
    // println!("length of array x1 {l}");
    // println!("value of x1[1] {}, and x1[5] {}",x1[1],x1[5]);
    let month = ["january","february", "march", "april","may","june","july","august","september","october","november","december"];
    // println!("value of month[0] {}, and month[11] {}",month[0],month[11]);
    println!("enter a number "); 
    
    let mut index = String::new();
    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let index: usize = index
        .trim()
        .parse()
        .expect("Index entered was not a number");
    
    println!("you choose index {index}, and the value is {}",month[index])

}
