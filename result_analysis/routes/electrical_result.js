const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addElectrical_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ee_subject = results.slice(96, 146).join('\n');

            res.render('electrical_result.ejs', {
                title: 'KTU Result Analysis | Login'
                , message: '',
                ee_subject : ee_subject,
            });
        });
    }
};
