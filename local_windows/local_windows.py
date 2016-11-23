import os


class LocalWindows:
    def __init__(self):
        return
    def browse_webpage(self,url):
        os.system('chrome.exe '+url)