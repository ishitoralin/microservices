// index.js
import express from 'express';

const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
    console.log("hello")
    return res.status(200).json({ message: 'Welcome to the Ad Service!' });
});

app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    if (username === 'admin' && password === '1234') {
        res.json({ message: 'Login success' });
    } else {
        res.status(401).json({ message: 'Login failed' });
    }
});

app.listen(3000, '0.0.0.0', () => {
    console.log("Server listening on port 3000");
});