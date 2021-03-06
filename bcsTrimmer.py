
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

import bcsTrimmer_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = BCS_Message_Converter (root)
    bcsTrimmer_support.init(root, top)
    root.mainloop()

w = None

def create_BCS_Message_Converter(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = BCS_Message_Converter (w)
    bcsTrimmer_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_BCS_Message_Converter():
    global w
    w.destroy()
    w = None


class BCS_Message_Converter:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1200x927+575+8")
        top.title("BCS Message Converter")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.02, rely=0.01, relheight=0.93, relwidth=0.95)
        self.TNotebook1.configure(width=854)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Convert   ", compound="left", underline="-1",)
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Email   ",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.textScroll = ScrolledText(self.TNotebook1_t0)
        self.textScroll.place(relx=0.01, rely=0.01, relheight=0.92
                , relwidth=0.97)
        self.textScroll.configure(background="white")
        self.textScroll.configure(font=font9)
        self.textScroll.configure(foreground="black")
        self.textScroll.configure(highlightbackground="#d9d9d9")
        self.textScroll.configure(highlightcolor="black")
        self.textScroll.configure(insertbackground="black")
        self.textScroll.configure(insertborderwidth="3")
        self.textScroll.configure(selectbackground="#c4c4c4")
        self.textScroll.configure(selectforeground="black")
        self.textScroll.configure(width=10)
        self.textScroll.configure(wrap=NONE)

        self.btnConvert = ttk.Button(self.TNotebook1_t0)
        self.btnConvert.place(relx=0.45, rely=0.95, height=30, width=98)
        self.btnConvert.configure(takefocus="")
        self.btnConvert.configure(text='''Convert''')
        self.btnConvert.bind('<Button-1>',lambda e:bcsTrimmer_support.btnConvert_1click(e))

        self.btnExit = ttk.Button(top)
        self.btnExit.place(relx=0.87, rely=0.95, height=30, width=98)
        self.btnExit.configure(takefocus="")
        self.btnExit.configure(text='''Exit''')
        self.btnExit.bind('<Button-1>',lambda e:bcsTrimmer_support.btnExit(e))



        #Start of email compose page
        
        self.TFrame1 = ttk.Frame(self.TNotebook1_t1)
        self.TFrame1.place(relx=0.01, rely=0.03, relheight=0.27, relwidth=0.98)
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(width=1005)

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.01, rely=0.05, height=24, width=86)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font9)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Message # :''')

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.31, rely=0.05, height=24, width=80)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font9)
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Customer :''')

        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.64, rely=0.05, height=24, width=101)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font=font9)
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''Boeing Focal :''')

        self.mNumber = ttk.Entry(self.TFrame1)
        self.mNumber.place(relx=0.1, rely=0.05, relheight=0.12, relwidth=0.2)
        self.mNumber.configure(textvariable=bcsTrimmer_support.mNumber)
        self.mNumber.configure(takefocus="")
        self.mNumber.configure(cursor="ibeam")
        self.mNumber.bind('<Enter>',lambda e:bcsTrimmer_support.mNumber(e))

        self.customer = ttk.Entry(self.TFrame1)
        self.customer.place(relx=0.39, rely=0.05, relheight=0.12, relwidth=0.24)
        self.customer.configure(textvariable=bcsTrimmer_support.customer)
        self.customer.configure(takefocus="")
        self.customer.configure(cursor="ibeam")
        self.customer.bind('<Enter>',lambda e:bcsTrimmer_support.customer(e))

        self.bFocal = ttk.Entry(self.TFrame1)
        self.bFocal.place(relx=0.75, rely=0.05, relheight=0.12, relwidth=0.23)
        self.bFocal.configure(textvariable=bcsTrimmer_support.bFocal)
        self.bFocal.configure(takefocus="")
        self.bFocal.configure(cursor="ibeam")
        self.bFocal.bind('<Enter>',lambda e:bcsTrimmer_support.bFocal(e))

        self.TLabel4 = ttk.Label(self.TFrame1)
        self.TLabel4.place(relx=0.01, rely=0.23, height=24, width=100)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font=font9)
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Product Line :''')

        self.TLabel5 = ttk.Label(self.TFrame1)
        self.TLabel5.place(relx=0.31, rely=0.23, height=24, width=105)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font=font9)
        self.TLabel5.configure(relief=FLAT)
        self.TLabel5.configure(text='''Product Type :''')

        self.TLabel6 = ttk.Label(self.TFrame1)
        self.TLabel6.place(relx=0.64, rely=0.23, height=24, width=67)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font=font9)
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''Product :''')

        self.TLabel7 = ttk.Label(self.TFrame1)
        self.TLabel7.place(relx=0.01, rely=0.42, height=24, width=63)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font=font9)
        self.TLabel7.configure(relief=FLAT)
        self.TLabel7.configure(text='''Subject :''')

        self.TLabel8 = ttk.Label(self.TFrame1)
        self.TLabel8.place(relx=0.01, rely=0.6, height=24, width=102)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font=font9)
        self.TLabel8.configure(relief=FLAT)
        self.TLabel8.configure(text='''Message Date :''')

        self.TLabel9 = ttk.Label(self.TFrame1)
        self.TLabel9.place(relx=0.23, rely=0.6, height=24, width=112)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font=font9)
        self.TLabel9.configure(relief=FLAT)
        self.TLabel9.configure(text='''BCS Due Date :''')

        self.TLabel10 = ttk.Label(self.TFrame1)
        self.TLabel10.place(relx=0.46, rely=0.6, height=24, width=109)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font9)
        self.TLabel10.configure(relief=FLAT)
        self.TLabel10.configure(text='''FTD Due Date :''')

        self.TLabel11 = ttk.Label(self.TFrame1)
        self.TLabel11.place(relx=0.68, rely=0.6, height=24, width=77)
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font=font9)
        self.TLabel11.configure(relief=FLAT)
        self.TLabel11.configure(text='''FTD Lead :''')

        self.pLine = ttk.Entry(self.TFrame1)
        self.pLine.place(relx=0.11, rely=0.23, relheight=0.12, relwidth=0.2)
        self.pLine.configure(textvariable=bcsTrimmer_support.pLine)
        self.pLine.configure(takefocus="")
        self.pLine.configure(cursor="ibeam")
        self.pLine.bind('<Enter>',lambda e:bcsTrimmer_support.pLine(e))

        self.pType = ttk.Entry(self.TFrame1)
        self.pType.place(relx=0.42, rely=0.23, relheight=0.12, relwidth=0.21)
        self.pType.configure(textvariable=bcsTrimmer_support.pType)
        self.pType.configure(takefocus="")
        self.pType.configure(cursor="ibeam")
        self.pType.bind('<Enter>',lambda e:bcsTrimmer_support.pType(e))

        self.product = ttk.Entry(self.TFrame1)
        self.product.place(relx=0.71, rely=0.23, relheight=0.12, relwidth=0.27)
        self.product.configure(textvariable=bcsTrimmer_support.product)
        self.product.configure(takefocus="")
        self.product.configure(cursor="ibeam")
        self.product.bind('<Enter>',lambda e:bcsTrimmer_support.product(e))

        self.subject = ttk.Entry(self.TFrame1)
        self.subject.place(relx=0.08, rely=0.42, relheight=0.12, relwidth=0.9)
        self.subject.configure(justify=CENTER)
        self.subject.configure(textvariable=bcsTrimmer_support.subject)
        self.subject.configure(takefocus="")
        self.subject.configure(cursor="ibeam")
        self.subject.bind('<Enter>',lambda e:bcsTrimmer_support.subject(e))

        self.mDate = ttk.Entry(self.TFrame1)
        self.mDate.place(relx=0.11, rely=0.6, relheight=0.12, relwidth=0.12)
        self.mDate.configure(textvariable=bcsTrimmer_support.mDate)
        self.mDate.configure(takefocus="")
        self.mDate.configure(cursor="ibeam")
        self.mDate.bind('<Enter>',lambda e:bcsTrimmer_support.mDate(e))

        self.bcsDueDate = ttk.Entry(self.TFrame1)
        self.bcsDueDate.place(relx=0.34, rely=0.6, relheight=0.12, relwidth=0.12)
        self.bcsDueDate.configure(textvariable=bcsTrimmer_support.bcsDueDate)
        self.bcsDueDate.configure(takefocus="")
        self.bcsDueDate.configure(cursor="ibeam")
        self.bcsDueDate.bind('<Enter>',lambda e:bcsTrimmer_support.bcsDueDate(e))

        self.ftdDueDate = ttk.Entry(self.TFrame1)
        self.ftdDueDate.place(relx=0.57, rely=0.6, relheight=0.12, relwidth=0.11)
        self.ftdDueDate.configure(textvariable=bcsTrimmer_support.ftdDueDate)
        self.ftdDueDate.configure(takefocus="")
        self.ftdDueDate.configure(cursor="ibeam")
        self.ftdDueDate.bind('<Enter>',lambda e:bcsTrimmer_support.ftdDueDate(e))

        self.ftdLead = ttk.Entry(self.TFrame1)
        self.ftdLead.place(relx=0.76, rely=0.6, relheight=0.12, relwidth=0.22)
        self.ftdLead.configure(textvariable=bcsTrimmer_support.ftdLead)
        self.ftdLead.configure(takefocus="")
        self.ftdLead.configure(cursor="ibeam")
        self.ftdLead.bind('<Enter>',lambda e:bcsTrimmer_support.ftdLead(e))

        self.TLabel12 = ttk.Label(self.TFrame1)
        self.TLabel12.place(relx=0.01, rely=0.79, height=24, width=119)
        self.TLabel12.configure(background="#d9d9d9")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font=font9)
        self.TLabel12.configure(relief=FLAT)
        self.TLabel12.configure(text='''Assigned Team :''')


        self.TLabel13 = ttk.Label(self.TFrame1)
        self.TLabel13.place(relx=0.68, rely=0.79, height=24, width=83)
        self.TLabel13.configure(background="#d9d9d9")
        self.TLabel13.configure(foreground="#000000")
        self.TLabel13.configure(font=font9)
        self.TLabel13.configure(relief=FLAT)
        self.TLabel13.configure(text='''FTD Team :''')

        self.aTeam = ttk.Entry(self.TFrame1)
        self.aTeam.place(relx=0.13, rely=0.79, relheight=0.12, relwidth=0.54)
        self.aTeam.configure(textvariable=bcsTrimmer_support.aTeam)
        self.aTeam.configure(takefocus="")
        self.aTeam.configure(cursor="ibeam")

        self.team = ttk.Combobox(self.TFrame1)
        self.team.place(relx=0.77, rely=0.79, relheight=0.12, relwidth=0.21)
        self.team.configure(textvariable=bcsTrimmer_support.team)
        self.team.configure(takefocus="")
        self.team.configure(cursor="ibeam")

        self.TFrame2 = ttk.Frame(self.TNotebook1_t1)
        self.TFrame2.place(relx=0.01, rely=0.32, relheight=0.35, relwidth=0.98)
        self.TFrame2.configure(relief=GROOVE)
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief=GROOVE)
        self.TFrame2.configure(width=1005)

        self.TLabel14 = ttk.Label(self.TFrame2)
        self.TLabel14.place(relx=0.01, rely=0.04, height=24, width=104)
        self.TLabel14.configure(background="#d9d9d9")
        self.TLabel14.configure(foreground="#000000")
        self.TLabel14.configure(font=font9)
        self.TLabel14.configure(relief=FLAT)
        self.TLabel14.configure(text='''BCS Message :''')

        self.TLabel15 = ttk.Label(self.TFrame2)
        self.TLabel15.place(relx=0.59, rely=0.04, height=24, width=111)
        self.TLabel15.configure(background="#d9d9d9")
        self.TLabel15.configure(foreground="#000000")
        self.TLabel15.configure(font=font9)
        self.TLabel15.configure(relief=FLAT)
        self.TLabel15.configure(text='''Attachments :''')

        self.attachment = ttk.Combobox(self.TFrame2)
        self.attachment.place(relx=0.71, rely=0.04, relheight=0.09
                , relwidth=0.28)
        self.attachment.configure(textvariable=bcsTrimmer_support.attachment)
        self.attachment.configure(takefocus="")

        self.message = ScrolledText(self.TFrame2)
        self.message.place(relx=0.01, rely=0.22, relheight=0.78, relwidth=0.97)
        self.message.configure(background="white")
        self.message.configure(font="TkTextFont")
        self.message.configure(foreground="black")
        self.message.configure(highlightbackground="#d9d9d9")
        self.message.configure(highlightcolor="black")
        self.message.configure(insertbackground="black")
        self.message.configure(insertborderwidth="3")
        self.message.configure(selectbackground="#c4c4c4")
        self.message.configure(selectforeground="black")
        self.message.configure(width=10)
        self.message.configure(wrap=WORD)

        self.TFrame3 = ttk.Frame(self.TNotebook1_t1)
        self.TFrame3.place(relx=0.01, rely=0.69, relheight=0.20, relwidth=0.98)
