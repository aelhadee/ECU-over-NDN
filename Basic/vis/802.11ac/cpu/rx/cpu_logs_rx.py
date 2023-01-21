import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.size'] = 14
plt.figure(figsize=(10,10))

processes = {"lidar_receiver.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}}
#________________________LIDAR NDN UDP_________________________________
# Open the text file and read its content
with open("rpi11_lidar_ndn_cpu_s_udp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "lidar_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="LiDAR NDN UDP (S)", linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="LiDAR NFD UDP (S)", linewidth = 2)

#________________________LIDAR NDN TCP_____________________-------
processes = {"lidar_receiver.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}
             }

with open("rpi11_lidar_ndn_cpu_s_tcp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "lidar_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="LiDAR NDN TCP",  linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="LiDAR NFD TCP", linewidth = 2)


#_________________DDS LIDAR____________________--

processes = {"lidar_receiver.py": {"cpu_values": []}}

with open("rpi11_lidar_dds_wireless.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "lidar_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="LiDAR DDS", linewidth = 2)

#________________________CAM NDN UDP_________________________________

processes = {"cam_receiver.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}}
# Open the text file and read its content
with open("rpi12_cam_ndn_cpu_s_udp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "cam_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="CAM NDN UDP (S)", dashes=[2, 2, 10, 2], linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="CAM NFD (S)", dashes=[2, 2, 10, 2],linewidth = 2)

#________________________CAM NDN TCP_____________________-------
processes = {"cam_receiver.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}
             }
with open("rpi12_cam_ndn_cpu_s_tcp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "cam_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="CAM NDN TCP", dashes=[2, 2, 10, 2], linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="CAM NFD TCP", dashes=[2, 2, 10, 2], linewidth = 2)

#_________________cam DDS____________________--

processes = {"cam_receiver.py": {"cpu_values": []}}

with open("rpi12_cam_dds_wireless.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "cam_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="CAM DDS", dashes=[2, 2, 10, 2], linewidth = 2)

#________________________CAN NDN UDP_________________________________

processes = {"can_receiver.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}}
# Open the text file and read its content
with open("rpi13_can_ndn_cpu_s_udp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "can_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="CAN NDN UDP (S)", linestyle='--', linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="CAN NDN UDP (S)", linestyle='--', linewidth = 2)

#________________________CAN NDN TCP_____________________-------
processes = {"can_receiver.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}
             }
with open("rpi13_can_ndn_cpu_s_tcp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "can_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="CAN NDN TCP", linestyle='--', linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="CAN NFD TCP", linestyle='--', linewidth = 2)


#_________________can DDS____________________--

processes = {"can_receiver.py": {"cpu_values": []}}

with open("rpi13_can_dds_wireless.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "can_receiver.py":
        plt.plot( processes[process]["cpu_values"], label="CAN DDS", linestyle = '--', linewidth = 2)

#_______












plt.ylim([0, 175])

plt.xlabel("Time in Seconds")
plt.ylabel("CPU %")
plt.title("CPU Consumption Percentage at each receiver")

plt.legend( ncol=1, loc = 'best') # ,bbox_to_anchor=(0.3,0.3) ,
plt.show()

# import os
# import bs4
# #
#
#
#
# lidar = ''
#
# # # Use os.listdir() to get a list of all HTML files in a directory
# # for filename in os.listdir("./"):
# #     if filename.endswith(".log"):
# with open("pc_tx_ndn_cpu.log",'r') as f:
#     all_cpu_string = f.read()
#     index = 0
#     number = 0
#     while True:
#         index = all_cpu_string.find('lidar', index)
#         all_cpu_string[index: index + 100]
#         if index == -1:
#             break
#         lidar = '\n' + all_cpu_string[index:index +100]
#         index += 1
#
#     #
#     # for line in lines:
#     #     # print(html_string)
#     #     if line.find("lidar"):
#     #         lidar += '\n' + line
#     #     # print(power)
#     #
#     #     # print(power)
#     #     # lidar += '\n' + ((html_string[power - 80:power + 15]))
#     #
#     #     # print(html_string[power-95: power - 90])
#     #
#     #
#
#     print(lidar)
