def detect_start_of_message(datastream):
    for i in range(13, len(datastream)):
        if len(set(datastream[i-13:i+1])) == 14:
            return i +1
    return "UNKNOWN"

with open("day6_data.txt", "r") as file:
    datastream = file.read()
position = detect_start_of_message(datastream)
print(position)