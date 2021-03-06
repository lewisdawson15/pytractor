# Copyright 2014 Konrad Podloucky
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

import logging
import os
import os.path
import signal
import SimpleHTTPServer
import SocketServer
import time

from .testserver import SimpleWebServerProcess

webserver_process = None


def setup_package():
    global webserver_process
    webserver_process = SimpleWebServerProcess()
    webserver_process.run()


def teardown_package():
    webserver_process.stop()
