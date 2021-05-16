from watchdog.events import PatternMatchingEventHandler, FileSystemEvent
from transport import transport
from debug import *


class PymonEventHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        # Send restart message whenever file system changes
        debug("Change detected")
        transport.emit("restart")
