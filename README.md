# Pot Hole Detection Using Fuzzy Logic

# Fuzzy-Logic-Distance
This Project of mine , displays the Probability of potholes that are in front of the sensors


This Python script implements a simple fuzzy logic system to predict the chance of pot holes based on mean distance readings from sensors and the range from the ground. It uses the scikit-fuzzy library for fuzzy logic operations.

## Requirements
Python 3.x
scikit-fuzzy library (pip install scikit-fuzzy)
Usage
Clone the repository or download the pot_hole_detection.py file.
Install the required library using pip install scikit-fuzzy.
Run the script: python pot_hole_detection.py.
Enter the mean distance of 5 sensors and the range from the ground when prompted.
The script will compute and display the predicted pot hole detection level (low, medium, high).
Code Structure
pot_hole_detection.py: Main Python script containing the fuzzy logic implementation.
test_distance.csv: Example CSV file with test data for distance readings.
Fuzzy Logic System
Input Variables:

Distance: Represents the mean distance of 5 sensors.
Range Ground: Represents the range from the ground.
Output Variable:

Pot Hole Detection: Predicts the chance of encountering pot holes (low, medium, high).
Fuzzy Rules:

Defined based on expert knowledge or empirical data to map input variables to output.
Example Usage
mathematica
Copy code
Enter the mean distance of 5 sensors: 40
Enter the range from the ground: 30
Mean Distance: 40.0
Range from Ground: 30.0
Pot Hole Detection: 36.45 (Medium)
In this example, with a mean distance of 40 and a range from the ground of 30, the system predicts a medium chance of encountering pot holes.
