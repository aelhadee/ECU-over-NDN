#    @Author: Justin C Presley
#    @Author-Email: justincpresley@gmail.com
#    @Project: NDN State Vector Sync Protocol
#    @Source-Code: https://github.com/justincpresley/ndn-python-svs
#    @Pip-Library: https://pypi.org/project/ndn-svs
#    @Documentation: https://ndn-python-svs.readthedocs.io

# Basic Libraries
import logging
import sys
import os
from argparse import ArgumentParser, SUPPRESS
from typing import List, Callable, Optional
# NDN Imports
from ndn.encoding import Name
import numpy as np
import time
import base64
from Crypto.Cipher import AES  # pip3 install pycryptodome

# Custom Imports
sys.path.insert(0, '.')
from src.ndn.svs import SVSyncShared_Thread, SVSyncBase_Thread, SVSyncLogger, MissingData, AsyncWindow

fps, st, frames_to_count, cnt = (0, 0, 20, 0)
global t, e, rx_bytes, seg_cont, secret_key, iv, decrypted_rx_bytes, dt_data_received, start_time_data_received, frame_number, max_frames
rx_bytes = b''
seg_cont = 0
secret_key = b'\x95S)\x93\x93)\xa0\xae\xf8\x9fuY\xec\xec\xdf\xd4]<\xb2\x00Y\xcdr}\x17U/\x1e\xb1\xe62\xac'
iv = b'\xa7S\x94{\x8c\xdf\x81E\xc5i}j\xa8\r~'
import matplotlib.pyplot as plt
decrypted_rx_bytes = 0
dt_data_received = []
start_time_data_received = time.time()
frame_number = 0
max_frames = 1 * 1000

while True:

    def parse_cmd_args() -> dict:
        # Command Line Parser
        parser = ArgumentParser(add_help=False, description="An SVS Chat Node capable of syncing with others.")
        requiredArgs = parser.add_argument_group("required arguments")
        optionalArgs = parser.add_argument_group("optional arguments")
        informationArgs = parser.add_argument_group("information arguments")
        # Adding all Command Line Arguments
        requiredArgs.add_argument("-n", "--nodename", action="store", dest="node_name", required=True,
                                  help="id of this node in svs")
        optionalArgs.add_argument("-gp", "--groupprefix", action="store", dest="group_prefix", required=False,
                                  help="overrides config | routable group prefix to listen from")
        informationArgs.add_argument("-h", "--help", action="help", default=SUPPRESS,
                                     help="show this help message and exit")
        # Getting all Arguments
        argvars = parser.parse_args()
        args = {}
        args["group_prefix"] = argvars.group_prefix if argvars.group_prefix is not None else "/svs"
        args["node_id"] = argvars.node_name
        return args


    def on_missing_data(thread: SVSyncBase_Thread) -> Callable:
        taskwindow = AsyncWindow(10)  # original 10

        async def wrapper(missing_list: List[MissingData]) -> None:
            async def missingfunc(nid: Name, seqno: int) -> None:
                global t,rx_bytes, seg_cont, decrypted_rx_bytes
                global dt_data_received, start_time_data_received, frame_number, max_frames
                content_str: Optional[bytes] = await thread.getSVSync().fetchData(nid, seqno, 2)  # data rx, orig 2

                if content_str:
                    lidar_bytes = content_str[:1970]
                    tag = content_str[1970:1970 + 16]
                    aes_obj = AES.new(secret_key, AES.MODE_OCB, iv)
                    try:
                        decrypted_rx_bytes = aes_obj.decrypt_and_verify(lidar_bytes, tag)
                        lidar_rx_bytes = decrypted_rx_bytes[:1970]
                        print('authentic', time.time())

                    except:
                        print("not authentic or something went wrong with the rx data")
                        
                    dt_data_received.append((time.time() - start_time_data_received) * 1000)
                    start_time_data_received = time.time()
                    if frame_number == max_frames:
                        print(dt_data_received)
                        logfilename_tcp_rx = "lidar_rx_dt_" + str(time.time_ns()) + ".log"
                        with open(logfilename_tcp_rx, "a") as log1:
                            log1.write("Lidar_RX_Delta_time" + "\n")
                            for ii in range(1, int(len(dt_data_received))):
                                log1.write(str(dt_data_received[ii]) + "\n")
                            log1.close()
                        frames_plt = list(range(1, len(dt_data_received)))
                        plt.figure(figsize=(8,6))
                        plt.subplot(1, 2, 1)
                        plt.scatter(frames_plt, dt_data_received[1:])
                        plt.xlabel('NDN Data Packet Number')
                        plt.ylabel('Delta time (in ms): Received LiDAR bytes over NDN Data Packet')

                        plt.subplot(1, 2, 2)
                        plt.boxplot(dt_data_received[1:])
                        plt.savefig("dt_data_tx_box_" + str(time.time_ns())+".png")
                        print("Data RX Ended...going to sleep")
                        dt_data_received_pd = pd.DataFrame(dt_data_received[1:])
                        logfilename_lidar_rx_summ = "Lidar_rx_dt_" + str(time.time_ns()) + ".log"
                        with open(logfilename_lidar_rx_summ, "a") as log2:
                            log2.write("lidar_RX_dt_summary" + "\n")
                            log2.write(str(dt_data_received_pd) + "\n")
                            log2.close()
                        print(dt_data_received_pd.describe())
                        time.sleep(1000)

                    frame_number += 1    
                    img_bytes = b''
                    seg_cont = 0
                    content_str = []
                    lidar_bytes = b''
                t = t + 1

            for i in missing_list:
                while i.lowSeqno <= i.highSeqno:
                    taskwindow.addTask(missingfunc, (Name.from_str(i.nid), i.lowSeqno))
                    i.lowSeqno = i.lowSeqno + 1

        return wrapper


    class Program:
        def __init__(self, args: dict) -> None:
            self.args = args
            self.svs_thread: SVSyncShared_Thread = SVSyncShared_Thread(Name.from_str(self.args["group_prefix"]),
                                                                       Name.from_str(self.args["node_id"]),
                                                                       on_missing_data, self.args["cache_data"])
            self.svs_thread.daemon = True
            self.svs_thread.start()
            self.svs_thread.wait()
            print(f'SVS receiver started | {self.args["group_prefix"]} - {self.args["node_id"]} |')

        def run(self) -> None:
            while True:
                try:
                    val: str = input("")
                    sys.stdout.write("\033[F" + "\033[K")
                    sys.stdout.flush()
                    if val != "":
                        print(val)
                        self.svs_thread.publishData(val.encode())
                except KeyboardInterrupt:
                    sys.exit()


    def main() -> int:
        args = parse_cmd_args()

        args["node_id"] = Name.to_str(Name.from_str(args["node_id"]))
        args["group_prefix"] = Name.to_str(Name.from_str(args["group_prefix"]))
        args["cache_data"] = False

        SVSyncLogger.config(False, None, logging.INFO)

        prog = Program(args)
        prog.run()

        return 0


    if __name__ == "__main__":
        sys.exit(main())
