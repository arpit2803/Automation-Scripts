import os,sys,shutil
### copies a list of files from source. handles duplicates.
def rename(file_name, dst, num):
	#splits file name to add number distinction
	(file_prefix, extension) = os.path.splitext(file_name)
	if num == 0:
		renamed = file_prefix + extension#"%s%s" %  (file_prefix, extension)
	else:
		new_extension = ".local"
		renamed = file_prefix + new_extension#"%s%s" % (file_prefix, new_extension)
	#if "com" in file_prefix:
	#	new_extension = ".local"
	#	renamed = file_prefix + new_extension#"%s%s" % (file_prefix, new_extension)
	#else:
	#	renamed = file_prefix + extension#"%s%s" %  (file_prefix, extension)
	return renamed

def copy_files(src,dst,file_list):
	for files in file_list:
		count = 0
		if "com" in files:
			count = 2
			print count
		else:
			count = 1
		if not(".dll") in files:
			count = 0
		if ("CRMSpy") in files:
			count = 1
		if ("PvTimeLineViewCtrl.NET") in files:
			count = 1
		if ("CRMSpySettings") in files:
			count = 1
		if ("powerchart") in files:
			count = 1
		for num in range(0, count):
			print num
			src_file_path = os.path.join(src, files)  #src + '\' + files
			dst_file_path = os.path.join(dst, files)  #dst + '\' + files
			if not os.path.exists(dst_file_path) or num == 1:
				print "destination file doesn't exist....so copying"
				new_file_name =  rename(files, dst, num)
				dst_file_path = os.path.join(dst, new_file_name) #dst + new_file_name
				try:
					shutil.copyfile(src_file_path,dst_file_path)
				except IOError:
					print src_file_path + " does not exist"
					raw_input("Please, press enter to continue.")

def read_file(file_name):
    f = open(file_name)
    #reads each line of file (f), strips out extra whitespace and 
    #returns list with each line of the file being an element of the list
    content = [x.strip() for x in f.readlines()]
    f.close()
    return content

src = "P:\win32"
dst = "C:\COM_DLL_Script"
file_with_list = "C:\COM_DLL_Script\Files.txt"

copy_files(src,dst,read_file(file_with_list))