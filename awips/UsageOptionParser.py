import sys
from optparse import OptionParser


class UsageOptionParser(OptionParser):
    """
    A subclass of OptionParser that prints that overrides error() to print the
    whole help text, rather than just the usage string.
    """
    def error(self, msg):
        """
        Print the help text and exit.
        """
        self.print_help(sys.stderr)
        sys.stderr.write("\n")
        sys.stderr.write(msg)
        sys.stderr.write("\n")
        sys.exit(2)
