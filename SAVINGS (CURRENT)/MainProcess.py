from Savings import Statement

def processSaving():
    savingsList = []
    savings_file = open('file/Savings(Data).txt','r')
    for usavings in savings_file:
        list = usavings.split(',')
        s = Statement(list[0], list[1], list[2], float(list[3]))
        savingsList.append(s)
    return savingsList

"""""
def registerSavings():
    savingsdata = month + ',' + week + ',' + dates + ',' + amount +'\n'
    savings_file = open('file/Savings(Data).txt','a')
    savings_file.write(savingsdata)
"""""


processSaving()
