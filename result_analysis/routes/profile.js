const fs = require('fs');

module.exports = {
    addProfilePage: (req, res) => {
        res.render('profile.ejs', {
            title: 'KTU Resul Analysis | Profile'
            ,message: ''
        });
    },
    addProfile: (req, res) => {
        let message = '';        
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.redirect('/');
        });
    }
};
