import os
import sys
os.system('clear')
os.system('pip install cython')
os.system('clear')
import time
import marshal
import zlib
import base64
import cython
import compileall
import shutil

def run(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)
run(' \x1b[1;92m[\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Follow My Github Account\x1b[1;96m.......')
time.sleep(0.8)
os.system('xdg-open https://github.com/Indru740')
os.system('clear')
logo = """🔥                          \033[1;36m𓆰𓃮𓆪                         🔥            
  _____ _   _ _____  _____  _    _ 
 |_   _| \ | |  __ \|  __ \| |  | |
   | | |  \| | |  | | |__) | |  | |
   | | | . ` | |  | |  _  /| |  | |
  _| |_| |\  | |__| | | \ \| |__| |
 |_____|_| \_|_____/|_|  \_\\____/ 
                                                                                                      
                                                            \033[1;96m
 \x1b[1;97m===========================================================
 \033[1;37m[*] OWNER      : \033[1;36mINDRU'X'WD
 \033[1;37m[*] GITHUB     : \033[1;36mINDRU740
 \033[1;37m[*] STATUS     : \033[1;91mFREE
 \033[1;37m[*] TEAM       : ONE MAN ARMY
 \033[1;37m[*] TOOL       : ALL TYPE ENCODEDE
 \x1b[1;97m[*]=========================================================="""

