remoteAdapter = Runtime.createAndStart("RemoteAdapterB","RemoteAdapter")
# Change to the ip address of the remote host
remoteAdapter.connect("tcp://192.168.1.95:6767")
