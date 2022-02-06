import os
import tkinter as tk
from tkinter import ttk,font,colorchooser,messagebox,filedialog
main_software = tk.Tk()
#main software Size Geometry
main_software.geometry('1200x800')
#Title of Software
main_software.title('Vpad By Roshan')
#main_software.wm_iconbitmap("icons2/icon.ico")
##########  Icons #############################
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")
copy_icon = tk.PhotoImage(file="icons2/copy.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
cut_icon = tk.PhotoImage(file="icons2/cut.png")
clear_all_icon = tk.PhotoImage(file="icons2/clear_all.png")
find_icon = tk.PhotoImage(file="icons2/find.png")
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")
light_default_icon = tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
red_icon = tk.PhotoImage(file="icons2/red.png")
monokai_icon = tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons2/night_blue.png")
bold_icon = tk.PhotoImage(file="icons2/bold.png")
italic_icon = tk.PhotoImage(file="icons2/italic.png")
underline_icon = tk.PhotoImage(file="icons2/underline.png")
font_color_icon = tk.PhotoImage(file="icons2/font_color.png")
align_left_icon = tk.PhotoImage(file="icons2/align_left.png")
align_center_icon = tk.PhotoImage(file="icons2/align_center.png")
align_right_icon = tk.PhotoImage(file="icons2/align_right.png")
#+++++++++++++ End Icons +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
######## Tool Bar#####################################################################################
tool_bar_label = ttk.Label(main_software)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)
####### Font Families #########
font_tuple = tk.font.families()
font_family_var = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label,width = 28 , textvariable= font_family_var,state="readonly")
font_box['values'] = font_tuple
font_box.grid(row= 0 , column=0, padx = 5)
font_box.current(font_tuple.index("Noto Sans Georgian"))
########## Size Box #############
size_var = tk.IntVar()
size_box = ttk.Combobox(tool_bar_label,width = 5, textvariable= size_var,state="readonly") 
size_box.grid(row= 0, column= 1,padx=5)
size_box['values'] = tuple(range(6,100,2))
size_box.current(3)
########### Bold Button #################
bold_btn = ttk.Button(tool_bar_label,image=bold_icon)
bold_btn.grid(row=0, column=2,padx=5)
########### Italic Button ###############
italic_btn = ttk.Button(tool_bar_label,image=italic_icon)
italic_btn.grid(row=0, column=3,padx=5)
########### Underline Button##############
underline_btn = ttk.Button(tool_bar_label,image=underline_icon)
underline_btn.grid(row=0, column=4,padx=5)
############ Font Color Button ################
font_color_btn = ttk.Button(tool_bar_label,image=font_color_icon)
font_color_btn.grid(row=0 , column = 5 ,padx= 5)
############ Align Left Button ################
align_left_btn = ttk.Button(tool_bar_label,image=align_left_icon)
align_left_btn.grid(row=0 , column = 6 ,padx= 5)
############ Align Center Button ################
align_center_btn = ttk.Button(tool_bar_label,image=align_center_icon)
align_center_btn.grid(row=0 , column = 7 ,padx= 5)
############ Align Right Button ################
align_right_btn = ttk.Button(tool_bar_label,image=align_right_icon)
align_right_btn.grid(row=0 , column = 8 ,padx= 5)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

############# Text Editor########################
text_editor = tk.Text(main_software)
text_editor.config(wrap="word",relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_software)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
####### current Values of Variables ###########
current_font_family = "Noto Sans Georgian"
current_font_size = 12
#Font Family Binding
def change_font(event=None):
    global current_font_family
    current_font_family = font_family_var.get()
    text_editor.configure(font=(current_font_family))
font_box.bind("<<ComboboxSelected>>",change_font)
# Font Size Binding
def change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
size_box.bind("<<ComboboxSelected>>",change_font_size)
# Font Bold Button
def change_bold():
    bold_property = tk.font.Font(font=text_editor['font'])
    if bold_property.actual()["weight"] == "normal":
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    elif bold_property.actual()["weight"] == "bold":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))  
bold_btn.configure(command=change_bold)
# Font Italic Button
def change_italic():
    italic_property = tk.font.Font(font=text_editor['font'])
    if italic_property.actual()["slant"] == "roman" or italic_property.actual()["slant"] == "normal":
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    elif italic_property.actual()["slant"] == "italic":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))  
italic_btn.configure(command = change_italic) 
#Underline Button
def change_underline():
    underline_property = tk.font.Font(font=text_editor['font'])
    if underline_property.actual()["underline"] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, "underline"))
    elif underline_property.actual()["underline"] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))  
