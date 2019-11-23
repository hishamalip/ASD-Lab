const fs = require('fs');

module.exports = {
    addLoginPage: (req, res) => {
        res.render('login.ejs', {
            title: 'KTU Result Analysis | Login'
            ,message: ''
        });
    },

    addLogin: (req, res) => {
        let message = '';
        let username = req.body.user_name;
        let password = req.body.pass_word;
        
        let query = "INSERT INTO `login`(username, password) VALUES ('" + username + "', '" + password + "')";
        
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/profile');
        });
    }
};
