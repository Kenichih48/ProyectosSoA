const express = require('express');
const path = require('path');
const app = express();

// Serve static files from the build folder
app.use(express.static(path.join(__dirname, 'myrestaurantapp/build')));

// Serve index.html for all other routes
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'myrestaurantapp/build', 'index.html'));
});

// Start the server
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});