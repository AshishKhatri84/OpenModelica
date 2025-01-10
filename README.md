# Purpose of the Application:
The purpose of this application is to provide a simple and user-friendly GUI interface to execute a compiled OpenModelica model program with specified start and stop times. It allows users to select the executable file, input simulation parameters, and validate the time constraints, ensuring they fall within the range __0≤start time<stop time<5__. This tool simplifies running model simulations by automating the execution process and improving user experience with intuitive controls and error handling.

# Project Description :
The task involves two parts. The first part is to compile a model and create an executable program from the OpenModelica simulation tool. The second part is to create a GUI application in Python that will run the above-generated executable with some parameters.

# Steps:
1. Download and install OpenModelica on a Windows 10 / 11 machine.
2. Download the model package from here. Load it (all models) in OMEdit which is installed along with OpenModelica. 
3. Build (compile) the “TwoConnectedTanks” model. This should create an executable program of this model along with other 
   dependent files that this executable program requires to execute it. It corresponds to the simulation of the mentioned 
   model.
4. Collect the executable program, its dependent files/libraries, its runtime OS dependencies, etc.
        <-- All Dependencies are not uploaded to this directory because of large no. and size--> 
6. Now, create an app consisting of a simple GUI application in Python.
7. It should have 3 input fields:
           a. the application to launch
           b. start time
           c. stop time
8. Within the first input field, one should be able to select an application to execute. Here, it will be the executable 
   created from the OpenModelica model.
9. The second input field will be the start time for the executable as an Integer.
10. The third input field will be the stop time for the executable as an Integer.
11. A button should be added to the app. On clicking it, the app will execute the program selected/mentioned in the first 
    input field. As the program here corresponds to the OpenModelica model, running it requires start and stop time. Hence, 
    the values in the second and third input fields need to be given as arguments to the executable. 
	
Hint: Refer to the documentation for passing arguments: https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/simulationflags.html#simflag-override 

For test purposes, you need to ensure the following condition:	
           0 <= start time < stop time < 5

# Technologies used:
1. Python 3.6+
2. PyQt6
3. OpenModelica
4. Windows 10/11 OS

# Features of the Code:
1. GUI Components:
    * Input fields for executable path, start time, and stop time.
    * A browse button to select the executable file.
    * A run button to execute the program with the provided arguments.
2. Validation:
    * Ensures 0 <= start time < stop time < 5.
    * Checks for valid file path and numeric input for time fields.
3. OOP Design:
    * Encapsulates functionality in a class ModelLauncherApp.
    * Separates logic into methods for readability and reusability.
4. PEP8 Compliance:
    * Code is properly formatted, readable, and maintainable.
5. Error Handling:
    * User-friendly error messages for invalid input or file selection.

# How to Run the Application
1. Install PyQt6:
        pip install PyQt6
2. Save the Script: Save the above script as model_launcher.py.
3. Run the Script:
        python model_launcher.py
4. Usage:
    * Use the browse button to select the OpenModelica executable.
    * Enter valid start and stop times.
    * Click the "Run" button to execute.
