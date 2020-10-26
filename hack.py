from voice import voice
import pyautogui
import time
import os
import subprocess
from records import record,first_record,second_record,third_record
# start recording here
# pro=record()
# pyautogui.moveTo(38,186)# vscode
# pyautogui.click()
# voice("ok, let's now create a hack application open your vscode",1)
# time.sleep(3)
# first_record(pro)
# pro=record()
# voice("create a project using terminal, let's name it appwrite-sdk-hack",1)
# time.sleep(3)
# pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
# pyautogui.click()
# pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
# pyautogui.click()
# pyautogui.hotkey("alt","shift","=")
# pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
# pyautogui.click()
# pyautogui.write("mkdir appwrite-sdk-hack", interval=0.1)
# pyautogui.press("enter")
# second_record(pro)
# pro=record()
# pyautogui.hotkey("alt","shift","-")
# voice("now open it up in vscode",1)
# time.sleep(3)
# pyautogui.click(101,80,duration=1, tween=pyautogui.easeInOutQuad)
# time.sleep(1)
# pyautogui.click(171,265,duration=1, tween=pyautogui.easeInOutQuad)
# time.sleep(1)
# pyautogui.doubleClick(396,171,duration=1, tween=pyautogui.easeInOutQuad)
# time.sleep(1)
# pyautogui.click(1216,46,duration=1, tween=pyautogui.easeInOutQuad)
# time.sleep(1)
# pyautogui.write("appwrite-sdk-hack",interval=0.1)
# time.sleep(1)
# pyautogui.doubleClick(479,147,duration=1, tween=pyautogui.easeInOutQuad)
# time.sleep(1)
# pyautogui.click(1269,47,duration=1, tween=pyautogui.easeInOutQuad)
# time.sleep(1)
# third_record(pro)
# pro=record()
# voice("after you open your project let's setup our hack programming language first, first of all create . h h config",1)
# time.sleep(3)
# pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
# pyautogui.click()
# pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
# pyautogui.click()
# pyautogui.hotkey("alt","shift","=")
# pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
# pyautogui.click()
# pyautogui.write("cd appwrite-sdk-hack", interval=0.1)
# pyautogui.press("enter")
# time.sleep(1)
# pyautogui.write("curl https://raw.githubusercontent.com/hhvm/hhast/master/.hhconfig > .hhconfig", interval=0.1)
# pyautogui.press("enter")
# time.sleep(1)
# second_record(pro)
# pro=record()
# voice("now let's create s r c folder for our s d k library and tests folder to test our library",1)
# time.sleep(3)
# pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
# pyautogui.click()
# pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
# pyautogui.click()
# pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
# pyautogui.click()
# pyautogui.write("mkdir src tests", interval=0.1)
# pyautogui.press("enter")
# time.sleep(1)
# third_record(pro)
pro=record()
voice("create hh autoload json",1)
time.sleep(3)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("mkdir src tests", interval=0.1)
pyautogui.press("enter")
pyautogui.write("touch hh_autoload.json", interval=0.1)
pyautogui.press("enter")
time.sleep(1)
second_record(pro)
pro=record()
voice("open your hh autoload . json and write this",1)
time.sleep(3)
pyautogui.hotkey("alt","shift","-")
pyautogui.hotkey("ctrl","p")
time.sleep(1)
pyautogui.write("hh_autoload.json", interval=0.1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("alt","shift","=")
pyautogui.click(1265,280,duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.hotkey("ctrl","a")
pyautogui.write("""
{
  "roots": [
    "src/"
  ],
  "devRoots": [
    "tests/"
  ],
  "devFailureHandler": "Facebook\\\\AutoloadMap\\\\HHClientFallbackHandler"
}
""",interval=0.1)
time.sleep(2)
third_record(pro)
pro=record()
voice("let's download the dependency for our hack apps",1)
time.sleep(3)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("composer require hhvm/hsl hhvm/hhvm-autoload", interval=0.1)
pyautogui.press("enter")
time.sleep(10)
second_record(pro)
pro=record()
voice("now let's create our client object, what this does is, it encapsulate method call, which we will use later, to access the appwrite server",1)
time.sleep(2)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("wget https://raw.githubusercontent.com/spiritbro1/sdk-for-hack/main/src/client.hack -O src/client.hack", interval=0.1)
pyautogui.press("enter")
time.sleep(3)
third_record(pro)
pro=record()
voice("create services folder so that we can get the services that we want from appwrite server, for now we use health service api to check if the server is ok or no",1)
time.sleep(2)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("mkdir src/services", interval=0.1)
pyautogui.press("enter")
time.sleep(3)
second_record(pro)
pro=record()
voice("let's download the file that i create earlier for the health api service",1)
time.sleep(2)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("wget https://raw.githubusercontent.com/spiritbro1/sdk-for-hack/main/src/services/health.hack -O src/services/health.hack", interval=0.1)
pyautogui.press("enter")
time.sleep(3)
third_record(pro)
pro=record()
voice("now let's create index . hack and lets use the library that we create earlier to access the appwrite server hack api",1)
time.sleep(3)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("touch index.hack", interval=0.1)
pyautogui.press("enter")
pyautogui.hotkey("ctrl","p")
time.sleep(1)
pyautogui.hotkey("alt","shift","-")
pyautogui.write("index.hack", interval=0.1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("alt","shift","=")
pyautogui.click(1265,280,duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.hotkey("ctrl","a")
pyautogui.write(r"""
<<__EntryPoint>>
function main(): void {
 require_once(__DIR__.'/vendor/autoload.hack');
  \Facebook\AutoloadMap\initialize();
  

$client = new Health();
$client->setProject("5f91246e2dfcd");
$client->setKey("0ba7d715d05357762b6e81b158df7242aea2ab4237dbe9e8bbd8870a27b2bb85666ccc567cbeaaf97bf2272217bbc966d5908611f05069f7031f0783e87d6136038ca6fc979af17a9b92333eec0acf34034646dd921d64f362a63af065e4a54e8bd8e69b8e01c819b6c27d9eba26b925563a2366641377c9ad505991668a2aa5");
$pum=\HH\Asio\join($client->get());
$hai=json_decode($pum)->status;
  echo $hai;
}
""",interval=0.1)
time.sleep(2)
second_record(pro)
pro=record()
pyautogui.hotkey("alt","shift","-")
voice("let's generate our h h v m auto load by running this command",1)
time.sleep(2)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("vendor/bin/hh-autoload", interval=0.1)
pyautogui.press("enter")
time.sleep(3)
third_record(pro)
pro=record()
voice("what we are trying to do now is accessing this health api from our hack apps",1)
time.sleep(2)
pyautogui.click(14,84,duration=1, tween=pyautogui.easeInOutQuad)
time.sleep(3)
second_record(pro)
pro=record()
voice("lets see it in action in insomnia first",1)
time.sleep(2)
pyautogui.click(4,324,duration=1, tween=pyautogui.easeInOutQuad)
time.sleep(3)
third_record(pro)
pro=record()
voice("so as you can see here i have setup all the necessary header to access our appwrite server when we call the api we will get status ok if our call is successful",1)
time.sleep(2)
pyautogui.click(847,104,duration=1, tween=pyautogui.easeInOutQuad)
time.sleep(3)
second_record(pro)
pro=record()
voice("let's go back to our vscode terminal and check if it will show the same result",1)
time.sleep(2)
pyautogui.hotkey("alt","shift","=")
pyautogui.click(49,203,duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
pyautogui.click()
pyautogui.moveTo(1042,492,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
pyautogui.click()
pyautogui.moveTo(1313,625,duration=1, tween=pyautogui.easeInOutQuad)# terminal vscode
pyautogui.click()
pyautogui.write("hhvm index.hack", interval=0.1)
pyautogui.press("enter")
time.sleep(3)
third_record(pro)
pro=record()
voice("as you can see here it show the same result as the api call in insomnia, i will put the link to full code in the description thank you for watching, see you again next time",1)
time.sleep(2)
pyautogui.hotkey("alt","shift","-")
second_record(pro)