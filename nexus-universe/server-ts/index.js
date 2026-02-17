const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Projeto Aurora - Lord Eclipse Online! Sistema de Comando Ativo.');
});

app.get('/status', (req, res) => {
  res.json({
    status: 'ONLINE',
    system: 'Nexus Universe',
    subsystems: ['MilitaryBase', 'EconomySystem', 'TechTree', 'NeuralLink'],
    version: '1.1.0'
  });
});

// Endpoint conceitual para integração com o cérebro em Python
app.post('/command', express.json(), (req, res) => {
  const { command, code } = req.body;
  console.log(`Recebido comando: ${command} com código: ${code}`);

  // Aqui haveria uma chamada via gRPC ou Socket para o unified_core.py
  res.json({
    received: true,
    processing_unit: 'Brain-Py',
    message: 'Comando enviado para validação do SecurityGuardian.'
  });
});

app.listen(port, () => {
  console.log(`Sistema rodando em http://localhost:${port}`);
});
