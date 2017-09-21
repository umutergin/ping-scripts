#!/usr/bin/python
from scapy.all import *
import sys
import socket

try:
	destinationIP= sys.argv[1]
	destinationPort= sys.argv[2]
	ttlValue= sys.argv[3]
	flag= sys.argv[4]
	icmpType= sys.argv[5]
	message= sys.argv[6]

except:
	print '#######################################'
	print '            Let\'s Ping! '
	print '#######################################'
	print ' \nUsage: ping.py  [IP]  [Port]   [TimeToLive]   [Flag[1-8]]   [ICMPType]   [MessageToSend]\n\n\n'
	exit()

try:
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.connect((destinationIP, int(destinationPort)))

	packet = IP(dst=destinationIP)/ICMP()/message
	packet.ttl = int(ttlValue)
	packet.flags = int(flag)
	packet.type= int(icmpType)

	send(packet)

	packet.show()

except:
	print '\nSocket connection failed. Are you certain host is up?\n'
