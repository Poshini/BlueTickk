import random
def Encryptmsg(msg):
    rand = 63*random.random()
    rand = int(rand)
    msglen = len(msg)
    temp = msglen
    noofdigits = 0
    while(temp):
        noofdigits = noofdigits+1
        temp = temp//10
    tempstr = ""
    for i in range(msglen) :
        if i%2==0 :
            tempstr += chr(ord(msg[i])^rand)
        else :
            tempstr += chr(ord(msg[i])+i%5);
    finalstr = str(noofdigits) + str(msglen) + tempstr + str(rand)
    return finalstr

def Decryptmsg(p):
    msglenstr = ""
    for i in range(1,int(p[0])+1):
        msglenstr += p[i]
    msglen = int(msglenstr)
    msg = ""
    start = int(p[0])+1
    for i in range(start,start+msglen):
        msg += p[i]
    plen = len(p)
    randstr = ""
    for i in range(start+msglen,plen):
        randstr += p[i]
    rand = int(randstr)
    decryptedmsg = ""
    for i in range(msglen) :
        if i%2==0:
            decryptedmsg += chr(ord(msg[i])^rand)
        else :
            decryptedmsg +=  chr(ord(msg[i])-i%5);
