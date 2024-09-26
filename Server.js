// 1. Import Required Libraries
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const path = require('path'); // Add this line to import the path module

// 2. Create Express App and Set the Port
const app = express();
const PORT = process.env.PORT || 3000;

// 3. Enable Cross-Origin Resource Sharing (CORS)
app.use(cors());

// 4. Serve Static Files from the current directory
app.use(express.static(path.join(__dirname))); // Add this line

// 5. Connect to SQLite Database
const db = new sqlite3.Database('mma_fighters.db', (err) => {
    if (err) {
        console.error('Could not connect to database', err);
    } else {
        console.log('Connected to SQLite database');
    }
});

// 6. Endpoint to Retrieve Fighters from Database
app.get('/api/fighters', (req, res) => {
    db.all('SELECT * FROM fighters', [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

// 7. Start the Server and Listen on the Specified Port
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
