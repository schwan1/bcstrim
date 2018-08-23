import sys
import re
import datetime
#BCS message dictionary


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

#### Start Email tab code ********************************

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

def save_1click(p1):
    print('bcsTrimmer_support.save_1click')
    sys.stdout.flush()

def aTeam(p1):
    print('bcsTrimmer_support.aTeam')
    sys.stdout.flush()

def team(p1):
    print('bcsTrimmer_support.team')
    sys.stdout.flush()

def attachment(p1):
    print('bcsTrimmer_support.attachment')
    sys.stdout.flush()

def stdPhrase(p1):
    print('bcsTrimmer_support.stdPhrase')
    sys.stdout.flush()
    
#### end bcsactive code ************************************

# Conversion Functions for BCS
def btnConvert_1click(p1):
    sys.stdout.flush()
    mtext=''
    obj = w.textScroll
    mtext = obj.get('1.0', 'end')
    bcsLines = mtext.splitlines()
    notset = 'notset'
    bcsInfo = {
    'mNumber': notset,
    'customer': notset,
    'bFocal': notset ,
    'pLine': notset ,
    'pType': notset ,
    'product': notset ,
    'subject': notset ,
    'mDate': notset ,
    'bcsDueDate': notset ,
    'ftdDueDate': notset ,
    'ftdLead': notset ,
    'aTeam': notset ,
    'ftdTeam': notset ,
    'attachment': notset ,
    'bcsMessage': notset ,
    'bcsDescription': notset ,
    'bcsDesire': notset ,
    'stdPhrase': notset ,
    'email': notset ,
    'bcsRawData': notset
    }

# Conversion of the BCS message pasted in and placing in fields on email tab

   
    # Fill FTD team members
    team = ['Guest, Gregory C','Atkings, Mark A','Baca, Mark','Capece, Richard N','Dahlstrom, David B','Delgado, John C','Garcia, Avalito D','Gray, Susan S', 'Johnson, Emily A', 'Johnson, Noel G', 'Klabacha, Cheryl A', 'Lyon, Amber C', 'Nashery, Payam', 'Nguyen Helen H', 'Pople, Michael S', 'Sanderson, Brian K', 'Schwan, Mel E','Sharp, Keith A']
    bcsInfo['ftdTeam'] = team
    w.team['values'] = team
    w.team.current(0)

    #Clear all the conversion information fields from the last conversion
    clearform()

