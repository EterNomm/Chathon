import chathon

client = chathon.Client(username="LyQuid", badword_filter=True)
client.connect(server_ip="127.0.0.1", server_port=1212)
