kill `cat server_pid`

python app.py &> output &
SERVER_PID=$!
echo "$SERVER_PID" > server_pid
