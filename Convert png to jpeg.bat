@echo off
setlocal enabledelayedexpansion

title Convert PNG to JPG

echo To use this tool, install MozJPEG from its website or github(open source). You may need to add it to environment variable.
echo You can adjust image quality (default 98).
echo(
set /p "inputFolder=Enter the path to the input folder: "
set /p "outputFolder=Enter the path to the output folder: "

if not exist "%inputFolder%" (
    echo Input folder "%inputFolder%" not found.
    pause
    exit /b
)

if not exist "%outputFolder%" (
    mkdir "%outputFolder%"
)

for %%f in ("%inputFolder%\*.png") do (
    set "filename=%%~nf.jpg"
    cjpeg -quality 100 "%%f" > "%outputFolder%\!filename!"
    echo Converted "%%f" to "!filename!"
)

echo All PNG files converted to JPEG format.
pause
