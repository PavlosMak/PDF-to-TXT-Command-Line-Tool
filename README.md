# PDF-to-TXT-Command-Line-Tool
A command line tool that extracts text from PDF files. The extracted text is saved in a txt file. Made with PyPDF2.

## Dependencies ##
In order for the script to work you will have to install PyPDF2. You can do that by running the following in your terminal.
```
$pip install PyPDF2
```

## Usage ##
To use the script you simply have to navigate to the directory you have saved the python file and then run:
```
$python pdf_to_txt.py /path/to/pdf.file /where/to/create/text.txt name_of_txt_file 
```
In case that the PDF is encrypted you need to add the password as a forth argument:
```
$python pdf_to_txt.py /path/to/file.pdf /where/to/create/txt/file name_of_txt_file password
``` 






