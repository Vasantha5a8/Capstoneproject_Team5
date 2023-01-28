import os
class SystemDriveFinder:
    def __init__(self):
        pass
    def find_drives(self):
        #write the logic to get all the drives in the system(Active or Inactive)
        print("This is the find drives method of system drive finder class")

        drives = []
        for x in range (65,91):
            if os.path.exists(chr(x)+ ":"):
                drives.append(chr(x))
        return drives
if __name__=='__main__':
    obj=SystemDriveFinder()
    print(obj.find_drives())