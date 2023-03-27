import requests

cookies = {
    'SID': 'UQhJC1Wj6EcsBYzjCv62KZ02vYjnWCYGC76MQvMFQRgE9IHumZev3xUj5ErlbYrB8V8www.',
    '__Secure-1PSID': 'UQhJC1Wj6EcsBYzjCv62KZ02vYjnWCYGC76MQvMFQRgE9IHuhunJVp5OwYJV4MtmBc4oDQ.',
    '__Secure-3PSID': 'UQhJC1Wj6EcsBYzjCv62KZ02vYjnWCYGC76MQvMFQRgE9IHu-26KusCZHQkGWoRzghuzxA.',
    'HSID': 'AHCzeIH6vPzMISBGJ',
    'SSID': 'AtsiRmgB_xst5kFKA',
    'APISID': 'eQfRxuPVnHR8Tmjs/ANZZNAxk6P0sw8dnN',
    'SAPISID': '3AQ8U2XFJ5jYAzq-/AOyV6NWssFBPdcF_5',
    '__Secure-1PAPISID': '3AQ8U2XFJ5jYAzq-/AOyV6NWssFBPdcF_5',
    '__Secure-3PAPISID': '3AQ8U2XFJ5jYAzq-/AOyV6NWssFBPdcF_5',
    'SEARCH_SAMESITE': 'CgQI5pcB',
    'NID': '511=mMW18v-aY-sMoccJDc9bLgZmKGwJFug6cGiPIqOnjeWfF1dWZgIv_n9ROMo1xX3fTzb02uSQslZHhT4qD7Vz292qW3upAVSuIDgWZG3WUYDg7kS-bzejrgrV73piBaWePq08T44vq-JQekA6jGD2pJSf1GWcKzIrXvVJFz0cPS1CpJebZMGePCjN3i7iH3FZ5mldUnnYcb9GIE_vGXC3V8LHLk5aW_MBEcvNOtIXBb39VMCForXaxgIhkb3a_VrWi8e_5mQxYKaaIiVPjBdZa-uxLRg',
    'AEC': 'AUEFqZc7mzlwN9INWkTMJRanyuEfuszybRSYhcRziDCy4oELaWC_pG-Rbg',
    '1P_JAR': '2023-03-24-08',
    'SIDCC': 'AFvIBn_Y21IF9Zx--XCclUX0dV4ooaMeiF0ZaVhwhUV8jwRzRZ3yPTJaas9TZPSzT10FVVvYrw',
    '__Secure-1PSIDCC': 'AFvIBn_gP1f-2jRLf--ZrjczU5KJaWGctItg51CMl4eThmE7Q1kzYJbRrwcQUd1DNy8rDm97-g',
    '__Secure-3PSIDCC': 'AFvIBn-CXeN6S97BU4Rip9tnmVv0SaYLEKi0B6YkauRuQnBJ_BDtSeH5heha1U4hx0yzfEAS6j8',
}

headers = {
    'authority': 'inputtools.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'SID=UQhJC1Wj6EcsBYzjCv62KZ02vYjnWCYGC76MQvMFQRgE9IHumZev3xUj5ErlbYrB8V8www.; __Secure-1PSID=UQhJC1Wj6EcsBYzjCv62KZ02vYjnWCYGC76MQvMFQRgE9IHuhunJVp5OwYJV4MtmBc4oDQ.; __Secure-3PSID=UQhJC1Wj6EcsBYzjCv62KZ02vYjnWCYGC76MQvMFQRgE9IHu-26KusCZHQkGWoRzghuzxA.; HSID=AHCzeIH6vPzMISBGJ; SSID=AtsiRmgB_xst5kFKA; APISID=eQfRxuPVnHR8Tmjs/ANZZNAxk6P0sw8dnN; SAPISID=3AQ8U2XFJ5jYAzq-/AOyV6NWssFBPdcF_5; __Secure-1PAPISID=3AQ8U2XFJ5jYAzq-/AOyV6NWssFBPdcF_5; __Secure-3PAPISID=3AQ8U2XFJ5jYAzq-/AOyV6NWssFBPdcF_5; SEARCH_SAMESITE=CgQI5pcB; NID=511=mMW18v-aY-sMoccJDc9bLgZmKGwJFug6cGiPIqOnjeWfF1dWZgIv_n9ROMo1xX3fTzb02uSQslZHhT4qD7Vz292qW3upAVSuIDgWZG3WUYDg7kS-bzejrgrV73piBaWePq08T44vq-JQekA6jGD2pJSf1GWcKzIrXvVJFz0cPS1CpJebZMGePCjN3i7iH3FZ5mldUnnYcb9GIE_vGXC3V8LHLk5aW_MBEcvNOtIXBb39VMCForXaxgIhkb3a_VrWi8e_5mQxYKaaIiVPjBdZa-uxLRg; AEC=AUEFqZc7mzlwN9INWkTMJRanyuEfuszybRSYhcRziDCy4oELaWC_pG-Rbg; 1P_JAR=2023-03-24-08; SIDCC=AFvIBn_Y21IF9Zx--XCclUX0dV4ooaMeiF0ZaVhwhUV8jwRzRZ3yPTJaas9TZPSzT10FVVvYrw; __Secure-1PSIDCC=AFvIBn_gP1f-2jRLf--ZrjczU5KJaWGctItg51CMl4eThmE7Q1kzYJbRrwcQUd1DNy8rDm97-g; __Secure-3PSIDCC=AFvIBn-CXeN6S97BU4Rip9tnmVv0SaYLEKi0B6YkauRuQnBJ_BDtSeH5heha1U4hx0yzfEAS6j8',
    'origin': 'https://www.google.com',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-client-data': 'CJK2yQEIprbJAQipncoBCJzeygEIk6HLAQiI08wBCJGMzQEIgZbNAQjhl80BCOOXzQEI/5jNAQi1ms0BCOibzQEIzJzNAQj8nM0BCPyezQEIv5/NAQ==',
}
def get_suggestions(text):
    params = {
        'text': text,
        'itc': 'ta-t-i0-und',
        'num': '13',
        'cp': '0',
        'cs': '1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'app': 'demopage',
    }

    response = requests.post('https://inputtools.google.com/request', params=params, cookies=cookies, headers=headers)
    return (response.json()[1][0][1][:5])

