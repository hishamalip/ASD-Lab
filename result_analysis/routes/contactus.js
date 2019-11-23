const fs = require('fs');

module.exports = {
    addContactPage: (req, res) => {
        res.render('contactus.ejs', {
            title: 'KTU Result Analysis | Contactus'
            ,message: ''
        });
    },

    addContact: (req, res) => {
        let email = req.body.email;
        let message = req.body.message;

        let query = "INSERT INTO `feedback`(email, message) VALUES ('" + email + "',    '" + message + "')";
        
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/contactus');
        });
    }
};
