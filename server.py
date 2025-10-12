# Basic Flask app to serve HTML files
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
	return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
	# Only allow serving files that exist in the root directory
	if os.path.isfile(filename):
		return send_from_directory('.', filename)
	else:
		return 'File not found', 404

if __name__ == '__main__':
	app.run(debug=True)