underline_btn.configure(command = change_underline)         
#  Color chooser
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg= color_var[1])
font_color_btn.configure(command=change_font_color)
# Alignment 
# Left 
def align_left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left",justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"left")
align_left_btn.configure(command=align_left)
# Center 
def align_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center",justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")
align_center_btn.configure(command=align_center)
# Right
def align_right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right",justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")
align_right_btn.configure(command=align_right)

text_editor.configure(font=("Noto Sans Georgian",12))
#+++++++++++++End Text Editor+++++++++++++++++++++++++
############# Status Bar ######################
status_bar = ttk.Label(text_editor)
status_bar.pack(side=tk.BOTTOM)
text_change = False
def changed(event=None):
    if text_editor.edit_modified():
        global text_change
        text_change = True
        words = len(text_editor.get(1.0,"end-1c").split())
        char = len(text_editor.get(1.0,"end-1c"))
        status_bar.config(text=f"Characters : {char} Words : {words}")
        text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)
#+++++++++++++End Status Bar+++++++++++++++++++++
################## Menu Bar #############################################################################
############ Menu ########################
main_menu = tk.Menu(main_software ,tearoff=False)
file_menu = tk.Menu(main_menu, tearoff=False)
edit_menu = tk.Menu(main_menu, tearoff=False)
view_menu = tk.Menu(main_menu, tearoff=False)
color_theme_menu = tk.Menu(main_menu, tearoff=False)
############ Menu Variables ##################################################################################
color_theme_choice = tk.StringVar()
color_dict = {
	"Light Default" : ("black","white"),
	"Light Plus" : ("#474747","#e0e0e0"),
	"Dark" : ("white","black"),
	"Red" :("#2d2d2d","#ffe8e8"),
	"Monokai" : ("#d3b774","#474747"),
	"Night Blue" : ("#ededed","#6b9dc2")
}
############ Bar #############################################################################################
#Functionality 
url = ""
#New
def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)
#Open
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Files",filetypes=(("Txt Files",'*.txt'),("All Files","*.*")))
    try:
        with open(url,"r") as f:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,f.read())
    except FileNotFoundError:
        return 
    except:
        return
#Save
def save_file(event=None):
    try:
        global url
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,"w", encoding="utf-8") as f :
                f.write(content)
        else:
            url = filedialog.asksaveasfile(mode="w", defaultextension = '.txt',filetypes=(("Txt Files",".txt"),("All Files","*.*")))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
        
#Save as 
def save_as_file(event=None):
    try :
        global url
        url = filedialog.asksaveasfile(mode="w", defaultextension = '.txt',filetypes=(("Txt Files",".txt"),("All Files","*.*")))
        content3 = text_editor.get(1.0,tk.END)
        url.write(content3)
        url.close()
    except:
        return
    
# Quit
def quit_file(event=None):
    try:
        global url, text_change
        if text_change:
            mbox = messagebox.askyesnocancel("Warning","Do You want to save file")
            if mbox == True:
                content = str(text_editor.get(1.0,tk.END))
                if url:
                    with open(url,"w", encoding="utf-8") as f :
                        f.write(content)
                        main_software.destroy()
                else:
                    url = filedialog.asksaveasfile(mode="w", defaultextension=".txt",filetypes=(("Txt Files","*.txt"),("All Files","*.*")))
                    url.write(content)
                    url.close()
                    main_software.destroy()
            elif mbox == False:
                main_software.destroy()
        else:
            main_software.destroy()
    except:
        return 

