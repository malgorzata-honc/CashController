from tkinter import *
from tkinter import ttk
from abc import abstractmethod
from tkcalendar import DateEntry
from matplotlib.figure import Figure


class Template_View(ttk.Frame):
    @abstractmethod
    def createWidgets():
        raise NotImplementedError


### FIRST VIEW - MAIN
class View(Template_View):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title("CashControler")
        self.createWidgets()

    def createWidgets(self):
        self.root.geometry ('925x500+300+200')
        self.root.configure(bg='#fff')
#Creating first frame with heading
        self.frame1 = Frame(self.root, width=900, height=50, bg='white', border=1)
        self.frame1.place(x=10,y=0)

        self.heading=Label(self.frame1,text='Apeczka', fg='#FFD200', bg='white', font=('Microsoft YaHei UI',20))
        self.heading.place(x=400, y = 0)
#Creating second frame with photobuttons, addcategory function and piggyimage
        self.frame2 = Frame(self.root, width=900, height=100, bg='white', border=1)
        self.frame2.place(x=10,y=60)

        global imgGraph
        imgGraph = PhotoImage(file='./images/graph.png')
        Label(self.frame2, image=imgGraph, bg='white')

        self.b1=Button (self.frame2, image = imgGraph,  border=1, bg='white')
        self.b1.place(x=50,y=0)

        global imgDetails
        imgDetails = PhotoImage(file='./images/table.png')
        Label(self.frame2, image=imgDetails, bg='white')

        self.b2=Button (self.frame2, image = imgDetails,  border=1, bg='white')
        self.b2.place(x=170,y=0)

        l0=Label(self.frame2,text="NOWA KATEGORIA: ",  fg='black', bg='white', font=('Microsoft YaHei UI Light',8))
        l0.place(x=600, y=0)

        self.new_category=StringVar()
        e0=Entry(self.frame2, textvariable=self.new_category, width = 25, fg = 'black', border = 0, bg='white', font=('Microsoft YaHei UI',10))
        e0.place(x=600, y=20)
        Frame(self.frame2, width=130, height=1, bg='black').place(x=590, y=40)

        self.b0=Button(self.frame2, text="DODAJ KATEGORIĘ",  width=16, pady=5,  bg= '#b2bf30', fg='white', border =1)
        self.b0.place(x=600, y =45)

        global imgPiggy
        imgPiggy = PhotoImage(file='./images/piggy.png')
        Label(self.frame2, image=imgPiggy, bg='white').place(x=750,y=0)
#Creating third frame on the left with labels, entry boxes and addbutton
        self.frame3 = Frame(self.root, width=450, height=300, bg='white', border=1)
        self.frame3.place(x=10,y=175)

        global imgMen
        imgMen = PhotoImage(file='./images/men.png')
        Label(self.frame3, image=imgMen, bg='white').place(x=0,y=30)

        l1=Label(self.frame3,text="NAZWA: ",  fg='black', bg='white', font=('Microsoft YaHei UI Light',12))
        l1.place(x=220, y=20)

        l2=Label(self.frame3,text="KATEGORIA: ", fg='black', bg='white', font=('Microsoft YaHei UI Light',12))
        l2.place(x=220, y=70)

        l3=Label(self.frame3,text="DATA: ", fg='black', bg='white', font=('Microsoft YaHei UI Light',12))
        l3.place(x=220, y=120)

        l4=Label(self.frame3,text="KWOTA: ", fg='black', bg='white', font=('Microsoft YaHei UI Light',12))
        l4.place(x=220, y=170)

        self.title_text=StringVar()
        e1=Entry(self.frame3, textvariable=self.title_text,  width = 25, fg = 'black', border = 0, bg='white', font=('Microsoft YaHei UI Light',11))
        e1.place(x=320, y=20)
        Frame(self.frame3, width=120, height=1, bg='black').place(x=320, y=47)

        self.category_text=StringVar()
        self.e2=ttk.Combobox(self.frame3, textvariable = self.category_text, width=12, font=('Microsoft YaHei UI Light',11))
        self.e2.place(x=320, y=70)

        self.date_text=StringVar()
        e3=DateEntry(self.frame3, selectmode='day', textvariable=self.date_text, date_pattern='dd/mm/yyyy', width=12, font=('Microsoft YaHei UI Light',11))
        e3.place(x=320, y=120)

        self.price_text=StringVar()
        e4=Entry(self.frame3, textvariable=self.price_text, width = 25, fg = 'black', border = 0, bg='white', font=('Microsoft YaHei UI Light',11))
        e4.place(x=320, y=170)
        Frame(self.frame3, width=120, height=1, bg='black').place(x=320, y=197)

        self.b4=Button (self.frame3, text="DODAJ",  width=50, pady=10,  bg= 'white', fg='#b2bf30', border =1)
        self.b4.place(x=50, y =230)

