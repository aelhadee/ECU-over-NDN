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
import random
import string 

logging.basicConfig(format='[{asctime}]{levelname}:{message}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    style='{')

app = NDNApp()

# population = string.ascii_letters + string.digits
# population *= (8600 // len(population)) + 1

@app.route('/cam')
def on_interest(name: FormalName, param: InterestParam, _app_param: Optional[BinaryStr]):
    # print(f'>> I: {Name.to_str(name)}, {param}')
    content = os.urandom(4000)

    # content = ''.join(random.sample(population, 4000))

    app.put_data(name, content=content, no_signature=True) #freshness_period=10000)
    time.sleep(20 / 1000)


if __name__ == '__main__':
    app.run_forever()