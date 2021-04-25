#encoding: utf-8


from biplist import *
from datetime import datetime
import sys


url = sys.argv[1]
env = sys.argv[2]
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
    elif env == 'sandbox':
        writePlist(plist, "sandboxfest.plist", binary=False)
    elif env == 'development':
        writePlist(plist, "developmentfest.plist", binary=False)
except(InvalidPlistException, NotBinaryPlistException) as e:
    print("Something bad happened:", e)
