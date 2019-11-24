const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addIndustrial_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ie_subject = results.slice(146, 195).join('\n');

            res.render('industrial_result.ejs', {
                title: 'KTU Result Analysis'
                , message: '',
                ie_subject : ie_subject,
            });
        });
    }
};