import tkinter as tk
current_word=''
last_suggestion=''
writing = 0 
import pyautogui
import pyperclip
import platform

def type(text: str):    
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")

pressed_keys = set()
is_active = 0
   
from pynput import keyboard
def on_release(key):
    # Remove the key from the set of currently pressed keys
    if key in current_keys:
        current_keys.remove(key)

    pressed_keys.discard(key)

hotkey_combination = {keyboard.Key.alt,  keyboard.Key.shift}
current_keys = set()
def on_press(key):
    global is_active
    # Check if the pressed key is part of the hotkey combination
    if key in hotkey_combination:
        current_keys.add(key)
        print(key)
        # If all keys in the combination are pressed, execute the action
        if current_keys == hotkey_combination:
            if is_active:
                print('Global hotkey deactivated!')
            else:
                print('Global hotkey activated!')
            is_active = not is_active
            print(f'{is_active = }')
            # Perform your desired action here
    global current_word,last_suggestion, writing
    if not is_active:
        return
    # Get the current text in the entry box
    try:
        current_text = ''
        if key.char.isalpha() or key.char.isdigit():
            if not pressed_keys:
                current_text = key.char
        else:
            if not pressed_keys:
                print(key.char)              
                    
    except AttributeError:
        if not pressed_keys:
            if key == keyboard.Key.space:
                    current_text = 'space'
    pressed_keys.add(key)

    import re
    if current_text == 'space':
        last_word = current_word
        current_word = ''
        
        # replace the typed current word with the selected suggestion
        writing = 1
        if 1:
            last_suggestion = get_suggestions(last_word)[0]
            pyautogui.hotkey('ctrl','backspace')
            type(last_suggestion+' ')
        writing = 0
        if 0:
            for k in range(5):
                labels[k]['text'] = f'{k+1}.)'
        return
        
    elif not re.match(r'^[a-z0-9]$',current_text.lower()):return
    else:
        current_word += current_text
    return 
    
    print(current_word)
    suggestions =   get_suggestions(current_word)
    last_suggestion = suggestions[0]
    # Create a new window to show the suggestions

    # Create a label for each suggestion and pack them into the window
    if 0:
        for k,suggestion in enumerate(suggestions):
            # print(suggestion)
            labels[k]['text'] = suggestion
            

    # hide the suggestion window after 5 seconds
    # suggestion_window.after(5000, suggestion_window.destroy)
    # show the suggestion window
    # suggestion_window.deiconify()

# Create a window

# Add a text entry box to the window

# Bind the show_suggestions function to all key presses
from pynput import keyboard
if 0:
    # non block
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
if 1:
    # Run the application
    window = tk.Tk()
    suggestion_window = tk.Toplevel()
    suggestion_window.geometry('200x100')
    suggestion_window.title('Suggestions')
    labels =  []
    for _ in range(5):
        label = tk.Label(suggestion_window, text=f'{_+1}.)')
        label.pack()
        labels.append(label)
    window.mainloop()
