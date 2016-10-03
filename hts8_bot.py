from irc_bot import irc_bot
import time
import hashlib
import argparse

parser = argparse.ArgumentParser(description='+++ HackThisSite Programming Challenge 8.')
parser.add_argument('--server', default="irc-hub.hackthissite.org",
                    help="IRC server to connect to. Default: irc-hub.hackthissite.org")
parser.add_argument('--nick', help="Nickname to use on login", required=True)
parser.add_argument('--password',
                    help="Password for nick. Must have previously registered this nick "
                         "and linked to HTS account", required=True)
args = parser.parse_args()

server = args.server
nick = args.nick
irc_password = args.password

irc = irc_bot(server, nick=nick, password=irc_password)

"""-------------------------------------------------------------------
Main
------------------------------------------------------------------"""
irc.hold_for_response("NOTICE")
irc.message("nickserv", "identify " + irc_password)
irc.hold_for_response("recognized")
irc.send_command("JOIN #perm8")
irc.hold_for_response("End of /NAMES list")


def reflect_md5(data):
    global irc
    md5 = hashlib.md5()
    md5.update(bytes(data[data.find("!md5 ")+5:-2]))
    irc.notice("moo", "!perm8-result " + md5.hexdigest())

# Note: moo is currently in the lille.irc.hackthissite.org server
# The IP of the server is 137.74.187.150

def attack(data):
    irc.join_channel("#takeoverz")
    #time.sleep(.5)
    #irc.send_command("KICK #takeoverz moo")

# Note: currently stuck trying to kick moo
def kick(data):
    # To find out where moo was
    #irc.send_command("WHOIS moo")
    irc.send_command("KICK #takeoverz moo")


irc.add_listener("!md5", reflect_md5)
irc.add_listener("!perm8-attack", attack)
irc.add_listener("MODE #takeoverz", kick)

irc.notice("moo", "!perm8")


while True:
    time.sleep(1)

