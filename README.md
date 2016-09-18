# Spam-Email-Classifier-DataSet
Some simple codes to format the CSDMC2010 SPAM corpus

* The original dataset is [CSDMC2010 SPAM corpus](http://csmining.org/index.php/spam-email-datasets-.html). This dataset is composed of a selection of mail messages as training data and testing data. Due to this dataset was used for a competition, it doesn't label the testing data but only training data. Thus, what can we use to train and test our naive Bayes classifier is the training data in CSDMC2010 which contains 2929 ham messages and 1378 spam messages. 
* For convenience, these codes can be used to format this dataset to make it similar with the dataset in FTP.
	* convert.py  removes the html labels in .eml files.
	* move.sh moves the emails to "./ham/" and "./spam" folders respectively according to the labels.
* The result is **ham.zip** and **spam.zip** although there are some meaningless symbols(like '<' or '>') remained in the files. 
* Suggestions and improvements are encouraged.


Please direct any questions regarding these batches to <zhangrz14@fudan.edu.cn>.
