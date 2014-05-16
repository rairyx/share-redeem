import os
import os.path
import sys

def import_dir(dir):
    __name__  =  os.path.basename(dir)
    try:
        for filename in os.listdir(dir):
            if filename.endswith('.py'):
                if '__init__' in filename: continue
                model_name = __name__+'.%s' % filename.split('.')[0]
                sys.modules.get(model_name) or __import__(model_name)
    except Exception,why:
        print filename,why