# Start of the message conversion process
    # Find the line that has the BCS focal
    if bcsInfo['bFocal'] == 'notset':
        focal = between(mtext, ' for ', 'Replies to')
        focal = focal.rstrip()
        bcsInfo['bFocal'] = focal
        w.bFocal.insert(0,bcsInfo['bFocal'])
    # Find the line that has the BCS focal
    if bcsInfo['ftdLead'] == 'notset':
        focal = between(mtext, 'Boeing:\n', 'DUE DATE:')
        focal = focal.rstrip()
        bcsInfo['ftdLead'] = focal
        w.ftdLead.insert(0,bcsInfo['ftdLead'])
    # Find the line that has the BCS message number
    if bcsInfo['mNumber'] == 'notset':
        mNumber = betweenlast(mtext, '[MESSAGE NUMBER:',']')
        mNumber = mNumber.lstrip()
        bcsInfo['mNumber'] = mNumber[:19]
        w.mNumber.insert(0, bcsInfo['mNumber'])
        print("mNumber>"+bcsInfo['mNumber'])
    # Find the line that has the BCS customer
    if bcsInfo['customer'] == 'notset':
        customer = betweenlast(mtext, 'FROM: THE BOEING COMPANY','[MESSAGE NUMBER:')
        customer = after(customer, 'TO:')
        bcsInfo['customer'] = customer.strip()
        w.customer.insert(0,bcsInfo['customer'])
        print("customer>"+bcsInfo['customer'])
    #Message date extraction
    if bcsInfo['mDate'] == 'notset':
        mDate = between(mtext, 'TO:','SERVICE REQUEST ID:')
        mDate = after(mDate, 'MESSAGE DATE:')
        if mDate == '' :
            mDate = after(mDate, 'MESSAGE DATE:')
        mDate=mDate.strip()
        bcsInfo['mDate'] = mDate[:11]
        w.mDate.insert(0,bcsInfo['mDate'])

    #Due date extraction and FTD Due Date creation 
    if bcsInfo['bcsDueDate'] == 'notset':
        dueDate = betweenlast(mtext, 'DUE DATE:', 'SUBJECT:')
        dueDate=dueDate.strip()
        if dueDate != '':
            bcsInfo['bcsDueDate'] = dueDate[:11]
            w.bcsDueDate.insert(0,bcsInfo['bcsDueDate'])
            #Add 14 days to the BCS message due date
            tempDate = datetime.datetime.strptime(bcsInfo['bcsDueDate'], "%d-%b-%Y")+datetime.timedelta(days=14)
            myDate='{:%d-%b-%Y}'.format(tempDate)
            bcsInfo['ftdDueDate']=myDate
            w.ftdDueDate.insert(0,myDate)
    #Subject extraction
    if bcsInfo['subject'] == 'notset':
        subject=between(mtext, 'SUBJECT:', 'DESIRED ACTION:')
        if subject.find('// ') :
            subject = between(subject,'// ', '\n')
        subject=subject.strip()
        bcsInfo['subject'] = subject
        w.subject.insert(0,bcsInfo['subject'])
    #pType extraction  
    if bcsInfo['pType'] == 'notset':
        pType=between(mtext, 'Product Type:', 'Product Line:')
        if pType == '' :
            pType=between(mtext, 'PRODUCT TYPE:', 'PRODUCT LINE:')  
        pType=pType.strip()
        bcsInfo['pType'] = pType
        w.pType.insert(0,bcsInfo['pType'])
    #pLine extraction  
    if bcsInfo['pLine'] == 'notset':
        pLine=between(mtext, 'Product Line:', 'Series/Product:')
        if pLine == '' :
            pLine=between(mtext, 'PRODUCT LINE:', 'PRODUCT:')
        pLine=pLine.strip()
        bcsInfo['pLine'] = pLine
        w.pLine.insert(0,bcsInfo['pLine'])
    #Product extraction 
    if bcsInfo['product'] == 'notset': 
        product=between(mtext, 'Series/Product:', 'ATA:')
        if product == '' :
            product=between(mtext, 'PRODUCT:', 'ATA:')
        product=product.strip()
        bcsInfo['product'] = product
        w.product.insert(0,bcsInfo['product'])
    #Description and Desired action extraction
    if bcsInfo['bcsDescription'] == 'notset':
        bcsDescription = ''
        fieldservice = ''
        bcsDesired = '' 
        bcsDescription=betweenlast(mtext, 'DESCRIPTION:', '+++++++++++')
        bcsDescription=bcsDescription.strip()
        fieldservice=betweenlast(mtext, 'DESCRIPTION:', '+++++++++++')
        fieldservice=fieldservice.strip()
        if bcsDescription == fieldservice :
            bcsDescription = ''
        bcsDesired=between(mtext, 'DESIRED ACTION:', '+++++++++++')
        bcsDesired=bcsDesired.strip()
        bcsDescription =  "Desired Action:\n\n" + bcsDesired + '\n\n\nASE Additional Description:\n'+bcsDescription + '\n\n\nField Service Description:\n\n'+ fieldservice
        bcsDescription = cleanmarkup(bcsDescription)
        bcsDescription = before(bcsDescription, 'Service Request System:')
        bcsInfo['bcsDescription'] = bcsDescription
        w.message.insert(END, bcsInfo['bcsDescription'])

    # Delete lines with  '-----' or '####' characters
    cleanmarkup(mtext)
    x = 1
    j = 0 
    # Loop for filling out data in bcsInfo dictionary
    while x < len(bcsLines)-1 :
        '''print (bcsLines[x])


        # Find line that has the Boeing focals name
        if re.search('^From the Boeing', bcsLines[x]) :
            focal = after(bcsLines[x], ' for ')
            focal = focal.rstrip()
            bcsInfo['bFocal'] = focal
            w.bFocal.insert(0,bcsInfo['bFocal'])
            print("bFocal>"+bcsInfo['bFocal'])
        # Find the line that indicates the next line contains FTD focal(s) names 
        elif re.search('^Boeing.*', bcsLines[x]) :
            x += 1
            focal = bcsLines[x]
            focal = focal.rstrip()
            bcsInfo['ftdLead'] = focal
            w.ftdLead.insert(0,bcsInfo['ftdLead'])
            print("ftdLead>"+bcsInfo['ftdLead'])'''

       # Find the line that has the BCS attachments
        if re.search('^REFERENCES:.*', bcsLines[x]) :
            x += 1
            attachment = ['']
            attachment.clear()
            tempAttachment = bcsLines[x]
            attachment.append(tempAttachment.rstrip())
            while re.search(r'\/', bcsLines[x+1]):
                tempAttachment = bcsLines[x+1]
                attachment.append(tempAttachment.rstrip())
                x += 1
            bcsInfo = {'attachment': attachment}
            w.attachment['values'] = attachment
            w.attachment.current(0)

        # Find the line that has the BCS Message
        '''elif re.search('^DESCRIPTION:.*', bcsLines[x]) :
            bcsDescription=''
            x += 1
            templine = bcsLines[x]
            # Combine all the lines in the description

            if  not re.search( '++++++++++++++++++++++++++++++' , templine ) :
                bcsDescription = bcsDescription + templine
                templine = bcsLines[x]
                x += 1
                
            bcsInfo = {'bcsDescription': bcsLines[x]}
            w.message.insert(END, bcsInfo['bcsDescription'])
            print("bcsDescription>"+bcsInfo['bcsDescription'])

            templine = bcsLines[x]

            bcsDesire = ''
            while templine[0:5] != '-----' :
                templine = bcsLines[x]
                bcsDesire = bcsDesire.rstrip()
                bcsDesire = bcsDesire + templine
                x += 1
                templine = bcsLines[x]
            bcsInfo = {'bcsDesire': bcsDesire}
            print("bcsDesire>"+bcsInfo['bcsDesire'])'''

        x += 1

