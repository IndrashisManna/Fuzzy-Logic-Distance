import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

path= r'G:\Python code\Fuzzy logic\distance.csv'
file1 = pd.read_csv(path)
#print(file1)


for i in range (24):

    # Define linguistic variables and membership functions
    distance = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')
    distance['close'] = fuzz.trimf(distance.universe, [0, 0, 50])
    distance['medium'] = fuzz.trimf(distance.universe, [20, 50, 80])
    distance['far'] = fuzz.trimf(distance.universe, [50, 100, 100])

    range_ground = ctrl.Antecedent(np.arange(0, 101, 1), 'range_ground')
    range_ground['low'] = fuzz.trimf(range_ground.universe, [0, 0, 50])
    range_ground['medium'] = fuzz.trimf(range_ground.universe, [20, 50, 80])
    range_ground['high'] = fuzz.trimf(range_ground.universe, [50, 100, 100])

    pot_hole = ctrl.Consequent(np.arange(0, 101, 1), 'pot_hole')
    pot_hole['low'] = fuzz.trimf(pot_hole.universe, [0, 0, 30])
    pot_hole['medium'] = fuzz.trimf(pot_hole.universe, [10, 50, 90])
    pot_hole['high'] = fuzz.trimf(pot_hole.universe, [70, 100, 100])

    # Define fuzzy rules
    rule1 = ctrl.Rule(distance['close'] & range_ground['low'], pot_hole['high'])
    rule2 = ctrl.Rule(distance['close'] & range_ground['medium'], pot_hole['medium'])
    rule3 = ctrl.Rule(distance['close'] & range_ground['high'], pot_hole['low'])
    rule4 = ctrl.Rule(distance['medium'] & range_ground['low'], pot_hole['medium'])
    rule5 = ctrl.Rule(distance['medium'] & range_ground['medium'], pot_hole['medium'])
    rule6 = ctrl.Rule(distance['medium'] & range_ground['high'], pot_hole['low'])
    rule7 = ctrl.Rule(distance['far'] & range_ground['low'], pot_hole['low'])
    rule8 = ctrl.Rule(distance['far'] & range_ground['medium'], pot_hole['low'])
    rule9 = ctrl.Rule(distance['far'] & range_ground['high'], pot_hole['low'])

    # Create Fuzzy Control System
    pot_hole_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    pot_hole_detection = ctrl.ControlSystemSimulation(pot_hole_ctrl)

    # Accept user input for mean distance and range from ground
    #mean_distance = 0
    #range_value = 1

    #while mean_distance < range_value:
        #mean_distance = float(input("Enter the mean distance of 5 sensors: "))
        #range_value = float(input("Enter the range from the ground: "))

    mean_distance = file1.loc[i, 'mean']
    range_value = file1.loc[i, 'std dis']
    # Compute pot hole detection level
    pot_hole_detection.input['distance'] = mean_distance
    pot_hole_detection.input['range_ground'] = range_value
    pot_hole_detection.compute()

    dd = pot_hole_detection.output['pot_hole']

    # Output pot hole detection level
    print('Mean Distance:', mean_distance)
    print('Range from Ground:', range_value)
    print('Pot Hole Detection:', dd)
    file1.loc[i, 'percent'] = dd

output_path = r'G:\Python code\Fuzzy logic\file1.csv'
file1.to_csv(output_path, index=False)


