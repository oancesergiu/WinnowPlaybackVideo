How to run the application:
After creating an environment for Python and installing flask and python-vlc, the provided code can be runed by python app.py. This should display “http://localhost 5000”.
Keeping  the window open, the windows powershell needs to be opened to trigger a video playback using the command:
 Invoke-RestMethod -Method Post -Uri "http://localhost:5000/play" -ContentType "application/json" -Body '{"path": "Add_specific_video_path"}'
For checking the status of the app the command used is :
Invoke-RestMethod -Method Get -Uri "http://localhost:5000/status"
For stoping the video playback the command used is :
Invoke-RestMethod -Method Post -Uri http://localhost:5000/stop

Dependencies required to run the application:
•	VLC Media Player
•	Some food video stored at a specific path
•	System files: libvlc.dll and libvlccore.dll
•	Python libraries:	
o	Flask for the HTTP API interface 
o	python-vlc allows python to control VLC


Assumptions or limitations in your implementation:
The system uses specific videos from a local machine at a specific path instead of using a data base with videos.

What you would improve if you had more time
I would try to make it so that the system can run videos in parallel and also make the system access videos from a specific database. I would also try to add a feature so that the user could access a specific time stamp and run the video from there.


1.	The overall design of your solution:
Design Architecture: this is an API driven service that combines automated test scripts with a local VLC to provide video playback control.
•	Flask: is the API layer that is used as a service gateway towards an HTTP interface. 
•	Python-VLC: translates API requests into simple commands for video playback.

2.	The interface or API you propose
Proposed interface: RESTfull HTTP API that allows testing frameworks to control video playback with standard requests.
•	POST /play: Triggers playback of a specific file path provided in a JSON body.
•	GET /status: Returns real-time telemetry (state, current time, and duration) for test assertions.
•	POST /stop: Terminates active playback and releases system resources.
•	POST /reset: Force-clears the media engine to ensure a "clean slate" for the next test run.
3.	The main components of the system
•	API Gateway (Flask): receives HTTP commands (Play, Stop, Status) from test scripts.
•	Controller Logic (Python): validates file paths, handles errors, and manages the player's state.
•	Media Engine (LibVLC): handles high-performance video decoding and rendering.
•	State Monitor: An internal tracker that provides real-time telemetry for test assertions.

4.	How your design would support automated testing
•	Feedback: Returns immediate HTTP error codes so tests fail 
•	Test Isolation: Provides a /reset endpoint to clear the engine's memory and ensure every test run starts from a "clean slate."
•	Collision Detection: Automatically identifies and warns if a test step attempts to play a video over an already active one.

5.	Any assumptions or limitations
Some further improvements could be automation of multiple video playbacks since this can only run a single video at a time. Also running a specific part of the video and controlling the timestamps and frames could be a future improvement.


