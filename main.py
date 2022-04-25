from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from controller.DialogConfirmacao import OpenDialog

Builder.load_file("view/home.kv")
Builder.load_file("view/jogo_1_p.kv")
Builder.load_file("view/jogo_2_p.kv")
Builder.load_file("view/confirm_dialog.kv")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TelaDoisJogadores(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(TelaDoisJogadores(name='doisjogadores'))

class MeuAplicativo(App):

    correntes = {
    (1,6) : "5 cartas",
    (7,12) : "4 Cartas",
    (13,18) : "3 Cartas",
    (19,24) : "2 Cartas"
    }

    def build(self):
        self.incializar()
        return sm
    
    def mudar_tela(self, nome_da_tela):
        sm.current = nome_da_tela
    
    def aumentar_corrente(self):
        if (self.qtd_corrente < 24):
            self.qtd_corrente = self.qtd_corrente + 1
            self.atualizar_corrente()
    
    def diminuir_corrente(self):
        if (self.qtd_corrente > 0):
            self.qtd_corrente = self.qtd_corrente - 1
            self.atualizar_corrente()

    def aumentar_aembar(self):
        self.qtd_aembar = self.qtd_aembar + 1
        self.atualizar_aembar()
    
    def diminuir_aembar(self):
        if (self.qtd_aembar > 0):
            self.qtd_aembar = self.qtd_aembar - 1
            self.atualizar_aembar()

    def aumentar_aembar_para_forjar(self):
        self.qtd_aembar_para_forjar = self.qtd_aembar_para_forjar + 1
        self.atualizar_aembar_para_forjar()
    
    def diminuir_aembar_para_forjar(self):
        if (self.qtd_aembar_para_forjar > 0):
            self.qtd_aembar_para_forjar = self.qtd_aembar_para_forjar - 1
            self.atualizar_aembar_para_forjar()
    
    def atualizar_corrente(self):
        self.root.get_screen("settings").ids["lb_qtd_corrente"].text = str(self.qtd_corrente)
        for item, valor in self.correntes.items():
            if(self.qtd_corrente == 0):
                self.root.get_screen("settings").ids["lb_qtd_cartas"].text = "(6 cartas)"
                break
            elif(item[0] <= self.qtd_corrente <= item[1]):
                self.root.get_screen("settings").ids["lb_qtd_cartas"].text = f"({valor})"
                break
    
    def atualizar_aembar(self):
        self.root.get_screen("settings").ids["lb_qtd_aembar"].text = str(self.qtd_aembar)

    def atualizar_aembar_para_forjar(self):
        self.root.get_screen("settings").ids["lb_qtd_aembar_para_forjar"].text = str(self.qtd_aembar_para_forjar)

    def forjar_chave(self):
        if (self.qtd_aembar >= self.qtd_aembar_para_forjar):
            self.qtd_aembar = self.qtd_aembar - self.qtd_aembar_para_forjar
            self.atualizar_aembar()
            
            if(self.chave_1_forjada):
                if(self.chave_2_forjada):
                    if(self.chave_3_forjada):
                        pass
                    else:
                        self.root.get_screen("settings").ids["chave3"].source = "imagens/chave_amarela-forjada.png"
                        self.chave_3_forjada = True
                        obj = OpenDialog("Parabens você venceu a partida!\nO que deseja fazer agora?", "fimdojogo", "Resetar", "Sair do app")
                        obj.open()
                else:
                    self.root.get_screen("settings").ids["chave2"].source = "imagens/chave_amarela-forjada.png"
                    self.chave_2_forjada = True
            else:
                self.root.get_screen("settings").ids["chave1"].source = "imagens/chave_amarela-forjada.png"
                self.chave_1_forjada = True
    
    def incializar(self):
        self.qtd_corrente = 0
        self.qtd_aembar_para_forjar = 6
        self.qtd_aembar = 0
        self.chave_1_forjada = False
        self.chave_2_forjada = False
        self.chave_3_forjada = False

    def resetar_chaves_forjadas(self):
        self.root.get_screen("settings").ids["chave1"].source = "imagens/chave_amarela-n_forjada.png"
        self.root.get_screen("settings").ids["chave2"].source = "imagens/chave_amarela-n_forjada.png"
        self.root.get_screen("settings").ids["chave3"].source = "imagens/chave_amarela-n_forjada.png"

    def resetar(self):
        obj = OpenDialog("Deseja realmente resetar?")
        obj.open()

    def bt_voltar_handler(self):
        obj = OpenDialog("Deseja realmente voltar?", "voltar")
        obj.open()

if __name__ == '__main__':
    MeuAplicativo().run()