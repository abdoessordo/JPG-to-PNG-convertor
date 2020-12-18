from tkinter import *
from tkinter import filedialog
from JPGtoPNGconvertor import convert_all_imgs

WIDTH = 500
HEIGHT = 600

root = Tk()
canvas = Canvas(root, width=WIDTH,height=HEIGHT)
root.iconbitmap('./logo.ico')
root.title('PNG Convert')
canvas.pack()

#----------------------------------------------------------
#                  		FUNCTIONS
#----------------------------------------------------------


def add_folder(label):
	foldername = filedialog.askdirectory()
	if foldername != '':
		label['text'] = foldername

def convert():
	convert_all_imgs(input_folder_status_result['text'], output_folder_status_result['text'])
	msg_label['text'] = 'All Done !'






#----------------------------------------------------------
#                  		  GUI
#----------------------------------------------------------
bg_frame = Frame(root, bg='red')
bg_frame.place(relwidth=1, relheight=1, relx=0, rely=0)


holder_frame = Frame(root, bg='white')
holder_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

HTU_frame = Frame(holder_frame, bg='#c8c9cc')
HTU_frame.place(relwidth=0.9, relheigh = 0.35, relx=0.05, rely = 0.05)

HTU_label_title = Label(HTU_frame, bg='#c8c9cc', fg='black', text='How To Use :',font= ('Helvetica', 14, 'underline'))
HTU_label_title.place(relx = 0.05, rely=0.05)

text='Group all the images you want to convert in one folder then select that folder using the "Input Folder" button, then select the destination folder where all the converted images will be using the "Output Folder" button, and finally press "Convert"'
HTU_label_text = Text(HTU_frame, bg='#c8c9cc', fg='black',font= ('Helvetica', 13), 
	bd=0, spacing2=5, pady=15, wrap = WORD)
HTU_label_text.insert(INSERT,text)
HTU_label_text.config(state=DISABLED)
HTU_label_text.place(relwidth=0.9, relheight =0.8, relx = 0.05, rely=0.2)


input_folder = Button(holder_frame, text='Input Folder', command = lambda:add_folder(input_folder_status_result))
input_folder.place(relwidth=0.2, relheight=0.05, relx=0.15, rely=0.5)

output_folder = Button(holder_frame, text='Output Folder', command = lambda:add_folder(output_folder_status_result))
output_folder.place(relwidth=0.2, relheight=0.05, relx=0.65, rely=0.5)

status_frame = Frame(holder_frame, bg='#c8c9cc')
status_frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.6)


input_folder_status = Label(status_frame,text='Selected Input Folder: ',bg='#c8c9cc', fg='black', font=('Helvetica', 12, UNDERLINE))
input_folder_status.place(relx=0.01, rely=0.05)

input_folder_status_result = Label(status_frame,text='',font=('Helvetica', 11), bg='#c8c9cc', fg='black')
input_folder_status_result.place(relx=0.1, rely=0.25)

output_folder_status = Label(status_frame,text='Selected Output Folder: ', bg='#c8c9cc', fg='black', font=('Helvetica', 13, UNDERLINE))
output_folder_status.place(relx=0.01, rely=0.5)
output_folder_status_result=Label(status_frame,text='',font=('Helvetica', 11), bg='#c8c9cc', fg='black')
output_folder_status_result.place(relx=0.1, rely=0.75)


convert_btn = Button(holder_frame, text='Convert', command = lambda:convert())
convert_btn.place(relwidth=0.15, relheight=0.05, relx=0.425, rely=0.85)

msg_label = Label(holder_frame, text='', fg='green', bg='white', font=('Helvetica', 16, 'bold'))
msg_label.place(relx=0.4, rely=0.91)


root.mainloop()