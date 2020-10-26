import pyautogui
import time
# pyautogui.moveTo(14,129,duration=1, tween=pyautogui.easeInOutQuad)
# pyautogui.click() 
# pyautogui.write("""cd /home/panda/projects/pyautogui
# panda
# panda
# """, interval=0.25) 
pyautogui.moveTo(38,186,duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click() 
pyautogui.hotkey('ctrl', 'p')
pyautogui.write('client.hack', interval=0.25)
pyautogui.press('enter') 
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.write("""use HH\Lib\Str\lowercase;
class Client {
public function __construct(public string $endpoint,public dict<string,string> $headers,public bool $selfSigned) {
$this->endpoint = 'https://appwrite.io/v1';
$this->headers = dict[
    'content-type'=> '',
    'x-sdk-version'=> 'appwrite:hack:1.1.0',
    ];
    $this->selfSigned = false;
}

""",interval=0.1)