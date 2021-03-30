from tkinter import *
import os

c=os.path.dirname(__file__)
nomeArquivo=c+"\\datas.txt"


def impDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("\n Dia de nascimento:%s" % vnasc .get())
    arquivo.write("\n Mês de nascimento:%s" % vmes.get())
    arquivo.write("\n Ano de nascimento:%s" % vano.get())
    arquivo.write("\n Estamos no ano de:%s" % vemq.get())
    arquivo.close()



app = Tk()
app.title('Verificação de segurança')
app.geometry("600x400")
app.configure(background="#dde")

texto=Label(app,text="Dia de nascimento",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=200,height=20)
vnasc=Entry(app)
vnasc.place(x=10,y=30,width=200,height=20)

texto=Label(app,text="Mês de nascimento",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=200,height=20)
vmes=Entry(app)
vmes.place(x=10,y=80,width=200,height=20)

texto=Label(app,text="Ano de nascimento",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=200,height=20)
vano=Entry(app)
vano.place(x=10,y=130,width=200,height=20)

texto=Label(app,text="Em que ano estamos?",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=200,height=20)
vemq=Entry(app)
vemq.place(x=10,y=180,width=200,height=20)

Button(app,text="Acessar",command=impDados).place(x=10,y=210,width=100,height=20)






app.mainloop()