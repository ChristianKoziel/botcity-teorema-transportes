from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()




"""
CÓDIGO FEITO PARA SISTEMA FATURAMENTO 24.11
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - ICTUS 0000024
"""

class Bot(DesktopBot) :


    def find_button(self, label) :
        try :
            if not self.find(label,  matching=0.97, waiting_time=10000) :
                raise Exception("Element not found")
        except Exception as error :
            print("Error")
            filepath = self.save_screenshot(r"C:\Users\Usuário\Desktop\printserros\screenshot.png")
            maestro.error(task_id=execution.task_id,
                          exception=error,
                          screenshot=filepath)
            maestro.alert(task_id=execution.task_id,
                          title="Title",
                          message="Erro ao executar o Bot",
                          alert_type=AlertType.ERROR)




    def action(self,execution=None) :
                bot = self
                """
                #SESSÃO PÁGINA 1 (Empresas 26 - 2424)
            #######################-----LOGIN-----############################
                

                
                self.execute(r"C:\teorema\atualiza\atualiza - transportes.exe")
                self.wait(4000)
                # Searching for element 'Transportes_usuario_login'
                if not bot.find("Transportes_usuario_login", matching=0.97, waiting_time=10000):
                    not_found("Transportes_usuario_login")
                bot.click_relative(94, 15)
                self.type_keys_with_interval(50,"teorema")
                self.enter()
                self.wait(2000)
                self.enter()
                self.type_keys_with_interval(50, "1811")
                # Searching for element 'botao_login'
                if not bot.find("botao_login", matching=0.97, waiting_time=10000):
                    not_found("botao_login")
                bot.click()
                self.wait(1000)
                self.click()
                self.wait(3000)
                # Searching for element 'btn_cadastro'"
                """
                self.wait(1500)
                ################### ABA CADASTRO ######################
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_menu_empresas '
                if not bot.find("btn_menu_empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_menu_empresas")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_menu_empresas '
                if not bot.find("btn_menu_empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_menu_empresas")
                bot.click()
                # Searching for element 'btn_cadastro_incluir '
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_nao '
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.wait(1500)
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                self.type_keys_with_interval(50, "02.383.417/0001-06")
                self.tab()
                self.type_keys_with_interval(50, "123123")
                # Searching for element 'cad_nome_fantasia '
                if not bot.find("cad_nome_fantasia", matching=0.97, waiting_time=10000):
                    not_found("cad_nome_fantasia")
                bot.click_relative(10, 27)
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                x = 0
                while x < 4:
                     self.type_down()
                     x = x + 1
                
                self.tab()
                x = 0
                while x < 8:
                     self.type_down()
                     x = x + 1
                self.tab()
                x = 0
                while x < 8:    
                    self.type_keys_with_interval(50, "teste12!")
                    self.tab()
                    x = x + 1
                # Searching for element 'btn_municipio_cad '
                if not bot.find("btn_municipio_cad", matching=0.97, waiting_time=10000):
                    not_found("btn_municipio_cad")
                bot.click_relative(53, 26)
                # Searching for element 'btn_localizar '
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'btn_selecionar '
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "75345-000")
                self.tab()
                x = 0
                while x < 4:
                    self.type_keys_with_interval(50, "teste12!")
                    self.tab()
                    x = x + 1
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                self.type_keys_with_interval(50, "www.google.com.br")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                # Searching for element 'cad_responsavel '
                if not bot.find("cad_ responsavel", matching=0.97, waiting_time=10000):
                    not_found("cad_ responsavel")
                bot.click_relative(50, 29)
                # Searching for element 'btn_localizar '
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'btn_selecionar '
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "104.793.529-50")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "104.793.529-50")
                self.tab()
                self.type_keys_with_interval(50, "123123")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                x = 0
                while x < 6:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    x = x + 1
                
                ########### ABA cadastro rh ##################
                # Searching for element 'btn_cad_infoRh '
                if not bot.find("btn_cad_infoRh", matching=0.97, waiting_time=10000):
                    not_found("btn_cad_infoRh")
                bot.click()
                x = 0
                while x <= 12:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    x = x + 1
                x = 0
                while x <= 5:
                    self.type_down()
                    x = x + 1
                self.tab()
                x = 0
                while x <= 4:
                    self.type_down()
                    x = x + 1
                self.tab()
                x = 0
                while x <= 4:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "02.383.417/0001-06")
                self.tab()
                x = 0
                while x < 4:
                    self.type_keys_with_interval(50, "teste12!")
                    self.tab()
                    x = x + 1
                x = 0
                while x < 7:
                    self.type_up()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                x = 0
                while x < 7:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    x = x + 1
                # Searching for element 'btn_cad_dsr-rh '
                if not bot.find("btn_cad_dsr-rh", matching=0.97, waiting_time=10000):
                    not_found("btn_cad_dsr-rh")
                bot.click()
                # Searching for element 'form_cod_municipio '
                if not bot.find("form_cod_municipio", matching=0.97, waiting_time=10000):
                    not_found("form_cod_municipio")
                bot.click_relative(17, 26)
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 4:
                    self.space()
                    self.tab()
                    x = x + 1
                x = 0
                while x < 7:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                x = 0
                while x < 3:
                    self.space()
                    self.tab()
                    x = x + 1
                x = 0
                while x < 3:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 3:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")    
                self.tab()              
                x = 0
                while x < 3:
                    self.type_down()
                    x = x + 1
                self.tab()
                x = 0
                while x < 12:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    x = x + 1
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                # Searching for element 'btn_msgObservacaoRh '
                if not bot.find("btn_msgObservacaoRh", matching=0.97, waiting_time=10000):
                    not_found("btn_msgObservacaoRh")
                bot.click()
                x = 0
                while x < 3:
                    self.type_keys_with_interval(50, "teste12!")
                    self.tab()
                    x = x + 1
                
                


                
                
                

                    

def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  