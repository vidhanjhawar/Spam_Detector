import parse_out_email_text

# function to convert txt file into processed list
def takeInput ():
    input_file=open('../tools/testmail.txt','rb')
    st=input_file.read().decode('utf-8')
    input_file.close()
    lis=[]
    lis.append(st)
    lis=parse_out_email_text.parseOutText(lis)
    return lis
