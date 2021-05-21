import os
import shutil
from zipfile import ZipFile

if not os.path.exists(r"C:\Users\sip011635\Documents\Projects\practice\pdf_files"):
    os.makedirs('pdf_files')

if not os.path.exists(r"C:\Users\sip011635\Documents\Projects\practice\image_files"):
    os.makedirs('image_files')

if not os.path.exists(r"C:\Users\sip011635\Documents\Projects\practice\excel_files"):
    os.makedirs('excel_files')

if not os.path.exists(r"C:\Users\sip011635\Documents\Projects\practice\zip_files"):
    os.makedirs('zip_files')

if not os.path.exists(r"C:\Users\sip011635\Documents\Projects\practice\misc_files"):
    os.makedirs('misc_files')

def organizer(path):
    for i in os.walk(path):
        for j in i[2]:
                try:
                    if j.endswith('.pdf'):
                        shutil.move(os.path.join(i[0], j), r"C:\Users\sip011635\Documents\Projects\practice\pdf_files")
                    elif j.endswith('.jpg') or j.endswith('.png'):
                        shutil.move(os.path.join(i[0], j), r"C:\Users\sip011635\Documents\Projects\practice\image_files")
                    elif j.endswith('.xlsx') or j.endswith('.csv'):
                        shutil.move(os.path.join(i[0], j), r"C:\Users\sip011635\Documents\Projects\practice\excel_files")

                    elif j.endswith('.gz') or j.endswith('.zip'):
                        shutil.move(os.path.join(i[0], j), r"C:\Users\sip011635\Documents\Projects\practice\zip_files")
                    else:
                        shutil.move(os.path.join(i[0], j),r"C:\Users\sip011635\Documents\Projects\practice\misc_files")
                
                except shutil.SameFileError:
                    pass

organizer(r"C:\Users\sip011635\Documents\Projects\practice")




