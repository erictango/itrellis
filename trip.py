from tkinter import * 


class TripCalculator:
    
    def __init__(self):
        '''
        Create a new trip caclulator
        The UI is built here.
        '''
        self.root = Tk()
    
        self.root.wm_title('Trip Calculator')
        frame1 = Frame(self.root)
        frame1.pack()
        
        self.clear1 = True
        self.clear2 = True
        
        Label(frame1, text="Traveller Names").grid(row=0, column=0, sticky=W)
        Label(frame1, text="Expenses covered").grid(row=0, column=1, sticky=W)
        
        self.tb1 = Text(frame1, height=15, width=40 )
        self.tb2 = Text(frame1, height=15, width=40)
        
        self.tb1.grid(row=1, column=0)
        self.tb2.grid(row=1, column=1)
        self.tb1.insert(END, "Please enter the names of all those who went on the trip. Each line should have just one name.")
        self.tb2.insert(END, ("Please enter the expenses covered by each participant. "
                    "Please make sure to follow the same order as the names of participants. "
                    "Separate multiple expenditures with a , and leave out the $ symbol."))
        
        self.tb1.bind("<Button-1>", self.clear_text1)
        self.tb2.bind("<Button-1>", self.clear_text2)

        btn = Button(frame1, text='Calculate')
        btn.grid(row=2,columnspan=2)
        btn.bind('<Button-1>', self.click_handler)
        
        self.results = Text(frame1, height=15, width=80)
        self.results.grid(row=3, columnspan=2)
        
        
    def start(self):
        '''
        Starts the main loop.
        
        Which keeps the UI visible until it's shut down
        '''
        self.root.mainloop()
        
    def click_handler(self, event):
        '''
        Handler for the calculate button
        '''
        resp = self.calculate(self.tb1.get('1.0', END), self.tb2.get('1.0', END))
        self.results.delete('1.0',END)
        self.results.insert(END, resp)
        
        
    def calculate(self, txt1, txt2):
        '''
        Makes the calculation
        
        txt1 is a string containing a new line seprated list of participant names
        txt2 is a string with each line containing a list of numbers separated by
             comma. The lines are separated by the new line character
        '''
        
        names = self.clean_up(txt1)
        expenses = self.clean_up(txt2)
        
        if len(expenses) != len(names):
            return 'The number of entries in the two datasets do not match'
        
        for i in range(len(expenses)) :
            try:
                expenses[i] = sum([float(x.strip()) for x in expenses[i].split(',')])
            except ValueError:
                return "Error in reading expenses, please make sure you have entered valid numbers."
        
        total = sum(expenses)
        average = total/len(expenses)
    
        resp = []
        for i in range(len(names)):
            paid = expenses[i]
            if paid > average:
                difference = paid - average
                # print the name and the amount rounded to the nearest cent.
                resp.append("Others owe {0} ${1:.2f}".format(names[i], difference ))
            
            elif paid < average:
                difference = average - paid
                resp.append("{0} owes others ${1:.2f}".format(names[i], difference ))
        
            else:
                resp.append("{0} has paid the exact amount".format(names[1]))
                
                
        return "\n".join(resp)
    
    
    def clean_up(self, txt):
        '''
        Cleans up a text by removing blank lines
        '''
        return [x.strip() for x in txt.split('\n') if x.strip()]
    
    def clear_text1(self, event):
        '''
        Clears the first text box
        '''
        if self.clear1:
            self.clear1 = False
            self.tb1.delete('1.0',END)
            
    
    def clear_text2(self, event):
        '''
        Clears the second text box
        '''
        if self.clear2:
            self.clear2 = False
            self.tb2.delete('1.0',END)


if __name__ == '__main__':
    trip = TripCalculator()
    trip.start()