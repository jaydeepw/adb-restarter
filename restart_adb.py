import os

filename = "tmp.txt"

# copy ADB path to a file
os.system( "which adb > " + filename )

# form 2-pair of the result
lines = tuple( open(filename, 'r') )

adb_path = lines[0]

if adb_path is None:
	print "ADB path not found"
else:
	adb_path = adb_path.strip()

print "\nADB path ", adb_path

kill_command = "sudo " + adb_path + " kill-server"

print "===> Kill ADB..."
os.system(kill_command)

start_command = "sudo " + adb_path + " start-server"

print "===> Start ADB..."
os.system(start_command)
