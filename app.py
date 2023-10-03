from flask import Flask, request, render_template, send_from_directory
import os
import uuid  # Import the UUID library to generate unique IDs

app = Flask(__name__, template_folder='templates')
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
        # Generate a unique ID for the video
        unique_id = str(uuid.uuid4())

        # Define the filename using the unique ID
        filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{unique_id}.mp4')

        # Save the uploaded video using the unique filename
        video.save(filename)
        return "Video uploaded successfully"

@app.route('/play/<video_id>')
def play_video(video_id):
    # In the URL, 'video_id' should be the unique ID generated during upload
    return render_template('play.html', video_filename=f'{video_id}.mp4')

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
