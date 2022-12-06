#import webbrowser
import webbrowser
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
password = '805066343'
pas = input('Password:')
if pas == password:
    print('Welcome!')
    #webbrowser.get('chrome').open_new_tab('https://bmw-gt3.github.io/bank/index101.html')
    
    webbrowser.open('https://bmw-gt3.github.io/i.bank.805066343', new=2)
    #webbrowser.get(using='google-chrome').open_new_tab('https://bmw-gt3.github.io/bank/index101.html')
    
else:
    print('Wrong Password!')

        

