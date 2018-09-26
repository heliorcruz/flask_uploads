# flask_uploads
Transfer files to server by http using FLask
  
- Configure settings at config.py: 
DEVELOPMENT = True -- flag for dev enviroment 
SERVER_LOCAL = True -- flag for local running locally  
SECRET_KEY = ''  -- key for webservice  
CORS_HEADERS= 'Content-Type'  -- configure CORS  
CORS_ORIGINS = [] # or '*' -- Set COR IP adresses  
UPLOAD_FOLDER = 'root-path/uplodas' -- Set path to store files
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg']) -- set extensions allowed  
MAX_CONTENT_LENGTH =  16 * 1024 * 1024 -- set max size for file upload
SERVER_NAME = '127.0.0.1:8080' -- set ser host and port
  
1. Run server locally with `python webservice.py`  
2. Place files to be uploaded at files folder   
3. Test server running `python client.py`  
