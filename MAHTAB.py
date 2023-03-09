import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from HE import Main

    Main()

elif bit == '32bit':

    from HE32 import Main

    Main()
