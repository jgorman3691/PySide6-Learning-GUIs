from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to CLI args
import sys

# You only need one, and can only have one, QApplication instance per application.
# Pass in sys.argv to allow cli arguments into your app
# If you know you won't be using cli arguments, QApplication([]) works as well
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()

# REMEMBER, WINDOWS ARE HIDDEN BY DEFAULT!
window.show()

# Start the event loop
app.exec_()

# The application will not reach this section until we have closed the window, exited, and
# the event loop has stopped.