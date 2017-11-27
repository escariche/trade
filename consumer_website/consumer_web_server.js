var express = require("express");
var app = express();
var router = express.Router();
var path = __dirname + '/views/';
var kafkaPath = '/home/ec2-user/kafka/kafka_2.11-1.0.0/';

router.use(function (req,res,next) {
  console.log("/" + req.method);
  next();
});

router.get("/",function(req,res){
  res.sendFile(path + "index.html");
});

router.get("/test000",function(req,res){
  res.sendFile(kafkaPath + "test000.txt");
});



//We'll work on this
router.get("/topics",function(req,res){
  res.sendFile(path + "topics.html");
});

router.get("/about",function(req,res){
  res.sendFile(path + "about.html");
});

router.get("/contact",function(req,res){
  res.sendFile(path + "contact.html");
});

app.use("/",router);

app.use("*",function(req,res){
  res.sendFile(path + "404.html");
});

app.listen(3000,function(){
  console.log("Live at Port 3000");
});
