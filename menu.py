from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import paramiko
import time

class Gerenciador(ScreenManager):
    pass
class Diretor(Screen):
    def exec(self):
        numero=int(self.ids.nfoto.text)
        tempo=str(self.ids.tfoto.text)
        iso=str(self.ids.isofoto.text)
        ssh=str(self.ids.ssh.text)
        senha=str(self.ids.senha.text)
        conect=paramiko.SSHClient()
        conect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conect.connect(hostname=ssh, username="maia", password=senha, port=int(9054))
        conect.exec_command('gphoto2 --auto-detect')
        conect.connect(hostname=ssh, username="maia", password=senha, port=int(9054))
        conect.exec_command('gphoto2 --set-config iso='+iso)
        conect.connect(hostname=ssh, username="maia", password=senha, port=int(9054))
        conect.exec_command('gphoto2 --set-config shutterspeed='+tempo)
        while numero>0:
            conect.connect(hostname=ssh, username="maia", password=senha, port=int(9054))        
            conect.exec_command('gphoto2 --capture-image')
            time. sleep(15)
            numero=numero-1
        
        

        print(numero,tempo,iso,ssh,senha)
class Selecao(Screen):
    pass

class Programa(App):
    def build(self):
        return Gerenciador()

Programa().run()
