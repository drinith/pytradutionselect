import clipboard

#this function get clipboard stream and send console
def getClipboard():
    text = clipboard.paste()

    print(text)


if '__main__'==__name__:

    while(True):
        getClipboard()