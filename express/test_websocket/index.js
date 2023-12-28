const express = require("express");
const { WebSocketServer } = require("ws");
const app = express();

app.use(express.static("front"));
app.listen(8000, () => {
  console.log("Server listening on port 8000");
});

const wss = new WebSocketServer({ noServer: true });

// 기존 연결된 웹소켓 클라이언트를 저장할 배열
const clients = [];

wss.on("connection", (ws) => {
  // 새로운 클라이언트가 연결될 때
  console.log(`새로운 유저 접속 [현재:${clients.length}명]`);

  // 새로 연결된 클라이언트를 clients 배열에 추가
  clients.push(ws);

  // 클라이언트로 메시지를 보내어 새로운 유저가 입장했음을 알림
  broadcast(`새로운 유저 접속 [현재:${clients.length}명]`);
  ws.on("message", (data) => {
    console.log(`Received from client: ${data}`);

    // 클라이언트로부터 메시지를 받아서 모든 클라이언트에게 브로드캐스트
    broadcast(`${data}`);
  });

  ws.on("close", () => {
    // 클라이언트가 연결을 끊었을 때
    console.log("Client disconnected");

    // 해당 클라이언트를 clients 배열에서 제거
    clients.splice(clients.indexOf(ws), 1);

    // 클라이언트로 메시지를 보내어 유저가 퇴장했음을 알림
    broadcast(`유저 연결 해제 [현재:${clients.length}명]`);
  });
});

// 서버에 WebSocket을 직접 연결
const server = app.listen(8001, () => {
  console.log("WebSocket server listening on port 8001");
});

server.on("upgrade", (request, socket, head) => {
  wss.handleUpgrade(request, socket, head, (ws) => {
    wss.emit("connection", ws, request);
  });
});

// 모든 클라이언트에게 메시지를 브로드캐스트하는 함수
function broadcast(message) {
  clients.forEach((client) => {
    client.send(message);
  });
}
