from flask import Flask, request, render_template
import PyPDF2
import os

app = Flask(__name__)


current_directory = os.getcwd()
#upload_path = f"{current_directory}/uploads"


@app.route('/', methods=['GET', 'POST'])
def upload_and_read_file():
    if request.method == 'POST':
        file = request.files['file']
        other = str(request.form.get('other'))
        if file:
            print("File uploaded successfully")
            file.save(file.filename)
            f = open(file.filename, 'rb')
            reader = PyPDF2.PdfReader(f)
            file_contents = reader.pages[0].extract_text().split('\n')
            Name = []
            Bill = []
            Date = []
            Other = []
            for i in range(len(file_contents)):
                if file_contents[i].find("Name") != -1:
                    Name = file_contents[i].split(': ')[1]

                if file_contents[i].find("Bill No") != -1:
                    Bill = file_contents[i].split(': ')[1]

                if file_contents[i].find("Date") != -1:
                    Date = file_contents[i].split(': ')[1]

                if file_contents[i].find(other) != -1:
                    Other = file_contents[i].split(': ')[1]

            
            return render_template('file_contents.html', Name=Name,Bill_no=Bill,Date=Date,Other=Other)
                    

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

