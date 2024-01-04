const ftp = require('./upload');
var fs = require ('fs');
var schedule = require('node-schedule');
var _ = require('underscore');
var path = require('path');
var folder = '/home/linaro/data/';
const SCHEDULE = "*/5 * * * *";
const ftpclient = new ftp('103.9.86.285', 21, 'capnuocsoctrang', 'BsmaK0Elcq', false)
var schedule = require('node-schedule');
function time(){
  var coeff = 1000*60*5;
  var rounded = new Date(Math.round((new Date().getTime() + 7*60*1000*60) / coeff) * coeff);
  return rounded.toISOString(true).replace(/-|T|:/g,'').slice(0,14);
}
function MostRecent(dir){
   var files = fs.readdirSync(dir);
   return _.max(files, function (f) {
       var fullpath = path.join(dir,f);
       return fs.statSync(fullpath).ctime;
});
}
function upl(){
  let fname = MostRecent(folder);
  let month = ("0" + (new Date().getMonth() + 1)).slice(-2);
  let pathfile = './ST/{F63C96B5-01AD-40A4-895A-69BD8746B95F}/{D1627000-7B5E-468F-83F0-F4F35AC619E4}/'+new Date().getFullYear()+ '/' + month+ '/' +  ("0" + new Date().getDate()).slice(-2) +'/';
  ftpclient.upload(folder + fname ,pathfile, fname ,755);
  console.log(fname);
}

upl();
