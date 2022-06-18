@echo off

if not exist "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\TheEvilPuzwick.exe" (
if not exist "%appdata%\TheEvilPuzwick\" (

echo msgbox "TheEvilPuzwick non rilevato! Pc al sicuro!" > %tmp%\tmp.vbs
cscript /nologo %tmp%\tmp.vbs
del %tmp%\tmp.vbs
goto :EOF

)
)

del "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\TheEvilPuzwick.exe"
@RD /S /Q "%appdata%\TheEvilPuzwick\"
echo msgbox "TheEvilPuzwick e' stato rispedito nel suo barile! Pc al sicuro!" > %tmp%\tmp.vbs
cscript /nologo %tmp%\tmp.vbs
del %tmp%\tmp.vbs
