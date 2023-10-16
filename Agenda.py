from tkinter import *
from Cor import Cor
from tkinter import ttk
from banco_agenda import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


root=Tk()
cores=Cor()

class Relatorio():
    def printContato(self):
        webbrowser.open(".\contatos.pdf")
    def gerar(self):
        self.arq=canvas.Canvas(".\contatos.pdf")
        self.idRel=self.id_espaco.get()
        self.nomeRel=self.nome_espaco.get()
        self.emailRel=self.email_espaco.get()
        self.teleRel=self.tel_espaco.get()
        self.arq.setFont("Helvetica-Bold",24)
        self.arq.drawString(200, 790,'--------INFO-------')
        self.arq.setFont("Helvetica",12)
        self.arq.drawString(80,680,'Nome: '+self.nomeRel + "   Email:  "+self.emailRel+"    Telefone:  "+self.teleRel)




class Funcoes(Relatorio):
    def __init__(self):
        self.aux
        self.listau=[]

    def limpa_tela(self):
        self.nome_espaco.delete(0,END)
        self.email_espaco.delete(0,END)
        self.tel_espaco.delete(0,END)
        self.id_espaco.delete(0,END)
      
    def Menubar(self):
        mbarra=Menu(self.root)
        self.root.config(menu=mbarra)
        filemenu=Menu(mbarra)
        filemenu2=Menu(mbarra)
        def Quit():self.root.destroy()
    
        mbarra.add_cascade(label="opcões",menu=filemenu2)
        filemenu2.add_command(label="INFO", command=self.gerar)
        filemenu2.add_command(label="sair", command=Quit)
        
    def insere(self):

        tenta=Conexao()
        tenta.insere(self.nome_espaco.get(), self.email_espaco.get(), self.tel_espaco.get())
        self.lista_tab()
        self.limpa_tela()
    def buscar(self):
        tenta=Conexao()
        self.lista.delete(*self.lista.get_children())
        self.nome_espaco.insert(END, '%')
        if self.nome_espaco.get()=='%':
            self.lista_tab()
        else:  
            lrel=tenta.busca(self.nome_espaco.get())
            for i in lrel:
                    self.lista.insert("", END, values=i)
        self.limpa_tela()
        
    def lista_tab(self):
        tenta=Conexao()
        self.lista.delete(*self.lista.get_children())
        listarr=tenta.lista_toda()
     
        for i in listarr:
         
           self.lista.insert("",END,values=i)

        self.limpa_tela()
        
       

    def deleta(self):
        tenta=Conexao()
        print(self.aux)
        tenta.deleta(self.aux)
        self.lista_tab()

        
    def clique_duplo(self, event):
        self.limpa_tela()
        self.lista.selection()
    
        for n in self.lista.selection():
            col1,col2,col3,col4=self.lista.item(n,'values')
            self.id_espaco.insert(END, col1)
            self.nome_espaco.insert(END, col2)
            self.email_espaco.insert(END, col3)
            self.tel_espaco.insert(END, col4)
            
        self.aux=self.id_espaco.get()
    def atualiza(self):
        tenta=Conexao()
        tenta.atualiza(self.nome_espaco.get(),self.email_espaco.get(),self.tel_espaco.get(),self.aux)
        self.lista_tab()
        self.limpa_tela()
       

        
