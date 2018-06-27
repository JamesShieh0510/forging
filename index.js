var express = require('express');
var app = express();
var bodyParser = require('body-parser');
//set body-parser options
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

const child_process = require('child_process');

var fs = require('fs');//file system module

var BPMtimer;
var isBPMRunning = false;

app.get('/start', function(req, res){
	if (isBPMRunning) //if BPM is running -> don't run again
		res.send('One BPM has been running.');
	else { //else, BPM is not running -> run BPM
		
		isBPMRunning = true;
				var workerProcess = child_process.exec('IPython Forging-preprocess.py',
					function (error, stdout, stderr) {
						if (error) {
							console.log(error.stack);
							console.log('Error code: '+error.code);
							console.log('Signal received: '+error.signal);
						}
					}
				);
				
				workerProcess.on('exit', function (code) {
					console.log('Child process exited with exit code ' + code);
				});		
		
		console.log('Forging is now running!');
		res.send('Forging is now running!');
	}
});

app.post('/stop', function(req, res){

	clearInterval(BPMTimer);
	isBPMRunning = false;
	
	console.log('Forging is now stopped!');
	res.send('Forging is now stopped!');
});
var server = app.listen(8055);


