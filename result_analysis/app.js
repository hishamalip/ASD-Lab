const express = require('express');
const fileUpload = require('express-fileupload');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');
const app = express();


const {getHomePage} = require('./routes/index');
const {addPlayerPage, addPlayer, deletePlayer, editPlayer, editPlayerPage} = require('./routes/player');
const {addTest, addTestPage} = require('./routes/test');


const {addLogin, addLoginPage} = require('./routes/login');
const {addRegister, addRegisterPage} = require('./routes/register');

const {addProfile, addProfilePage} = require('./routes/profile');

const {addResult, addResultPage} = require('./routes/result');

const {addContact, addContactPage} = require('./routes/contactus');

const {addSubject_result, addSubject_resultPage} = require('./routes/sub_result');


const {addCivil_resultPage} = require('./routes/civil_result');
const {addElectrical_resultPage} = require('./routes/electrical_result');
const {addMechanical_resultPage} = require('./routes/mechanical_result');
const {addIndustrial_resultPage} = require('./routes/industrial_result');
const {addApplied_resultPage} = require('./routes/applied_result');
const {addElectronics_resultPage} = require('./routes/electronics_result');
const {addComputer_resultPage} = require('./routes/computer_result');

const port = 5000;

// create connection to database
// the mysql.createConnection function takes in a configuration object which contains host, user, password and the database name.
const db = mysql.createConnection ({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'socka'
});

// connect to database
db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to database');
});
global.db = db;

// configure middleware
app.set('port', process.env.port || port); // set express to use this port
app.set('views', __dirname + '/views'); // set express to look in this folder to render our view
app.set('view engine', 'ejs'); // configure template engine
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json()); // parse form data client
app.use(express.static(path.join(__dirname, 'public'))); // configure express to use public folder
app.use(fileUpload()); // configure fileupload


// routes for the app

app.get('/', getHomePage);

app.get('/add', addPlayerPage);
app.post('/add', addPlayer);

app.get('/edit/:id', editPlayerPage);
app.post('/edit/:id', editPlayer);

app.get('/delete/:id', deletePlayer);

app.get('/test', addTestPage);
app.post('/test', addTest);

app.get('/login', addLoginPage);
app.post('/login', addLogin);

app.get('/register', addRegisterPage);
app.post('/register', addRegister);

app.get('/profile', addProfilePage);
app.post('/profile', addProfile);

app.get('/result', addResultPage);
app.post('/result', addResult);

app.get('/contactus', addContactPage);
app.post('/contactus', addContact);


app.get('/sub_result', addSubject_resultPage);
app.post('/sub_result', addSubject_result);



app.get('/civil_result', addCivil_resultPage);
app.get('/electrical_result', addElectrical_resultPage);
app.get('/mechanical_result', addMechanical_resultPage);
app.get('/industrial_result', addIndustrial_resultPage);
app.get('/applied_result', addApplied_resultPage);
app.get('/electronics_result', addElectronics_resultPage);
app.get('/computer_result', addComputer_resultPage);

// app.get('/electrical_result', addCivil_resultPage);

// including css files
app.use(express.static(__dirname + '/public'));


app.listen(port, () => {
    console.log(`Server running on port: ${port}`);
});
