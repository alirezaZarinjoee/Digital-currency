
from uuid import uuid4
import os

class FileUpload:
    def __init__(self,dir,perfix,custom=''):
        self.dir=dir
        self.perfix=perfix
        self.custom=custom
    
    def upload_to(self,instance,filename):
        name,ext=os.path.splitext(filename)
        return f'{self.dir}/{self.perfix}/{self.custom}/{uuid4()}{ext}'