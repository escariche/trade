var kafka = require('kafka-node'),
    Producer = kafka.Producer,
    KeyedMessage = kafka.KeyedMessage,
    client = new kafka.Client({kafkaHost: '18.217.106.184:9092'}),
    producer = new Producer(client),
    km = new KeyedMessage('key', 'message');

var msgArray =[];
var payloads = [];
// { topic: 'test000', messages: 'hi', partition: 0 },
// { topic: 'test000', messages: ['hello', 'world', km] }

producer.on('ready', function () {
    setInterval(genBeatRate, 60000); //every minute, 60s
    payloads[0] = { topic: 'test000', messages: msgArray }
    producer.send(payloads, function (err, data) {
        console.log(data);
    });
});

producer.on('error', function (err) {})


//Heart beatrate emulator
function genBeatRate(){
  var rand = Math.random();
  var beatrate = rand * 40 + 60;
  //return beatrate
  msgArray[msgArray.length -1 ] = beatrate;
  msgArray[msgArray.length] = km;
}
