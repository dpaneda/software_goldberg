## Languages used:
 * Python
 * Bash scripting 
 * C
 * Go

Needed packages:

python2.7
tweepy

## Nodes
I call nodes to each step in this awesome rube goldberg machine. 
Nodes appears in trigger activation order. 

Nodes always (at least by the moment) are a process or thread but
a single file could result in different process (for example the
multi-language autocompiling bash_c.cpp)

### send_tweet.py 

#### trigger
User launched, first step
#### actions
Send a tweet to the timeline of the user configured in auth.json

### read_tweet.py

#### trigger
Read the timeline of the user configured in auths.json until a new tweet appears

#### actions
Exec bash_c.cpp

### bash_c.cpp (sh instance)

#### trigger
Is being executed by previous node

#### actions
Compile itself with gcc and exec the result

### bash_c.cpp (cpp instance)

#### trigger
Is being executed by previous node

#### actions
Connect throught a socket with the next node and send a token

### tunnel.go
This node works as a socket tunnel. It just open a listen socket and write the 
received data to other socket much like the anciend echo inetd service.

### goodbye

#### trigger
Listen on a socket, being triggered when receiving stuff on it.

#### actions
Outputs goodbye world to the screen. Final step
