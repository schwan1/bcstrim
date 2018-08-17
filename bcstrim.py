import re

#BCS message dictionary
bcsInfo = {
    'mNumber': '' ,
    'customer': '' ,
    'bFocal': '' ,
    'pLine': '' ,
    'pType': '' ,
    'product': '' ,
    'subject': '' ,
    'mDate': '' ,
    'bcsDueDate': '' ,
    'ftdDueDate': '' ,
    'ftdLead':'' ,
    'aTeam':'' ,
    'ftdTeam':'[]' ,
    'attachment':'[]' ,
    'bcsMessage':'' ,
    'bcsDescription':'' ,
    'bcsDesire':'' ,
    'stdPhrase':'' ,
    'email':'' ,
    'bcsRawData':'' ,
    }

def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
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


def messageconvert():
    bcsRaw = open("bcsraw.txt", "r")
    bcsLines = bcsRaw.readlines()
    bcsRaw.close()
    x = 3 
    # Loop for filling out data in bcsInfo dictionary
    while x < len(bcsLines):

        # Find line that has the Boeing focals name
        if re.search('^From the Boeing', bcsLines[x]) :
            focal = after(bcsLines[x], ' for ')
            focal = focal.rstrip()
            bcsInfo = {'bFocal': focal}
            print("bFocal>"+bcsInfo['bFocal'])
            
        # Find the line that indicates the next line contains FTD focal(s) names 
        elif re.search('^Boeing.*', bcsLines[x]) :
            x += 1
            focal = bcsLines[x]
            focal = focal.rstrip()
            bcsInfo = {'ftdFocal': focal}
            print("ftdFocal>"+bcsInfo['ftdFocal'])
            
        # Find the line that has the BCS message due date
        elif re.search('^DUE DATE:.*', bcsLines[x]) :
            keyDate = after(bcsLines[x], 'DUE DATE: ')
            keyDate = keyDate.rstrip()
            bcsInfo = {'dueDate': keyDate[:11]}
            print("dueDate>"+bcsInfo['dueDate'])
            
        # Find the line that has the BCS message number
        elif re.search('^.MESSAGE NUMBER:.*', bcsLines[x]) :
            mesNumber = after(bcsLines[x], 'MESSAGE NUMBER:')
            bcsInfo = {'mNumber': mesNumber[:19]}
            print("mNumber>"+bcsInfo['mNumber'])
            
        # Find the line that has the BCS message date
        elif re.search('^MESSAGE DATE:.*', bcsLines[x]) :
            keyDate = after(bcsLines[x], 'MESSAGE DATE: ')
            bcsInfo = {'mDate': keyDate[:11]}
            print("mDate>"+bcsInfo['mDate'])
 
        # Find the line that has the BCS customer
        elif re.search('^ACCOUNT:.*', bcsLines[x]) :
            customer = after(bcsLines[x], 'ACCOUNT: ')
            bcsInfo = {'customer': customer}
            print("customer>"+bcsInfo['customer'])

        # Find the line that has the BCS product type
        elif re.search('^PRODUCT TYPE:.*', bcsLines[x]) :
            pType = after(bcsLines[x], 'PRODUCT TYPE: ')
            bcsInfo = {'pType': pType}
            print("pType>"+bcsInfo['pType'])

        # Find the line that has the BCS product line
        elif re.search('^PRODUCT LINE:.*', bcsLines[x]) :
            pLine = after(bcsLines[x], 'PRODUCT LINE: ')
            bcsInfo = {'pLine': pLine}
            print("pLine>"+bcsInfo['pLine'])

        # Find the line that has the BCS product 
        elif re.search('^PRODUCT:.*', bcsLines[x]) :
            product = after(bcsLines[x], 'PRODUCT: ')
            if bcsLines[x+1] != "ATA::":
                product = product.rstrip() + bcsLines[x+1]
                x += 1
            bcsInfo = {'product': product}
            print("product>"+bcsInfo['product'])
           

        # Find the line that has the BCS subject
        elif re.search('^SUBJECT:.*', bcsLines[x]) :
            subject = after(bcsLines[x], 'SUBJECT: ')
            subject = after(subject, '// ')
            if bcsLines[x+1] != "REFERENCES:":
                subject = subject.rstrip() + bcsLines[x+1]
                x += 1
            bcsInfo = {'subject': subject}
            print("subject>"+bcsInfo['subject'])
     
        # Find the line that has the BCS attachments
        elif re.search('^REFERENCES:.*', bcsLines[x]) :
            x += 1
            attachment = bcsLines[x]
            while re.search(r'\/', bcsLines[x+1]):
                attachment = attachment.rstrip() + "," + bcsLines[x+1]
                x += 1
            bcsInfo = {'attachment': attachment}
            print("attachment>"+bcsInfo['attachment'])

        # Find the line that has the BCS Message
        elif re.search('^DESCRIPTION:.*', bcsLines[x]) :
            x += 2
            templine = bcsLines[x]
            bcsDescription = templine.rstrip()
            da = -1
            # Combine all the lines in the description
            while  da < 0 :
                if templine[0:5] == '-----' :
                    x += 1
                    templine = bcsLines[x]

                bcsDescription = bcsDescription+templine
#                bcsDescription = bcsDescription.rstrip()
                x += 1
                templine = bcsLines[x]
                da = templine.find('DESIRED ACTION:')
            
            bcsInfo = {'bcsDescription': bcsDescription}
            print("bcsDescription>"+bcsInfo['bcsDescription'])
            x += 2
            templine = bcsLines[x]
#            bcsDesire = templine.rstrip()
#            x += 1
            bcsDesire = ''
            while templine[0:5] != '-----' :
                templine = bcsLines[x]
#                bcsDesire = bcsDesire.rstrip()
                bcsDesire = bcsDesire + templine
                x += 1
                templine = bcsLines[x]
            bcsInfo = {'bcsDesire': bcsDesire}
            print("bcsDesire>"+bcsInfo['bcsDesire'])


        x += 1 
#        print(bcsLines[x])

main()