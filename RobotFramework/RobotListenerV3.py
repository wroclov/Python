from robot.libraries.BuiltIn import BuiltIn

"""
Listeners can listen 👂 to the events that are fired during the execution of a test suite and react to them.
They are like a hook 🪝 into the test run, allowing us to execute code at a specific point in time during the execution.
You can use them to e.g. notify other systems about the progress of your test suite in real time.
https://docs.robotframework.org/docs/extending_robot_framework/listeners_prerun_api/listeners
e.g. robot --listener .\RobotListenerV3.py .\calculate\ .\DemoLibrary\ .\StaticLibrary\
"""


class RobotListenerV3:

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LISTENER_API_VERSION = 3


    def __init__(self, filename='report.md'):
        self.filename = filename
        self.fh = open(self.filename, 'w')
        self.fh.write("# Robot Framework Report\n")
        self.fh.write("|Test|Status|\n")
        self.fh.write("|---|---|\n")

    """Listener that writes result and status of each test to a file"""

    def end_test(self, data, result):
        print("end_test func")
        self.fh.write(f"|{result.name}|{result.status}|\n")

    def close(self):
        self.fh.close()

    def start_suite(self, suite, result):
        pass

    def start_test(self, test, result):
        pass

    def end_suite(self, suite, result):
        pass

    def log_message(self, message):
        pass

    def message(self, message):
        pass

    def debug_file(self, path):
        pass

    def output_file(self, path):
        pass

    def xunit_file(self, path):
        pass

    def log_file(self, path):
        pass

    def report_file(self, path):
        pass


