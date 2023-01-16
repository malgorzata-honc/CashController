from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from view import View, Details
from model import Model



class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.b0["command"] = self.addCategory
        self.view.b1["command"] = self.showGraph
        self.view.b2["command"] = self.showDetails
        self.view.b4["command"] = self.addToDB
        self.createPieChar()
        self.showSumOfExpenses()
        self.showCategories()


    def addCategory (self):
        new_category = self.view.getCategoryName()
        self.model.addCategory(new_category)
        messagebox.showinfo('Zapis', 'Zapisano do bazy')
        self.showCategories()

    def showGraph(self):
        kwoty = []
        daty = []
        expenses= self.model.getGraphData()

        for row in expenses:
            daty.append(row[0])
            kwoty.append(row[1])

        fig, ax1 = plt.subplots()
        ax1.plot(daty, kwoty, color='#B2BF30', marker='o',  linewidth=2, markersize=5)
        plt.title("Wykres sumy wydatków w czasie")
        plt.xlabel("Data")
        plt.ylabel("Suma wydatków")
        plt.show()

    def showCategories(self):
        categories = self.model.getCategories()
        self.view.e2['values']= categories

    def createPieChar(self):
        sumy_kwot = []
        kategorie = []
        data = self.model.getPieChartData()

        for row in data:
            sumy_kwot.append(row[0])
            kategorie.append(row[1])

            print (sumy_kwot)
            print (kategorie)

        self.view.ax.pie(sumy_kwot, labels = kategorie, colors=self.view.colors, autopct='%1.1f%%', textprops={'fontsize': 11, 'color': 'white'})
        chart1 = FigureCanvasTkAgg(self.view.fig,self.view.frame5)
        chart1.get_tk_widget().pack()

    def showSumOfExpenses(self):
        sum = self.model.getExpensesSum()
        self.view.l6["text"] = sum

    def addToDB(self):
        name = self.view.getName()
        category = self.view.getCategory()
        date = self.view.getDate()
        price = self.view.getPrice()
        self.model.addExpense(name, category, date, price)
        messagebox.showinfo('Zapis', 'Zapisano do bazy')

        self.createPieChar()
        self.showSumOfExpenses()

    def showDetails(self):
        self.top=Details(Toplevel())
        
        self.showDetailsOfDetails()
        self.top.b1_3["command"] = self.showDetailsOfDetails
        self.top.tv.bind('<<ListboxSelect>>', self.getSelectedRow)
        self.top.b1_1["command"] = self.deleteRecord
        self.top.b1_2["command"]= self.searchRecord

   
    def showDetailsOfDetails(self):
        global count
        count =0
        for record in self.top.tv.get_children():
            self.top.tv.delete(record)
        data_list =[]
        data_list.clear()
        data_list=self.model.getAllExpenses()
        for row in data_list:
            if count %2==0:
                self.top.tv.insert(parent='', index='end', iid=count, text ='', values=(row[0], row[1], row[2], row[3], row[4]), tags = ('evenrow',))
            else:
                self.top.tv.insert(parent='', index='end', iid=count, text ='', values=(row[0], row[1], row[2], row[3], row[4]), tags = ('oddrow',))
            count+=1

    def searchRecord(self):
        global count
        count = 0
        for record in self.top.tv.get_children():
            self.top.tv.delete(record)
        for row in self.model.searchExpense(self.top.e_search.get(), self.top.e_search.get(), self.top.e_search.get(), self.top.e_search.get(),):
            if count %2==0:
                self.top.tv.insert(parent='', index='end', iid=count, text ='', values=(row[0], row[1], row[2], row[3], row[4]), tags = ('evenrow',))
            else:
                self.top.tv.insert(parent='', index='end', iid=count, text ='', values=(row[0], row[1], row[2], row[3], row[4]), tags = ('oddrow',))
            count+=1

    def deleteRecord(self):
        self.getSelectedRow()
        self.model.deleteExpense(self.selected_tuple[0])
        messagebox.showinfo( 'Zapis', 'Pozycja została usunięta - więcej pieniędzy w portfelu?', parent = self.top) 

        self.showDetailsOfDetails()
        

    def getSelectedRow(self):
        self.index=self.top.tv.focus()
        self.selected_tuple=self.top.tv.item(self.index, 'values')
        print (self.selected_tuple)
