# Copyright 2015 gRPC authors.
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
"""The Python implementation of the GRPC helloworld.Greeter server."""
import argparse
import logging
from concurrent import futures
import grpc
import function_pb2
import function_pb2_grpc
from function import main

port = '3000'
function_name = "functionA"
max_workers = 5


class HandleEvent(function_pb2_grpc.HandleEventServicer):

    def ProcessEvent(self, request, context):
        # 动态导入模块
        # module_object = importlib.import_module(function_name)

        # 调用handler
        receive = main.handler(context, request)

        return function_pb2.Reply(body=receive)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    function_pb2_grpc.add_HandleEventServicer_to_server(HandleEvent(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


def parse_args():
    parser = argparse.ArgumentParser(description='function parameter')
    parser.add_argument("-fn", "--function", action="store", dest="function", type=str, required=True,
                        help="runnable function file")
    parser.add_argument("-p", "--port", action="store", dest="port", default="3000", type=int, required=True,
                        help="function port= [%(default)s].")
    parser.add_argument("-m", "--max_workers", action="store", dest="max_workers", default="5", type=int,
                        help="max workers= [%(default)s].")
    parameter = parser.parse_args()
    global function_name, port, max_workers
    function_name = parameter.function
    port = str(parameter.port)
    max_workers = parameter.max_workers


if __name__ == '__main__':
    logging.basicConfig()
    parse_args()
    serve()
