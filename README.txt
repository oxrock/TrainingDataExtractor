This script is a simple way to extract useable data from replays and package it into accessible easy to use format for use in training an rlbot agent. Carball is required for this script to function and can be viewed here: https://github.com/SaltieRL/carball

Refer to the example script provided to gain an understanding of how to utilize TrainingDataExtractor's functionality.

packet format:
The outter layer of the saved data is simply a list of all the frames.
So data[0] == first frame
data[1] == second frame, etc

each frame is a dict with the following format:
frame{
	frame.GameState{
        	"time" : seconds elapsed 
        	"seconds_remaining" :  game time remaining
        	"deltatime" : time since previous frame

        	frame.GameState.ball {
        		"position" : current location of the ball as a list [x,y,z]
        		"velocity" : current velocity of the ball as a list [x,y,z]
        		"rotation" : current rotation of the ball as a list [x,y,z]
		}
	}
        frame.PlayerData is a list containing the data for each agent by index{ 
		"index" : player's index
    		"name" : player's name
		"team" : team index 0 for blue, 1 for orange
		"position" : current location of the player as a list [x,y,z]
    		"rotation" : current rotation of the player as a list [x,y,z]
    		"velocity" : current velocity of the player as a list [x,y,z]
    		"angular_velocity" : current angular velocity of the player as a list [x,y,z]
		"boost_level" : player's current boost amount
		"boosting" : bool indicating whether player is actively boosting
    		"throttle" : player's emulated throttle input
		"steer" :  player's emulated steering input
 		"pitch": player's emulated pitch input
 		"yaw" : player's emulated yaw input
 		"roll" : player's emulated roll input
		"jump" : player's emulated jump input
 		"handbrake" : player's emulated handbrake input

	}
	
}


Example of how you'd load replays, convert them to the above packet format and save them. Example stops at 5 but you could continue for however many replays you have available:

from  TrainingDataExtractor.createTrainingData import *
import os

path = "rl_replays"
files = os.listdir(path)
for i in range(5):
    try:
        _path = "{}/{}".format(path, files[i])
        output = f"myReplayType/{files[i]}.pbz2"
        createDataFromReplay(_path,output,"temp.json", save_json= True)
    except Exception as e:
        print("===== FAILURE ======")
        print(e, "\n"+_path)
        print("====================")
