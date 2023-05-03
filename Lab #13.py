import shutil
import tempfile
import urllib.request
import urllib.error

try:
    url = input("Введите любой адрес URL:")
    with urllib.request.urlopen('http://python.org/') as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

    if url.startswith('http'):
        name = url.split('//')[-1] + '.html'
    else:
        name = url.split('//')[-1].split('/')[0]

        
    with open(tmp_file.name) as html, open(name, 'w', encoding='utf-8') as file:
        for line in html:
            file.write(line)
            
except urllib.error.URLError as e:
    print("Ошибка URL:", e.reason)
except ValueError:
    print("Введите действительный адрес URL")

