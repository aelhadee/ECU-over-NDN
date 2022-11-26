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
import time
from typing import Optional
from ndn.app import NDNApp
from ndn.encoding import Name, InterestParam, BinaryStr, FormalName, MetaInfo
import logging
import os
import cv2
import imutils
import struct

logging.basicConfig(format='[{asctime}]{levelname}:{message}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    style='{')

app = NDNApp()
vid_obj = cv2.VideoCapture(4)
# 0 - colored webcam
# 2 - grayscale 
# 4 & 5 - USB webcam 
print('.')
print('.')
print('Waiting for interest packets for /trailer/cam...')

# vid_obj = cv2.VideoCapture(2)
@app.route('/trailer/cam')
def on_interest(name: FormalName, param: InterestParam, _app_param: Optional[BinaryStr]):
    try:
        
        # print(f'>> I: {Name.to_str(name)}, {param}')
        ret, frame = vid_obj.read()

        # frame = imutils.resize(frame, width=449)
        cv2.imshow("Transmitting...", frame)

        # e, tx_img = cv2.imencode(".png", frame)  # encoding each frame into an image
        e, tx_img = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY,70])  # encoding each frame into an image
        img_bytes = tx_img.tobytes()  # you can also try pickle

        print(len(img_bytes))

        #content = os.urandom(8000)
        app.put_data(name, content=img_bytes, no_signature=True) #freshness_period=10000)

        # time.sleep(20 / 1000)
        if cv2.waitKey(1) == ord('x'):
            print('something')
    except: 
        print('something went wrong')
if __name__ == '__main__':
    app.run_forever()