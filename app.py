from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Hello, this is your video playback page."

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return "No video part"
    
    video = request.files['video']
    if video.filename == '':
        return "No selected video file"
    
    if video:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(filename)
        return "Video uploaded successfully"

@app.route('/play/<video_filename>')
def play_video(video_filename):
    return render_template('play.html', video_filename=video_filename)

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