#Files
file_menu.add_command(label="New",image=new_icon, compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)
file_menu.add_command(label="Open",image=open_icon,compound=tk.LEFT, accelerator='Ctrl+O', command= open_file)
file_menu.add_command(label="Save",image=save_icon,compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As",image=save_as_icon, compound=tk.LEFT,accelerator="Ctrl+Shift+S", command = save_as_file)
file_menu.add_command(label="Exit",image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command = quit_file)
#Edit
# Edit Functionality
#Find
def find_func(event = None):
	find_dialogue = tk.Toplevel()
	find_dialogue.geometry("600x400")
	find_dialogue.title("Find")
	find_dialogue.resizable(0,0)
	def find():
		word = find_input.get()
		text_editor.tag_remove("match","1.0",tk.END)
		matches = 0
		if word:
			start_pos = "1.0"
			while True:
				start_pos = text_editor.search(word , start_pos,tk.END)
				if not start_pos:
					break
				end_pos = f'{start_pos}+{len(word)}c'
				text_editor.tag_add("match",start_pos,end_pos)
				matches += 1
				start_pos = end_pos
				text_editor.tag_config("match",foreground= "red",background="yellow")
	def replace():
		word2 = find_input.get()
		replace_txt = replace_input.get()
		content = text_editor.get(1.0,tk.END)
		new_content = content.replace(word2,replace_txt)
		text_editor.delete(1.0,tk.END)
		text_editor.insert(1.0,new_content)
	#frame 
	find_frame = ttk.LabelFrame(find_dialogue,text="Find/Replace")
	find_frame.pack(pady=20)
	#labels
	text_find_label = ttk.Label(find_frame,text = "Find")
	text_replace_label = ttk.Label(find_frame,text="Replace")
	#entry 
	find_input = ttk.Entry(find_frame,width = 30)
	replace_input = ttk.Entry(find_frame,width = 30)
	# Button
	find_btn = ttk.Button(find_frame , text = "Find",command=find)
	replace_btn = ttk.Button(find_frame,text="Replace",command = replace)
	# Grids
	# Frame Grid
	text_find_label.grid(row = 0 , column = 0)
	text_replace_label.grid(row= 1 , column = 0)
	#Entry Grid
	find_input.grid(row = 0, column = 1)
	replace_input.grid(row= 1, column = 1)
	# Button Grid
	find_btn.grid(row = 2, column = 0)
	replace_btn.grid(row = 2, column = 1)
# Edit Menu
edit_menu.add_command(label="Copy",image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C",command = lambda : text_editor.event_generate("<Control c>"))
edit_menu.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V", command = lambda : text_editor.event_generate("<Control v>"))
edit_menu.add_command(label="Cut",image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X",command = lambda : text_editor.event_generate("<Control x>"))
edit_menu.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Shift+DEL",command =lambda: text_editor.delete(1.0,tk.END))
edit_menu.add_command(label="Find",image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F",command = find_func)
#View Check Button
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
def hide_toolbar():
	global show_toolbar,show_statusbar,tool_bar_label,status_bar
	if show_toolbar:
		tool_bar_label.pack_forget()
		show_toolbar = False
	else :
		text_editor.pack_forget()
		status_bar.pack_forget()
		tool_bar_label.pack(side=tk.TOP,fill=tk.X)
		text_editor.pack(fill=tk.BOTH,expand=True)
		if show_statusbar:
			status_bar.pack(side= tk.BOTTOM)
		else:
			status_bar.pack_forget()

		show_toolbar = True
def hide_statusbar():
	global show_statusbar ,status_bar
	if show_statusbar:
		status_bar.pack_forget()
		show_statusbar = False
	else:
		status_bar.pack(side = tk.BOTTOM)
		show_statusbar =True
view_menu.add_checkbutton(label="Tool Bar",onvalue = True,offvalue= 0,variable = show_toolbar,image = tool_bar_icon, compound=tk.LEFT,command = hide_toolbar)
view_menu.add_checkbutton(label="Status Bar",onvalue= 1,offvalue=False,variable = show_statusbar,image = status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
#Color Theme Radio Button
def change_theme():
	chosen_theme = color_theme_choice.get()
	chosen_tuple = color_dict.get(chosen_theme)
	fgcolor,bgcolor = chosen_tuple[0],chosen_tuple[1]
	text_editor.configure(background=bgcolor,foreground=fgcolor)
color_theme_menu.add_radiobutton(label="Light Default",image = light_default_icon, compound= tk.LEFT, variable=color_theme_choice,command= change_theme)
color_theme_menu.add_radiobutton(label="Light Plus",image = light_plus_icon, compound= tk.LEFT, variable=color_theme_choice,command= change_theme)
color_theme_menu.add_radiobutton(label="Dark",image = dark_icon, compound = tk.LEFT, variable=color_theme_choice,command= change_theme)
color_theme_menu.add_radiobutton(label="Red",image = red_icon, compound=tk.LEFT, variable= color_theme_choice,command= change_theme)
color_theme_menu.add_radiobutton(label="Monokai",image = monokai_icon, compound= tk.LEFT, variable = color_theme_choice,command= change_theme)
color_theme_menu.add_radiobutton(label="Night Blue",image= night_blue_icon, compound= tk.LEFT, variable= color_theme_choice,command= change_theme)
############ Cascade #################
main_menu.add_cascade(label="Files",menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='View', menu=view_menu)
main_menu.add_cascade(label="Color Theme", menu=color_theme_menu)
main_software.config(menu=main_menu)
#============End Menu Bar====================================================================================================================
### Bind Sortcuts ####
main_software.bind("<Control-n>",new_file)  
main_software.bind("<Control-o>",open_file)  
main_software.bind("<Control-s>",save_file)  
main_software.bind("<Control-Shift-s>",save_as_file)  
main_software.bind("<Control-q>",quit_file)  
main_software.bind("<Control-f>",find_func)    

main_software.mainloop()