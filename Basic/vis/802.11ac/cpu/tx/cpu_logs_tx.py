import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.size'] = 14
plt.figure(figsize=(10,10))
# #
# processes = {"lidar_sender.py": {"cpu_values": []},
#              "cam_sender.py": {"cpu_values": []},
#              "can_sender.py": {"cpu_values": []},
#              "nfd.conf": {"cpu_values": []}}
# #________________________NDN UDP (BYTES)_________________________________
# # Open the text file and read its content
# with open("pc_tx_ndn_cpu_s_tcp.log", "r") as file:
#     for i, line in enumerate(file):
#         for process in processes:
#             if process in line:
#                 values = line.split()
#                 processes[process]["cpu_values"].append(float(values[2]))
#
# # Plot the CPU values
# for process in processes:
#     if process == "lidar_sender.py":
#         plt.plot( processes[process]["cpu_values"], label="LiDAR NDN UDP (B)", linewidth = 2, linestyle=':')
#     elif process == "cam_sender.py":
#         plt.plot( processes[process]["cpu_values"], label="CAM NDN UDP (B)", linewidth = 2, linestyle=':')
#     elif process == "can_sender.py":
#         plt.plot( processes[process]["cpu_values"], label="CAN NDN UDP (B)", linewidth = 2, linestyle=':')
#     elif process == "nfd.conf":
#         plt.plot( processes[process]["cpu_values"], label="NFD UDP (B)", linewidth = 2, linestyle=':')
# # plt.show()
# # plt.legend()
# #
# #________________________NDN TCP (BYTES)_____________________-------
# processes = {"lidar_sender.py": {"cpu_values": []},
#              "cam_sender.py": {"cpu_values": []},
#              "can_sender.py": {"cpu_values": []},
#              "nfd.conf": {"cpu_values": []}}
#
# with open("pc_tx_ndn_cpu_b_tcp.log", "r") as file:
#     for i, line in enumerate(file):
#         for process in processes:
#             if process in line:
#                 values = line.split()
#                 processes[process]["cpu_values"].append(float(values[2]))
#
# # Plot the CPU values
# for process in processes:
#     if process == "lidar_sender.py":
#         plt.plot( processes[process]["cpu_values"], label="LiDAR NDN TCP (B)", linestyle='-.', linewidth = 2)
#     elif process == "cam_sender.py":
#         plt.plot( processes[process]["cpu_values"], label="CAM NDN TCP (B)", linestyle='-.', linewidth = 2)
#     elif process == "can_sender.py":
#         plt.plot( processes[process]["cpu_values"], label="CAN NDN TCP (B)", linestyle='-.', linewidth = 2)
#     elif process == "nfd.conf":
#         plt.plot( processes[process]["cpu_values"], label="NFD TCP (B)", linestyle='-.', linewidth = 2)

#________________________NDN TCP (STRING)_____________________-------
processes = {"lidar_sender.py": {"cpu_values": []},
             "cam_sender.py": {"cpu_values": []},
             "can_sender.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}}

with open("pc_tx_ndn_cpu_s_tcp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "lidar_sender.py":
        plt.plot( processes[process]["cpu_values"], label="LiDAR NDN TCP (S)", dashes=[2, 2, 10, 2], linewidth = 2)
    elif process == "cam_sender.py":
        plt.plot( processes[process]["cpu_values"], label="CAM NDN TCP (S)", dashes=[2, 2, 10, 2], linewidth = 2)
    elif process == "can_sender.py":
        plt.plot( processes[process]["cpu_values"], label="CAN NDN TCP (S)", dashes=[2, 2, 10, 2], linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="NFD TCP (S)", dashes=[2, 2, 10, 2], linewidth = 2)
print(processes[process]["cpu_values"])

# plt.show()
# plt.legend()
#________________________NDN UDP (STRING)_________________________________
# Open the text file and read its content
processes = {"lidar_sender.py": {"cpu_values": []},
             "cam_sender.py": {"cpu_values": []},
             "can_sender.py": {"cpu_values": []},
             "nfd.conf": {"cpu_values": []}}
with open("pc_tx_ndn_cpu_s_udp.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "lidar_sender.py":
        plt.plot( processes[process]["cpu_values"], label="LiDAR NDN UDP (S)", linewidth = 2)
    elif process == "cam_sender.py":
        plt.plot( processes[process]["cpu_values"], label="CAM NDN UDP (S)", linewidth = 2)
    elif process == "can_sender.py":
        plt.plot( processes[process]["cpu_values"], label="CAN NDN UDP (S)", linewidth = 2)
    elif process == "nfd.conf":
        plt.plot( processes[process]["cpu_values"], label="NFD UDP (S)", linewidth = 2)

#_________________DDS____________________--

processes = {"lidar_sender.py": {"cpu_values": []},
             "cam_sender.py": {"cpu_values": []},
             "CAN_sender.py": {"cpu_values": []}}

with open("pc_tx_dds_wireless.log", "r") as file:
    for i, line in enumerate(file):
        for process in processes:
            if process in line:
                values = line.split()
                processes[process]["cpu_values"].append(float(values[2]))

# Plot the CPU values
for process in processes:
    if process == "lidar_sender.py":
        plt.plot( processes[process]["cpu_values"], label="LiDAR DDS", linestyle = '--', linewidth = 2)
    elif process == "cam_sender.py":
        plt.plot( processes[process]["cpu_values"], label="CAM DDS", linestyle = '--', linewidth = 2)
    elif process == "CAN_sender.py":
        plt.plot( processes[process]["cpu_values"], label="CAN DDS", linestyle = '--', linewidth = 2)


















plt.xlabel("Time in Seconds")
plt.ylabel("CPU %")
plt.title("CPU Consumption Percentage at the transmitter")

# plt.legend( bbox_to_anchor=(0.3,0.3) ,ncol=4, loc = 'best') # ,
plt.legend()
plt.show()
#
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
