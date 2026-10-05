import { createServer } from "node:http";

const port = Number(process.env.PORT ?? 4000);

createServer((_req, res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ service: "paylog", status: "ok" }));
}).listen(port, () => {
  console.log(`paylog dev server: http://localhost:${port}`);
});
