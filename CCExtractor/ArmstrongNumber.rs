use std::io;

fn main() {
  let mut num:u64  = 0;

    let mut input_text = String::new();
    println!("Enter the no : " );
       io::stdin()
           .read_line(&mut input_text)
           .expect("failed to read from input");
       let trimmed = input_text.trim();
       match trimmed.parse::<u64>() {
           Ok(i) => num=i,
           Err(..) => println!("This was not an integer: {}", trimmed),
       };

    let no = num;
    let nstr = num.to_string();
    let length:u32 = nstr.chars().count() as u32;

    let mut n:u64 = 0;


    while num != 0 {
    n += (num%10 as u64).pow(length);
    num = num/10;
    }
    if n == no{
        print!("The number {} is an Amstrong number\n",no );
    }
    else {
        print!("The number {} is not an Amstrong number\n",nok );
    }
}
