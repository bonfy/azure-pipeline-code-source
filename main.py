# coding: utf-8

import glob
import sys

def get_files(pattern):
    return glob.glob(pattern)
    
if __name__ == '__main__':
    pattern = '**/*.template'
    
    
    if len(sys.argv) == 1:
        print('No input, will use default pattern:', pattern)
    else:
        pattern = sys.argv[1]
        print('Use pattern:', pattern)

    filelist = get_files(pattern)
    if not filelist:
        print('Please check pattern, no files found')
        raise Exeption('No Files Found')
        
    for filename in filelist:
        print('scan ', filename)
