""" Qt test program that exists after X seconds.

    The first command line argument is the number of seconds to exit. If not given the program
    runs until the user closes it.
"""

import logging
import sys
import time

from PyQt5 import QtCore, QtWidgets

logger = logging.getLogger("myrepo")

class MyWindow(QtWidgets.QWidget):

    def __init__(self, timeout:int = None, parent=None):
        super().__init__(parent=parent)
        logger.debug("Window timeout = {!r}".format(timeout))
        self.formLayout = QtWidgets.QFormLayout()
        self.setLayout(self.formLayout)

        self.label = QtWidgets.QLabel("<no time given>")
        self.formLayout.addRow("Self destructing in", self.label)

        self._startTime = time.perf_counter()
        self._endTime = None if timeout is None else self._startTime + timeout


        self._onStartupTimer = QtCore.QTimer(self)
        self._onStartupTimer.setInterval(100) # Start when event loop has started
        self._onStartupTimer.setSingleShot(False)
        self._onStartupTimer.timeout.connect(self.onTimeout)
        self._onStartupTimer.start()




    def onTimeout(self):
        if self._endTime is not None:
            now = time.perf_counter()
            wait = self._endTime - now

            if wait < 0:
                logger.info("Self destruct sequence initiated!")
                self.close()
            else:
                logger.info("Exiting program in {:.2f} seconds".format(wait))
                self.label.setText("{:.2f} seconds".format(wait))




def main():
    logger.info("myrepo test program")

    if len(sys.argv) > 1:
        timeout = int(sys.argv[1])
    else:
        timeout = None

    app = QtWidgets.QApplication([])
    win = MyWindow(timeout=timeout)
    win.show()
    win.raise_()
    app.exec()
    logger.info("done")


if __name__ == "__main__":
    LOG_FMT = '%(asctime)s %(filename)25s:%(lineno)-4d : %(levelname)-7s: %(message)s'
    logging.basicConfig(level='DEBUG', stream=sys.stderr, format=LOG_FMT)
    main()