def clearform():
    w.bFocal.delete(0, END)
    w.ftdLead.delete(0, END)
    w.bcsDueDate.delete(0, END)
    w.ftdDueDate.delete(0,END)
    w.mNumber.delete(0, END)
    w.mDate.delete(0, END)
    w.customer.delete(0, END)
    w.pType.delete(0, END)
    w.pLine.delete(0, END)
    w.subject.delete(0, END)
def cleanmarkup(cleantext) :
    #Removes ===, ++++, --- line delimiting characters
    cleantext = cleantext.splitlines()
    for i in range(len(cleantext) - 1, -1, -1):
        element = cleantext[i]
        if re.search('^----------', cleantext[i]) : 
            del cleantext[i]

    for i in range(len(cleantext) - 1, -1, -1):
        element = cleantext[i]
        if re.search('^\+\+\+', cleantext[i]) : 
            del cleantext[i]

    for i in range(len(cleantext) - 1, -1, -1):
        element = cleantext[i]
        if re.search('^======', cleantext[i]) : 
            del cleantext[i]
    sep = "\n"
    cleantext = sep.join(cleantext)
    cleantext = cleantext.replace('\n\n\n\n', '\n\n')
    cleantext = cleantext.replace('\n\n\n', '\n\n')
    return(cleantext)
    
   
def after(value, a):
    # Find and validate first part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def betweenlast(value, a, b):
    # Find and validate before-part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.find(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]

def subextract(mask, text):
    # Extract subject line
    sub = re.findall(mask, text)
    for subject in sub:
        subject = subject.replace('\n',' ')
        subject = subject.rstrip()
        subject = after(subject, '// ')
    # Return last found instance in message
    return subject
   
def dateextract(mask, text):
    # Extract message line
    mdate = re.findall(mask, text)
    
    for alldate in mdate:
        alldate = alldate.replace('\n',' ')
        alldate = alldate.rstrip()
        alldate = after(alldate, ':')
        alldate = alldate.lstrip()
    # Return last found instance in message
    return alldate

def descextract(mask, text):
    # Extract message line
    mdesc = re.findall(mask, text)
    for alldesc in mdesc:
        alldesc = alldesc.replace('\n',' ')
        alldesc = alldesc.rstrip()
        alldesc = after(alldesc, ':')
       # alldesc = alldesc.lstrip()
    # Return last found instance in message
    return alldesc

def numextract(mask,text):
    mNumber = ""
    # Extract message line
    mNum = re.findall(mask, text)
    for mNumber in mNum:
        mNumber = mNumber.replace('\n',' ')
        mNumber = mNumber.rstrip()
        mNumber = after(mNumber, 'A')
    # Return last found instance in message
    return mNumber

def btnExit(p1):
    print('bcsTrimmer_support.btnExit')
    sys.stdout.flush()
    destroy_window()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
#    w.destroy()
    top_level = None

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

if __name__ == '__main__':
    import bcsTrimmer
    bcsTrimmer.vp_start_gui()


