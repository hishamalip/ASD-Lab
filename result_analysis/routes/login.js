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
        
        let query = "SELECT username, password, type FROM `register` WHERE username = '" + username + "' and password = '" + password + "'";
        
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            console.log(result);
            if (result.length == 0) {
                message = 'invalid username or password';
                res.render('login.ejs', {
                    message,
                    title: 'KTU Result Analysis'
                });
            }
            else if(result[0].type == 'user'){
                res.redirect('/profile');
                }
            else{
                res.redirect('/feedback');
                   
                
            }


        });
    }
};
