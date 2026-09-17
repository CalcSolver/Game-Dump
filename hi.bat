@echo off
color 0A
title SYSTEM BREACH - INITIALIZING...

echo Connecting to remote host...
ping 127.0.0.1 -n 2 >nul

echo Bypassing firewall rules...
ping 127.0.0.1 -n 2 >nul

echo Escalating privileges...
ping 127.0.0.1 -n 2 >nul

:loop
set /a r=%random% * %random%
echo [LOG] 0x%r% :: ACCESS_GRANTED :: CHANNEL_OPEN
goto loop
