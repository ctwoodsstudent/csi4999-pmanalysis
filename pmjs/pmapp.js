const http = require('http');

const hostname = '127.0.0.1'; //home
const port = 3000; //may use port 8000?

const server = http.createServer((req, res) => {
	res.statusCode = 200;
	res.setHeader('Content-Type', 'text/plain');
	res.end('Phenotype Microarray Analysis Tool\n');
});

server.listen(port, hostname, () => {
	console.log('Server running at http://${hostname}:${port}/');
});