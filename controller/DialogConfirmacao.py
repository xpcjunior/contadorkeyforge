from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.app import App

class OpenDialog(Popup):
    
    mensagem = StringProperty()
    funcao = StringProperty()
    mgs_bt1 = StringProperty()
    mgs_bt2 = StringProperty()

    def __init__(self, msg, funcao = "resetar", mgs_bt1 = "Sim", mgs_bt2 = "Não", *args):
        super(OpenDialog, self).__init__(*args)
        self.mensagem = msg
        self.funcao = funcao
        self.mgs_bt1 = mgs_bt1
        self.mgs_bt2 = mgs_bt2

    def _enter(self):
        if(self.funcao == "voltar"):
            App.get_running_app().mudar_tela("menu")
        else:
            App.get_running_app().incializar()
            App.get_running_app().atualizar_corrente()
            App.get_running_app().atualizar_aembar()
            App.get_running_app().atualizar_aembar_para_forjar()
            App.get_running_app().resetar_chaves_forjadas()

        self.dismiss()

    def _cancel(self):
        if(self.funcao == "fimdojogo"):
            App.get_running_app().Exit()
        else:
            self.dismiss()