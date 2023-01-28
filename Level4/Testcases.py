import pytest
from Level1.findfile import FileFinder
from Level1.democlass import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','C:\\')
        act=['C:\\hcl\\demo.txt', 'C:\\hcl1\\demo.txt']
        self.expected=act
        self.actual_res=d
        assert self.expected==self.actual_res
