# Install

    pip install packets

# Use

    from packets import Server
    s=Server()
    while True:
        p = s.next
        if p.body == 'die':
            p.reply('Bye.')
            break
        elif p.body == 'ping':
            p.reply('pong')

# Documantation

*To be written*

# Bugs & Co.

If you find bugs or new features that are not implemented you can:

 * [Fork and implement the changes](https://github.com/medecau/packets/fork)
 * [Fork and write a test that fails but shouldn't](https://github.com/medecau/packets/fork)
 * [Submit an issue in github](https://github.com/medecau/packets/issues)


