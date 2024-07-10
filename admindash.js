const express = require('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname)); // Serve static files (e.g., admin.html)

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/admin.html');
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
