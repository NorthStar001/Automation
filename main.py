import os

ext = {
    '.docx': 'document_docs',
    '.pdf': 'document_pdfs',
    '.txt': 'document_texts',
    '.mkv': 'video_mkv',
    '.mp4': 'video_mp4',
    '.mp3': 'audio_mp3',
}

# loop through the extensions of all the files and move them to the respective folders based on the extension dictionary definition
for file in os.listdir():
    # print(file)
    if os.path.isfile(file):
        file_ext = os.path.splitext(file)[1]
        if file_ext in ext:
            dest_dir = os.path.join('organized_files', ext[file_ext])
            os.makedirs(dest_dir, exist_ok=True)
            os.rename(file, os.path.join(dest_dir, file))



# for directory in ext.values():
#     os.makedirs(os.path.join('organized_files', directory), exist_ok=True)
#     if not os.path.exists(os.path.join('organized_files', directory)):
#         os.makedirs(os.path.join('organized_files', directory))
#     else:
#         print(f"Directory '{directory}' already exists.")

# os.makedirs('organized_files', exist_ok=True)