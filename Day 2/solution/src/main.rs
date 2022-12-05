use std::fs;
fn main() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}
fn part1() -> u64 {
    let contents = fs::read_to_string("input.txt").expect("no file found");
    let mut totalpoints = 0;
    for line in contents.lines() {
        let me = line.as_bytes()[2];
        let opponent = line.as_bytes()[0];
        totalpoints += (me - 87) as u64;
        totalpoints += (((me - opponent + 2) % 3) * 3) as u64;
    }
    return totalpoints;
}
fn part2() -> u64 {
    let contents = fs::read_to_string("input.txt").expect("no file found");
    let mut totalpoints = 0;
    for line in contents.lines() {
        let me = line.as_bytes()[2];
        let opponent = line.as_bytes()[0];
        totalpoints += ((me - 88) * 3) as u64;
        totalpoints += ((((opponent - 65) + (me - 88) + 2) % 3) + 1) as u64;
    }
    return totalpoints;
}
