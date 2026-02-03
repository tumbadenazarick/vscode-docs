const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Projeto Aurora - Lord Eclipse Online!');
});

app.listen(port, () => {
  console.log(`Sistema rodando em http://localhost:${port}`);
});
