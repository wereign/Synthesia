from flask import Flask
from flask import render_template,send_file 
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from Synthesia import Synthesia

app = Flask(__name__)
app.config["SECRET_KEY"] = "somethingsimple"
app.config ["UPLOAD FOLDER"] = "static/files"


ALLOWED_EXTENSIONS = set(['png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFileForm(FlaskForm):
    file = FileField("File",validators=[InputRequired()])
    submit = SubmitField("Upload Image")


@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])

def home():
    form = UploadFileForm()

    if form.validate_on_submit():
        file = form.file.data # First getting the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD FOLDER'],secure_filename(file.filename))) # Save the file
        save_location = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD FOLDER'],secure_filename(file.filename))
        print(save_location)

        output_file_path = Synthesia(save_location).save_file(secure_filename(file.filename))
        return send_file(output_file_path,as_attachment=True)
    return render_template("index.html", form=form)

# minor change to trigger redeploy
if __name__ == "__main__":
    app.run(debug=True)