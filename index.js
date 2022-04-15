const { spawn } = require('child_process');
const express = require('express');

app = express();

app.get('/', (req, res) => {
    var dataToSend;
    const python = spawn('python', ['championParser.py']);

    // collect data from script
    python.stdout.on('data', function (data) {
        dataToSend = data.toString();
    });

    python.on('close', (code) => {
        res.send(dataToSend)
    });
})

app.listen(15000, () => {
    console.log(`Example app listening on port http://localhost:${15000}/`)
})