const fs = require('fs');
let { PythonShell } = require('python-shell');

module.exports = {
    addSubject_resultPage: (req, res) => {

        PythonShell.run(__dirname + '/subject.py', null, function (err, results) {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            //  results.forEach(result => {console.log( result);}) 
            let length = results.length;
            let ce_subject = results.slice(0, 49).join('\n');
            let me_subject = results.slice(51, 94).join('\n');
            let ee_subject = results.slice(96, 146).join('\n');
            let ie_subject = results.slice(146, 195).join('\n');
            let ec_subject = results.slice(196, 245).join('\n');
            let cs_subject = results.slice(246, 296).join('\n');
            let ae_subject = results.slice(296, 347).join('\n');

            // ce_subject.forEach(result => {console.log(result)});
            // me_subject.forEach(result => {console.log(result)});
            // ee_subject.forEach(result => {console.log(result)});
            // ie_subject.forEach(result => {console.log(result)});
            // ec_subject.forEach(result => {console.log(result)});
            // cs_subject.forEach(result => {console.log(result)});
            // ae_subject.forEach(result => {console.log(result)});

            res.render('sub_result.ejs', {
                title: 'KTU Result Analysis | Login'
                , message: '',
                ce_subject : ce_subject,
                me_subject : me_subject,
                ee_subject : ee_subject,
                ie_subject : ie_subject,
                ec_subject : ec_subject,
                cs_subject : cs_subject,
                ae_subject : ae_subject
            });
        });
    },

    addSubject_result: (req, res) => {
        let message = '';
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/sub_result');
        });
    }
};
