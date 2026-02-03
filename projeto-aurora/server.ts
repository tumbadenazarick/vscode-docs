import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: "*",
  }
});

const PORT = process.env.PORT || 3000;

app.get('/health', (req, res) => {
  res.send('Projeto Aurora Server is healthy!');
});

io.on('connection', (socket) => {
  console.log(`Jogador conectado: ${socket.id}`);

  socket.on('player_move', (data) => {
    // Lógica de movimentação básica para broadcast
    socket.broadcast.emit('player_moved', {
      id: socket.id,
      position: data.position
    });
  });

  socket.on('disconnect', () => {
    console.log(`Jogador desconectado: ${socket.id}`);
  });
});

httpServer.listen(PORT, () => {
  console.log(`Servidor de Jogo (Aurora) rodando na porta ${PORT}`);
});
