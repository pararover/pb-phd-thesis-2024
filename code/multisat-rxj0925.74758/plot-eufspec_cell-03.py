output_folder = analysis_path+'outputs/' # To be modified while on Google Colab
pdf_folder = 'pdf'
png_folder = 'png'
try:
    os.mkdir(output_folder)
except FileExistsError as error:
    print(f"The folder 'outputs' already exists.")
try:
    os.mkdir(os.path.join(output_folder, pdf_folder)) # To be modified while on Google Colab
except FileExistsError as error:
    print(f"The folder '{pdf_folder}' already exists.")
try:
    os.mkdir(os.path.join(output_folder, png_folder)) # To be modified while on Google Colab
except FileExistsError as error:
    print(f"The folder '{png_folder}' already exists.")