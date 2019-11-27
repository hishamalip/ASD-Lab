const fs = require('fs');


module.exports = {
    addProfilePage: (req, res) => {
        res.render('profile.ejs', {
            title: 'KTU Resul Analysis'
            , message: ''
            
        });
    },
    addProfile: (req, res) => {
       
    
        let message = '';
        let uploadedFile = req.files.myFile;
        let file_name = uploadedFile.name;
        // let fileExtension = uploadedFile.mimetype.split('/')[1];
        if (uploadedFile.mimetype === 'application/pdf') {
            uploadedFile.mv(`/home/ak/Downloads/result_analysis/views/${file_name}`, (err) => {
                if (err) {
                    return res.status(500).send(err);
                }
                // send the player's details to the database
                let query = "INSERT INTO `pdf_table` (pdf_name) VALUES ('" + file_name + "') ";
                db.query(query, (err, result) => {
                    if (err) {
                        return res.status(500).send(err);
                    }
                    // res.redirect('/profile');

                let query1 = "SELECT pdf_name from `pdf_table` WHERE pdf_name =     '" + file_name + "'  ";
                db.query(query1, (err, result) => {
                        if (err) {
                           return res.status(500).send(err);
                        }
                        //  message = file_name ;
                        // res.render('profile.js', {
                        //     message
                        //  });
                        res.redirect('/profile');
                      
                 }); 

                });

            });

        }
        else {
            message = "Invalid File format. only '.pdf' files are allowed.";
            res.render('profile.ejs', {
                message
            });
            
        }
    }
};