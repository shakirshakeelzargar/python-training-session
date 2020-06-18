from __future__ import unicode_literals
import os

from pathlib import Path
import json

from flask import (render_template)
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',data={"name":"Shakir"})


if __name__ == '__main__':
    app.run(debug=True)
