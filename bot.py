import socket


class Bot():
    def __init__(self, name, welcome_message=''):
        self.name = name
        self.len_name = len(name)
        self.welcome_message = welcome_message
        self.simple_listeners = {}
        self.complex_listeners = {}

    def add_simple_listener(self, term, action):
        self.simple_listeners[term] = action

    def add_complex_listener(self, term, action):
        self.complex_listeners[term] = action

    def connect(self, network, port, channel):
        irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        irc.connect ( ( network, port ) )

        nick_command = 'NICK ' + self.name + '\r\n'
        user_command = 'USER ' + self.name + ' ' + self.name + ' ' + self.name + ' :Python IRC\r\n'
        join_command = 'JOIN #' + channel + '\r\n'
        priv_command = 'PRIVMSG #' + channel + ' :' + self.welcome_message + '\r\n'
        irc.send(nick_command.encode())
        irc.send(user_command.encode())
        irc.send(join_command.encode())
        irc.send(priv_command.encode())

        message_base = 'PRIVMSG #' + channel + ' :'

        keep_running = True
        while keep_running:
            byte_data = irc.recv ( 1024 )
            data = byte_data.decode().rstrip()
            name_index = data.find('@' + self.name)

            # If the message is not aimed at a bot simply ignore it
            if name_index != -1:

                # Ugly string parsing nonsense to get the command and arguments
                end_name_index = name_index + self.len_name + 2
                bot_command = data[end_name_index:]
                first_space = bot_command.find(' ')
                arguments = None
                if first_space != -1:
                    arguments = bot_command[first_space + 1:]
                    bot_command = bot_command[:first_space].lower()

                # Every message will be sent to the channel - might as well initialize this up here
                message = None

                # Quit if receiving the quit command - this is universal to all bots
                if bot_command == 'quit':
                    message = self.name + ' is quitting due to popular request.  Goodbye'
                    keep_running = False
                else:
                    # Send the arguments (even if still None) to the assigned listener
                    if bot_command in self.simple_listeners:
                        message = self.simple_listeners[bot_command](arguments)
                    elif bot_command in self.complex_listeners:
                        messages = self.complex_listeners[bot_command](arguments)
                        if messages is not None:
                            for m in messages:
                                single_line = message_base + m + '\r\n'
                                irc.send(single_line.encode())
                    else:
                        message = 'Command ' + bot_command + ' not found for ' + self.name

                # Send the message no matter what has been created
                if message is not None:
                    message = message_base + message.rstrip() + '\r\n'
                    irc.send(message.encode())
