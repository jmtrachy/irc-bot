import bot
import config

def ketchup_listener(arguments):
    return 'mustard' 

def ping_listener(arguments):
    return 'pong'

def jimbob_listener(arguments):
    return 'rocko'

def complex_listener(num_lines):
    messages = []
    if num_lines is not None:
        num_lines_to_print = int(num_lines)
        for j in range(0, num_lines_to_print):
            messages.append('Whoa this is complex!!!')

    return messages

if __name__ == '__main__':
    bot = bot.Bot('test', 'Hello everybody')
    bot.add_simple_listener('ketchup', ketchup_listener)
    bot.add_simple_listener('ping', ping_listener)
    bot.add_simple_listener('jimbob', jimbob_listener)
    bot.add_complex_listener('c', complex_listener)

    # The first argument is the host - a fully qualified domain name.  Second argument is the port.  Third argument is the irc channel
    # example: bot.connect('www.mydomain.com', 6667, 'friends_and_family')
    bot.connect(config.host, config.port, config.channel)
