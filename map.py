#!/usr/bin/env python

#created by Caleb Meeson
#follow me on instagram: @fawkespickshop
#check out the website I admin: http://ninjacache.com
#Updated on March 3, 2016

import os
import urllib2
import json
import codecs

os.system('cls' if os.name == 'nt' else 'clear')

ans=True
while ans:
    print
    print '===================================='
    print '#            MAPPY v1.1            #'
    print '===================================='
    print("1. Network Tools")
    print("2. Vulnerability Scan")
    print("C. Clear The Terminal")
    print("E. Exit")
    print("G. Get The Tools")
    print '===================================='
    ans=raw_input("What would you like to do? Enter your selection: ")

    if ans=="1":
        os.system('cls' if os.name == 'nt' else 'clear')

        ans=True
        while ans:

            print
            print '===================================='
            print '#            Network Time          #'
            print '===================================='
            print("1. Scan The Network For All Devices")
            print("2. Scan An IP Address For Open Ports")
            print("3. Look Up A MAC Address")
            print("4. Operating System Scan")
            print("M. Main Menu")
            print '===================================='
            print 
            ans=raw_input("What would you like to do? Enter your selection: ")

            if ans=="1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print
                    print("______________________________________________________________________")
                    print
                    address=raw_input("Enter your address and range (i.e. 192.168.0.1/24) now: ")
                    print
                    print("______________________________________________________________________")
                    os.system("sudo nmap -sn " + address)
                    print("______________________________________________________________________")
            elif ans=="2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print
                    print("______________________________________________________________________")
                    print
                    portscan=raw_input("Enter the IP you want to scan the ports of: ")
                    print("______________________________________________________________________")
                    os.system("sudo nmap " + portscan)
                    print("______________________________________________________________________")
            elif ans=="3":
                    os.system('cls' if os.name == 'nt' else 'clear')
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
                    print '================================================================='
            elif ans=="4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print
                    print("______________________________________________________________________")
                    print
                    osscan=raw_input("Enter the IP you want to find the operating system of: ")
                    print("______________________________________________________________________")
                    os.system("sudo nmap -O " + osscan)
                    print("______________________________________________________________________") 
                          
            elif ans=="M":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    os.system('sudo python map1-1.py')
                   
            else:
                    print
                    print("Not Valid Choice Try again")
                    print
                    os.system("sudo python map1-1.py")
                    ans = None
                    
                    
    elif ans=="2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        print("___________________________________________________________________________")
        print
        target=raw_input("Enter target: ")
        print("___________________________________________________________________________")
        print
        os.system("nikto -host " + target)
        print("______________________________________________________________________")
        if ans=="":
            os.system('cls' if os.name == 'nt' else 'clear')
              

    elif ans=="C":
        print
        os.system('cls' if os.name == 'nt' else 'clear')

    elif ans=="E":
        os.system('cls' if os.name == 'nt' else 'clear')
        ans = None

    elif ans=="G":
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        ans=True
        while ans:

            print
            print '===================================='
            print '#            TOOL TIME             #'
            print '===================================='
            print("1. Download Nmap")
            print("2. Download Nikto")
            print("M. Main Menu")
            print '===================================='
            print 
            ans=raw_input("Which program do you still need? Enter the number: ")

            if ans=="1":
                print 'Downloading Nmap Now...'
                print
                print
                os.system("sudo apt-get install nmap")

            if ans=="2":
                print 'Downloading Nikto Now...'
                print
                print
                os.system("sudo apt-get install nikto")

            if ans=="M":
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system('sudo python map1-1.py')
                
            

    else:
        print
        print("Not Valid Choice Try again")
        print
        os.system("sudo python map1-1.py")
            
