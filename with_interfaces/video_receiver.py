# -----------------------------------------------------------------------------
# Copyright (C) 2019-2020 The python-ndn authors
#
# This file is part of python-ndn.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------
import logging
import time

import ndn.utils
from ndn.app import NDNApp
from ndn.types import InterestNack, InterestTimeout, InterestCanceled, ValidationFailure
from ndn.encoding import Name, Component, InterestParam
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import numpy as np

global start_time, start_time_data_received, dt_data_received, MB
start_time = time.time()
start_time_data_received = time.time()
dt_data_received = []
MB = []
logging.basicConfig(format='[{asctime}]{levelname}:{message}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    style='{')

app = NDNApp()


async def main():
    global start_time, start_time_data_received, dt_data_received
    MB = 0
    while True:
        try:
            timestamp = ndn.utils.timestamp()
            name = Name.from_str('/trailer/cam') #+ [Component.from_timestamp(timestamp)]
            data_name, meta_info, content = await app.express_interest(
                name, validator=None, no_signature=True) #must_be_fresh=True, can_be_prefix=False, lifetime=6000)
            # print(bytes(content))
            MB += len(content)
            # time.sleep(10 / 1000)
            print(len(content))
            rx_img_int = np.frombuffer(bytes(content), dtype=np.uint8)
            frame_final = cv2.imdecode(rx_img_int, cv2.IMREAD_COLOR)
            # cv2.imshow("Received video", frame_final) # does not show on ssh
            cv2.waitKey(0)


        except InterestNack as e:
            print(f'Nacked with reason={e.reason}')
        except InterestTimeout:
            print(f'Timeout')
        except InterestCanceled:
            print(f'Canceled')
        except ValidationFailure:
            print(f'Data failed to validate')

        dt_data_received.append((time.time() - start_time_data_received) * 1000)
        start_time_data_received = time.time()
        if (time.time() - start_time) >= (1 * 60):
            print(dt_data_received)
            logfilename_tcp_rx = "video_rx_dt_" + str(time.time_ns()) + ".log"
            with open(logfilename_tcp_rx, "a") as log1:
                log1.write("video_RX_Delta_time" + "\n")
                for ii in range(1, int(len(dt_data_received))):
                    log1.write(str(dt_data_received[ii]) + "\n")
                log1.close()
            frames_plt = list(range(0, len(dt_data_received[5:])))
            frames_plt = [x / 1000 for x in frames_plt]

            plt.figure(figsize=(10, 8))
            plt.subplot(1, 2, 1)
            plt.scatter(frames_plt, dt_data_received[5:])
            plt.xlabel('NDN Data Packet Number (in thousands)')
            plt.ylabel('Delta time (in ms): Received video bytes over NDN Data Packets')

            plt.subplot(1, 2, 2)
            plt.boxplot(dt_data_received[5:])
            plt.savefig("video_dt_data_tx_box_" + str(time.time_ns()) + ".png")
            print("Data RX Ended...going to sleep")
            dt_data_received_pd = pd.DataFrame(dt_data_received[5:])
            logfilename_lidar_rx_summ = "video_rx_dt_" + str(time.time_ns()) + ".log"
            with open(logfilename_lidar_rx_summ, "a") as log2:
                log2.write("summ_video_RX_dt_summary" + "\n")
                log2.write(str(dt_data_received_pd.describe()) + "\n")
                log2.close()
            print(dt_data_received_pd.describe())
            print(MB, 'bytes')
            print(MB / 1000000, 'MB')
            print(((MB/1000000)*8)/(40 * 60), 'Mbps')

            time.sleep(60 * 60)
            app.shutdown()


if __name__ == '__main__':
    app.run_forever(after_start=main())