#        self.TFrame3.place(relx=0.01, rely=0.69, relheight=0.29, relwidth=0.98)
        self.TFrame3.configure(relief=GROOVE)
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief=GROOVE)
        self.TFrame3.configure(width=1005)

        self.TLabel16 = ttk.Label(self.TFrame3)
        self.TLabel16.place(relx=0.01, rely=0.04, height=24, width=133)
        self.TLabel16.configure(background="#d9d9d9")
        self.TLabel16.configure(foreground="#000000")
        self.TLabel16.configure(font=font9)
        self.TLabel16.configure(relief=FLAT)
        self.TLabel16.configure(text='''STD Email Phrase :''')

        self.stdPhrase = ttk.Combobox(self.TFrame3)
        self.stdPhrase.place(relx=0.15, rely=0.04, relheight=0.12, relwidth=0.83)

        self.stdPhrase.configure(textvariable=bcsTrimmer_support.stdPhrase)
        self.stdPhrase.configure(takefocus="")

        self.TLabel17 = ttk.Label(self.TFrame3)
        self.TLabel17.place(relx=0.01, rely=0.22, height=24, width=96)
        self.TLabel17.configure(background="#d9d9d9")
        self.TLabel17.configure(foreground="#000000")
        self.TLabel17.configure(font=font9)
        self.TLabel17.configure(relief=FLAT)
        self.TLabel17.configure(text='''Email Editor :''')

        self.email = ScrolledText(self.TFrame3)
        self.email.place(relx=0.15, rely=0.22, relheight=0.50, relwidth=0.83)
