from flask import *
import pdfSplitter
app =Flask(__name__)

@app.route("/")
def upload():
    return render_template("index.html")
@app.route("/success",methods=["POST"])
def success():
    global s
    global e
    global f
    s=int(request.form['start'])
    e=int(request.form['end'])
    f=request.files['file']
    file=f.filename
    f.save(file)   
    pdfSplitter.cropper(s,e,file)
    filename = file.split(".")[0]+"cropped.pdf"
    send_file(filename,as_attachment=True)
    
    return render_template("success.html")
   
if __name__=="__main__":
    app.run(debug=False)