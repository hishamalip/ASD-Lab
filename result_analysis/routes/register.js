const fs = require('fs');

module.exports = {
    addRegisterPage: (req, res) => {
        res.render('register.ejs', {
            title: 'KTU Result Analysis'
            , message: ''
        });
    },

    addRegister: (req, res) => {
        let message = '';
        let fullname = req.body.full_name;
        let username = req.body.user_name;
        let password = req.body.pass_word;

        let usernameQuery = "SELECT * FROM `register` WHERE username = '" + username + "'";

        db.query(usernameQuery, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            if (result.length > 0) {
                message = 'This email id is already registered. Please login';
                res.render('register.ejs', {
                    message,
                    title: 'KTU Result Analysis'
                });
            } else {
                // send the player's details to the database
                let query = "INSERT INTO `register` (fullname, username, password) VALUES ('" + fullname + "', '" + username + "', '" + password + "')";
                db.query(query, (err, result) => {
                    if (err) {
                        return res.status(500).send(err);
                    }
                    res.redirect('/');
                });
            }
        });
    }
};
