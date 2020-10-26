import pyautogui
import time
import subprocess
import os
import signal

def first_record(pro):
    # line kebawah selesai recording
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM) 
    # pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
    # pyautogui.click()
    # pyautogui.moveTo(1076,473,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
    # pyautogui.click()
    time.sleep(3)
    cmd="ffmpeg -i 1.mp4 -i 1.mp3 -c:v copy -c:a aac final.mp4".split()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    fout = p.stdin
    fout.close()
    p.wait()
    os.remove("1.mp4")
    os.remove("1.mp3")
    print("merging audio video done")
def second_record(pro):
    # line kebawah selesai recording
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM) 
    # pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
    # pyautogui.click()
    # pyautogui.moveTo(1076,473,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
    # pyautogui.click()
    time.sleep(3)
    cmd="ffmpeg -i 1.mp4 -i 1.mp3 -c:v copy -c:a aac 2.mp4".split()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    fout = p.stdin
    fout.close()
    p.wait()
    cmd='ffmpeg -i final.mp4 -i 2.mp4 -filter_complex [0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a] -map [v] -map [a] output.mp4'.split()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    fout = p.stdin
    fout.close()
    p.wait()
    os.remove("1.mp4")
    os.remove("final.mp4")
    os.remove("2.mp4")
    os.remove("1.mp3")
    print("merging audio video done")

def third_record(pro):
    # line kebawah selesai recording
    
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM) 
    # pyautogui.moveTo(1090,459,duration=1, tween=pyautogui.easeInOutQuad)# selector terminal vscode
    # pyautogui.click()
    # pyautogui.moveTo(1076,473,duration=1, tween=pyautogui.easeInOutQuad)# ganti terminal
    # pyautogui.click()
    time.sleep(3)
    cmd="ffmpeg -i 1.mp4 -i 1.mp3 -c:v copy -c:a aac 2.mp4".split()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    fout = p.stdin
    fout.close()
    p.wait()
    cmd='ffmpeg -i output.mp4 -i 2.mp4 -filter_complex [0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a] -map [v] -map [a] final.mp4'.split()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    fout = p.stdin
    fout.close()
    p.wait()
    os.remove("1.mp4")
    os.remove("output.mp4")
    os.remove("2.mp4")
    os.remove("1.mp3")
    print("merging audio video done")
def record():
    cmd='ffmpeg -f x11grab -framerate 30 -threads 0 -s 1366x768 -i :0 1.mp4'
    pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid) 
    return pro
    