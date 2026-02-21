input_file_name = input('File name: ').strip().lower()
if input_file_name.endswith('.gif'): #*.gif
    print('image/gif')
elif input_file_name.endswith('.jpg') or input_file_name.endswith('.jpeg'): #*.jpg; *.jpeg
    print('image/jpeg')
elif input_file_name.endswith('.png'): #*.png
    print('image/png')
elif input_file_name.endswith('.pdf'): #*.pdf
    print('application/pdf')
elif input_file_name.endswith('.txt'): #*.txt
    print('text/plain')
elif input_file_name.endswith('.zip'): #*.zip
    print('application/zip')
else:
    print('application/octet-stream')
