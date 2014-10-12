CSNE_EMGRoboCam
===============
Nile Wilson, Laurie Zhang, October 12, 2014
----------------------------

Physical Setup

1) Plug in ground to the top of the Biometrics DataLog
2) Plug in left arm EMG to channel 1
2) Plug in right arm EMG to channel 2
3) Plug in left arm goniometer to channels 3 and 4
4) Plug in right arm goniometer to channels 5 and 6

Make sure the small USB stub thing for bluetooth, the turret, and the webcame are plugged into the computer

----------------------------

Getting code to work

Make sure you have all the necessary python libraries installed

1) Go to the log file, clear it out, and save
2) Open Biometrics DataLog
3) In the "Units" window, make sure your bluetooth device is selected
4) Click "Analogue Input for Recording" (it's the red sine curve button)
5) Make the settings match the image "Biometrics DataLog settings"
6) Turn on the Biometrics DataLog device (bluetooth device)
7) Click "Start Data Transfer" (the green octagon button with a black check inside it)
8) Start Team5Project Folder -> Biometrics Ltd -> DataLog -> Example Projects -> VClinkTest_VC6 -> VClinkTest -> Debug -> VClinkTest.exe
	(when you start this EXE, this is when data is going to start being written to the log file)
9) Open python IDE (pyscripter), go to Run -> Command Line Parameters
10) Add the log file file location and check the "Use Command Line Parameters?" box
	(i.e. C:\Users\Hackathon5\Documents\Team5ProjectFolder\LogFile\Test.log)
10) Run the python code "RoboCameraMain"

There you go
