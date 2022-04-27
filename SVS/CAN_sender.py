#    @Author: Justin C Presley
#    @Author-Email: justincpresley@gmail.com
#    @Project: NDN State Vector Sync Protocol
#    @Source-Code: https://github.com/justincpresley/ndn-python-svs
#    @Pip-Library: https://pypi.org/project/ndn-svs
#    @Documentation: https://ndn-python-svs.readthedocs.io


# Basic Libraries
import logging
import sys
from argparse import ArgumentParser, SUPPRESS
from typing import List, Callable, Optional
# NDN Imports
from ndn.encoding import Name
from Crypto.Cipher import AES # + pip3 install pycryptodome


# Custom Imports
sys.path.insert(0, '.')
from src.ndn.svs import SVSyncShared_Thread, SVSyncBase_Thread, SVSyncLogger, MissingData, AsyncWindow
import time
from random import randrange
import datetime
import numpy as np
import time
import base64


global seg
seg = 7500
global fps1
fps1 =0

global secret_key
secret_key = b'\x95S)\x93\x93)\xa0\xae\xf8\x9fuY\xec\xec\xdf\xd4]<\xb2\x00Y\xcdr}\x17U/\x1e\xb1\xe62\xac'
global iv
iv = b'\xa7S\x94{\x8c\xdf\x81E\xc5i}j\xa8\r~'

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
    taskwindow = AsyncWindow(10)

    async def wrapper(missing_list: List[MissingData]) -> None:
        async def missingfunc(nid: Name, seqno: int) -> None:
            content_str: Optional[bytes] = await thread.getSVSync().fetchData(nid, seqno, 2)
            if content_str:
                print(content_str)

        for i in missing_list:
            while i.lowSeqno <= i.highSeqno:
                taskwindow.addTask(missingfunc, (Name.from_str(i.nid), i.lowSeqno))
                i.lowSeqno = i.lowSeqno + 1

    return wrapper


class Program:
    def __init__(self, args: dict) -> None:
        self.args = args
        self.svs_thread: SVSyncShared_Thread = SVSyncShared_Thread(Name.from_str(self.args["group_prefix"]),
                                                                   Name.from_str(self.args["node_id"]), on_missing_data,
                                                                   self.args["cache_data"])
        self.svs_thread.daemon = True
        self.svs_thread.start()
        self.svs_thread.wait()
        print(f'SVS sender started, group id is {self.args["group_prefix"]} and node id is {self.args["node_id"]}')

    def run(self) -> None:

        start_time_fps_mbps = time.time()
        f_n = 0
        global seg
        global fps1
        global secret_key
        global iv
        msgs_matrix = []
        while True:
            try:
                for i in range(162):  # generate 400 values to convert to bytes --> to simulate fresh CAN data
                    msgs_matrix.append(randrange(256))
                msgs_matrix_bytes = bytes(msgs_matrix)
                aes_obj = AES.new(secret_key, AES.MODE_OCB, iv)
                secret_key = b'\x95S)\x93\x93)\xa0\xae\xf8\x9fuY\xec\xec\xdf\xd4]<\xb2\x00Y\xcdr}\x17U/\x1e\xb1\xe62\xac'
                iv = b'\xa7S\x94{\x8c\xdf\x81E\xc5i}j\xa8\r~'
                [encrypted_payload, tag] = aes_obj.encrypt_and_digest(msgs_matrix_bytes)  # the jpg frame + CAN bytes

                message = encrypted_payload + tag

                self.svs_thread.publishData(message)
                #time.sleep(5 / 1000)
                val = []
                message = []
                msgs_matrix = []
                msgs_matrix_bytes = b''


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
