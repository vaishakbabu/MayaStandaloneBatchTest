import os, sys
import maya.standalone
import tempfile
maya.standalone.initialize(name='python')

import maya.cmds as cmds
mFile = sys.argv[1]

#This function takes care of errorLogging
def exitstand(e=None):
  maya.standalone.uninitialize()
  if e!= None:
    errorFile = 'D:\Vaishak\Scripts\errorlog.txt'
    if os.path.exists(errorFile):
      os.remove(errorFile)
    
    with open(errorFile, 'w') as mfile:
      mfile.write(str(e))
    mfile.close()
    sys.exit(-1)
  else:
    sys.exit(0)
    
  
#This function generates spheres and places them at random spots in the scene
def randomSphere():
  import random as r

  for i in range(0,15):
    cmds.polySphere()
    cmds.move(r.randint(-25,25),r.randint(-25,25),r.randint(-25,25))

#This is the main function that performs the operations
def main():
  cmds.file(mFile, f=True, 0=True)
  cmds.select(cmds.ls(geometry=True))
  cmds.delete()
  randomSphere()
  cmds.file(save=True)

#Entry point of the application
try:
  main()
except Exception, e:
  exitstand(str(repr(e)))
