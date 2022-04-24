'''
Author: Victor Wedden

Description:
    This program displays integers as their base 2, base 8, and base 16 counterparts and outputs them to console
'''

import sys
import stdio
import BaseConversions

for i in range(1, len(sys.argv)):
    n = int(sys.argv[i])

    stdio.writeln('Base 10: ' + str(n))

    stdio.writeln('Base 2: ' + BaseConversions.base_2(n))

    stdio.writeln('Base 8: ' + BaseConversions.base_8(n))

    stdio.writeln('Base 16: ' + BaseConversions.base_16(n))

    stdio.writeln()