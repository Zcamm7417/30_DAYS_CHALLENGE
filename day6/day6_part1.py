def find_start_of_packet_marker(datastream):
    for i in range(3, len(datastream)):
        if len(set(datastream[i-3:i+1])) == 4:
            return i+1
    return "DONT KNOW"

with open("day6_data.txt", "r") as file:
    datastream = file.read()
position = find_start_of_packet_marker(datastream)
print(position)

