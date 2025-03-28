#Name: Brayden
#Date: 2025-03-28
#Purpose: URL Shortener

from flask import Flask, render_template, request, redirect, url_for
import hashlib
import os
from datetime import datetime

app = Flask(__name__)

# mem storage for urls (use db in prod)
url_mapping = {}

def generate_short_url(long_url):
    """gen short url using md5 hash, first 7 chars"""
    hash_object = hashlib.md5(long_url.encode())
    return hash_object.hexdigest()[:7]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('url')
    if not long_url:
        return "Please provide a URL", 400
    
    # gen short url
    short_url = generate_short_url(long_url)
    
    # store mapping
    url_mapping[short_url] = {
        'long_url': long_url,
        'created_at': datetime.now().isoformat()
    }
    
    return render_template('result.html', 
                         short_url=request.host_url + short_url,
                         original_url=long_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in url_mapping:
        return redirect(url_mapping[short_url]['long_url'])
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True) 