const fs = require('fs');

module.exports = {
    // addFeedbackPage: (req, res) => {
    //     res.render('feedback.ejs', {
    //         title: 'KTU Result Analysis'
    //         ,feedback: ''
    //     });
    // },

    addFeedback: (req, res) => {
        // query database to get all the players
        let query = "SELECT * FROM `feedback` ORDER BY id DESC"; 
        // execute query
        db.query(query, (err, result) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.render('feedback.ejs', {
                title: 'Welcome to KTU result analysis | View feedback'
                ,feedback: result
            });
        });
    },
};