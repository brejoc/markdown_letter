from os import remove
from os import path
from sh import pandoc
from uuid import uuid4

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import send_file

DEBUG = False

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
	uuid = str(uuid4())
        f = request.files['file']
        f.save('/tmp/%s.md' % (uuid, ))
        pdf_filename = '/tmp/%s.pdf' % (uuid, )
        out = pandoc('/tmp/%s.md' % (uuid, ), "-o", pdf_filename, "--template", "brief.tex")
        remove('/tmp/%s.md' % (uuid, ))
        return send_file(pdf_filename,
                         attachment_filename=path.splitext(f.filename)[0] + ".pdf",
                         add_etags=False,
                         as_attachment=True)
    else:
        html = """<html><body><form action="/" method="post" enctype="multipart/form-data"> <input name="file" type="file" size="50" accept="text/*"> <button type="submit">Upload</button></form>
<p>Keep in mind, that this is just a proof of concept. Download the <a href="https://gist.github.com/brejoc/6774bd9974b71a48b624520de788d0de" target="_blank">example Markdown file</a> from GitHub and upload it here. You should get a nicely formatted German DIN-letter.</p>
</body></html>

"""
        return html


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=DEBUG,
    )
