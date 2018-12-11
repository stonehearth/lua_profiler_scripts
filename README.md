# lua_profiler_scripts
Scripts used to profile your Stonehearth game's lua performance

1. Place the following in your user_settings.json:
```
"lua" : {
    "enable_cpu_profiler" : true,
    "enable_memory_profiler" : true,
    "cpu_profiler_method" : "sampling", // or "time_accumulation"
    "profiler_instruction_sampling_rate" : 1,
    "max_profile_length": 10000 //optional, how long in ms we can run the profiler
},
"simulation" : {
    "initial_speed_override" : 0,
    "long_profile_tick_threshold" : 500
},
 ```
 Remove the comments before pasting into your user settings, and adjust the config values as needed.

2. Build the lua file map by navigating to the folder where you downloaded the `lua_profiler` scripts folder to, and then running the python script with the following arguments:

`collect_lua_file_map.py [PATH_TO_MODS_FOLDER] lua_file_map.js`

3. Replace [PATH_TO_MODS_FOLDER] with the path to your stonehearth mods folder.

4. Load up the game you want to profile
5. Wait for the UI to come up, select the "Performance Monitor" icon (upper right, looks like a line graph) in debug tools
6. When ready (after clicking the speed 1 button and wait for initial script catch up), click on the profiling button (the play button). If you are looking for what is causing sudden hitches, check the `Long Ticks Only` checkbox.
7. Press the stop button to finish profiling.
9. Open Chrome and navigate to the lua_profiler.html file in the lua_profiler folder
10. Click on the "Choose Files" button and navigate to the profile dump under `Stonehearth\profiler_output\DATE_AND_TIME_OF_PROFILE_CAPTURE`. The `profiler_output` folder can be found in the same folder as the `mods` folder.
11. Select ALL files under that folder and click open
12. When the profiler finishes loading the files, it will populate the rows with each method name, total time, # calls, percentage of lua consumption (this number is the important one), and the file path.
13. Look at the function that is taking the most amount of time and figure out if there's a way to make it faster
14. Profile again!

IMPORTANT: launch a new tab of `lua_profiler/lua_profiler.html` every time you need to load a new profile

Note: If you are getting a game crash while profiling in `ai::CreateAction`, add a check for `ai.get()` on the preceding line.
 
