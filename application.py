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
		
		self.charLabelList = list()
		
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
		
		#Characters
		self.row += 1
		self.lblPrompt = Label(self, text="Characters", anchor=W, width=self.labelWidth)
		self.lblPrompt.grid(row=self.row, column=self.col)
		
		self.col+=1
		self.index = 0
		while self.index < self.characterCount:
			self.row+=1
			#Character name
			self.lblPrompt = Label(self, text="Name:", anchor=W, width=self.labelWidth)
			self.lblPrompt.grid(row=self.row, column=self.col)
			#Entry for Name
			
			#LOOP for Number of Links
			#Adjust for 
			#Link to Character
			#Owner of Character
				#LOOP for Num_Sites
				#Dropdown listing Site Types
				# Specific sites, or general URL
			self.index+=1
	    
		#Artist
		self.row += 1
		self.lblPrompt = Label(self, text="Artists", anchor=W,width=self.labelWidth)
		self.lblPrompt.grid(row=self.row, column=self.col)
			#LOOP for number of Links
				#Dropdown - Type of Link 
				#Website Username