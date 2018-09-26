#!flask/bin/python
import os
import json
from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from config import  CORS_ORIGINS

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
@cross_origin(origin=CORS_ORIGINS, headers=['Content-Type','Authorization'])
def upload_file():
    if request.method == 'POST':      
        if not request.files:
            return Response({'error': 'no file part'}, status=404, mimetype='application/json')       
        if 'filenames' not in request.values:
            return Response({'error': 'no filenames'}, status=404, mimetype='application/json')  
              
        files = request.files.getlist('files')
        filenames = request.values.getlist('filenames')
        file_erros = []      
        file_count = 0
        for f in range(len(files)):           
            try:
                if files[f] and allowed_file(filenames[f]):
                    filename = secure_filename(filenames[f])
                    files[f].save(os.path.join(app.config['UPLOAD_FOLDER'], filename.replace('.temp', '')))
                    file_count += 1    
                else:
                    file_erros.append({'file': filenames[f],'error': 'no file or filename not allowed'})  
                                  
            except Exception as we:
                file_erros.append({'file': filename,'error': we})
        r_dict = json.dumps({'result': 'File saved: {0}'.format(file_count), 'errors': file_erros})   
        return Response(r_dict, status=200, mimetype='application/json')                
            
    return Response({'error': 'GET method not allowed'}, status=404, mimetype='application/json')


if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.run()
