import os
import subprocess
import webbrowser

webbrowser.open_new('https://developer.apple.com')
webbrowser.open_new('https://appleid.apple.com')
p = subprocess.Popen(["open", "-n", "/Applications/Utilities/Keychain Access.app"], stdout=subprocess.PIPE)
appName = "Application Loader"
p = subprocess.Popen(["open", "-n", "/Applications/Application Loader.app"], stdout=subprocess.PIPE)

