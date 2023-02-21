# -convert-microsip-local-address-book-to-twinkle

When I migrated from Windows to Arch Linux I wanted to copy my local address book from MicroSIP under Windows to Twinkle on Linux, because SIP softphone is my daily work tool.

MicroSIP stores the local address book in a file:
C:\Users\user\AppData\Roaming\MicroSIP\Contacts.xml

Twinkle stores the local address book in a file:
/home/user/.twinkle/twinkle.ab

Due to the fact that the format of the address book in MicroSIP and in Twinkle is different, it is not possible to transfer data by simply copying the Contacts.xml file. Therefore, I decided make a tool for do this task.

Using MicroSIP, I complete data in the "Name" and "Number" fields when adding contacts to the database.

In my case, I use a public SIP server and each caller is presented as 12345567@sip.MyPublicSIPserver.pl in Twinkle.

Before you run the script, modify the data in line 5,6,7.

After using the script, copy your outFile as /home/user/.twinkle/twinkle.ab

Tested on:
Python 3.10.9 & Twinkle 1.10.3 & MicroSIP 3.20.7
