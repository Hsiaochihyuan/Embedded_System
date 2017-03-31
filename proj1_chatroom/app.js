var express = require('express'),
	app = express(),
	server = require('http').createServer(app),
	io = require('socket.io').listen(server),
	usernames = [];

server.listen(3000);
// HTTP GET request -> middleware function
app.get('/', function(req, res){
	res.sendfile(__dirname + '/index.html');
});
// Static file provided
app.use('/frame', express.static(__dirname + '/frame'));

io.sockets.on('connection', function(socket) {
	socket.on('new user', function(data){
		console.log(data);
		if (usernames.indexOf(data) != -1) {

		} else {
			socket.emit('chat', 'SERVER', '歡迎光臨 ' + data);

			socket.username = data;
			usernames.push(socket.username);
			io.sockets.emit('usernames', usernames);
			updateUsernames();
		}
	});

	function updateUsernames(){
		io.sockets.emit('usernames', usernames);
	}

	//
	socket.on('send message', function(data){
		io.sockets.emit('new message', { msg: data, nick: socket.username });
	});

	socket.on('disconnect', function(data){
		if (!socket.username) return;
		io.sockets.emit('chat', 'SERVER', socket.username + ' 離開了聊天室');
		usernames.splice(usernames.indexOf(socket.username), 1);
		updateUsernames();
	});
});
