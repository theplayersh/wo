#!/usr/bin/python
# -*- coding:utf-8 -*-

######################################## LIBRARY ########################################

import os
import time
import sys, traceback

######################################## COLOR VARIABLES ########################################

yellow = "\033[1;33m"
normal = "\033[0;1m"
green = "\033[32;1m"
blue = "\033[34;1m"
red = "\033[31;1m"
white = "\033[0m"

######################################## LOGO CODESEC BR ########################################

codesec = """
\033[0m  ██████████╗ ██    ██   ██╗ ██████    ██ ██████╗ ████████╗
\033[0m  ██╔════╝██╔═██╗   ██╔══██╗  ██  ██═══██ █╔════╝    ██╔════╝
\033[0m  ██████████║ ████████║  ██║  ██║  █   ██ ███████    ██║     
\033[0m  ██║     ║   ██║   ██║  ██║  ██    █  ██╔█══╝  ╚════██║     
\033[0m ╚██╔╝        ██    ██╔╝ ██   ██     ████╗███████║   ██      
\033[0m  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝    
"""

######################################## SEPARATION LINE ########################################

line = """

\033[1;33m   **************************************************************************
"""

######################################## NETWORK SOCIAL CODESEC BR ########################################

network = """

\033[0;1m    [!] This software was developed for phinet ng

\033[1;33m    [+] Coded: Mirror                        


\033[31;1m    [!] http://fb.com/Mirror               \033[0;1mFacebook
\033[31;1m    [!] http://fb.com/Mirror               \033[0;1mFacebook
\033[31;1m    [!] http://fb.com/Mirror               \033[0;1mFacebook
\033[31;1m    [!] http://t.me/Mirror                 \033[0;1mTelegram
\033[31;1m    [!] http://t.me/Mirror                 \033[0;1mTelegram



"""

######################################## FUNTION EXIT ########################################

def exit_script():
	
	clear_logo_line()
	print(red + "    [-] Exiting the software ...\n")
	time.sleep(2)
	exit()






################# INFORMATION GATHERING ########################################
	def information_gathering():

	 
	 print (codesec + network)
	
	
	armitage()
	beef_xss_fr()
	metasploit()
	msf_payload()
	searchsploit()
	social_engineering()
	sqlmap()
	termineter()

	

################# VULNERABILITY ANALYSIS ########################################
	def Vulnerability_analysis():

	 
	 print (codesec + network)
	
	
	golismero()
	lynis()
	nikto()
	nmap()
	sparta()
	unix-prive()
	
	

################# WEB APPLICATION ANALYSIS ########################################
	def Web_application_analysis():

	
	 print (codesec + network)
	
	
	burpsuite()
	commix()
	httrack()
	owasp-zap()
	paros()
	skipfish()
	sqlmap()
	webscarab()
	wpscan()
	
	

################# DATABASE ASSESSMENT ########################################
	def Database_Assessment():

	 
	 print (codesec + network)
	
	
	bbqsql()
	hexorbase()
	jSQL_Injection()
	mdb-sql()
	oscanner()
	sidguesser()
	sqldict()
	SQLite_dat()
	sqlmap()
	sqlninja()
	sqlsus()
	tnscmd10g()
	
	

################# PASSWORD ATTACKS ########################################
	def Password_Attacks():

	
	 print (codesec + network)
	
	
	cewl()
	crunch()
	hashcat()
	john()
	johnny()
	medusa()
	ncrack()
	ophcrack()
	pyrit()
	rainbowcr()
	rcracki_mt()
	wordlists()

	

################# WIRELESS ATTACKS ########################################
	def Wireless_Attacks():

	
	 print (codesec + network)
	
	
	aircrack-ng()
	chirp()
	cowpatty()
	fern_wifi_cr()
	ghost_phis()
	giskismet()
	mdk3()
	mfoc()
	mfterm()
	pixiewps()
	reaver()
	wififte()
	Social_Engineering_Tools()
	

################# REVERSE ENGINEERING ########################################
	def Reverse_Engineering():

	 
	 print (codesec + network)
	
	
	apktool()
	clang()
	clang+++()
	dex2jar()
	edb-debug()
	flasm()
	jad()
	javasnoop()
	NASM_shell()
	ollydbg()
	radare2()
	
	

################# EXPLOITATION TOOLS ########################################
	def xploitation_Tools():

	
	 print (codesec + network)
	
	
	armitage()
	beef_xss_fr()
	metasploit()
	msfpayload()
	searchsploit()
	social_engineering()
	sqlmap()
	termineter()
	
	

################# SNIFFING & SPOOFING ########################################
	def Sniffing_Spoofing():

	 
	 print (codesec + network)
	
	
	bdfproxy()
	driftnet()
	ettercap()
	hamster()
	macchanger()
	mitmproxy()
	netsniff-ng()
	responder()
	wireshark()
	Post_Exploitation()
	Forensics()
	Reporting_Tools()
	Social_Engineering_Tools()
	

################# POST EXPLOITATION ########################################
	def Post_Exploitation():


	 print (codesec + network)
	
	
	backdoor()
	bdfproxy()
	exe2hex()
	intersect()
	mimikatz()
	nishang()
	powersploit()
	proxychains()
	weevely()
	
	

################# FORENSICS ########################################
	def Forensics():

         
	 print (codesec + network)
	
	
	autopsy()
	binwalk()
	bulk_extra()
	chkrootkit()
	foremost()
	galleta()
	hashdeep()
	volafox()
	volatility()
	

################# REPORTING TOOLS ########################################
	def Reporting_Tools():

	 
	 print (codesec + network)
	
	
	cutycapt()
	dradis_fra()
	farady_IDE()
	maltego()
	pipal()
	recordmyd()
	
	

################# SOCIAL ENGINEERING TOOLS ########################################
	def Social_Engineering_Tools():

	 
	 print (codesec + network)
	
	backdoor-f()
	beef_xss_fr()
	ghost_phis()
	maltego()
	msf_payload()
	social_engi()
	u3-pwn()
	
	
	
######################################## FUNTION ADDING REPOSITORIES ########################################

def metasploit():

	clear_logo_line()
	print (red + "    [+] Opening\n" + yellow)
#os.system("metasploit")
######################################## FUNTION UPDATING REPOSITORIES ########################################



######################################## FUNTION INSTALLING THE TOOLS ########################################



######################################## FUNTION REMOVING REPOSITORIES ########################################



######################################## FUNTION MAIN ########################################

def main():

 os.system("clear")
	
	
	
	information_gathering()
	Vulnerability_analysis()
	Web_application_analysis()
	Database_Assessment()
	Password_Attacks()
	Wireless_Attacks()
	Reverse_Engineering()
	Exploitation_Tools()
	Sniffing__Spoofing()
	Post_Exploitation()
	Forensics()
	Reporting_Tools()
	Social_Engineering_Tools()
	

################# STARTING A SCRIPT ########################################
	

try:

	main()

except KeyboardInterrupt:

	exit_script()
