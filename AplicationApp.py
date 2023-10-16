from tkinter import *
from Cor import Cor

root=Tk()

cores=Cor()
class ApplicationApp():

    def __init__(self):
        self.root=root
        self.tela()
        self.frame_tela()
        self.botao()
        self.labels()
        self.login_email()
        self.menubar()
        root.mainloop()
        
    def menubar(self):
        mbarra=Menu(self.root)
        self.root.config(menu=mbarra)
        filemenu=Menu(mbarra)
        filemenu2=Menu(mbarra)
        def Quit():self.root.destroy()
        
        mbarra.add_cascade(label="sobre",menu=filemenu)
        mbarra.add_cascade(label="opcoes",menu=filemenu2)
        filemenu2.add_command(label="sair", command=Quit)
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
        self.frames.place(relx=0.3, rely=0.2, relwidth=0.40, relheight=0.7)

    #tela pequena
        self.frames2=Frame( self.frames,bg=cores.tela_titulo(),highlightthickness=2)
        self.frames2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    def botao(self):
        #bg=background,fg=cor de letra
        #botao enter
        self.botao=Button(self.frames, text="enter",bd=4,bg=cores.botao(),fg="black",font=('verdana',8,'bold'))
        self.botao.place(relx=0.30,rely=0.8,relwidth=0.40, relheight=0.10)
    def labels(self):
        #titulo
        self.lab_cod=Label(self.frames2, text="Login",bd=4,bg=cores.tela_titulo(),fg="black",font=('verdana',25,'bold'))
        self.lab_cod.place(relx=0.1, rely=0.1)
        #email
        self.lab_cod2=Label(self.frames, text="Email",bg=cores.telas_grande(),fg=cores.letras(),font=('verdana',8,'bold'))
        self.lab_cod2.place(relx=0.03, rely=0.4)
        #senha
        self.lab_cod3=Label(self.frames, text="Senha",bg=cores.telas_grande(),fg=cores.letras(),font=('verdana',8,'bold'))
        self.lab_cod3.place(relx=0.03, rely=0.6)
    def login_email(self):
        #email
        self.login=Entry(self.frames,bg=cores.label_fundo())
        self.login.place(relx=0.2, rely=0.4,relwidth=0.7, relheight=0.06)
        #senha
        self.senha=Entry(self.frames,bg=cores.label_fundo())
        self.senha.place(relx=0.2, rely=0.6,relwidth=0.7, relheight=0.06)
ApplicationApp()
        

