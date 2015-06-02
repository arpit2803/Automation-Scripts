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
            #formaing final text to display
            first_line_text = left_side_data[0:2] + right_side_data[1:3]
            print first_line_text
            second_line_text = left_side_data[-3:-1] + right_side_data[-2:]
            print second_line_text

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
            print right_side_data[-3] + "  aaaaa"
            second_line = left_side_data[2] + "(" + left_side_data[-1] + ")" + "\t" + "\t" + right_side_data[0] + "(" + right_side_data[-3] + ")"
            final_text = second_line + "\n" + "------------------------------------------------------" + "\n" + final_text
            print final_text
                
            balloon_tip(first_line, final_text)       
                
            
##            Batting_Team = soup.find("div",{"class":"ssr-live-card-right-team-name ssr-live-card-right-team-name_178031"})
##            Bowling_Team = soup.find("div",{"class":"ssr-live-card-left-team-name bowling-team ssr-live-card-left-team-name_178031"})
##            print Batting_Team
##            print Batting_Team
##            First_Line = str(Batting_Team.text) + " vs " + str(Bowling_Team.text) + "\n"
##            print First_Line
##            batting_player_stricker = soup.find("span",{"class":"ssr-live-card-player-name ssr-live-card-left-player-name-top-row_178031"})
##            batting_player_stricker_score = soup.find("span",{"class":"ssr-live-card-player-stats ssr-live-card-left-player-stats-top-row_178031"})
##            score = soup.find("span",{"class":"ssr-live-card-left-team-total-run ssr-live-card-left-team-total-run_178031"})
##            current_bowler_name = soup.find("span",{"class":"ssr-live-card-player-name ssr-live-card-right-player-name-top-row_178031"})
##            current_bowler_figures = soup.find("span",{"class":"ssr-live-card-player-stats ssr-live-card-right-player-stats-top-row_178031"})
##            
##            stricker_batting = batting_player_stricker.text.encode("utf-8")
##            final_stricker = re.sub(r'[^\w]', ' ', stricker_batting)
##
##            stricker_bowler = current_bowler_name.text.encode("utf-8")
##            final_bowler = re.sub(r'[^\w]', ' ', stricker_bowler)
##            Second_Line_Text = final_stricker.encode("utf-8") + " " + batting_player_stricker_score.text.encode("utf-8") + "\t" + score.text.encode("utf-8") + "\t" + final_bowler.encode("utf-8") + " " + current_bowler_figures.text.encode("utf-8") + "\n"
##            
##                          
##            batting_player_non_stricker = soup.find("span",{"class":"ssr-live-card-player-name ssr-live-card-left-player-name_178031"})
##            batting_player_non_stricker_score = soup.find("span",{"class":"ssr-live-card-player-stats ssr-live-card-left-player-stats_178031"})
##            overs = soup.find("span",{"class":"ssr-live-card-left-team-overs ssr-live-card-left-team-overs_178031"})
##            second_bowler_name = soup.find("span",{"class":"ssr-live-card-player-name ssr-live-card-right-player-name_178031"})
##            second_bowler_figures = soup.find("span",{"class":"ssr-live-card-player-stats ssr-live-card-right-player-stats_178031"})
##
##            #Third_Line_Text = str(batting_player_non_stricker.text.encode("utf-8")) + ' ' + str(batting_player_non_stricker_score.text.encode("utf-8")) + "\t" + str(overs.text.encode("utf-8")) + "\t" + str(second_bowler_name.text.encode("utf-8")) + ' ' + str(second_bowler_figures.text.encode("utf-8"))
##            Third_Line_Text = batting_player_non_stricker.text.encode("utf-8") + " " + batting_player_non_stricker_score.text.encode("utf-8") + "  " + overs.text.encode("utf-8") + "  " + second_bowler_name.text.encode("utf-8") + " " + second_bowler_figures.text.encode("utf-8")
##
##            Final_String  = First_Line + Second_Line_Text + Third_Line_Text
##            
##            #fielding_team = soup.find("div",{"class":"ssr-mc-slot-right-teams-name"})
##            #between_team = str(batting_team.text) + " vs " + str(fielding_team.text)
##            #item2 = between_team + "\n"
##            #for item in soup.find_all("div",{"class":"ssr-mc-slot-match-status-concluded"}):
##            #    item2 = item2 + item.text.encode("utf-8") + "\n"
            #balloon_tip("Match Status", Final_String)
            
if __name__ == '__main__':
        display_again()
        

