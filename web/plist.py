#encoding: utf-8


from biplist import *
from datetime import datetime
plist = {
    'items':
    [
        {
            'assets':
            [
                {
                    'kind': 'software-package',
                    'url': 'http://10.7.21.106/ipa/Antia_042217:38:59_release_r5.0_production_1.ipa',
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
    writePlist(plist, "manifest.plist",binary=False)
except(InvalidPlistException, NotBinaryPlistException) as e:
    print ("Something bad happened:", e)