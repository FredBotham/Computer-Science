@echo off
start /min cmd /k "C:\Users\Fredd\Documents\Computer Science\ngrokstartup.bat"
if not exist "C:\Computer Science\php-server" mkdir "C:\Computer Science\php-server"
cd "c:\Computer Science\php-server"
php -S localhost:4567