#!/bin/bash
Xvfb :99 -screen 0 1024x768x24 +extension GLX +render -noreset &
sleep 2
DISPLAY=:99 python main.py