def load(word):
    lix = ['/', '-', '╲', '|', '/', '-', '╲', '|', '/', '-', '╲', '|', '/', '-', '╲', 'done']
    for i in range(1):
        for x in range(len(lix)):
            sys.stdout.write('\r{}{}'.format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def verInput(data):
    version = sys.version_info[:2]
    if version < (3, 0):
        dataInput = raw_input(data)
    else:
        dataInput = input(data)
    return dataInput
marshalHead = '#ENCODED BY : INDRU\n#ENCRYPTION : Py3 MARSHAL\n#GITHUB : https://github.com/Indru740\n#----------------------------------------------\nimport marshal\nexec(marshal.loads('
marshalTail = '))'
b64Head = '#ENCODED BY : INDRU\n#ENCRYPTION : Py3 BASE64\n#GITHUB : https://github.com/Indru740\n#----------------------------------------------\nimport base64\nexec(base64.b64decode('
b64Tail = '))'
zlibHead = '#ENCODED BY : INDRU\n#ENCRYPTION : Py3 ZLIB\n#GITHUB : https://github.com/Indru740\n#----------------------------------------------\nimport zlib\nexec(zlib.decompress('
zlibTail = '))'
mbHead = '#ENCODED BY : INDRU\n#ENCRYPTION : Py3 MARSHAL+BASE64\n#GITHUB : https://github.com/Indru740\n#----------------------------------------------\nimport marshal, base64\nexec(marshal.loads(base64.b64decode('
mbTail = ')))'
allHead = '#ENCODED BY : INDRU\n#ENCRYPTION : Py3 MARSHAL+ZLIB+B64\n#GITHUB : https://github.com/Indru740\n#----------------------------------------------\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode('
allTail = '))))'

def encodeMarshal(data):
    code = compile(data, '___INNOCENT-BOY___', 'exec')
    dump = marshal.dumps(code)
    encData = marshalHead + repr(dump) + marshalTail
    return encData

def encodeZlib(data):
    code = data.encode()
    dump = zlib.compress(code, 2)
    encData = zlibHead + repr(dump) + zlibTail
    return encData

def encodeBase64(data):
    code = data.encode()
    dump = base64.b64encode(code)
    encData = b64Head + repr(dump) + b64Tail
    return encData

def encodeMb(data):
    data = compile(data, '___INNOCENT-BOY___', 'exec')
    data = marshal.dumps(data)
    dump = base64.b64encode(data)
    encData = mbHead + repr(dump) + mbTail
    return encData

def encodeAll(data):
    data = compile(data, '___INNOCENT-BOY___', 'exec')
    data = marshal.dumps(data)
    data = zlib.compress(data)
    dump = base64.b64encode(data)
    encData = allHead + repr(dump) + allTail
    return encData

def encodePyc(data):
    tmp = open('temp.py', 'w')
    tmp.write(data)
    tmp.close()
    if sys.version_info[:2] < (3, 0):
        compileall.compile_file('temp.py')
    else:
        compileall.compile_file('temp.py', legacy=True)
    return True

def encodeHard(data):
    power = verInput('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Enter Power Amount \x1b[37m[\x1b[36mMAX\x1b[33m•\x1b[36m99\x1b[97m] :\x1b[32m ')
    print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    try:
        power = int(power)
    except:
        power = verInput('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Enter Power Amount \x1b[37m[\x1b[36mMAX\x1b[33m•\x1b[36m99\x1b[97m] :\x1b[32m ')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        power = int(power)
    while power > 99:
        power = verInput('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Power Amount \x1b[37m[\x1b[36mMAX\x1b[33m•\x1b[36m99\x1b[97m] :\x1b[32m ')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        power = int(power)
    load('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Encoding Your File ...\x1b[32m ')
    print('\n\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    powerData = data
    for i in range(power):
        powerData = encodeAll(powerData)
    encodePyc(powerData)
    return True

def getFile():
    global fileName
    path = verInput('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Put File Path :\x1b[32m ')
    print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    while not os.path.exists(path):
        psb('\x1b[1;92m [\x1b[1;91m!\x1b[1;92m]\x1b[1;91m File Not Found..!!')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        time.sleep(0.4)
        path = verInput('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Put File Path :\x1b[32m ')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    fileData = open(path, 'r').read()
    if '/' in path:
        fileName = path.split('/')[-1]
    else:
        fileName = path
    return fileData

def saveFile(encData):
    if '.py' in fileName:
        savefileName = fileName.replace('.py', '_enc.py')
    else:
        savefileName = fileName + '_enc.py'
    savePath = '/sdcard/' + savefileName
    file = open(savePath, 'w')
    file.write(encData)
    file.close()

def moveFile():
    if '.py' in fileName:
        savefileName = fileName.replace('.py', '_enc.py')
    else:
        savefileName = fileName + '_enc.py'
    savePath = '/sdcard/' + savefileName
    os.system('mv temp.pyc ' + savePath + ' >/dev/null 2>&1')
    os.system('rm temp.py > /dev/null 2>&1')

def encode(type):
    fileData = getFile()
    if not type == 'hard':
        load('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Encoding Your File ...\x1b[32m ')
        print('\n\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    if type == 'marshal':
        encData = encodeMarshal(fileData)
        saveFile(encData)
    elif type == 'zlib':
        encData = encodeZlib(fileData)
        saveFile(encData)
    elif type == 'base64':
        encData = encodeBase64(fileData)
        saveFile(encData)
    elif type == 'mb':
        encData = encodeMb(fileData)
        saveFile(encData)
    elif type == 'all':
        encData = encodeAll(fileData)
        saveFile(encData)
    elif type == 'hard':
        encData = encodeHard(fileData)
        moveFile()
    time.sleep(1)
    psb('\x1b[1;92m [\x1b[1;91m✓\x1b[1;92m]\x1b[1;97m Your File Encoding Completed..!!')
    print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    psb('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m File Saved in : \x1b[32m/sdcard/' + fileName.replace('.py', '_enc.py') + '\x1b[92m\x1b[37m')
    print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    input('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Click Enter To Back Menu')
    main()

def main():
    os.system('clear')
    print(logo)
    print('\x1b[1;92m [\x1b[1;91m1\x1b[1;92m]\x1b[1;97m Encode Marshal')
    print('\x1b[1;92m [\x1b[1;91m2\x1b[1;92m]\x1b[1;97m Encode Zlib')
    print('\x1b[1;92m [\x1b[1;91m3\x1b[1;92m]\x1b[1;97m Encode Base64')
    print('\x1b[1;92m [\x1b[1;91m4\x1b[1;92m]\x1b[1;97m Encode Marshal+Base64')
    print('\x1b[1;92m [\x1b[1;91m5\x1b[1;92m]\x1b[1;97m Encode Marshal+Zlib+Base64')
    print('\x1b[1;92m [\x1b[1;91m6\x1b[1;92m]\x1b[1;97m Encode Simple')
    print('\x1b[1;92m [\x1b[1;91m7\x1b[1;92m]\x1b[1;97m Encode Cython')
    print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    op = verInput('\x1b[1;92m [\x1b[1;91m?\x1b[1;92m]\x1b[1;97m Select :\x1b[32m ').replace('0', '')
    print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
    while op not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        psb('\x1b[1;92m [\x1b[1;91m!\x1b[1;92m]\x1b[1;91m Enter a Correct Option..!!')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        op = verInput('\x1b[1;92m [\x1b[1;91m?\x1b[1;92m]\x1b[1;97m Select :\x1b[32m ').replace('0', '')
    if op == '1':
        encode('marshal')
    elif op == '2':
        encode('zlib')
    elif op == '3':
        encode('base64')
    elif op == '4':
        encode('mb')
    elif op == '5':
        encode('all')
    elif op == '6':
        encode('hard')
    elif op == '7':
        print('\x1b[1;92m [\x1b[1;91m!\x1b[1;92m]\x1b[1;96m NOTE : \x1b[1;93mFirst Do Marshal Encode,Then Put')
        print('            Enc File For Hard Cythonize...!!')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        file = input('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Put Enc File :\x1b[32m ')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        load('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Cythonize Your File ...\x1b[1;92m ')
        print('\n\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        try:
            open(file, 'r').read()
        except:
            exit('\x1b[1;92m [\x1b[1;91m!\x1b[1;92m]\x1b[1;91m File Not Found..!!\x1b[1;97m ')
            print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        os.system('cythonize -i -3 ' + file + '> /dev/null')
        psb('\x1b[1;92m [\x1b[1;91m✓\x1b[1;92m]\x1b[1;97m Your File Cythonize Completed..!!')
        print('\x1b[38;5;46m -\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\x1b[1;32m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[38;5;196m-\x1b[38;5;46m-')
        input('\x1b[1;92m [\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Click Enter To Back Menu')
        main()
if __name__ == '__main__':
    main()
