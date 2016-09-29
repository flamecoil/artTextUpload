"""
Art Text Uploader
v0.1
@flamecoil
"""
from tkinter import *

debug = False;

class Application(Frame):
	
	
    
	def __init__(self, master):
		super().__init__(master)
		self.grid()
		
		self.characterCount = 2
		self.artistCount = 1
		
		self.charStringList = list()
		self.refStringList = list()
		
		self.row = 0
		self.col = 0
		self.labelWidth = 10		
		#Description of Artwork 
		#SCROLLBAR?
		"""
		self.scrollbar = Scrollbar(self)
		self.scrollbar.grid(row=self.row, column=self.col)		
		
		self.textWidth = 80
		self.textHeight = 40
		self.txtDisplayWords = Text(self, width=self.textWidth, height=self.textHeight, wrap = WORD, yscrollcommand=self.scrollbar.set)
		self.txtDisplayWords.grid(row=self.row, column=self.col)	 
		"""
		#Loop for Number of Characters
		self.index = 0
		while self.index < self.characterCount:
			self.charString = StringVar()
			self.charStringList.append(self.charString)
			
			self.refString = StringVar()
			self.refStringList.append(self.refString)
			self.index+=1
		
		#Characters
		self.row += 1
		self.lblPrompt = Label(self, text="Characters: " + str(self.characterCount), anchor=W, width=self.labelWidth)
		self.lblPrompt.grid(row=self.row, column=self.col)
		
		self.col+=1
		self.index = 0
		while self.index < self.characterCount:
			self.row+=1
			#Character name
			self.lblPrompt = Label(self, text="Name:", anchor=W, width=self.labelWidth)
			self.lblPrompt.grid(row=self.row, column=self.col)
			#Entry for Name
			self.entName1 = Entry(self, state=NORMAL, textvariable=self.charStringList[self.index])
			self.entName1.grid(row=self.row, column=self.col+1)
			#Link to Reference
			self.row+=1
			self.lblPrompt = Label(self, text="Reference URL:", anchor=W, width=self.labelWidth)
			self.lblPrompt.grid(row=self.row, column=self.col)
			#Entry for Name
			self.entName1 = Entry(self, state=NORMAL, textvariable=self.refStringList[self.index])
			self.entName1.grid(row=self.row, column=self.col+1)
			#LOOP for Number of Links - USERNAMES
			self.row+=1
			self.lblPrompt = Label(self, text="Usernames", anchor=W, width=self.labelWidth)
			self.lblPrompt.grid(row=self.row, column=self.col)
			#Adjust for 
			#Link to Character Owner
			#Owner of Character
			self.row+=1
			self.lblPrompt = Label(self, text="http://www.furaffinity.net/user/", anchor=E, width=self.labelWidth)
			self.lblPrompt.grid(row=self.row, column=self.col)			
			
			
			#LATER VERSIONS
				#LOOP for Num_Sites
				#Dropdown listing Site Types
				# Specific sites, or general URL
			self.index+=1
	    
		#Artist
		self.col = 0
		self.row += 1
		self.lblPrompt = Label(self, text="Artists", anchor=W,width=self.labelWidth)
		self.lblPrompt.grid(row=self.row, column=self.col)
			#LOOP for number of Links
				#Dropdown - Type of Link 
				#Website Username