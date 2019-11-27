const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addCivil_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ce_subject = results.slice(0, 49).join('\n');


            res.render('civil_result.ejs', {
                title: 'KTU Result Analysis '
                , message: '',
                ce_subject : ce_subject,
            });
        });
    }
};
