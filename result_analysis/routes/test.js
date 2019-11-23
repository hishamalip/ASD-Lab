const fs = require('fs');

module.exports = {
    addTestPage: (req, res) => {
        res.render('test.ejs', {
            title: 'Welcome to Socka | Test'
            ,message: ''
        });
    },
    addTest: (req, res) => {
        let message = '';
        let test_string = req.body.test_name;

        let query = "INSERT INTO `test` (test) VALUES ('" + test_string + "')";
        
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/');
        });
    }
};