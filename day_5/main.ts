import * as fs from 'fs';


fs.readFile('input', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    var ids = part1(data.split("\n"))
    part2(ids)
  });

function part1(data:string[]){
  var highest_id:number = 0
  var ids:number[] = []
  for(const card of data){
    if(card == ""){
      continue;
    }
    // console.log(card)
    var seat_binary = ""
    var row_binary = ""
    for(var i = 0; i < card.length-1; i++){
      if(i <= 6)
        row_binary += card.charAt(i) == "B" ? "1" : "0"
      else
        seat_binary += card.charAt(i) == "R" ? "1" : "0"
    }
    // console.log(row_binary + seat_binary)
    const row = parseInt(row_binary, 2)
    const seat = parseInt(seat_binary, 2)  
    // console.log("Row " + row)
    // console.log("Seat " + seat)

    const id = row * 8 + seat
    // console.log("ID " + id)

    if(highest_id < id)
      highest_id = id

      ids.push(id)
  }
  console.log("highest: " + highest_id)
  return ids
}

function part2(ids: number[]){
  ids.sort((a, b) => a - b)
  for(var i = 0; i < ids.length - 1; i++){
    const diff = ids[i + 1] - ids[i]
    if(diff == 2)
      console.log("Seat ID is between " + ids[i] + " and " + ids[i + 1])
  }
}