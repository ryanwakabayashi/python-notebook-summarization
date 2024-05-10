Data for fine tuning was found on Kaggle at https://www.kaggle.com/datasets/kaggle/meta-kaggle-code/data

folders 0000, 0001, and 0002 were used for data training

extract downloads to data/unzip-data.
run remove_extra_files.py to remove extra files (files that are not ipynb). THe unzip-data fold can now be removed.


can I generate statistics on how many lines of code are in each notebook?
how many characters are in each notebook?
how many cells are in each notebook?


what is the training input size for the model?

can I reduce the dataset using a standard deviation from the image of lines vs characters?


The first step of my prompt engineering:
1. Summarize the following code in two to three sentences. Focus on the intentions of the code, emphasize the type of data being handled and do nothing else. 

Why?
* This project is meant to be used by a red team member to evaluate python notebooks for interesting data and opportunity.


What is important to a red team member?
* I need to emphasize the type of data being handled.
* Identify if the data is related to PII, PHI, or other sensitive data.
* ~~Categorize the work being done~~

I found this info "512 tokens might correspond to about 2500 characters (~letters), which might correspond to about 400 words"
Google flan-t5-small should be able to handle 512 tokens. will revisit this later for other ways to manipulate the data.




Should i remove comment lines? How can i take important information from them