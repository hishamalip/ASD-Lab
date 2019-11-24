const fs = require('fs');
let { PythonShell } = require('python-shell');


module.exports = {
    addResultPage: (req, res) => {
       
        PythonShell.run(__dirname+'/total_result.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ce_result = results.slice(1, 5).join('\n');;
            // ce_result= ce_result(); 
            // ce_result1 = ce_result.forEach() 
            let ee_result = results.slice(7, 11).join('\n');
            let me_result = results.slice(13, 17).join('\n');;
            let ie_result = results.slice(19, 23).join('\n');;
            let ec_result = results.slice(25, 29).join('\n');;
            let cs_result = results.slice(31, 35).join('\n');;
            let ae_result = results.slice(37, 41).join('\n');;
          
            // ce_result.forEach(result => { console.log(result) });
            // me_result.forEach(result => { console.log(result) });
            // ee_result.forEach(result => { console.log(result) });
            // ie_result.forEach(result => { console.log(result) });
            // ec_result.forEach(result => { console.log(result) });
            // cs_result.forEach(result => { console.log(result) });
            // ae_result.forEach(result => { console.log(result) });
            // console.log(ce_result);
            res.render('result.ejs', {
                title: 'KTU Result Analysis | Test'
                ,message: '',
                ce_result: ce_result,
                ee_result : ee_result,
                me_result : me_result,
                ie_result : ie_result,
                ec_result : ec_result,
                cs_result : cs_result,
                ae_result : ae_result
            });
        });
    },
    addResult: (req, res) => {
        let message = '';        
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/result');
        });
    }
};
