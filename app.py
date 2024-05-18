from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-spider', methods=['POST'])
def run_spider():
    url = request.form['url']
    process = subprocess.Popen(['scrapy', 'crawl', 'feed_spider', '-a', f'url={url}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.path.dirname(os.path.abspath(__file__)))
    stdout, stderr = process.communicate()
    return jsonify({
        'output': stdout.decode('utf-8'),
        'error': stderr.decode('utf-8')
    })

if __name__ == '__main__':
    app.run(debug=True)
