import os, sys
from PyPDF2 import PdfReader,PdfWriter,PdfMerger

def get_all_files(path, target_extention, ans):
    files = os.listdir(path)

    for file in files:
        full_path = path + "/" + file
        if os.path.isfile(full_path):
            _, extention = os.path.splitext(file)
            if extention == target_extention:
                # print(full_path)
                arr = full_path.split('/')
                all_pdfs[arr[-1]] = full_path
                # all_pdfs.append(full_path)
        elif os.path.isdir(full_path):
            get_all_files(full_path, target_extention, ans)


def unite_pdf(input_dir, output_dir, all_pdfs):
    arr = input_dir.split('/')
    name = arr[-1].split('-')[-1]
    keys = sorted(all_pdfs.keys())
    # print(keys)
    
    merger = PdfMerger()
    for k in keys:
        pdf = all_pdfs[k]
        merger.append(pdf)
    merger.write(output_dir + "/" + name + ".pdf")
    merger.close()

if __name__ =="__main__":
    input_dir = sys.argv[1]
    files = os.listdir(input_dir)

    for file in files:
        full_path = input_dir + "/" + file
        print("start")
        print(full_path)
        if os.path.isdir(full_path):
            all_pdfs = {}
            try:
                get_all_files(full_path, ".pdf", all_pdfs)
                unite_pdf(full_path, "./pdf", all_pdfs)
                print("success")
            except:
                print("error")
        print("end")