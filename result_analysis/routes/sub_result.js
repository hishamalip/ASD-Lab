const fs = require('fs');

module.exports = {
    addSubject_resultPage: (req, res) => {
        res.render('sub_result.ejs', {
            title: 'KTU Result Analysis | Login'
            ,message: ''
        });
    },

    addSubject_result: (req, res) => {

        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/sub_result');
        });
    }
};
