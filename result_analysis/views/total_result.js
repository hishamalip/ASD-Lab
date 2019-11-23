let { PythonShell } = require('python-shell');
// let ce_result;
PythonShell.run(__dirname+'/total_result.py', null, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  //  results.forEach(result => {console.log( result);}) 
  let length = results.length;
  let ce_result = results.slice(0, 5);
  let me_result = results.slice(6, 11);
  let ee_result = results.slice(12, 17);
  let ie_result = results.slice(18, 23);
  let ec_result = results.slice(24, 29);
  let cs_result = results.slice(30, 35);
  let ae_result = results.slice(36, 41);

  // ce_result.forEach(result => { console.log(result) });
  // me_result.forEach(result => { console.log(result) });
  // ee_result.forEach(result => { console.log(result) });
  // ie_result.forEach(result => { console.log(result) });
  // ec_result.forEach(result => { console.log(result) });
  // cs_result.forEach(result => { console.log(result) });
  // ae_result.forEach(result => { console.log(result) });

  module.exports = {
    ce_result:ce_result
  }
});

