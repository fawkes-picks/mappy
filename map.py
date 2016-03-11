#!/usr/bin/env python

import os
import urllib2
import json
import codecs

ans=True
while ans:

    print
    print '===================================='
    print '======== Nmap Python Scanner ======='
    print '===================================='
    print("1. Scan The Network For All Devices")
    print("2. Scan An IP Address For Open Ports")
    print("3. Look Up A MAC Address")
    print("4. Operating System Scan")
    print("C. Clear The Terminal")
    print("E. Exit")
    print("GN. Get Nmap")
    print '===================================='
    print 

    ans=raw_input("What would you like to do? Enter your selection: ")
    if ans=="1":
        print
        address=raw_input("Enter your address and range (i.e. 192.168.0.1/24) now: ")
        os.system("sudo nmap -sn " + address)
    elif ans=="2":
        print
        portscan=raw_input("Enter the IP you want to scan the ports of: ")
        os.system("sudo nmap " + portscan)
    elif ans=="3":
        print
        url = "http://macvendors.co/api/"
        print '================================================================='
        mac_address =raw_input('Enter the MAC Address you want vendor info for: ')

        request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
        response = urllib2.urlopen( request )

        reader = codecs.getreader("utf-8")
        obj = json.load(reader(response))

        print '================================================================='
        print (obj['result']['company']);
        print (obj['result']['address']);
        print '=============================================='
    elif ans=="4":
        print
        osscan=raw_input("Enter the IP you want to find the operating system of: ")
        os.system("sudo nmap -O " + osscan)
    elif ans=="C":
        print
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ans=="E":
        print
        print("Peace Out Girl Scout!") 
        print
        ans = None
    elif ans=="GN":
        print 'Downloading Nmap Now...'
        print
        print
        os.system("sudo apt-get install nmap")
    else:
        print("Not Valid Choice Try again")
