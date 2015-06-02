import os

project_name = raw_input("Enter Project you want to work on :")

f = open(r"P:\vc10\cpp\project_name\project_name.vcproj", 'r+b')

f_content = f.readlines()
print len(f_content)

count = 0
text = '      <ExcludedFromBuild Condition="\'$(Configuration)|$(Platform)\'==\'Test Release|Win32\'">true</ExcludedFromBuild>\n'
for line in f_content:
	count = count + 1
	if line.find("Test.cpp") > 0:
		f_content.insert(count+1, text)
	
print len(f_content)		
f.seek(0)
f.truncate()
f.write(''.join(f_content))
f.close()
	
		
