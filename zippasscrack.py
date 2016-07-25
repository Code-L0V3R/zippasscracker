#!/usr/bin/env python
# Author : L0V3R IN MYANMAR
# Date : 25.7.2016


import zipfile,sys,os,time

version = 1

def logo():
	print """
	 ______       ____                ____                _             
	|__  (_)_ __ |  _ \ __ _ ___ ___ / ___|_ __ __ _  ___| | _____ _ __ 
	  / /| | '_ \| |_) / _` / __/ __| |   | '__/ _` |/ __| |/ / _ \ '__|
	 / /_| | |_) |  __/ (_| \__ \__ \ |___| | | (_| | (__|   <  __/ |   
	/____|_| .__/|_|   \__,_|___/___/\____|_|  \__,_|\___|_|\_\___|_|   
	       |_|                                                          
	       					  ==================
	       					  == Version : %s  ==
	       					  ==================
	"""%version
def main():

	zipfilename = sys.argv[1]
	if not os.path.exists(zipfilename):
		print "Zip File Not Found!"
		exit(1)
	passfile = sys.argv[2]
	if not os.path.exists(passfile):
		print "Password File Not Found!"
		exit(1)

	if not zipfile.is_zipfile(zipfilename):
		print "Zip File Error!"
		exit(1)
	zip_file = zipfile.ZipFile(zipfilename)
	f = open(passfile, 'r')
	data = f.readlines()
	f.close()
	tot = len(data)
	now = 1
	st = time.time()
	found = False
	for line in data:
		password = line.strip('\n')
		try:
			sys.stdout.write("\rUsing Password [ %d/%d ] : %s"%(now,tot,password))
			sys.stdout.flush()
			zip_file.extractall(pwd=password)
			print '\nPassword Found : %s ' % password
			found = True
			# exit(1)
		except KeyboardInterrupt,e:
			# print e
			exit(1)
		except Exception,e:
			# print e
			pass
		now += 1
		if found:
			break
			
	if not found:
		print "\nNo Password Found!"
	else:
		lt = time.time()
		ts = int(lt-st)
		print "Total Time to crack : %s s"%ts

if __name__ == '__main__':
	logo()
	if len(sys.argv) == 3:
		main()
	else:
		print "\tUsage :"
		print "\tpython zippasscrack.py zipfilename passwordfile"
