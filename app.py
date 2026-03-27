import os
import vlc
from flask import Flask, request, jsonify


VLC_PATH = r'D:\Stuff\VLC'

if os.path.exists(VLC_PATH):
    os.add_dll_directory(VLC_PATH)

app = Flask(__name__)
instance = vlc.Instance(f'--plugin-path={VLC_PATH}', '--quiet')
player = instance.media_player_new()



@app.route('/play', methods=['POST'])
def play_video():
    data = request.get_json(silent=True)
    video_path = data.get('path') if data else None

    if not video_path or not os.path.isfile(video_path):
        return jsonify({"error": "File not found"}), 404

    was_playing = player.is_playing()

    media = instance.media_new(video_path)
    player.set_media(media)

    if player.play() == -1:
        return jsonify({"error": "VLC failed to load file"}), 500

    res = {"status": "playing", "video": video_path}
    if was_playing:
        res["warning"] = "Interrupted existing playback."
    return jsonify(res), 200


@app.route('/status', methods=['GET'])
def get_status():
    state = str(player.get_state()).split('.')[-1]
    return jsonify({
        "state": state,
        "is_playing": player.is_playing() == 1,
        "time_ms": player.get_time()
    }), 200


@app.route('/stop', methods=['POST'])
def stop_video():
    player.stop()
    return jsonify({"status": "stopped"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
