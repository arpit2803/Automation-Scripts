import os
import time
present = os.listdir("C:\code\VC10\cpp")

req = []
for line in open(r"C:\required.txt").readlines():
	req.append(line.rstrip())

print "projects required" + "\n"

for line in req:
	print line

pre = []
for i in present:
	pre.append(i.lower())

print "\n" + "\n" + "projects present in VC10" + "\n"
req1 = []
for i in req:
	req1.append(i.lower())

for i in pre:
	print i
print "\n" + "\n" +"projects to be added" + "\n"
for tt in req1:
	if tt not in pre:
                print "------------"
		print tt
time.sleep(100)