#Creating forth frame on the right with information about sum of expenses
        self.frame4 = Frame(self.root, width=400, height=300, bg='#68E1FD')
        self.frame4.place(x=480,y=170)

        self.l5=Label(self.frame4,text="SUMA WYDATKÓW: ",  fg='white', bg='#68E1FD', font=('Microsoft YaHei UI',16))
        self.l5.place(x=100, y=20)

        self.l6=Label(self.frame4,text='0',  fg='white', bg='#68E1FD', font=('Microsoft YaHei UI',30, 'bold'))
        self.l6.place(x=150, y=50)

#Creating fifth frame inside the forth for the piechart
        self.frame5 = Frame (self.frame4, width=370, height=200 ,bg = 'red')
        self.frame5.place(x=15,y=100)

        self.fig = Figure(facecolor='#68E1FD')
        self.ax = self.fig.add_subplot(111)
        self.fig.set_size_inches(4,2)
        self.colors = ['#FFD200','#B2BF30','#57a1f8']


    def getCategoryName(self):
        return self.new_category.get()
    def getName(self):
        return self.title_text.get()
    def getCategory(self):
        return self.category_text.get()
    def getDate(self):
        return self.date_text.get()
    def getPrice(self):
        return self.price_text.get()

### SECOND VIEW OF THE DETAILS
class Details(Template_View):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title("Szczegóły")
        self.root.geometry ('800x400+300+200')
        self.root.configure(bg='#fff')
        self.createWidgets()

    def createWidgets(self):
#Creating first frame with treeview
         
        frame1_1 = Frame(self.root)
        frame1_1.pack(padx=5)

        scrollbar = Scrollbar(frame1_1, orient='vertical')
        scrollbar.pack(side="right", fill="y")

        self.tv = ttk.Treeview(frame1_1, columns=(1, 2, 3, 4, 5), show='headings', height=8, yscrollcommand=scrollbar.set, selectmode="extended")
        self.tv.pack()
        scrollbar.configure(bg='white',command=self.tv.yview)
        self.tv.config(yscrollcommand=scrollbar.set)

        style = ttk.Style(self.tv)
        style.theme_use('clam')
        style.configure('Treeview.Heading', foreground = 'black', background = 'white', font=('Microsoft YaHei UI Light', 12))
        style.configure('Treeview', fg='black', bg='white', font=('Microsoft YaHei UI Light',10))
        style.layout ('Treeview', [('clam.Treeview.treearea', {'sticky':'nswe'})])

        self.tv.column(1, anchor=CENTER, stretch=NO, width=100)
        self.tv.column(2, anchor=CENTER, width=150)
        self.tv.column(3, anchor=CENTER, width=150)
        self.tv.column(4, anchor=CENTER, width=150)
        self.tv.column(5, anchor=CENTER, width=150)
        self.tv.heading(1, text="Lp.")
        self.tv.heading(2, text="Nazwa")
        self.tv.heading(3, text="Kategoria")
        self.tv.heading(4, text="Data")
        self.tv.heading(5, text="Kwota")
        
#Creating second frame for buttons and search entry
        self.frame1_2 = Frame(self.root, width=750, height=170, bg='white', border=1)
        self.frame1_2.place(x=20,y=200)

        self.b1_1=Button (self.frame1_2, text="USUŃ",  width=25, pady=10,  bg= '#b2bf30', fg='white', border =1)
        self.b1_1.place(x=260, y =55)

        self.b1_2=Button (self.frame1_2, text="SZUKAJ",  width=25, pady=10,  bg= '#b2bf30', fg='white', border =1)
        self.b1_2.place(x=40, y =55)

        self.e_search=Entry(self.frame1_2,  fg = 'black', border = 1, bg='white', font=('Microsoft YaHei UI Light',11))
        self.e_search.place (x= 50, y=20 )

        self.b1_3=Button (self.frame1_2, text="POKAŻ WSZYSTKIE",  width=15, pady=5,  bg= '#b2bf30', fg='white', border =1)
        self.b1_3.place(x=600, y =20)

