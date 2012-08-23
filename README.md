# Install

    pip install packets

# Use for clients

        import packets

        client = packets.User()
        client.sendto((server.host, server.port), 'Hi!')
        print client.next.body

# Use for servers

        import packets

        server = packets.User()
        packet = server.next
        if packet.body == 'ping':
            packet.reply('pong')
        

# Documentation

*To be written*

Meanwhile take a look at the [source code](https://github.com/medecau/packets/blob/master/packets.py).

# Bugs & Co.

If you find bugs or new features that are not implemented you can:

 * [Fork and implement the changes](https://github.com/medecau/packets/fork)
 * [Fork and write a test that fails but shouldn't](https://github.com/medecau/packets/fork)
 * [Submit an issue in github](https://github.com/medecau/packets/issues)