#        self.email.place(relx=0.15, rely=0.22, relheight=0.68, relwidth=0.83)
        self.email.configure(background="white")
        self.email.configure(font="TkTextFont")
        self.email.configure(foreground="black")
        self.email.configure(highlightbackground="#d9d9d9")
        self.email.configure(highlightcolor="black")
        self.email.configure(insertbackground="black")
        self.email.configure(insertborderwidth="3")
        self.email.configure(selectbackground="#c4c4c4")
        self.email.configure(selectforeground="black")
        self.email.configure(width=10)
        self.email.configure(wrap=NONE)


        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="File")


        self.TFrame4 = ttk.Frame(self.TNotebook1_t1)
        self.TFrame4.place(relx=0.01, rely=0.90, relheight=0.07, relwidth=0.28)
        self.TFrame4.configure(relief=GROOVE)
        self.TFrame4.configure(borderwidth="2")
        self.TFrame4.configure(relief=GROOVE)
        self.TFrame4.configure(width=285)

        self.save = ttk.Button(self.TFrame4)
        self.save.place(relx=0.04, rely=0.18, height=30, width=98)
        self.save.configure(takefocus="")
        self.save.configure(text='''Save''')
        self.save.bind('<Button-1>',lambda e:bcsTrimmer_support.save_1click(e))

        self.search = ttk.Button(self.TFrame4)
        self.search.place(relx=0.63, rely=0.18, height=30, width=98)
        self.search.configure(takefocus="")
        self.search.configure(text='''Search''')
        self.search.bind('<Button-1>',lambda e:bcsTrimmer_support.search_1click(e))

        self.createEmail = ttk.Button(self.TNotebook1_t1)
        self.createEmail.place(relx=0.45, rely=0.91, height=30, width=128)
        self.createEmail.configure(takefocus="")
        self.createEmail.configure(text='''Create Email''')
        self.createEmail.bind('<Button-1>',lambda e:bcsTrimmer_support.createEmail_1click(e))


#end second tab





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



