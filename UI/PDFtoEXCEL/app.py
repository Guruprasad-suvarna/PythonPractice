import os
import tabula
import pandas as pd
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import zipfile

app = Flask(__name__)

# Set the upload folder and output folder
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Create the output folder if it doesn't exist
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    download_link = None

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(pdf_path)

                excel_filename = os.path.splitext(filename)[0] + '.xlsx'
                excel_path = os.path.join(app.config['OUTPUT_FOLDER'], excel_filename)

                dfs = tabula.read_pdf(pdf_path, pages='all', stream=True, multiple_tables=True, pandas_options={'header': None})

                combined_df = pd.concat(dfs, ignore_index=True)

                combined_df.to_excel(excel_path, index=False, header=False)

                download_link = excel_filename

        elif 'folder' in request.form:
            folder_path = request.form['folder']
            pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
            generated_files = []

            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                excel_filename = os.path.splitext(pdf_file)[0] + '.xlsx'
                excel_path = os.path.join(app.config['OUTPUT_FOLDER'], excel_filename)

                dfs = tabula.read_pdf(pdf_path, pages='all', stream=True, multiple_tables=True, pandas_options={'header': None})

                combined_df = pd.concat(dfs, ignore_index=True)

                combined_df.to_excel(excel_path, index=False, header=False)
                generated_files.append(excel_filename)

            download_link = 'output.zip'
            with zipfile.ZipFile(os.path.join(app.config['OUTPUT_FOLDER'], download_link), 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in generated_files:
                    zipf.write(os.path.join(app.config['OUTPUT_FOLDER'], file), file)

    return render_template('index.html', download_link=download_link)

@app.route('/output/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
