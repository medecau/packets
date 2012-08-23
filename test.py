import packets

# CREATE BOTH SERVER AND CLIENT USERS
server = packets.User(port=2000)
client = packets.User(port=3000)

# CLIENT SENDS A MESSAGE TO THE SERVER
client.sendto((server.host, server.port), 'Hi!')

# SERVER RETRIEVES THE PACKAGE AND PRESENTS IT
packet = server.next
print packet.body

# USING THAT PACKAGE THE SERVER CAN REPLY
packet.reply('Hey!')

# AND THE CLIENT GETS THE RESPONSE
print client.next.body
