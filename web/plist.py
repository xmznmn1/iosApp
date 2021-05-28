#encoding: utf-8


from biplist import *
from datetime import datetime
import sys
import os

url = ''
env = sys.argv[1]
if env == 'production':
    url = 'http://10.7.2.101/ipa/downloads/production.ipa'
elif env == 'sandbox':
    url = 'http://10.7.2.101/ipa/downloads/sandbox.ipa'
elif env == 'development':
    url = 'http://10.7.2.101/ipa/downloads/development.ipa'
plist = {
    'items':
    [
        {
            'assets':
            [
                {
                    'kind': 'software-package',
                    'url': url,
                },
            ],
            'metadata':
                {
                    'bundle-identifier': 'com.SolarSoft.SolarWallet',
                    'bundle-version': '1.0',
                    'kind': 'software',
                    'title': 'Puzzle&Heroes',
                }
        }
    ]
}
try:
    if env == 'production':
        writePlist(plist, "manifest.plist", binary=False)
        os.system('cat manifest.plist')
    elif env == 'sandbox':
        writePlist(plist, "sandboxfest.plist", binary=False)
        os.system('cat sandboxfest.plist')
    elif env == 'development':
        writePlist(plist, "developmentfest.plist", binary=False)
        os.system('cat developmentfest.plist')
except(InvalidPlistException, NotBinaryPlistException) as e:
    print("Something bad happened:", e)
