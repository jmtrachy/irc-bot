## irc-bot
Gives developers the ability to quickly create an IRC bot.  A friend and I have created several bots recently for irc and every time I find myself building boiler plate code.

This code only works in python3 because of how 2 and 3 handle strings/bytes differently.

#### Initializing the bot

example.py is an example implementation.  Simply create a bot, add some listeners and get on your way.

```
Bot(bot_name, bot_welcome_message)
```
example: ```bot = bot.Bot('test', 'Hello Everybody')```

The above example registers a bot under the name "test".  Any time a message is sent to the channel if it contains the phrase "@test" the bot will attempt to match a listener to the statement

#### Adding listeners

##### Simple listener

```
bot.add_simple_listener(term, action)
```
example: ```bot.add_simple_listener('foo', some_function)```

The above line adds a simple listener for the term "foo".  When a message is sent to the channel containing "@test foo" the bot will call some_function with any additional arguments for the command.  For example - if somebody types ```@test foo bar``` then the function will be called with ```some_function('bar')```

The function is expected to return a string - which the bot will send as a message to the channel.  However - returning None is acceptable too and will not cause the bot to write anything to the channel

##### Complex listener

```
bot.add_complex_listener(term, action)
```
example: ```bot.add_complex_listener('complex', some_function)```

The above line adds a coplex listener for the term "complex".  Behavior is the same as for simple listeners except with a complex listener "some_function" is expected to return an array of messages.  The bot will loop through the array and send each as a message to the channel.

#### Connect

```
bot.connect(host, port, channel)
```
example: ```bot.connect('www.yourdomain.com', 6667, 'friends_and_family')```

Connects to an IRC server at the designated host/port - and in this case enters the "friends_and_family" channel.  After the bot enters the channel it will send the message defined in the constructor.

#### Quit

By default any bot using this framework will exit the channel (and the program) if it receives the command "quit" (in this case "@test quit").
