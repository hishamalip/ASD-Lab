const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addApplied_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ae_subject = results.slice(296, 347).join('\n');

            res.render('applied_result.ejs', {
                title: 'KTU Result Analysis'
                , message: '',
                ae_subject : ae_subject,
            });
        });
    }
};

