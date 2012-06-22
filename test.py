
s=Server()
while True:
    r = s.next
    if r.body == 'die':
        break
