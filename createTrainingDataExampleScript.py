import createTrainingData

"how decompile a .replay file into .json format, save it locally(optional) returns extracted game frames data and controls"
#extractedGameStatesAndControls = createTrainingData.convert_replay_to_game_frames("rocket league replays/00C878424939F13B2E9643B905A5E833.replay","test.json",save_json = True)



"how to extract game frames data and controls from a previously decompiled .json file"
#x = convert_json_to_game_frames("PreviouslyUnpackedJson.json")


"how to load the data from a previously saved .pbz2 file"
#gameData = createTrainingData.loadSavedTrainingData("exampleSavedTrainingData.pbz2")


"uncomment below code and replace dummy arg with the path to a valid previously saved training data file. Run to see frame data format"
# gameData = createTrainingData.loadSavedTrainingData("insert valid path to saved training data")
# print(f"This variable contains data for {len(gameData)} game frames in addition to controller input data")
# print(gameData[500]["GameState"])
# print(gameData[500]["PlayerData"][0])

