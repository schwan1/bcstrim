import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
# Email tab code ********************************

def bFocal(p1):
    print('bcsTrimmer_support.bFocal')
    sys.stdout.flush()

def createEmail_1click(p1):
    print('bcsTrimmer_support.createEmail_1click')
    sys.stdout.flush()

def customer(p1):
    print('bcsTrimmer_support.customer')
    sys.stdout.flush()

def exit_lclick(p1):
    print('bcsTrimmer_support.exit_lclick')
    sys.stdout.flush()

def mNumber(p1):
    print('bcsTrimmer_support.mNumber')
    sys.stdout.flush()
    
def pLine(p1):
    print('bcsTrimmer_support.pLine')
    sys.stdout.flush()

def pType(p1):
    print('bcsTrimmer_support.pType')
    sys.stdout.flush()

def product(p1):
    print('bcsTrimmer_support.product')
    sys.stdout.flush()

def subject(p1):
    print('bcsTrimmer_support.subject')
    sys.stdout.flush()

def mDate(p1):
    print('bcsTrimmer_support.mDate')
    sys.stdout.flush()

def bcsDueDate(p1):
    print('bcsTrimmer_support.bcsDueDate')
    sys.stdout.flush()

def ftdDueDate(p1):
    print('bcsTrimmer_support.ftdDueDate')
    sys.stdout.flush()

def ftdLead(p1):
    print('bcsTrimmer_support.ftdLead')
    sys.stdout.flush()

def search_1click(p1):
    print('bcsTrimmer_support.search_1click')
    sys.stdout.flush()

def aTeam(p1):
    print('bcsTrimmer_support.aTeam')
    sys.stdout.flush()

def attachment(p1):
    print('bcsTrimmer_support.attachment')
    sys.stdout.flush()

def stdPhrase(p1):
    print('bcsTrimmer_support.stdPhrase')
    sys.stdout.flush()

    
# end bcsactive code ************************************8

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
def btnConvert_1click(p1):
    print('bcsTrimmer_support.btnConvert_1click')
    sys.stdout.flush()

def btnExit(p1):
    print('bcsTrimmer_support.btnExit')
    sys.stdout.flush()
"""
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
"""
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import bcsTrimmer
    bcsTrimmer.vp_start_gui()


