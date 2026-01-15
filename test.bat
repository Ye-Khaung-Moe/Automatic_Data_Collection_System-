@echo off
cd /d "%~dp0"
echo [%date% %time%]


"C:\Users\skysk.LKK\AppData\Local\Programs\Python\Python314\python.exe" test.py

echo [%date% %time%] Done.
pause