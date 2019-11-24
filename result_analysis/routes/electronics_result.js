const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addElectronics_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ec_subject = results.slice(196, 245).join('\n');

            res.render('electronics_result.ejs', {
                title: 'KTU Result Analysis'
                , message: '',
                ec_subject : ec_subject,
            });
        });
    }
};

