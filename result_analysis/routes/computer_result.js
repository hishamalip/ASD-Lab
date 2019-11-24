const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addComputer_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let cs_subject = results.slice(246,296).join('\n');

            res.render('computer_result.ejs', {
                title: 'KTU Result Analysis'
                , message: '',
                cs_subject : cs_subject
            });
        });
    }
};

