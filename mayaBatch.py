import subprocess, os

standalone_path = "C:\\Program Files\\Autodesk\\Maya2016\\bin\\mayapy.exe"
source_path = "D:\\Vaishak\\Scripts"      #location of maya files to be worked on

allFiles = []

for files in os.listdir(source_path):
  if files.endswith(".ma"):
    allFiles.append('%s\%s', %(source_path,files))

#Feed each of the files to maya standalone to execute "mayaTest.py"
for files in allFiles:
  print 'Processing ' + files
  p = subprocess.Popen([standalone_path, 'D:\\Vaishak\\Scripts\\mayaTest.py', files], stdout=subprocess.PIPE, stdin-subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  
  while p.poll() == None:
    lastoutput = p.communicate()[0]\
    
  if p.returncode == 0:
    print "Successfully completed"
  else:
    print "Error - Code:" + p.returncode
    
