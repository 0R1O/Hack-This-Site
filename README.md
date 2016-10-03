# Hack-This-Site
Code for solving HackThisSite challenges.

:: Hack This Site :: Programming :: Unscramble the words

Find the original (unscrambled) words, which were randomly taken from a wordlist: https://www.hackthissite.org/missions/prog/1/wordlist.zip

Send a comma separated list of the original words, in the same order as in the list below.

You have 30 seconds time to send the solution.
	
List of scrambled words: 

++ Solution: 

See unscrambled.py

The words vary, so the words I got are not the words you will get

.

:: Hack This Site :: Programming :: Analyze the picture and find the ascii code

This level is about image analyzing.

Image:

https://www.hackthissite.org/missions/prog/2/PNG/

The pixels in the above image are numbered 0..99 for the first row, 100..199 for the second row etc. White pixels represent ascii codes. The ascii code for a particular white pixel is equal to the offset from the last white pixel. For example, the first white pixel at location 65 would represent ascii code 65 ('A'), the next at location 131 would represent ascii code (131 - 65) = 66 ('B') and so on.

The text contained in the image is the answer encoded in Morse, where "a test" would be encoded as ".- / - . ... -"

You have 15 seconds time to send the solution.

++ Solution: 

See image-to-morse-to-text.py

.

:: Hack This Site :: Programming :: Code an IRC bot

In this mission you need to write an IRC bot that can perform some simple tasks. To begin, your bot needs to use a registered nickname with autoop turned on(/ns set autoop on), which is linked to a HTS account.

You can link an irc nickname with a HTS account by typing: !link <hts account> in #perm8. Next your bot needs to connect to irc.hackthissite.org, and then it needs to notice moo with !perm8. Moo will notice you with !md5 <some random string> , your bot must reply with !perm8-result <hash>.

If that is correct and done in time, moo will version the bot to check if you aren't using mIRC. Your bot MUST reply to the version. When that is correct, moo will notice you with !perm8-attack. When your bot receives that command it must join #takeoverz as fast as possible and attempt to kick moo (You will automatically be oped when you join the channel). Each month we will have a competition in #takeoverz to see who can control the channel the longest (See #takeoverz rules). The winner's source code will be on display on the site for people who have already completed the challenge.

++ Solution:

See irc_bot.py and hts8_bot.py

.

More challenge solutions and code to be uploaded later...


