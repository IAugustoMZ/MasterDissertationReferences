import pyqrcode

url = pyqrcode.create(
    'https://github.com/IAugustoMZ/MasterDissertationReferences')
url.png('qrcode.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
url.show()