//Heart beatrate emulator
setInterval(genTemperature, 60000);// every minute, 60s

function genTemperature(){
  var rand = Math.random();
  var temp = rand + 36.5;
  //return beatrate
  console.log(temp);
}
