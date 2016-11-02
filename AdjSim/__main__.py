#-------------------------------------------------------------------------------
# ADJSIM SIMULATION FRAMEWORK
# Designed and developed by Sever Topan
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# IMPORTS
#-------------------------------------------------------------------------------
from core import *
from graphics import *
import tests
import sys

#-------------------------------------------------------------------------------
# MAIN EXECUTION SCRIPT
#-------------------------------------------------------------------------------
def main(argv=sys.argv):
    """The main routine."""

    adjSim = AdjSim(argv, True)

    # get char press to exit
    # input("Press Enter to Termainate")


# EXECUTION CALLBACK
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()