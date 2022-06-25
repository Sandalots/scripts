#!/bin/sh
# Update brew packages
# Clears shell history as well, then clears the screen buffer
brew update
brew upgrade
history -c
clear
