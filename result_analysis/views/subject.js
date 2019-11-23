let { PythonShell } = require('python-shell')

PythonShell.run('subject.py', null,function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
//  results.forEach(result => {console.log( result);}) 
 let length=results.length;
 let ce_subject= results.slice(0,49);
 let me_subject= results.slice(51,95);
 let ee_subject= results.slice(96,146);
 let ie_subject= results.slice(146,195);
 let ec_subject= results.slice(196,245);
 let cs_subject= results.slice(246,296);
 let ae_subject= results.slice(296,347);

  ce_subject.forEach(result => {console.log(result)});
  me_subject.forEach(result => {console.log(result)});
  ee_subject.forEach(result => {console.log(result)});
  ie_subject.forEach(result => {console.log(result)});
  ec_subject.forEach(result => {console.log(result)});
  cs_subject.forEach(result => {console.log(result)});
  ae_subject.forEach(result => {console.log(result)});
});

