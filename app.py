from flask import Flask, request, render_template, send_from_directory, jsonify
import os
import uuid
import sqlite3

app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = 'videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DATABASE = 'video_database.db'

def insert_video_metadata(video_id, filename):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO videos (id, filename) VALUES (?, ?)", (video_id, filename))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Hello, this is your video playback page."

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return jsonify({'message': 'No video part'}), 400
    
    video = request.files['video']
    if video.filename == '':
        return jsonify({'message': 'No selected video file'}), 400
    
    if video:
        unique_id = str(uuid.uuid4())
        filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{unique_id}.mp4')
        video.save(filename)
        
        insert_video_metadata(unique_id, filename)  # Store metadata in the database
        
        return jsonify({'message': 'Video uploaded successfully', 'video_id': unique_id}), 201

@app.route('/videos', methods=['GET'])
def get_videos():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos")
    videos = [{'video_id': row[0], 'filename': row[1]} for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(videos), 200

@app.route('/play/<video_id>')
def play_video(video_id):
    # In the URL, 'video_id' should be the unique ID generated during upload
    return render_template('play.html', video_filename=f'{video_id}.mp4')

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
