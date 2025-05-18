# ws
ws

pkg update && pkg install tmux python
pip install websocket-client

tmux new-session -s runws 'python runws.py'
ctrl+b d (keluar sementara)

tmux attach -t runws
