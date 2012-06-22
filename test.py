from packets import Server
s=Server()
while True:
    p = s.next
    if p.body == 'die':
        p.reply('Bye.')
        break
    elif p.body == 'ping':
        p.reply('pong')
