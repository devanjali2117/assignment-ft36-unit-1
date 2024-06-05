input_values=input().split()
distance=int(input_values[0])
time=int(input_values[1])
speed=distance/time
if speed > 40:
    print("Apply Brake")
else:
    print("Keep Going")
