import sys

class Printer:
    def __init__(self, echo=True):
        self.echo = echo
        self._buf = []
        self._col = 0

    def write(self, s):
        s = str(s)
        self._buf.append(s)
        if self.echo:
            sys.stdout.write(s)
            sys.stdout.flush()
        # update column: after last newline or add length
        if '\n' in s:
            self._col = len(s.rsplit('\n', 1)[-1])
        else:
            self._col += len(s)

    def print(self, *args, sep=' ', end='\n'):
        s = sep.join(map(str, args)) + end
        self.write(s)

    def getvalue(self):
        return ''.join(self._buf)

    def reset(self):
        self._buf = []
        self._col = 0

    def column(self):
        return self._col
