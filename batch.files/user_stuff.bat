@echo off
chcp 65001 >nul
title liam's devil plan
color 1f
 set /p pass="enter your password:"
 if %pass% NEQ liampom@24 exit

:menu

echo ----------------------
echo menu
echo ----------------------
echo 1) list users
echo 2) create a new user
echo 3) change a user password
echo 4) delete user account
echo 5) exit liam's devil plan
echo 6) nuke russia

set /p input="@"

if %input% EQU 1 (
	cls
	title users
	net user
	pause
	cls
	goto menu
)
	
if %input% EQU 2 (
	cls
	call:checkadmin
	title new user
	set /p username="username:"
	set /p password="password:"
	net user %username% %password% /add
	echo user created with credentials:
	echo %username% : %password%
	pause
	cls
	goto menu
)	
	
if %input% EQU 3 (
	cls
	call:checkadmin
	title pass changing
	set /p username="target user:"
	set /p password="new password:"
	net user %username% %password%
	pause
	cls
	goto menu
)
	
if %input% EQU 4 (
	cls
	title deleting an account
	set /p username= "target user:"
	net user %username% /delete
	echo youre a piece of shit for doing it
	pause 
	cls
	goto menu
)
	
if %input% EQU 5 (
	exit
)
	
if %input% EQU 6 ( 
	cls
	title countryy nuking
	echo russia has been sucessfully nuked
	echo --------------------------
	echo --------------------------
	echo --------------------------
	echo well if you look behind you you will notice an fbi agent ba bye 
	echo the pc is about to explode
	echo wait 1 minute
	pause
	timeout /1
	cls
	ECHO HI
	ECHO i
	ECHO EAT
	ECHO NIGGERS
	ECHO AND YOURE MOM'S HOT ASF
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	echo bom
	pause
	exit
	
)	

:checkadmin
net session >nul
if %errorlevel% NEQ 0 (
cls
echo. restart the script and run as adminstrator
)