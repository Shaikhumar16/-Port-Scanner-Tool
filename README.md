Port Scanner Tool



This is a Python-based port scanner I built to identify open TCP ports on a target system.  

It’s fast, easy to use, and even tries to grab banners from open ports so you can get an idea of the service running behind them.  

Think of it as a simple but effective tool for network reconnaissance.



---



\#Features

-Custom Port Range — Scan only the ports you care about

-Multi-threaded Scanning — Much faster than scanning one port at a time

-Banner Grabbing — Shows basic info about the service on an open port

-Error Handling — Handles unreachable hosts, closed ports, and timeouts smoothly

-Lightweight — No external dependencies; runs on any system with Python installed



---



\#Tech Stack

-Language: Python 

-Libraries: 

&nbsp; -socket (built-in) for TCP connections  

&nbsp; -concurrent.futures` (built-in) for multi-threading



---



\#How to Run

1.Clone this repository\*\*

&nbsp;  -bash

&nbsp;  git clone https://github.com/Shaikhumar16/-Port-Scanner-Tool.git



