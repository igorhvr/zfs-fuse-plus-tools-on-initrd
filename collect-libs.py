#!/usr/bin/python
import os
import popen2, string
import re
from lists import extralibs

def enumeratefiles(path):
    """Returns all the files in a directory as a list"""
    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_collection.append(path+file)
    return file_collection

def collect_libs(dict, file):
    print file+": "
    fin, fout = popen2.popen2("ldd "+file)
    fout.close()
    for line in fin.readlines():
        m=re.search("(\S*/lib\S+)", line)
        if m:
            dict[m.group(1)]=""
    fin.close()


if __name__ == "__main__":
    libs={}
    for pre in ("/lib", "/lib64"):
        for lib in ("/libgcc_s.so.1","/libnss_files.so.2","/libnss_compat.so.2"):
            libs[pre+lib]=""
            collect_libs(libs,pre+lib)
    for lib in extralibs:
        libs[lib]=""
        collect_libs(libs,lib)
    for path in ("source/bin/", "source/sbin/", "source/usr/local/sbin/", "source/usr/local/sbin/zfs.save/"):
        for file in enumeratefiles(path):
            collect_libs(libs, file)
    for lib in libs.keys():
        print lib
        if not os.path.exists("source"+os.path.dirname(lib)):
            os.makedirs("source"+os.path.dirname(lib))
        os.system("cp -u -v -L "+lib+ " source"+lib)
