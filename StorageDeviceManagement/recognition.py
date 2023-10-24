import os
drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]