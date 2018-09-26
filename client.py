import requests
import json
import os
import time
root_folder= 'path-to-root/files'
zip_folder = 'file_name.rar' 

def run_zip():
    url = 'http://127.0.0.1:5000/upload'
    f = open(root_folder + "/" + zip_folder, "rb")
    r =  requests.post(url=url, data =  {},  files =  {'file':f})
    print r.status_code
    print r.headers
    
def run_files():
    url = 'http://127.0.0.1:8080/upload'
    files_to = []
    filenames = []
    start_time = time.time() 
    count_files = 0 
    for folder, _, files in os.walk(root_folder):
        for filename in files:
            f = open(folder + "/" + filename, "rb")
            files_to.append(('files',f))
            filenames.append(filename)  
            count_files += 1  
    
    r =  requests.post(url=url, data = {'filenames': filenames},  files = files_to)
    print r.status_code  
    print r.text    
    end_time = time.time()
    print "Total files {0}".format(count_files)
    print "Total time: {0}".format(end_time - start_time)
    
    

if __name__ == '__main__':
    try:
        run_files() 
    except Exception as we:
        print we
        pass