#!/usr/bin/env python3
import os
from datetime import datetime

from flask import Flask, render_template, request


app = Flask('nanowiki')


@app.route('/')
def handle_main():
    all_files = os.listdir('pages/')
    # TODO: use pathlib
    all_files = [file[:-4] for file in all_files if file.endswith('.txt')]
    return render_template('main.html', all_files=all_files)


@app.route('/<name>')
def handle_page(name):
    with open('pages/' + name + '.txt') as f:
        text = f.read()

    tmpl = 'page.html'
    if 'edit' in request.args:
        tmpl = 'edit.html'
    
    return render_template(tmpl, name=name, text=text)


if __name__ == '__main__':
    app.run(debug=True)