#module for making pickle files

import pandas as pd
import pickle
from parse_out_email_text import parseOutText

def format_mails():
	
	#for creating emails pickle file
    ff=pd.read_csv('../tools/emails.csv')
    col=list(ff.text)
    for i in range(0,len(col)):
        col[i]=col[i].decode('utf-8')    
    col=parseOutText(col)
    f=open('../tools/processed_mails.pkl','wb')
    pickle.dump(col,f)
    f.close()
    del col
    
    #for creating labels pickle file
    col=list(ff.spam)
    f=open('../tools/check_spam.pkl','wb')
    pickle.dump(col,f)
    f.close()
    del col
