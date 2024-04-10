@echo off
setlocal enabledelayedexpansion

title Reduce Image File Size

echo Never put the output folder same as input folder, if you do then you will loose all the images.
REM Prompt user to input input and output folders
set /p input_folder="Enter the path to the input folder: "
set /p output_folder="Enter the path to the output folder: "

REM Check if input folder exists
if not exist "%input_folder%" (
    echo Input folder does not exist. Exiting...
    exit /b
)

REM Check if output folder exists, if not create it
if not exist "%output_folder%" (
    mkdir "%output_folder%"
)

REM Loop through images in the input folder
for %%i in ("%input_folder%\*.*") do (
    REM Check if the file is an image (assuming it has .jpg extension, you can adjust as needed)
    if /i "%%~xi"==".jpg" (
        REM Perform image compression using cjpeg
        cjpeg -quality 95 "%%i" > "%output_folder%\%%~nxi"
        echo Processed: %%i
    )
)

echo Image compression completed.
pause
