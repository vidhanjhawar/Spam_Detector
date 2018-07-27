import pickle
import cPickle
import numpy
import mail_input
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif



def preprocess(mails_file = "../tools/processed_mails.pkl", spams_file="../tools/check_spam.pkl"):
    
    #unpickling the pickled files
    spams_file_handler = open(spams_file, "rb")
    spams = pickle.load(spams_file_handler)
    spams_file_handler.close()

    mails_file_handler = open(mails_file, "rb")
    mails_data = cPickle.load(mails_file_handler)
    mails_file_handler.close()

    # test_size is the percentage of events assigned to the test set
    # (remainder go into training)
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(mails_data, spams, test_size=0.1, random_state=42)
    
    #function call to take email as an input
    final_test = mail_input.takeInput()
    
    # text vectorization--go from strings to lists of numbers
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed  = vectorizer.transform(features_test)
    final_transformed=vectorizer.transform(final_test)
    

    # feature selection, because text is super high dimensional and 
    # can be really computationally chewy as a result
    selector = SelectPercentile(f_classif, percentile=100)
    selector.fit(features_train_transformed, labels_train)
    final_transformed=selector.transform(final_transformed).toarray()
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed  = selector.transform(features_test_transformed).toarray()
   
    
    ### info on the data
    #print "no. of spam emails:", sum(labels_train)
    #print "no. of ham emails:", len(labels_train)-sum(labels_train)
    
    return features_train_transformed, features_test_transformed, labels_train, labels_test, final_transformed
