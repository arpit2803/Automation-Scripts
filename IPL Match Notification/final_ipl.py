from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import requests
from bs4 import *
import re

class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = LoadImage(hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                          hicon, "Balloon  tooltip",msg,400,title))
        # self.show_balloon(title, msg)
        time.sleep(5)
        DestroyWindow(self.hwnd)
        classAtom = UnregisterClass(classAtom, hinst)
        time.sleep(30)
        display_again()
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.

def balloon_tip(title, msg):
    w=WindowsBalloonTip(title, msg)

def display_again():
        #while True:
            url = "http://www.starsports.com/cricket/index.html"
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.content,from_encoding="utf-8")
            item2 = ""
            full_content = soup.find("div",{"class":"ssr-live-card-inner"})
            #first line text
            full_contentss = full_content.findChildren()
            left_side_team = full_contentss[2].text
            
            right_side_team = full_contentss[7].text
            first_line = left_side_team + " vs " + right_side_team

            #second line text
            left_side_data = []
            left_side = soup.find("div",{"class":"ssr-live-card-left-container"})
            for tag in left_side.findChildren():
                if (len(tag.findChildren()) == 0):
                    left_side_data.append(tag.text)
            #third line text
            right_side_data = []
            right_side = soup.find("div",{"class":"ssr-live-card-right-container"})
            for tag in right_side.findChildren():
                if (len(tag.findChildren()) == 0):
                    right_side_data.append(tag.text)
            #forming final text to display
            first_line_text = left_side_data[0:2] + right_side_data[1:3]
            print first_line_text #for debugging
            second_line_text = left_side_data[-3:-1] + right_side_data[-2:]
            print second_line_text #for debugging

            final_list = first_line_text + second_line_text
            final_text = ''
            i = 0
            for item in final_list:
                i = i+1
                if i%2 == 0:
                    final_text = final_text + item.rjust(8) + "  "
                else:
                    final_text = final_text + item.ljust(17) + "  "
                if i == 4:
                    final_text = final_text + "\n"
            if not "overs" in right_side_data[-3]:
                right_side_data[-3] = "Yet to bat"
            print right_side_data[-3] #for debugging
            second_line = left_side_data[2] + "(" + left_side_data[-1] + ")" + "\t" + "\t" + right_side_data[0] + "(" + right_side_data[-3] + ")"
            final_text = second_line + "\n" + "------------------------------------------------------" + "\n" + final_text
            print final_text
                
            balloon_tip(first_line, final_text)       

            
if __name__ == '__main__':
        display_again()
        

