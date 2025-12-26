@echo off
cd /d %~dp0
cd venv
cd Scripts
call activate
cd..
cd..
start python launch_kitty.py
	