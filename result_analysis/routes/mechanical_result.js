const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addMechanical_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let me_subject = results.slice(51, 94).join('\n');

            res.render('mechanical_result.ejs', {
                title: 'KTU Result Analysis | Login'
                , message: '',
                me_subject : me_subject,
            });
        });
    }
};
