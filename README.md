# Resume-Summarization
<p>
There are three python files in the project:<br>
main.py<br>
resumeasy.py<br>
skillsapi.py<br>
</p>
<br>
The functions written in resumeasy.py and skillsapi.py are imported inside main.py.<br>
A simple form is created using HTML where the user could give the text of the resume as the input. And using the get method, the input from the user is obtained.<br>
skillsapi.py python file contains the code to obtain the dataset of skills from EMSI skills API.<br>
The dataset obtained in skillsapi.py is imported inside resumeasy.py file.<br><br>
resumeasy.py contains six functions:<br>
1.preprocessing - for the preprocessing of the resume text<br>
2.delimiter_removal -removing delimiters from resume text<br>
3.extract_email - extracts email from the resume text using regular expressions<br>
4.extract_skills - extracts skills from the resume text using the dataset obtained from skillsapi.py. Here the resume text after preprocessing is broken into unigrams, bigrams and trigrams and are compared with the skills dataset.<br>
5.mobile_number_extraction - extracts mobile number from resume text. Extracts the following number formats- 9874562362, 09874562362, 91-9874562362, +91-9874562362, +91 9874562362, 91 9874562362, +912-9874562362, +912 9874562362<br>
6.ner_extraction- This function returns college degree and Companies worked at from the resume text. The model is trained separately and the model is stored in a pickle file in the form of bytes. The pickle file is imported to the resumeasy.py and tested.<br><br>
 
Present issues with the code:<br>
1.Need to find a way to accept resume as file.<br>
2.ner_extraction is throwing error. Need to fix it.<br>