class ApplicationApp(Funcoes):
    def __init__(self):
        self.root=root
        self.tela()
        self.frame_tela()
        self.botao()
        self.labels()
        self.dados_contato()
        self.listar()
        self.lista_tab()
        self.Menubar()
        root.mainloop()
        
    def tela(self):
        'titulo'
        self.root.title("Hello world")
        'fundo'
        self.root.configure(background=cores.fundo())
        'tamanho'
        self.root.geometry("700x456")
        'tamanho diminuir aumentar(HOZ/VERT)'
        self.root.resizable(True, True)
        'tamanho maximp'
        self.root.maxsize(width=800,height=500)
        'tamanho minimo'
        self.root.minsize(width=600,height=300)
    def frame_tela(self):
        #tela grande
        self.frames=Frame(self.root,bd=4,bg=cores.telas_grande(),highlightbackground=cores.telas_grande(),highlightthickness=2)
        self.frames.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.4)

        #tela pequena
        self.frames2=Frame( self.root,bg=cores.tela_titulo(),highlightbackground=cores.tela_titulo(),highlightthickness=2)
        self.frames2.place(relx=0.1, rely=0.5, relwidth=0.80, relheight=0.4)

    def labels(self):
        #nome
        self.lab_cod2=Label(self.frames, text="Nome",bg=cores.telas_grande(),fg=cores.letras(),font=('verdana',8,'bold'))
        self.lab_cod2.place(relx=0.03, rely=0.1)
        #telefone
        self.lab_cod4=Label(self.frames, text="Tel",bg=cores.telas_grande(),fg=cores.letras(),font=('verdana',8,'bold'))
        self.lab_cod4.place(relx=0.03, rely=0.3)
        #email
        self.lab_cod3=Label(self.frames, text="Email",bg=cores.telas_grande(),fg=cores.letras(),font=('verdana',8,'bold'))
        self.lab_cod3.place(relx=0.03, rely=0.5)
        #id
        self.lab_cod3=Label(self.frames, text="Id",bg=cores.telas_grande(),fg=cores.letras(),font=('verdana',8,'bold'))
        self.lab_cod3.place(relx=0.03, rely=0.65)
     
        
    def dados_contato(self):
        
        #nome
        self.nome_espaco=Entry(self.frames,bg=cores.label_fundo())
        self.nome_espaco.place(relx=0.15, rely=0.1,relwidth=0.4, relheight=0.1)
        #espaco
        self.tel_espaco=Entry(self.frames,bg=cores.label_fundo())
        self.tel_espaco.place(relx=0.15, rely=0.3,relwidth=0.4, relheight=0.1)
        #email
        self.email_espaco=Entry(self.frames,bg=cores.label_fundo())
        self.email_espaco.place(relx=0.15, rely=0.5,relwidth=0.8, relheight=0.1)
        #id
        self.id_espaco=Entry(self.frames,bg=cores.label_fundo())
      
        self.id_espaco.place(relx=0.15, rely=0.65,relwidth=0.09, relheight=0.09)
        
    def botao(self):
        #bg=background,fg=cor de letra
        #busca
        self.botao3=Button(self.frames, text="Pesquisar",bd=4,bg=cores.botao(),fg="black",font=('verdana',8,'bold'),command=self.buscar)
        self.botao3.place(relx=0.62,rely=0.1,relwidth=0.15, relheight=0.12)
        #inserir
        self.botao=Button(self.frames, text="inserir",bd=4,bg=cores.botao(),fg="black",font=('verdana',8,'bold'),command=self.insere)
        self.botao.place(relx=0.10,rely=0.8,relwidth=0.15, relheight=0.13)
        #excluir
        self.botao2=Button(self.frames, text="excluir",bd=4,bg=cores.botao(),fg="black",font=('verdana',8,'bold'),command=self.deleta)
        self.botao2.place(relx=0.3,rely=0.8,relwidth=0.15, relheight=0.13)
        #atualizar
        self.botao3=Button(self.frames, text="atualizar",bd=4,bg=cores.botao(),fg="black",font=('verdana',8,'bold'),command=self.atualiza)
        self.botao3.place(relx=0.5,rely=0.8,relwidth=0.15, relheight=0.13)
        #limpar
        self.botao3=Button(self.frames, text="limpar",bd=4,bg=cores.botao(),fg="black",font=('verdana',8,'bold'),command=self.limpa_tela)
        self.botao3.place(relx=0.7,rely=0.8,relwidth=0.15, relheight=0.13)

    def listar(self):
        self.lista=ttk.Treeview(self.frames2,height=3,column=('co1','co2','co3','col4'))
        self.lista.heading("#0",text="")
        self.lista.heading("#1",text="Id")
        self.lista.heading("#2",text="Nome")
        self.lista.heading("#3",text="Email")
        self.lista.heading("#4",text="Telefone")
        self.lista.column("#0",width=1,stretch=NO)
        self.lista.column("#1",width=50)
        self.lista.column("#2",width=50)
        self.lista.column("#3",width=200)
        self.lista.column("#4",width=70)
        self.lista.place(relx=0.01, rely=0.1, relwidth=0.93, relheight=0.8)
        self.scrollB=Scrollbar(self.frames2,orient='vertical')
        self.lista.configure(yscroll=self.scrollB.set)
        self.scrollB.place(relx=0.95, rely=0.1, relwidth=0.04, relheight=0.8)
        self.lista.bind("<Double-1>", self.clique_duplo)

ApplicationApp()
        

