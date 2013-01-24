import packets

# CREATE BOTH SERVER AND CLIENT USERS
server = packets.User(port=50000)
client = packets.User()

# CLIENT SENDS A MESSAGE TO THE SERVER
client.sendto((server.host, server.port), 'Hi!')

# SERVER RETRIEVES THE PACKAGE AND PRESENTS IT
packet = server.next
print packet.body

# USING THAT PACKAGE THE SERVER CAN REPLY
packet.reply('{"msg": "Hey!"}')

# AND THE CLIENT GETS THE RESPONSE
reply = client.next.json
print reply['msg']

# TEST EXCEPTION FOR LARGE PACKETS
#client.sendto((server.host, server.port), '0'*256*256)