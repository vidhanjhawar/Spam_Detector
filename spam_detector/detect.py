
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from data_formating import format_mails


#Formatting mails (coverting into pickle files) from the csv database file
format_mails()

#features_train is a numpy array contains emails for training
#features_test is a numpy array containing emails for testing
#labels_train is a numpy array containing training labels(spams/ham)
#mail_detect is a numpy array containing processed email to be checked as spam
features_train, features_test, labels_train, labels_test, final_transformed = preprocess()


#Random Forest algorithm to train classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 75, criterion='entropy', min_samples_split = 3)
t=time()
clf.fit(features_train,labels_train)
print "Training Time:", round(time()-t,3),"s"
t=time()
pred=clf.predict(features_test)
print "Prediction Time:", round(time()-t,3),"s"

#code to check accuracy
from sklearn.metrics import accuracy_score
acc=accuracy_score(pred,labels_test)

#predictor for predicting processed email input data
t=time()
pred=clf.predict(final_transformed)
print "Time to detect spam:", round(time()-t,3),"s"

if pred==1:
	print "Email is spam with accuracy:", acc
else:
	print "Email is ham with accuracy:", acc
