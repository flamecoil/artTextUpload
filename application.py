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

        #FormatVariables
        self.textColumnWidth = 25
        
        #Storing all Data Plans
        self.DATAPLANS = [        
            ("300 MB" , 20),
            ("1 GB" , 25),
            ("3 GB" , 40),
            ("6 GB" , 70),
            ("10 GB" , 100),
            ("15 GB" , 130),
            ("20 GB" , 150),
            ("30 GB" , 225),
            ("40 GB" , 300),
            ("50 GB" , 375)
        
        ]
        #Data plan price threshhold - If greater than this number, there is a price break.
        self.dataPlanThreshold = 80

        #Mobile Share Plan 10 Device Threshold
        self.deviceLimit = 10

        #Declaration / Init of Variables
        self.dataPlanPrice = IntVar()
        self.dataPlanPrice.set(0)
        
        self.numNonContractSmartphones = IntVar()
        self.numNonContractSmartphones.set(0)
        
        self.numContractSmartphones = IntVar()
        self.numContractSmartphones.set(0)
        
        self.numBasicPhones = IntVar()
        self.numBasicPhones.set(0)

        self.numLaptops = IntVar()
        self.numLaptops.set(0)

        self.numTablets = IntVar()
        self.numTablets.set(0)

        self.numHomePhone = IntVar()
        self.numHomePhone.set(0)

        self.totalCost = IntVar()
        self.totalCost.set(0)
                
        

        #Plan Variables
        self.strVarDataPlan = StringVar()
        self.strVarDataPlan.set("")

        self.strVarMultiChar = StringVar()
        self.strVarMultiChar.set("")

        self.strVarWordVerif = StringVar()
        self.strVarWordVerif.set("")

        self.lblDataPlan = Label(self,
                                 text="Select Data Plan:",
                                 width=self.textColumnWidth,
                                 anchor=W,
                                 justify=LEFT)
        self.lblDataPlan.grid(row=0, column=0)

        #Radio Button configuration
        self.row = 1
        self.col = 0
        self.numPerRow = 4

        self.shiftCol = 1
        self.shiftRow = 0

        self.radioButtonTextWidth = 10
        

        #Laying out Radio Buttons. 
        for text, cost in self.DATAPLANS:
            if debug:
                print(self.row + self.shiftRow, self.col + self.shiftCol)
            self.radioButton = Radiobutton (self,
                                            text = text + " ($" + str(cost)+")",
                                            variable=self.dataPlanPrice,
                                            value=cost,
                                            width=self.radioButtonTextWidth,
                                            anchor=W,
                                            justify=LEFT,
                                            command=self.calculatePlan)
            
            self.radioButton.grid (row=self.row + self.shiftRow,
                                   column=self.col + self.shiftCol)            
            self.col = ((self.col + 1) % self.numPerRow)
            if self.col % self.numPerRow == 0:
                self.row += 1
        if debug:
            print ("End of Radio Buttons")

        #Selection of NonContract Smartphones
        self.col = 0
        self.row = self.row + 1

        if debug:
            print (self.row)
        
        self.lblNonContractSmartphones = Label(self,
                                               text="Non-Contract Smartphones:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=LEFT)
        self.lblNonContractSmartphones.grid(row=self.row, column=self.col)

        self.col += 1
        
        self.entNonContractSmartphones = Entry (self,
                                                state=NORMAL,
                                                textvariable=self.numNonContractSmartphones,
                                                width=5)
        self.entNonContractSmartphones.grid(row=self.row, column=self.col)

                #Add Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "+",
                                   command=self.addNonContractSmartphone,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

                #Sub Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "-",
                                   command=self.subNonContractSmartphone,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

        #Selection of 2-Yr Contract Smartphones
        self.row += 1
        self.col = 0
        
        if debug:
            print (self.row)
        
        self.lblContractSmartphones = Label(self,
                                               text="2-Yr.-Contract Smartphones:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=LEFT)
        self.lblContractSmartphones.grid(row=self.row, column=self.col)

        self.col += 1
        
        self.entContractSmartphones = Entry (self,
                                            state=NORMAL,
                                            textvariable=self.numContractSmartphones,
                                            width=5)
        self.entContractSmartphones.grid(row=self.row, column=self.col)

            #Add Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "+",
                                   command=self.addContractSmartphone,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

                #Sub Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "-",
                                   command=self.subContractSmartphone,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)
        
        #Number of Basic Phones self.numBasicPhones
        
        self.row += 1
        self.col = 0
        
        if debug:
            print (self.row)
        
        self.lblContractSmartPhones = Label(self,
                                               text="Basic & Messaging Phones:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=LEFT)
        self.lblContractSmartPhones.grid(row=self.row, column=self.col)

        self.col += 1
        
        self.entContractSmartPhones = Entry (self,
                                            state=NORMAL,
                                            textvariable=self.numBasicPhones,
                                            width=5)
        self.entContractSmartPhones.grid(row=self.row, column=self.col)

            #Add Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "+",
                                   command=self.addBasicPhones,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

                #Sub Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "-",
                                   command=self.subBasicPhones,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

        #Number of Laptops & Devices self.numLaptops
        
        self.row += 1
        self.col = 0
        
        if debug:
            print (self.row)
        
        self.lblContractSmartPhones = Label(self,
                                               text="Laptops & Netbooks:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=LEFT)
        self.lblContractSmartPhones.grid(row=self.row, column=self.col)

        self.col += 1
        
        self.entContractSmartPhones = Entry (self,
                                            state=NORMAL,
                                            textvariable=self.numLaptops,
                                            width=5)
        self.entContractSmartPhones.grid(row=self.row, column=self.col)

        #Add Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "+",
                                   command=self.addLaptops,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

                #Sub Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "-",
                                   command=self.subLaptops,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

        #Number of Tablets and Devices self.numTablets
        
        self.row += 1
        self.col = 0
        
        if debug:
            print (self.row)
        
        self.lblContractSmartPhones = Label(self,
                                               text="Tablets, Devices, Wearables:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=LEFT)
        self.lblContractSmartPhones.grid(row=self.row, column=self.col)

        self.col += 1
        
        self.entContractSmartPhones = Entry (self,
                                            state=NORMAL,
                                            textvariable=self.numTablets,
                                            width=5)
        self.entContractSmartPhones.grid(row=self.row, column=self.col)

        #Add Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "+",
                                   command=self.addTablets,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

                #Sub Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "-",
                                   command=self.subTablets,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

        #Number of HomePhone
        
        self.row += 1
        self.col = 0
        
        if debug:
            print (self.row)
        
        self.lblContractSmartPhones = Label(self,
                                               text="# Of Home Phones:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=LEFT)
        self.lblContractSmartPhones.grid(row=self.row, column=self.col)

        self.col += 1
        
        self.entContractSmartPhones = Entry (self,
                                            state=NORMAL,
                                            textvariable=self.numHomePhone,
                                            width=5)
        self.entContractSmartPhones.grid(row=self.row, column=self.col)

                #Add Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "+",
                                   command=self.addHomePhone,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

                #Sub Button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "-",
                                   command=self.subHomePhone,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

        #Total Display
        self.row += 1
        self.col = 0
        
        if debug:
            print (self.row)
        
        self.lblTotalCost = Label(self,
                                               text="Total Cost:",
                                               width=self.textColumnWidth,
                                               anchor=E,
                                               justify=RIGHT)
        self.lblTotalCost.grid(row=self.row, column=self.col)
        
        self.col += 1
        
        self.txtTotalCost = Text (self,
                                  width=4,
                                  height=1,
                                  state=DISABLED)
        self.txtTotalCost.grid(row=self.row, column=self.col)

        #Solve button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "Solve",
                                   command=self.calculatePlan,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)

        #Clear button
        self.col+=1
        self.btnCalculate = Button(self,
                                   text = "Clear",
                                   command=self.clearEntries,
                                   width=self.radioButtonTextWidth)
        self.btnCalculate.grid(row=self.row,
                               column=self.col)


        #End def init

    def clearEntries(self):
        #Clearing of Variables
        self.dataPlanPrice.set(0)
        
        self.numNonContractSmartphones.set(0)
        
        self.numContractSmartphones.set(0)
        
        self.numBasicPhones.set(0)

        self.numLaptops.set(0)

        self.numTablets.set(0)

        self.numHomePhone.set(0)

        self.totalCost.set(0)

        self.txtTotalCost.config(state = "normal")
        self.txtTotalCost.delete(0.0, END)
        self.txtTotalCost.insert(0.0, str(0))
        self.txtTotalCost.config(state = "disabled")
        
    def calculatePlan(self):
        #Get Values...
        planCost = 0
        
        #DataPlan
        if self.numDevices() > 0 and self.dataPlanPrice.get() > 0:
            planCost += self.dataPlanPrice.get()
            #Non Contract Smartphones
            if ( self.dataPlanPrice.get() <= self.dataPlanThreshold):
                perPhoneCost = 25
            else:
                perPhoneCost = 15
            planCost += self.numNonContractSmartphones.get() * perPhoneCost

            #2-Year Contract Smartphones
            perPhoneCost = 40
            planCost += self.numContractSmartphones.get() * perPhoneCost

            #Basic Phones
            if ( self.dataPlanPrice.get() <= self.dataPlanThreshold):
                perPhoneCost = 20
            else:
                perPhoneCost = 15
            planCost += self.numBasicPhones.get() * perPhoneCost
                    
            #Laptops and Netbooks
            perPhoneCost = 20
            planCost += self.numLaptops.get() * perPhoneCost

            #Tablets and Devices
            perPhoneCost = 10
            planCost += self.numTablets.get() * perPhoneCost

            #Home Phones
            perPhoneCost = 20
            planCost += self.numHomePhone.get() * perPhoneCost
       
        self.txtTotalCost.config(state = "normal")
        self.txtTotalCost.delete(0.0, END)
        self.txtTotalCost.insert(0.0, str(planCost))
        self.txtTotalCost.config(state = "disabled")

    def numDevices(self):
        numDevices = 0
        #Phones
        numDevices = self.numNonContractSmartphones.get() + self.numContractSmartphones.get()
        #if numDevices > 0:
        numDevices += self.numBasicPhones.get() + self.numLaptops.get() + self.numTablets.get() + self.numHomePhone.get()
        return numDevices

    #Addition Functions
    def addNonContractSmartphone(self):
        if(self.numDevices() < self.deviceLimit ):
            self.numNonContractSmartphones.set(self.numNonContractSmartphones.get() + 1)
            self.calculatePlan()
        return

    def addContractSmartphone(self):
        if(self.numDevices() < self.deviceLimit ):
            self.numContractSmartphones.set(self.numContractSmartphones.get() + 1)
            self.calculatePlan()        
        return

    def addBasicPhones(self):
        if(self.numDevices() < self.deviceLimit ):
            self.numBasicPhones.set(self.numBasicPhones.get() + 1)
            self.calculatePlan()
        return

    def addLaptops(self):
        if(self.numDevices() < self.deviceLimit ):
            self.numLaptops.set(self.numLaptops.get() + 1)
            self.calculatePlan()
        return

    def addTablets(self):
        if(self.numDevices() < self.deviceLimit ):
            self.numTablets.set(self.numTablets.get() + 1)
            self.calculatePlan()
        return

    def addHomePhone(self):
        if(self.numDevices() < self.deviceLimit ):
            self.numHomePhone.set(self.numHomePhone.get() + 1)
            self.calculatePlan()
        return
        
        
    #Subtraction functions
    def subNonContractSmartphone(self):
        if ( self.numNonContractSmartphones.get() > 0 ):
            self.numNonContractSmartphones.set(self.numNonContractSmartphones.get() - 1)
            self.calculatePlan()
        return

    def subContractSmartphone(self):
        if ( self.numContractSmartphones.get() > 0 ):
            self.numContractSmartphones.set(self.numContractSmartphones.get() - 1)
            self.calculatePlan()
        return

    def subBasicPhones(self):
        if ( self.numBasicPhones.get() > 0 ):
            self.numBasicPhones.set(self.numBasicPhones.get() - 1)
            self.calculatePlan()
        return

    def subLaptops(self):
        if ( self.numLaptops.get() > 0 ):
            self.numLaptops.set(self.numLaptops.get() - 1)
            self.calculatePlan()
        return

    def subTablets(self):
        if ( self.numTablets.get() > 0 ):
            self.numTablets.set(self.numTablets.get() - 1)
            self.calculatePlan()
        return

    def subHomePhone(self):
        if ( self.numHomePhone.get() > 0 ):
            self.numHomePhone.set(self.numHomePhone.get() - 1)
            self.calculatePlan()
        return
                
                
       
