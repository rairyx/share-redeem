import os.path
from lib import import_dir
from lib.db import connection,Document
from config import DATABASE

Models = connection
class Base(Document):
    __database__   = DATABASE
    
    def ad_save(self,**args):
        for key in args:
            self[key] = args[key]
        return self.save()
    
    def add_or_update(self,where,**args):
        item = self.find_one(where)
        if not item:
            self.ad_save(**args)
        else:
            item.update(args)
            item.save()

__current_dir = os.path.abspath(__name__)
import_dir(__current_dir)
    
