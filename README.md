# CS 361 Final Project
<h3> Text Message Application </h3>
<p>This application lets you programmatically send text messages and emails from using the command line interface. </p>

<h4>Microservice Contract </h4>
<p>The microservice I'm supplying is a listening server that sends a text message. You request the server with a json object {'phone_num': number, 'message': message}. My server will then respond with a json object with either 200 (success) or 400 (error) message with details. </p>

<p>The microservice my partner is supplying is a translation service via a listening server. The server receives a request with json object {'lang': language, 'text': text} and responses with a string.</p>
