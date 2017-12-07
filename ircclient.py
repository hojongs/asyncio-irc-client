import asyncio

class IRCClient(asyncio.Protocol):
    def __init__(self, CHANNEL, NICK, PASS, proc_chat, loop):
        self.channel = CHANNEL
        self.nick = NICK
        self.password = PASS
        self.proc_chat = proc_chat # callback that is called data_received
        self.loop = loop

    # callback
    def connection_made(self, transport):
        self.transport = transport
        
        msg_list = []
        if self.password and len(self.password) > 0:
            msg_list.append('PASS %s\r\n' % self.password)
        msg_list.append('NICK %s\r\n' % self.nick)
        msg_list.append('USER dummy 0 * :dummy\r\n')
        msg_list.append('JOIN %s\r\n' % self.channel)
        
        for msg in msg_list:
            print('*** [SENDED]', msg, end='')
            transport.write(msg.encode())

    # callback
    def data_received(self, data):
        packet = data.decode().split(' ', 3) # split 3 times
        nick = (packet[0].split('!'))[0][1:]
        command = packet[1]
        
        if command != 'PRIVMSG':
            print(data.decode())
        else:
            chat = packet[3][1:].replace('\r\n', '')
            self.proc_chat(nick, chat)

    # callback
    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()
        
    # call by main()
    def send_chat(self, chat):
        msg = 'PRIVMSG %s :%s\r\n' % (self.channel, chat)
        print('*** [SENDED]', msg)
        self.transport.write(msg.encode())