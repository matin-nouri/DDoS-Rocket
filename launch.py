#!/bin/python3

import models.launcher as launcherlib

print(
    """MIT License

Copyright (c) 2024 Matin Nouri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")

host = input("Host : ")
port = int(input("Port : "))

launcher = launcherlib.Launcher(host,port)

message = "Turning On the Launcher Machine"
try:
    print(f"\033[1;33m[Pending] \033[0;0m{message}",end="\r")
    launcher.launch()
    print(f"\033[0;32m[Done] \033[0;0m{message}   ",end="\n")
except:
    print(f"\033[0;31m[Failed] \033[0;0m{message}    ",end="\n")