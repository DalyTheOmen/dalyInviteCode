#script name= dalyInviteCode
#version = 1.0 -- 2018
#Author = Daly The Omen
#if u think this script was easy , try to get invite code without it ...:) 
import requests as req
import codecs
import json
def dalyCode():
	print ''
	print ''
	print '                      ##########################################'
	print '                      #    Welcome to daly script hack_the_box #'
	print '                      #          Invite_Code_generator         #'
	print '                      ##########################################'
	print ''
	resp=req.post("https://www.hackthebox.eu/api/invite/generate")
	a= resp.text.split(',')[1]
	b=a.split(":")[2]
	en =  codecs.decode(b,'base64')
        print '                             -------------------------------'
	print "Your invite Code is ---->   | " +en +' |'
	print '                             -------------------------------'
	print "Enjoy :) to hack the box..."
if __name__ == "__main__":
	dalyCode()


