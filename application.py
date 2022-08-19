from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import os

app = Flask(__name__)

img_folder = os.path.join('static', 'img')
css_folder = os.path.join('static', 'css')
js_folder = os.path.join('static', 'js')
foundation_js_folder = os.path.join('static', 'js', 'vendor')
app.config['UPLOAD_FOLDER'] = img_folder
app.config['CSS_FOLDER'] = css_folder
app.config['JS_FOLDER'] = js_folder
app.config['FOUNDATION_JS_FOLDER'] = foundation_js_folder

@app.route('/')
def index():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('home.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)

@app.route('/register')
def register():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('register.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)

@app.route('/login')
def login():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('login.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)


@app.route('/about')
def about():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('about.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)

@app.route('/dashboard')
def dashboard():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('dashboard.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)

@app.route('/analyze-handle')
def analyze_handle():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('analyze-handle.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)

@app.route('/analyze-org')
def analyze_org():
    icon_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tweebicle.png')
    css_ref = os.path.join(app.config['CSS_FOLDER'], 'foundation.min.css')
    style_ref = os.path.join(app.config['CSS_FOLDER'], 'app.css')
    js_ref = os.path.join(app.config['JS_FOLDER'], 'app.js')
    foundation_js_ref = os.path.join(app.config['FOUNDATION_JS_FOLDER'], 'foundation.min.js')
    return render_template('analyze-org.html', icon_filename=icon_filename, css_ref=css_ref, js_ref=js_ref, foundation_js_ref=foundation_js_ref, style_ref=style_ref)