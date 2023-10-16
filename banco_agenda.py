import mysql.connector

class Conexao:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost',database='agenda_python',user='root',password='mysql02POPP')
        self.cursor=self.con.cursor()
    def cria_tab(self):
        cria_tab="""CREATE TABLE tab_agenda(IdNome int primary key AUTO_INCREMENT,Nome VARCHAR(700) NOT NULL,
                    Email VARCHAR(70) NOT NULL,
                    Telefone int(24) NOT NULL)"""
        try:
            if self.con.is_connected():
                self.cursor.execute(cria_tab)
                print("Sucesso ")
        except mysql.connector.Error as erro:
            print("falha", erro)


    def desconecta(self):
         if self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("Encerrando....")



    def conecta(self):
        try:
            if self.con.is_connected():
                db_info=self.con.get_server_info()
                #execute este comando se a tabela nao existe->self.cria_tab()
                print("Connectdao",db_info)
                print("Sucesso ")
        except mysql.connector.Error as erro:
            print("falha".format(erro))
    def lista_toda(self):
        try:
            self.conecta()
            comando="""SELECT * FROM tab_agenda ORDER BY Nome ASC"""

            self.cursor.execute(comando)
            retorna=self.cursor.fetchall()
            print(retorna)
            self.desconecta()
            return retorna
        except mysql.connector.Error as erro:
            print("falhou a seleção da lista total ", erro)
        finally:
            self.desconecta()
    def atualiza(self, nome, email, tel,idd):
        try:
            
            self.conecta()
            comando2="""UPDATE tab_agenda SET Nome =  """'\''+nome+'\','+ """Email = """+'\''+email+'\','+"""Telefone = """+tel+""" WHERE IdNome = """+idd
            print(comando2)
            self.cursor.execute(comando2)
            self.con.commit()
            print("Sucesso ")
        except mysql.connector.Error as erro:
            print("falhou a insersao ", erro)
        finally:
            self.desconecta()
    def insere(self, nome, email, tel):
        try:
            
            self.conecta()
            dads='\''+nome+'\','+ '\''+email+'\','+tel+')'
            #dads='\''+nome+'\','+ '\''+email+'\','+tel+'\''+ ')'
            print(dads)
            dados=(nome,email,tel)
        
            comando2="""INSERT INTO tab_agenda(Nome, Email, Telefone) VALUES("""
            
            print(nome,email,tel)
            
            self.cursor.execute(comando2 +dads)
            self.con.commit()
            print("Sucesso ")
        except mysql.connector.Error as erro:
            print("falhou a insersao ", erro)
        finally:
            self.desconecta()

    def deleta(self, idd):
        try:
            self.conecta()
            
            comando2="""DELETE  FROM tab_agenda WHERE IdNome= %s"""
            dado1=(idd,)
            self.cursor.execute(comando2,dado1)
            self.con.commit()
            
            print("Sucesso ")
            self.desconecta()
            
        except mysql.connector.Error as erro:
            print("falhou o comando deletar  ", erro)
        finally:
            self.desconecta()


    def busca(self,dado):
        try:
            self.conecta()
            comando="""SELECT IdNome, Nome, Email, Telefone FROM tab_agenda WHERE Nome like %s ORDER BY Nome ASC """
            dado1=(dado,)
            self.cursor.execute(comando,dado1)
            retorna=self.cursor.fetchall()
            print(retorna)
            print("Sucesso ")
            return retorna
        except mysql.connector.Error as erro:
            print("falhou o comando buscar  ", erro)
        finally:
            self.desconecta()


            

