from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()




"""
CÓDIGO FEITO PARA SISTEMA GESTAO TRANSPORTES 24.11
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - RACOES SERTANEJA 0042362
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
                """""
                #SESSÃO PÁGINA 1 (Empresas 26 - 2424)"
                #######################-----LOGIN-----############################
                                    teste@teste.com www.google.com.br
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
                # Searching for element 'btn_cadastro'"
                
                self.wait(3000)"""
                self.wait(1500)
                ################### ABA CADASTRO ######################                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_menu_empresas'
                if not bot.find("btn_menu_empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_menu_empresas")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_menu_empresas'
                if not bot.find("btn_menu_empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_menu_empresas")                                                                      
                bot.click()
                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.wait(1500)
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                self.type_keys_with_interval(50, "02.383.417/0001-06")
                self.tab()
                self.type_keys_with_interval(50, "123123")
                # Searching for element 'cad_nome_fantasia'
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
                # Searching for element 'btn_municipio_cad'
                if not bot.find("btn_municipio_cad", matching=0.97, waiting_time=10000):
                    not_found("btn_municipio_cad")
                bot.click_relative(53, 26)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
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
                # Searching for element 'cad_responsavel'
                if not bot.find("cad_ responsavel", matching=0.97, waiting_time=10000):
                    not_found("cad_ responsavel")
                bot.click_relative(50, 29)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
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
                # Searching for element 'btn_cad_infoRh'
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
                # Searching for element 'btn_cad_dsr-rh'
                if not bot.find("btn_cad_dsr-rh", matching=0.97, waiting_time=10000):
                    not_found("btn_cad_dsr-rh")
                bot.click()
                # Searching for element 'form_cod_municipio'
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
                # Searching for element 'btn_msgObservacaoRh'
                if not bot.find("btn_msgObservacaoRh", matching=0.97, waiting_time=10000):
                    not_found("btn_msgObservacaoRh")
                bot.click()
                x = 0
                while x < 3:
                    self.type_keys_with_interval(50, "teste12!")
                    self.tab()
                    x = x + 1
                # Searching for element 'btn_info_fiscais'
                if not bot.find("btn_info_fiscais", matching=0.97, waiting_time=10000):
                    not_found("btn_info_fiscais")
                bot.click()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                x = 0
                while x < 6:
                    self.type_down()
                    x = x + 1
                self.type_up()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down()
                    x = x + 1
                self.tab()         
                x = 0
                while x < 12:
                    self.type_down()
                    x = x + 1              
                self.tab()         
                x = 0
                while x < 7:
                    self.type_down()
                    x = x + 1
                self.tab()         
                x = 0
                while x < 6:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "teste12")
                self.tab()
                self.type_keys_with_interval(50, "teste12")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()         
                x = 0
                while x < 20:
                    self.type_down()
                    x = x + 1
                self.tab()         
                x = 0
                while x < 14:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                x = 0
                while x < 4:
                    self.type_down()
                    x = x + 1
                # Searching for element 'btn_agrupamentos_cad'
                if not bot.find("btn_agrupamentos_cad", matching=0.97, waiting_time=10000):
                    not_found("btn_agrupamentos_cad")
                bot.click()
                # # Searching for element 'lp_cad_grupoDeEmpresas'
                # if not bot.find("lp_cad_grupoDeEmpresas", matching=0.97, waiting_time=10000):
                #     not_found("lp_cad_grupoDeEmpresas")
                # bot.click_relative(65, 25)
                # # Searching for element 'btn_localizar'
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()                                                         ##
                
                # # Searching for element 'lp_UsaPdCdE'
                # if not bot.find("lp_UsaPdCdE", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaPdCdE")
                # bot.click_relative(64, 26)
                # # Searching for element 'btn_localizar'##
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()     
                # Searching for element 'lp_UsaHistoricodaEmpresa'
                # if not bot.find("lp_UsaHistoricodaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaHistoricodaEmpresa")
                # bot.click_relative(64, 21)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaCFdE'
                # if not bot.find("lp_Usa CF d E", matching=0.97, waiting_time=10000):
                #     not_found("lp_Usa CF d E")
                # bot.click_relative(64, 24)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()
                                                                    
                # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()

                

                # Searching for element 'lp_UsaItensdaEmpresa'
                # if not bot.find("lp_Usa Itens da Empresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_Usa Itens da Empresa")
                # bot.click_relative(63, 26)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # Searching for element 'lp_UsaPrecodaempresa'
                # if not bot.find("lp_Usa Preco da empresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_Usa Preco da empresa")
                # bot.click_relative(64, 26)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_usaPlanodcPfde'
                # if not bot.find("lp_usa Plano d c P f d e", matching=0.97, waiting_time=10000):
                #     not_found("lp_usa Plano d c P f d e")
                # bot.click_relative(62, 23)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaVendedoresdaEmpresa'
                # if not bot.find("lp_UsaVendedoresdaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaVendedoresdaEmpresa")
                # bot.click_relative(64, 23)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaSituacoesdaEmpresa'
                # if not bot.find("lp_UsaSituacoesdaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaSituacoesdaEmpresa")
                # bot.click_relative(63, 20)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_tabeladeprecositens'
                # if not bot.find("lp_tabeladeprecositens", matching=0.97, waiting_time=10000):
                #     not_found("lp_tabeladeprecositens")
                # bot.click_relative(65, 26)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # self.backspace()
                # self.tab()
                # self.tab()
                # # Searching for element 'lp_tabelaDePrecosServicos'
                # if not bot.find("lp_tabelaDePrecosServicos", matching=0.97, waiting_time=10000):
                #     not_found("lp_tabelaDePrecosServicos")
                # bot.click_relative(70, 25)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # self.backspace()
                # self.tab()
                # self.tab()
                # Searching for element 'lp_UsaVeiculoDaEmpresa'
                if not bot.find("lp_UsaVeiculoDaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaVeiculoDaEmpresa")
                bot.click_relative(66, 21)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaContratosdaEmpresa'
                if not bot.find("lp_UsaContratosdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaContratosdaEmpresa")
                bot.click_relative(63, 24)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_Contabilista'
                if not bot.find("lp_Contabilista", matching=0.97, waiting_time=10000):
                    not_found("lp_Contabilista")
                bot.click_relative(62, 26)
                # Searching for element 'btn_Localizarctb'
                if not bot.find("btn_Localizarctb", matching=0.97, waiting_time=10000):
                    not_found("btn_Localizarctb")
                bot.click()
                # Searching for element 'btn_selecionarctb'
                if not bot.find("btn_selecionarctb", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionarctb")
                bot.click()
                # Searching for element 'lp_UsaRubricasdaEmpresa'
                if not bot.find("lp_UsaRubricasdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaRubricasdaEmpresa")
                bot.click_relative(61, 20)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                #Botão que aparecia a mensagem na hora de salvar,
                #agora nao aparece mais a mensagem
                #apos desmarcar a opção auto-inclusão

                # Searching for element 'btn_Xnao'
                # if not bot.find("btn_Xnao", matching=0.97, waiting_time=10000):
                #     not_found("btn_Xnao")
                # bot.click()
                # # Searching for element 'btn_Xcancelar'
                # if not bot.find("btn_Xcancelar", matching=0.97, waiting_time=10000):
                #     not_found("btn_Xcancelar")
                # bot.click()
                # # Searching for element 'btn_Vsim'
                # if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                #     not_found("btn_Vsim")
                # bot.click()              
                
                #Searching for element 'retornarAlternativo '
                if not bot.find("retornarAlternativo", matching=0.97, waiting_time=10000):
                    not_found("retornarAlternativo")
                bot.click_relative(30, 37)
                
                # Searching for element 'voltarAlternativo'
                if not bot.find("voltarAlternativo", matching=0.97, waiting_time=10000):
                    not_found("voltarAlternativo")
                bot.click_relative(29, 36)
                                
                #testessss
                # Searching for element 'btn_cadastros'
                if not bot.find("btn_cadastros", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastros")
                bot.click()
                               
                # Searching for element 'btn_Empresas'
                if not bot.find("btn_Empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_Empresas")
                bot.click()
                # Searching for element 'btn_Empresas2'
                if not bot.find("btn_Empresas2", matching=0.97, waiting_time=10000):
                    not_found("btn_Empresas2")
                bot.click_relative(70, 13)
                # Searching for element 'btn_Localizar'
                if not bot.find("btn_Localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_Localizar")
                bot.click()
                # Searching for element 'selecionar_emprteste'
                if not bot.find("selecionar_emprteste", matching=0.97, waiting_time=10000):
                    not_found("selecionar_emprteste")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'btn_Agrupamentos'
                if not bot.find("btn_Agrupamentos", matching=0.97, waiting_time=10000):
                    not_found("btn_Agrupamentos")
                bot.click()
                # Searching for element 'lp_contasClientes'
                if not bot.find("lp_contasClientes", matching=0.97, waiting_time=10000):
                    not_found("lp_contasClientes")
                bot.click_relative(120, 25)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_contasdefornecedores'
                if not bot.find("lp_contas de fornecedores", matching=0.97, waiting_time=10000):
                    not_found("lp_contas de fornecedores")
                bot.click_relative(120, 30)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_codContabilCLientes'
                if not bot.find("lp_codContabilCLientes", matching=0.97, waiting_time=10000):
                    not_found("lp_codContabilCLientes")
                bot.click_relative(124, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                # Aguarde 5 segundos.
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()

                # Searching for element 'lp_codContabilFornecedore'
                if not bot.find("lp_codContabilFornecedore", matching=0.97, waiting_time=10000):
                    not_found("lp_codContabilFornecedore")
                bot.click_relative(121, 24)
                
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_cc994'
                if not bot.find("lp_cc994", matching=0.97, waiting_time=10000):
                    not_found("lp_cc994")
                bot.click_relative(118, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc993'
                if not bot.find("lp_cc993", matching=0.97, waiting_time=10000):
                    not_found("lp_cc993")
                bot.click_relative(124, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_cc992'
                if not bot.find("lp_cc992", matching=0.97, waiting_time=10000):
                    not_found("lp_cc992")
                bot.click_relative(123, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc991'
                if not bot.find("lp_cc991", matching=0.97, waiting_time=10000):
                    not_found("lp_cc991")
                bot.click_relative(88, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                # Aguarde 2 segundos.
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc990'
                if not bot.find("lp_cc990", matching=0.97, waiting_time=10000):
                    not_found("lp_cc990")
                bot.click_relative(86, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc989'
                if not bot.find("lp_cc989", matching=0.97, waiting_time=10000):
                    not_found("lp_cc989")
                bot.click_relative(87, 28)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc988'
                if not bot.find("lp_cc988", matching=0.97, waiting_time=10000):
                    not_found("lp_cc988")
                bot.click_relative(89, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_cc987'
                if not bot.find("lp_cc987", matching=0.97, waiting_time=10000):
                    not_found("lp_cc987")
                bot.click_relative(123, 25)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc986'
                if not bot.find("lp_cc986", matching=0.97, waiting_time=10000):
                    not_found("lp_cc986")
                bot.click_relative(122, 28)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                # Aguarde 2 segundos.
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc985'
                if not bot.find("lp_cc985", matching=0.97, waiting_time=10000):
                    not_found("lp_cc985")
                bot.click_relative(120, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc984'
                if not bot.find("lp_cc984", matching=0.97, waiting_time=10000):
                    not_found("lp_cc984")
                bot.click_relative(122, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc983'
                if not bot.find("lp_cc983", matching=0.97, waiting_time=10000):
                    not_found("lp_cc983")
                bot.click_relative(91, 29)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc982'
                if not bot.find("lp_cc982", matching=0.97, waiting_time=10000):
                    not_found("lp_cc982")
                bot.click_relative(90, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc981'
                if not bot.find("lp_cc981", matching=0.97, waiting_time=10000):
                    not_found("lp_cc981")
                bot.click_relative(84, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                ##### ABA RELACIONAMENTOS ######
                # Searching for element 'btn_ABA_RELACIONAMENTOS'
                if not bot.find("btn_ABA_RELACIONAMENTOS", matching=0.97, waiting_time=10000):
                    not_found("btn_ABA_RELACIONAMENTOS")
                bot.click()
                ######## AQUI TEM QUE SALVAR O AQUIVO PARA DAI CLICAR PARA ADICIONAR O ESTADO #########
                #VOU RODAR O PROCESSO MAIS OU MENOS ATÉ AQUI
                # Searching for element 'SalvarRelativeClick '
                if not bot.find("SalvarRelativeClick", matching=0.97, waiting_time=10000):
                    not_found("SalvarRelativeClick")
                bot.click_relative(83, -79)
                                
                # Searching for element 'btn_AddEstado '
                if not bot.find("btn_AddEstado", matching=0.97, waiting_time=10000):
                    not_found("btn_AddEstado")
                bot.click_relative(9, 95)
                               
                self.type_keys_with_interval(50, "teste12!")
                #Searching for element 'add_est '

                #### ultima aba foi a partir daqui
                if not bot.find("add_est", matching=0.97, waiting_time=10000):
                    not_found("add_est")
                bot.click_relative(-30, 7)
                
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.enter()
                self.type_keys_with_interval(50, "02")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.tab()
                self.enter()
                self.enter()
                # Searching for element 'exluirRegistro'
                if not bot.find("exluirRegistro", matching=0.97, waiting_time=10000):
                    not_found("exluirRegistro")
                bot.click()
                self.enter()
                if not bot.find("add_est", matching=0.97, waiting_time=10000):
                    not_found("add_est")
                bot.click_relative(-30, 7)
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.enter()
                # Searching for element 'cancelaroperacao'
                if not bot.find("cancelar operacao", matching=0.97, waiting_time=10000):
                    not_found("cancelar operacao")
                bot.click_relative(-535, 20)
                self.enter()
                # Searching for element 'aba_socios'
                if not bot.find("aba_socios", matching=0.97, waiting_time=10000):
                    not_found("aba_socios")
                bot.click()
                # Searching for element 'incluir_Socio'
                if not bot.find("incluir_Socio", matching=0.97, waiting_time=10000):
                    not_found("incluir_Socio")
                bot.click_relative(10, -15)
                
                # Searching for element 'acionaCampocadastro'
                # if not bot.find("acionaCampocadastro", matching=0.97, waiting_time=10000):
                #     not_found("acionaCampocadastro")
                # bot.click_relative(23, 257)
                
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "104.793.529-50")
                self.tab()
                self.type_keys_with_interval(50, "12.455.616-3")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "Arraias")
                self.tab()
                x = 0
                while x <= 27:
                     self.type_down()
                     x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "77330-000")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "9999999")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                x = 0
                while x < 10:
                     self.type_down()
                     x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 23:
                     self.type_down()
                     x = x + 1 
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "124")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                
                # Searching for element 'btn_SalvarCadastroSocio'
                if not bot.find("btn_SalvarCadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("btn_SalvarCadastroSocio")
                bot.click()
                
                # Searching for element 'clica_Consulta '
                if not bot.find("clica_Consulta", matching=0.97, waiting_time=10000):
                    not_found("clica_Consulta")
                bot.click()
                
                # Searching for element 'click_X '
                if not bot.find("click_X", matching=0.97, waiting_time=10000):
                    not_found("click_X")
                bot.click()
                
                # Searching for element 'Click_Sim '
                if not bot.find("Click_Sim", matching=0.97, waiting_time=10000):
                    not_found("Click_Sim")
                bot.click()
                
                # Searching for element 'click_CadastroSocio '
                #Atualizado
                # if not bot.find("click_CadastroSocio", matching=0.97, waiting_time=10000):
                #     not_found("click_CadastroSocio")
                # bot.click_relative(-4, 213)
                                
                # Searching for element 'click_CampoFuncao '
                if not bot.find("click_CampoFuncao", matching=0.97, waiting_time=10000):
                    not_found("click_CampoFuncao")
                bot.click_relative(37, 258)
                
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "01")   
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "Parou aqui")
                
                # # Searching for element 'click_Campo_Banco '
                # if not bot.find("click_Campo_Banco", matching=0.97, waiting_time=10000):
                #     not_found("click_Campo_Banco")
                # bot.click_relative(399, 216)
                                
                # # Searching for element 'click_Salvar '
                # if not bot.find("click_Salvar", matching=0.97, waiting_time=10000):
                #     not_found("click_Salvar")
                # bot.click()
                # Searching for element 'irParaAbaRelacionamentosAlt '
                if not bot.find("irParaAbaRelacionamentosAlt", matching=0.97, waiting_time=10000):
                    not_found("irParaAbaRelacionamentosAlt")
                bot.click()
                
                # Searching for element 'Click_ABA_Documentos '
                if not bot.find("Click_ABA_Documentos", matching=0.97, waiting_time=10000):
                    not_found("Click_ABA_Documentos")
                bot.click()

                # Searching for element 'salvarAlternativoBotaoVerdelaEmCimausandocomoimagemoonibus '
                if not bot.find("salvarAlternativoBotaoVerdelaEmCimausandocomoimagemoonibus", matching=0.97, waiting_time=10000):
                    not_found("salvarAlternativoBotaoVerdelaEmCimausandocomoimagemoonibus")
                bot.click_relative(338, 78)                
                
                # Searching for element 'incluir_Documentos '
                if not bot.find("incluir_Documentos", matching=0.97, waiting_time=10000):
                    not_found("incluir_Documentos")
                bot.click_relative(10, -15)
                
                ## IMPORTANTE, QUANDO INCLUIR DOCUMENTO CONFERIR SE TA CADASTRADO DOCUMENTO
                ## NA OPÇÃO TIPO DE DOCUMENTO NO MODULO GESTÃO DE PESSOAS

                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "teste")
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")

                # Searching for element 'salvar_Documento '
                if not bot.find("salvar_Documento", matching=0.97, waiting_time=10000):
                    not_found("salvar_Documento")
                bot.click()
                
                # Searching for element 'click_abOp '
                if not bot.find("click_abOp", matching=0.97, waiting_time=10000):
                    not_found("click_abOp")
                bot.click()
                # Searching for element 'sim_Click '
                if not bot.find("sim_Click", matching=0.97, waiting_time=10000):
                    not_found("sim_Click")
                bot.click()
                
                # Searching for element 'click_aba_PessoasAutorizadas '
                if not bot.find("click_aba_PessoasAutorizadas", matching=0.97, waiting_time=10000):
                    not_found("click_aba_PessoasAutorizadas")
                bot.click()
                
                # Searching for element 'incluir_PessoaAutorizada '
                if not bot.find("incluir_PessoaAutorizada", matching=0.97, waiting_time=10000):
                    not_found("incluir_PessoaAutorizada")
                bot.click_relative(9, -18)
                
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab() 
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                
                # Searching for element 'Salvar_InlcuirPessoaAutorizada '
                if not bot.find("Salvar_InlcuirPessoaAutorizada", matching=0.97, waiting_time=10000):
                    not_found("Salvar_InlcuirPessoaAutorizada")
                bot.click()
                # Searching for element 'Click_Consulta '
                if not bot.find("Click_Consulta", matching=0.97, waiting_time=10000):
                    not_found("Click_Consulta")
                bot.click()
                
                # Searching for element 'Click_X '
                if not bot.find("Click_X", matching=0.97, waiting_time=10000):
                    not_found("Click_X")
                bot.click()
                # Searching for element 'click_SIM '
                if not bot.find("click_SIM", matching=0.97, waiting_time=10000):
                    not_found("click_SIM")
                bot.click()
                # Searching for element 'CLICK_ABA_GNRE '
                if not bot.find("CLICK_ABA_GNRE", matching=0.97, waiting_time=10000):
                    not_found("CLICK_ABA_GNRE")
                bot.click()                
                
                # Searching for element 'testePastaAbrirarquivo '
                if not bot.find("testePastaAbrirarquivo", matching=0.97, waiting_time=10000):
                    not_found("testePastaAbrirarquivo")
                bot.click_relative(8, 68)
                
                # Searching for element 'cancelar '
                if not bot.find("cancelar", matching=0.97, waiting_time=10000):
                    not_found("cancelar")
                bot.click()
                
                # Searching for element 'testePastaarq '
                if not bot.find("testePastaarq", matching=0.97, waiting_time=10000):
                    not_found("testePastaarq")
                bot.click_relative(-109, 136)
                
                # Searching for element 'cancel '
                if not bot.find("cancel", matching=0.97, waiting_time=10000):
                    not_found("cancel")
                bot.click()
                
                # Searching for element 'testePastaArq '
                if not bot.find("testePastaArq", matching=0.97, waiting_time=10000):
                    not_found("testePastaArq")
                bot.click_relative(347, 136)
                
                # Searching for element 'cancel '
                if not bot.find("cancel", matching=0.97, waiting_time=10000):
                    not_found("cancel")
                bot.click()
              
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 72)
                
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                #################################################
                #### AQUI CONCLUI CADASTRO DE EMPRESA #########
                ############################################

                #ALTERAR PRINT CADASTROS
                #Alterado
                # Searching for element 'Cadastro '
                if not bot.find("Cadastro", matching=0.97, waiting_time=10000):
                    not_found("Cadastro")
                bot.click_relative(-93, -20)
                             
                # Searching for element 'empresas '
                if not bot.find("empresas", matching=0.97, waiting_time=10000):
                    not_found("empresas")
                bot.click()
                
                # Searching for element 'empresas2 '
                if not bot.find("empresas2", matching=0.97, waiting_time=10000):
                    not_found("empresas2")
                bot.click()
                
                # Searching for element 'localizar '
                if not bot.find("localizar", matching=0.97, waiting_time=10000):
                    not_found("localizar")
                bot.click()
                
                # Searching for element 'empresa_teste '
                if not bot.find("empresa_teste", matching=0.97, waiting_time=10000):
                    not_found("empresa_teste")
                bot.click()
                
                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()
                
                # Searching for element 'relacionamentos_ABA '
                if not bot.find("relacionamentos_ABA", matching=0.97, waiting_time=10000):
                    not_found("relacionamentos_ABA")
                bot.click()
                
                # Searching for element 'subAbaSocios '
                if not bot.find("subAbaSocios", matching=0.97, waiting_time=10000):
                    not_found("subAbaSocios")
                bot.click()
                
                # Searching for element 'selecionarNomeSocio '
                if not bot.find("selecionarNomeSocio", matching=0.97, waiting_time=10000):
                    not_found("selecionarNomeSocio")
                bot.click_relative(18, 287)
                
                # Searching for element 'exluirNomeSocio '
                if not bot.find("exluirNomeSocio", matching=0.97, waiting_time=10000):
                    not_found("exluirNomeSocio")
                bot.click_relative(-97, 214)
                
                self.enter()

                # Searching for element 'subABA_Documentos '
                if not bot.find("subABA_Documentos", matching=0.97, waiting_time=10000):
                    not_found("subABA_Documentos")
                bot.click()
                
                # Searching for element 'selecionaDocumentos '
                if not bot.find("selecionaDocumentos", matching=0.97, waiting_time=10000):
                    not_found("selecionaDocumentos")
                bot.click_relative(4, 230)
                
                # Searching for element 'excluiDocumento '
                if not bot.find("excluiDocumento", matching=0.97, waiting_time=10000):
                    not_found("excluiDocumento")
                bot.click_relative(-97, 215)
                
                # Searching for element 'sim '
                # if not bot.find("sim", matching=0.97, waiting_time=10000):
                #     not_found("sim")
                # bot.click()

                self.enter()
                
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-80, 73)
                                
                ####################################
                #####################################
                ########################################
                #### CADASTRO DE NOVA EMPRESA ########
                #####################################
                ######################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_menu_empresas'
                if not bot.find("btn_menu_empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_menu_empresas")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_menu_empresas'
                if not bot.find("btn_menu_empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_menu_empresas")
                bot.click()
                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.wait(1500)
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                self.type_keys_with_interval(50, "02.383.417/0001-06")
                self.tab()
                self.type_keys_with_interval(50, "123123")
                # Searching for element 'cad_nome_fantasia'
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
                # Searching for element 'btn_municipio_cad'
                if not bot.find("btn_municipio_cad", matching=0.97, waiting_time=10000):
                    not_found("btn_municipio_cad")
                bot.click_relative(53, 26)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
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
                # Searching for element 'cad_responsavel'
                if not bot.find("cad_ responsavel", matching=0.97, waiting_time=10000):
                    not_found("cad_ responsavel")
                bot.click_relative(50, 29)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
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
                # Searching for element 'btn_cad_infoRh'
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
                # Searching for element 'btn_cad_dsr-rh'
                if not bot.find("btn_cad_dsr-rh", matching=0.97, waiting_time=10000):
                    not_found("btn_cad_dsr-rh")
                bot.click()
                # Searching for element 'form_cod_municipio'
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
                # Searching for element 'btn_msgObservacaoRh'
                if not bot.find("btn_msgObservacaoRh", matching=0.97, waiting_time=10000):
                    not_found("btn_msgObservacaoRh")
                bot.click()
                x = 0
                while x < 3:
                    self.type_keys_with_interval(50, "teste12!")
                    self.tab()
                    x = x + 1
                # Searching for element 'btn_info_fiscais'
                if not bot.find("btn_info_fiscais", matching=0.97, waiting_time=10000):
                    not_found("btn_info_fiscais")
                bot.click()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                x = 0
                while x < 6:
                    self.type_down()
                    x = x + 1
                self.type_up()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down()
                    x = x + 1
                self.tab()         
                x = 0
                while x < 12:
                    self.type_down()
                    x = x + 1              
                self.tab()         
                x = 0
                while x < 7:
                    self.type_down()
                    x = x + 1
                self.tab()         
                x = 0
                while x < 6:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "teste12")
                self.tab()
                self.type_keys_with_interval(50, "teste12")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()         
                x = 0
                while x < 20:
                    self.type_down()
                    x = x + 1
                self.tab()         
                x = 0
                while x < 14:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                x = 0
                while x < 4:
                    self.type_down()
                    x = x + 1
                # Searching for element 'btn_agrupamentos_cad'
                if not bot.find("btn_agrupamentos_cad", matching=0.97, waiting_time=10000):
                    not_found("btn_agrupamentos_cad")
                bot.click()
                # Searching for element 'lp_cad_grupoDeEmpresas'
                if not bot.find("lp_cad_grupoDeEmpresas", matching=0.97, waiting_time=10000):
                    not_found("lp_cad_grupoDeEmpresas")
                bot.click_relative(65, 25)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()                                                         ##
                
                # # Searching for element 'lp_UsaPdCdE'
                # if not bot.find("lp_UsaPdCdE", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaPdCdE")
                # bot.click_relative(64, 26)
                # # Searching for element 'btn_localizar'##
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()     
                # # Searching for element 'lp_UsaHistoricodaEmpresa'
                # if not bot.find("lp_UsaHistoricodaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaHistoricodaEmpresa")
                # bot.click_relative(64, 21)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaCFdE'
                # if not bot.find("lp_Usa CF d E", matching=0.97, waiting_time=10000):
                #     not_found("lp_Usa CF d E")
                # bot.click_relative(64, 24)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaItensdaEmpresa'
                # if not bot.find("lp_Usa Itens da Empresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_Usa Itens da Empresa")
                # bot.click_relative(63, 26)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaPrecodaempresa'
                # if not bot.find("lp_Usa Preco da empresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_Usa Preco da empresa")
                # bot.click_relative(64, 26)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_usaPlanodcPfde'
                # if not bot.find("lp_usa Plano d c P f d e", matching=0.97, waiting_time=10000):
                #     not_found("lp_usa Plano d c P f d e")
                # bot.click_relative(62, 23)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaVendedoresdaEmpresa'
                # if not bot.find("lp_UsaVendedoresdaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaVendedoresdaEmpresa")
                # bot.click_relative(64, 23)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaSituacoesdaEmpresa'
                # if not bot.find("lp_UsaSituacoesdaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaSituacoesdaEmpresa")
                # bot.click_relative(63, 20)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_tabeladeprecositens'
                # if not bot.find("lp_tabeladeprecositens", matching=0.97, waiting_time=10000):
                #     not_found("lp_tabeladeprecositens")
                # bot.click_relative(65, 26)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # self.backspace()
                # self.tab()
                # self.tab()
                # # Searching for element 'lp_tabelaDePrecosServicos'
                # if not bot.find("lp_tabelaDePrecosServicos", matching=0.97, waiting_time=10000):
                #     not_found("lp_tabelaDePrecosServicos")
                # bot.click_relative(70, 25)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # self.backspace()
                # self.tab()
                # self.tab()
                # # Searching for element 'lp_UsaVeiculoDaEmpresa'
                # if not bot.find("lp_UsaVeiculoDaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaVeiculoDaEmpresa")
                # bot.click_relative(66, 21)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_UsaContratosdaEmpresa'
                # if not bot.find("lp_UsaContratosdaEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("lp_UsaContratosdaEmpresa")
                # bot.click_relative(63, 24)
                # # Searching for element 'btn_localizar'####
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                #     not_found("btn_localizar")                                      ##
                # bot.click()                                                         ##
                # # Searching for element 'btn_selecionar'##
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                #     not_found("btn_selecionar")                                     ##
                # bot.click()
                # # Searching for element 'lp_Contabilista'
                # if not bot.find("lp_Contabilista", matching=0.97, waiting_time=10000):
                #     not_found("lp_Contabilista")
                # bot.click_relative(62, 26)
                # # Searching for element 'btn_Localizarctb'
                # if not bot.find("btn_Localizarctb", matching=0.97, waiting_time=10000):
                #     not_found("btn_Localizarctb")
                # bot.click()
                # # Searching for element 'btn_selecionarctb'
                # if not bot.find("btn_selecionarctb", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionarctb")
                # bot.click()
                # Searching for element 'lp_UsaRubricasdaEmpresa'
                if not bot.find("lp_UsaRubricasdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaRubricasdaEmpresa")
                bot.click_relative(61, 20)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()


                #Botão que aparecia a mensagem na hora de salvar,
                #agora nao aparece mais a mensagem
                #apos desmarcar a opção auto-inclusão


                # Searching for element 'btn_Xnao'
                # if not bot.find("btn_Xnao", matching=0.97, waiting_time=10000):
                #     not_found("btn_Xnao")
                # bot.click()
                # # Searching for element 'btn_Xcancelar'
                # if not bot.find("btn_Xcancelar", matching=0.97, waiting_time=10000):
                #     not_found("btn_Xcancelar")
                # bot.click()
                # # Searching for element 'btn_Vsim'
                # if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                #     not_found("btn_Vsim")
                # bot.click()              
                
                
                
                
                #Searching for element 'retornarAlternativo '
                if not bot.find("retornarAlternativo", matching=0.97, waiting_time=10000):
                    not_found("retornarAlternativo")
                bot.click_relative(30, 37)
                
                # Searching for element 'voltarAlternativo'
                if not bot.find("voltarAlternativo", matching=0.97, waiting_time=10000):
                    not_found("voltarAlternativo")
                bot.click_relative(29, 36)
                
                
  
                
                
                #testessss
                # Searching for element 'btn_cadastros'
                if not bot.find("btn_cadastros", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastros")
                bot.click()
                
                
                
                # Searching for element 'btn_Empresas'
                if not bot.find("btn_Empresas", matching=0.97, waiting_time=10000):
                    not_found("btn_Empresas")
                bot.click()
                # Searching for element 'btn_Empresas2'
                if not bot.find("btn_Empresas2", matching=0.97, waiting_time=10000):
                    not_found("btn_Empresas2")
                bot.click_relative(70, 13)
                # Searching for element 'btn_Localizar'
                if not bot.find("btn_Localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_Localizar")
                bot.click()
                # Searching for element 'selecionar_emprteste'
                if not bot.find("selecionar_emprteste", matching=0.97, waiting_time=10000):
                    not_found("selecionar_emprteste")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'btn_Agrupamentos'
                if not bot.find("btn_Agrupamentos", matching=0.97, waiting_time=10000):
                    not_found("btn_Agrupamentos")
                bot.click()
                # Searching for element 'lp_contasClientes'
                if not bot.find("lp_contasClientes", matching=0.97, waiting_time=10000):
                    not_found("lp_contasClientes")
                bot.click_relative(120, 25)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_contasdefornecedores'
                if not bot.find("lp_contas de fornecedores", matching=0.97, waiting_time=10000):
                    not_found("lp_contas de fornecedores")
                bot.click_relative(120, 30)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_codContabilCLientes'
                if not bot.find("lp_codContabilCLientes", matching=0.97, waiting_time=10000):
                    not_found("lp_codContabilCLientes")
                bot.click_relative(124, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                # Aguarde 5 segundos.
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()

                
                # Searching for element 'lp_codContabilFornecedore'
                if not bot.find("lp_codContabilFornecedore", matching=0.97, waiting_time=10000):
                    not_found("lp_codContabilFornecedore")
                bot.click_relative(121, 24)
                
                








                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_cc994'
                if not bot.find("lp_cc994", matching=0.97, waiting_time=10000):
                    not_found("lp_cc994")
                bot.click_relative(118, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc993'
                if not bot.find("lp_cc993", matching=0.97, waiting_time=10000):
                    not_found("lp_cc993")
                bot.click_relative(124, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_cc992'
                if not bot.find("lp_cc992", matching=0.97, waiting_time=10000):
                    not_found("lp_cc992")
                bot.click_relative(123, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc991'
                if not bot.find("lp_cc991", matching=0.97, waiting_time=10000):
                    not_found("lp_cc991")
                bot.click_relative(88, 26)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                # Aguarde 2 segundos.
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc990'
                if not bot.find("lp_cc990", matching=0.97, waiting_time=10000):
                    not_found("lp_cc990")
                bot.click_relative(86, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc989'
                if not bot.find("lp_cc989", matching=0.97, waiting_time=10000):
                    not_found("lp_cc989")
                bot.click_relative(87, 28)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc988'
                if not bot.find("lp_cc988", matching=0.97, waiting_time=10000):
                    not_found("lp_cc988")
                bot.click_relative(89, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                # Searching for element 'lp_cc987'
                if not bot.find("lp_cc987", matching=0.97, waiting_time=10000):
                    not_found("lp_cc987")
                bot.click_relative(123, 25)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc986'
                if not bot.find("lp_cc986", matching=0.97, waiting_time=10000):
                    not_found("lp_cc986")
                bot.click_relative(122, 28)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                # Aguarde 2 segundos.
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc985'
                if not bot.find("lp_cc985", matching=0.97, waiting_time=10000):
                    not_found("lp_cc985")
                bot.click_relative(120, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc984'
                if not bot.find("lp_cc984", matching=0.97, waiting_time=10000):
                    not_found("lp_cc984")
                bot.click_relative(122, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc983'
                if not bot.find("lp_cc983", matching=0.97, waiting_time=10000):
                    not_found("lp_cc983")
                bot.click_relative(91, 29)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc982'
                if not bot.find("lp_cc982", matching=0.97, waiting_time=10000):
                    not_found("lp_cc982")
                bot.click_relative(90, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                # Searching for element 'lp_cc981'
                if not bot.find("lp_cc981", matching=0.97, waiting_time=10000):
                    not_found("lp_cc981")
                bot.click_relative(84, 27)
                # Searching for element 'lp2_localizarGruposnoPlano'
                if not bot.find("lp2_localizarGruposnoPlano", matching=0.97, waiting_time=10000):
                    not_found("lp2_localizarGruposnoPlano")
                bot.click()
                
                # Searching for element 'btn_LOCALIZAR'
                if not bot.find("btn_LOCALIZAR", matching=0.97, waiting_time=10000):
                    not_found("btn_LOCALIZAR")
                bot.click()
                bot.wait(2000)
                # Searching for element 'btn_SELECIONAR'
                if not bot.find("btn_SELECIONAR", matching=0.97, waiting_time=10000):
                    not_found("btn_SELECIONAR")
                bot.click()
                
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                ##### ABA RELACIONAMENTOS ######
                # Searching for element 'btn_ABA_RELACIONAMENTOS'
                if not bot.find("btn_ABA_RELACIONAMENTOS", matching=0.97, waiting_time=10000):
                    not_found("btn_ABA_RELACIONAMENTOS")
                bot.click()
                ######## AQUI TEM QUE SALVAR O AQUIVO PARA DAI CLICAR PARA ADICIONAR O ESTADO #########
                #VOU RODAR O PROCESSO MAIS OU MENOS ATÉ AQUI
                # Searching for element 'btn_vSalvar '
                if not bot.find("btn_vSalvar", matching=0.97, waiting_time=10000):
                    not_found("btn_vSalvar")
                bot.click()
                # Searching for element 'btn_AddEstado '
                if not bot.find("btn_AddEstado", matching=0.97, waiting_time=10000):
                    not_found("btn_AddEstado")
                bot.click_relative(9, 95)
                
                
                
                
                self.type_keys_with_interval(50, "teste12!")
                #Searching for element 'add_est '



                #### ultima aba foi a partir daqui
                if not bot.find("add_est", matching=0.97, waiting_time=10000):
                    not_found("add_est")
                bot.click_relative(-30, 7)
                
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.enter()
                self.type_keys_with_interval(50, "02")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.tab()
                self.enter()
                self.enter()
                # Searching for element 'exluirRegistro'
                if not bot.find("exluirRegistro", matching=0.97, waiting_time=10000):
                    not_found("exluirRegistro")
                bot.click()
                self.enter()
                if not bot.find("add_est", matching=0.97, waiting_time=10000):
                    not_found("add_est")
                bot.click_relative(-30, 7)
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.enter()
                # Searching for element 'cancelaroperacao'
                if not bot.find("cancelar operacao", matching=0.97, waiting_time=10000):
                    not_found("cancelar operacao")
                bot.click_relative(-535, 20)
                self.enter()
                # Searching for element 'aba_socios'
                if not bot.find("aba_socios", matching=0.97, waiting_time=10000):
                    not_found("aba_socios")
                bot.click()
                # Searching for element 'incluir_Socio'
                if not bot.find("incluir_Socio", matching=0.97, waiting_time=10000):
                    not_found("incluir_Socio")
                bot.click_relative(10, -15)
                
                # Searching for element 'acionaCampocadastro'
                if not bot.find("acionaCampocadastro", matching=0.97, waiting_time=10000):
                    not_found("acionaCampocadastro")
                bot.click_relative(23, 257)
                

                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "104.793.529-50")
                self.tab()
                self.type_keys_with_interval(50, "12.455.616-3")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "Arraias")
                self.tab()
                x = 0
                while x <= 27:
                     self.type_down()
                     x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "77330-000")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "9999999")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                x = 0
                while x < 10:
                     self.type_down()
                     x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 23:
                     self.type_down()
                     x = x + 1 
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "124")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.space()
                self.tab()
                
                # Searching for element 'btn_SalvarCadastroSocio'
                if not bot.find("btn_SalvarCadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("btn_SalvarCadastroSocio")
                bot.click()
                
                # Searching for element 'clica_Consulta '
                if not bot.find("clica_Consulta", matching=0.97, waiting_time=10000):
                    not_found("clica_Consulta")
                bot.click()
                
                # Searching for element 'click_X '
                if not bot.find("click_X", matching=0.97, waiting_time=10000):
                    not_found("click_X")
                bot.click()
                
                # Searching for element 'Click_Sim '
                if not bot.find("Click_Sim", matching=0.97, waiting_time=10000):
                    not_found("Click_Sim")
                bot.click()
                
                # Searching for element 'click_CadastroSocio '
                #Atualizado
                if not bot.find("click_CadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("click_CadastroSocio")
                bot.click_relative(-4, 213)
                
                # Searching for element 'click_CampoFuncao '
                if not bot.find("click_CampoFuncao", matching=0.97, waiting_time=10000):
                    not_found("click_CampoFuncao")
                bot.click_relative(37, 258)
                
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "01")   
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "Parou aqui")
                
                # Searching for element 'click_Campo_Banco '
                if not bot.find("click_Campo_Banco", matching=0.97, waiting_time=10000):
                    not_found("click_Campo_Banco")
                bot.click_relative(399, 216)
                
                
                
                
                # Searching for element 'click_Salvar '
                if not bot.find("click_Salvar", matching=0.97, waiting_time=10000):
                    not_found("click_Salvar")
                bot.click()
                
                # Searching for element 'Click_ABA_Documentos '
                if not bot.find("Click_ABA_Documentos", matching=0.97, waiting_time=10000):
                    not_found("Click_ABA_Documentos")
                bot.click()
                
                # Searching for element 'incluir_Documentos '
                if not bot.find("incluir_Documentos", matching=0.97, waiting_time=10000):
                    not_found("incluir_Documentos")
                bot.click_relative(10, -15)
                
                ## IMPORTANTE, QUANDO INCLUIR DOCUMENTO CONFERIR SE TA CADASTRADO DOCUMENTO
                ## NA OPÇÃO TIPO DE DOCUMENTO NO MODULO GESTÃO DE PESSOAL

                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "teste")
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")

                # Searching for element 'salvar_Documento '
                if not bot.find("salvar_Documento", matching=0.97, waiting_time=10000):
                    not_found("salvar_Documento")
                bot.click()

                
                # Searching for element 'click_abOp '
                if not bot.find("click_abOp", matching=0.97, waiting_time=10000):
                    not_found("click_abOp")
                bot.click()
                # Searching for element 'sim_Click '
                if not bot.find("sim_Click", matching=0.97, waiting_time=10000):
                    not_found("sim_Click")
                bot.click()
                
                # Searching for element 'click_aba_PessoasAutorizadas '
                if not bot.find("click_aba_PessoasAutorizadas", matching=0.97, waiting_time=10000):
                    not_found("click_aba_PessoasAutorizadas")
                bot.click()
                
                # Searching for element 'incluir_PessoaAutorizada '
                if not bot.find("incluir_PessoaAutorizada", matching=0.97, waiting_time=10000):
                    not_found("incluir_PessoaAutorizada")
                bot.click_relative(9, -18)
                
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab() 
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                
                # Searching for element 'Salvar_InlcuirPessoaAutorizada '
                if not bot.find("Salvar_InlcuirPessoaAutorizada", matching=0.97, waiting_time=10000):
                    not_found("Salvar_InlcuirPessoaAutorizada")
                bot.click()
                # Searching for element 'Click_Consulta '
                if not bot.find("Click_Consulta", matching=0.97, waiting_time=10000):
                    not_found("Click_Consulta")
                bot.click()
                
                # Searching for element 'Click_X '
                if not bot.find("Click_X", matching=0.97, waiting_time=10000):
                    not_found("Click_X")
                bot.click()
                # Searching for element 'click_SIM '
                if not bot.find("click_SIM", matching=0.97, waiting_time=10000):
                    not_found("click_SIM")
                bot.click()
                # Searching for element 'CLICK_ABA_GNRE '
                if not bot.find("CLICK_ABA_GNRE", matching=0.97, waiting_time=10000):
                    not_found("CLICK_ABA_GNRE")
                bot.click()                
                
                # Searching for element 'testePastaAbrirarquivo '
                if not bot.find("testePastaAbrirarquivo", matching=0.97, waiting_time=10000):
                    not_found("testePastaAbrirarquivo")
                bot.click_relative(8, 68)
                
                # Searching for element 'cancelar '
                if not bot.find("cancelar", matching=0.97, waiting_time=10000):
                    not_found("cancelar")
                bot.click()
                
                # Searching for element 'testePastaarq '
                if not bot.find("testePastaarq", matching=0.97, waiting_time=10000):
                    not_found("testePastaarq")
                bot.click_relative(-109, 136)
                
                # Searching for element 'cancel '
                if not bot.find("cancel", matching=0.97, waiting_time=10000):
                    not_found("cancel")
                bot.click()
                
                # Searching for element 'testePastaArq '
                if not bot.find("testePastaArq", matching=0.97, waiting_time=10000):
                    not_found("testePastaArq")
                bot.click_relative(347, 136)
                
                # Searching for element 'cancel '
                if not bot.find("cancel", matching=0.97, waiting_time=10000):
                    not_found("cancel")
                bot.click()
              
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 72)
                
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                
                # Searching for element 'Cadastro '
                if not bot.find("Cadastro", matching=0.97, waiting_time=10000):
                    not_found("Cadastro")
                bot.click_relative(21, -21)
                
                
                # Searching for element 'Empresas '
                if not bot.find("Empresas", matching=0.97, waiting_time=10000):
                    not_found("Empresas")
                bot.click()                                
                
                # Searching for element 'GrupoDeEmpresas '
                if not bot.find("GrupoDeEmpresas", matching=0.97, waiting_time=10000):
                    not_found("GrupoDeEmpresas")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                self.type_keys_with_interval(50, "testeGrupoEmrpesa12!")
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'selecionatesteGE '
                if not bot.find("selecionatesteGE", matching=0.97, waiting_time=10000):
                    not_found("selecionatesteGE")
                bot.click()
                
                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()
                
                # Searching for element 'exclui '
                if not bot.find("exclui", matching=0.97, waiting_time=10000):
                    not_found("exclui")
                bot.click()
                
                # Searching for element 'sim '
                if not bot.find("sim", matching=0.97, waiting_time=10000):
                    not_found("sim")
                bot.click()
                
                # Searching for element 'retorna '
                if not bot.find("retorna", matching=0.97, waiting_time=10000):
                    not_found("retorna")
                bot.click_relative(-82, 68)
                # Searching for element 'localizar '
                if not bot.find("localizar", matching=0.97, waiting_time=10000):
                    not_found("localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                self.type_keys_with_interval(50, "testeGrupoEmrpesa12!")
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 71)



                ############### 
                # ATENÇÃO, USUARIO DE ACESSO
                # PRECISA TER A EMPRESA LIBERADA 
                # NO ADMINISTRADOR
                # PARA INCLUIR NOS PARAMETROS - F9
                ###############
                #                 
                # Searching for element 'Cadastros '
                if not bot.find("Cadastros", matching=0.97, waiting_time=10000):
                    not_found("Cadastros")
                bot.click()              
                                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()
                
                # Searching for element 'ParametrodaEmrpesa '
                if not bot.find("Parametro da Emrpesa", matching=0.97, waiting_time=10000):
                    not_found("Parametro da Emrpesa")
                bot.click()
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                # Searching for element 'Nao '
                if not bot.find("Nao", matching=0.97, waiting_time=10000):
                    not_found("Nao")
                bot.click()
                
                # Searching for element 'lupa '
                if not bot.find("lupa", matching=0.97, waiting_time=10000):
                    not_found("lupa")
                bot.click()
                                
                # Searching for element 'selecionaEmp '
                if not bot.find("selecionaEmp", matching=0.97, waiting_time=10000):
                    not_found("selecionaEmp")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'clickCampo '
                if not bot.find("clickCampo", matching=0.97, waiting_time=10000):
                    not_found("clickCampo")
                bot.click_relative(57, 187)

                self.type_down()
                self.type_down()
                self.type_down()
                self.type_up()
                self.enter()

                x = 0
                while x < 25:
                    self.type_down()
                    self.type_down()
                    self.type_down()
                    self.type_up()
                    self.tab()
                    x = x + 1
                
                # Searching for element 'CampoSetorDFrete '
                if not bot.find("CampoSetorDFrete", matching=0.97, waiting_time=10000):
                    not_found("CampoSetorDFrete")
                bot.click_relative(229, 8)

                self.type_keys_with_interval(50, "123")   

                # Searching for element 'campRelactiveNdCasasDecimaisTarifas '
                if not bot.find("campRelactiveNdCasasDecimaisTarifas", matching=0.97, waiting_time=10000):
                    not_found("campRelactiveNdCasasDecimaisTarifas")
                bot.click_relative(211, 8)                

                self.type_keys_with_interval(50, "123")                
                
                # Searching for element 'formulários '
                if not bot.find("formulários", matching=0.97, waiting_time=10000):
                    not_found("formulários")
                bot.click()
                
                # Searching for element '+ '
                if not bot.find("+", matching=0.97, waiting_time=10000):
                    not_found("+")
                bot.click()

                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_down() 
                self.tab()   
                self.type_down() 
                
                # Searching for element 'salvarVverdeso '
                if not bot.find("salvarVverdeso", matching=0.97, waiting_time=10000):
                    not_found("salvarVverdeso")
                bot.click_relative(-325, 240)
                
                # Searching for element 'MDFe '
                if not bot.find("MDFe", matching=0.97, waiting_time=10000):
                    not_found("MDFe")
                bot.click()
                
                # Searching for element '+d '
                if not bot.find("+d", matching=0.97, waiting_time=10000):
                    not_found("+d")
                bot.click()

                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                # Searching for element 'salvarVso '
                if not bot.find("salvarVso", matching=0.97, waiting_time=10000):
                    not_found("salvarVso")
                bot.click_relative(-329, 238)
                
                # Searching for element 'NdD '
                if not bot.find("NdD", matching=0.97, waiting_time=10000):
                    not_found("NdD")
                bot.click()

                # Searching for element 'selecionaCampoNOdC '
                if not bot.find("selecionaCampoNOdC", matching=0.97, waiting_time=10000):
                    not_found("selecionaCampoNOdC")
                bot.click_relative(82, 206)

                self.type_keys_with_interval(50, "99")

                self.tab()

                self.type_keys_with_interval(50, "99")
                
                self.tab()
                
                # Searching for element 'aba_codPadroes '
                if not bot.find("aba_codPadroes", matching=0.97, waiting_time=10000):
                    not_found("aba_codPadroes")
                bot.click()
                
                # Searching for element 'lp_codDOC '
                if not bot.find("lp_codDOC", matching=0.97, waiting_time=10000):
                    not_found("lp_codDOC")
                bot.click_relative(50, 23)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'TPP '
                if not bot.find("TPP", matching=0.97, waiting_time=10000):
                    not_found("TPP")
                bot.click_relative(52, 23)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpBombaDeCombustivel '
                if not bot.find("lpBomba De Combustivel", matching=0.97, waiting_time=10000):
                    not_found("lpBomba De Combustivel")
                bot.click_relative(52, 24)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpPSdA '
                if not bot.find("lpPSdA", matching=0.97, waiting_time=10000):
                    not_found("lpPSdA")
                bot.click_relative(52, 24)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpIMdO-OS '
                if not bot.find("lpIMdO-OS", matching=0.97, waiting_time=10000):
                    not_found("lpIMdO-OS")
                bot.click_relative(53, 26)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpCdP-C '
                if not bot.find("lpCdP-C", matching=0.97, waiting_time=10000):
                    not_found("lpCdP-C")
                bot.click_relative(51, 26)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                                
                # Searching for element 'lpCFRaE '
                if not bot.find("lpCFRaE", matching=0.97, waiting_time=10000):
                    not_found("lpCFRaE")
                bot.click_relative(60, 25)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123") 
                self.tab()
                self.type_keys_with_interval(50, "123")
                                
                ##### ABA exportação ftp #####
                 
                # Searching for element 'abaExportacaoFTP '
                if not bot.find("abaExportacaoFTP", matching=0.97, waiting_time=10000):
                    not_found("abaExportacaoFTP")
                bot.click()
                
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()        
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab() 
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'voltar '
                if not bot.find("voltar", matching=0.97, waiting_time=10000):
                    not_found("voltar")
                bot.click_relative(-86, 73)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'seleciona '
                if not bot.find("seleciona", matching=0.97, waiting_time=10000):
                    not_found("seleciona")
                bot.click()
                
                # Searching for element 'Editar '
                if not bot.find("Editar", matching=0.97, waiting_time=10000):
                    not_found("Editar")
                bot.click()
                
                # Searching for element 'Excluir '
                if not bot.find("Excluir", matching=0.97, waiting_time=10000):
                    not_found("Excluir")
                bot.click()
                
                # Searching for element 'Sim '
                if not bot.find("Sim", matching=0.97, waiting_time=10000):
                    not_found("Sim")
                bot.click()
                
                
                # Searching for element 'voltar '
                if not bot.find("voltar", matching=0.97, waiting_time=10000):
                    not_found("voltar")
                bot.click_relative(-81, 70)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'Voltar '
                if not bot.find("Voltar", matching=0.97, waiting_time=10000):
                    not_found("Voltar")
                bot.click_relative(-86, 71)

                # Searching for element 'Cadastros '
                if not bot.find("Cadastros", matching=0.97, waiting_time=10000):
                    not_found("Cadastros")
                bot.click()              
                                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()
                
                # Searching for element 'ParametrodaEmrpesa '
                if not bot.find("Parametro da Emrpesa", matching=0.97, waiting_time=10000):
                    not_found("Parametro da Emrpesa")
                bot.click()
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                # Searching for element 'Nao '
                if not bot.find("Nao", matching=0.97, waiting_time=10000):
                    not_found("Nao")
                bot.click()
                
                # Searching for element 'lupa '
                if not bot.find("lupa", matching=0.97, waiting_time=10000):
                    not_found("lupa")
                bot.click()
                                
                # Searching for element 'selecionaEmp '
                if not bot.find("selecionaEmp", matching=0.97, waiting_time=10000):
                    not_found("selecionaEmp")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'clickCampo '
                if not bot.find("clickCampo", matching=0.97, waiting_time=10000):
                    not_found("clickCampo")
                bot.click_relative(57, 187)

                self.type_down()
                self.type_down()
                self.type_down()
                self.type_up()
                self.enter()

                x = 0
                while x < 25:
                    self.type_down()
                    self.type_down()
                    self.type_down()
                    self.type_up()
                    self.tab()
                    x = x + 1
                
                # Searching for element 'CampoSetorDFrete '
                if not bot.find("CampoSetorDFrete", matching=0.97, waiting_time=10000):
                    not_found("CampoSetorDFrete")
                bot.click_relative(229, 8)

                self.type_keys_with_interval(50, "123")   

                # tirar print novo
                # campo 
                # n de casas decimais
                # Searching for element 'selecionaCampo '
                # Searching for element 'campRelactiveNdCasasDecimaisTarifas '
                if not bot.find("campRelactiveNdCasasDecimaisTarifas", matching=0.97, waiting_time=10000):
                    not_found("campRelactiveNdCasasDecimaisTarifas")
                bot.click_relative(211, 8)    

                self.type_keys_with_interval(50, "123")                
                
                # Searching for element 'formulários '
                if not bot.find("formulários", matching=0.97, waiting_time=10000):
                    not_found("formulários")
                bot.click()
                
                # Searching for element '+ '
                if not bot.find("+", matching=0.97, waiting_time=10000):
                    not_found("+")
                bot.click()

                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_down() 
                self.tab()   
                self.type_down() 
                
                # Searching for element 'salvarVverdeso '
                if not bot.find("salvarVverdeso", matching=0.97, waiting_time=10000):
                    not_found("salvarVverdeso")
                bot.click_relative(-325, 240)
                
                # Searching for element 'MDFe '
                if not bot.find("MDFe", matching=0.97, waiting_time=10000):
                    not_found("MDFe")
                bot.click()
                
                # Searching for element '+d '
                if not bot.find("+d", matching=0.97, waiting_time=10000):
                    not_found("+d")
                bot.click()

                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                # Searching for element 'salvarVso '
                if not bot.find("salvarVso", matching=0.97, waiting_time=10000):
                    not_found("salvarVso")
                bot.click_relative(-329, 238)
                
                # Searching for element 'NdD '
                if not bot.find("NdD", matching=0.97, waiting_time=10000):
                    not_found("NdD")
                bot.click()
                
                # Searching for element 'selecionaCampoNOdC '
                if not bot.find("selecionaCampoNOdC", matching=0.97, waiting_time=10000):
                    not_found("selecionaCampoNOdC")
                bot.click_relative(82, 206)

                self.type_keys_with_interval(50, "99")

                self.tab()

                self.type_keys_with_interval(50, "99")
                
                self.tab()
                
                # Searching for element 'aba_codPadroes '
                if not bot.find("aba_codPadroes", matching=0.97, waiting_time=10000):
                    not_found("aba_codPadroes")
                bot.click()
                
                # Searching for element 'lp_codDOC '
                if not bot.find("lp_codDOC", matching=0.97, waiting_time=10000):
                    not_found("lp_codDOC")
                bot.click_relative(50, 23)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'TPP '
                if not bot.find("TPP", matching=0.97, waiting_time=10000):
                    not_found("TPP")
                bot.click_relative(52, 23)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpBombaDeCombustivel '
                if not bot.find("lpBomba De Combustivel", matching=0.97, waiting_time=10000):
                    not_found("lpBomba De Combustivel")
                bot.click_relative(52, 24)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpPSdA '
                if not bot.find("lpPSdA", matching=0.97, waiting_time=10000):
                    not_found("lpPSdA")
                bot.click_relative(52, 24)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpIMdO-OS '
                if not bot.find("lpIMdO-OS", matching=0.97, waiting_time=10000):
                    not_found("lpIMdO-OS")
                bot.click_relative(53, 26)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                # Searching for element 'lpCdP-C '
                if not bot.find("lpCdP-C", matching=0.97, waiting_time=10000):
                    not_found("lpCdP-C")
                bot.click_relative(51, 26)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                                
                # Searching for element 'lpCFRaE '
                if not bot.find("lpCFRaE", matching=0.97, waiting_time=10000):
                    not_found("lpCFRaE")
                bot.click_relative(60, 25)
                
                # Searching for element 'lpLocalizar '
                if not bot.find("lpLocalizar", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizar")
                bot.click()
                
                # Searching for element 'selecionar '
                if not bot.find("selecionar", matching=0.97, waiting_time=10000):
                    not_found("selecionar")
                bot.click()
                
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123") 
                self.tab()
                self.type_keys_with_interval(50, "123")
                                
                ##### ABA exportação ftp #####
                 
                # Searching for element 'abaExportacaoFTP '
                if not bot.find("abaExportacaoFTP", matching=0.97, waiting_time=10000):
                    not_found("abaExportacaoFTP")
                bot.click()
                
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()        
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab() 
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'voltar '
                if not bot.find("voltar", matching=0.97, waiting_time=10000):
                    not_found("voltar")
                bot.click_relative(-86, 73)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'voltar '
                if not bot.find("voltar", matching=0.97, waiting_time=10000):
                    not_found("voltar")
                bot.click_relative(-86, 73)

                # #
                # #
                # # Cadastro parametros Configuração de formulários
                # #
                # #
                
                # Searching for element 'Cadastros '
                if not bot.find("Cadastros", matching=0.97, waiting_time=10000):
                    not_found("Cadastros")
                bot.click()
                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()
                                
                # Searching for element 'ConfdeFormulario '
                if not bot.find("Conf de Formulario", matching=0.97, waiting_time=10000):
                    not_found("Conf de Formulario")
                bot.click()
                
                # Searching for element 'incluir '
                if not bot.find("incluir", matching=0.97, waiting_time=10000):
                    not_found("incluir")
                bot.click()                
                
                self.type_keys_with_interval(50, "teste12!")
                
                self.tab()
                self.type_down()
    
                self.tab()
                self.type_left()
                self.tab()  
                self.type_left()
                self.type_left()
                self.type_left()
                self.type_left()
                self.tab() 
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")            
        
                # Searching for element 'cmpSeriePadrao '
                if not bot.find("cmpSeriePadrao", matching=0.97, waiting_time=10000):
                    not_found("cmpSeriePadrao")
                bot.click_relative(176, 289)

                self.type_keys_with_interval(50, "123")        
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                # Searching for element 'aba_Campos '
                if not bot.find("aba_Campos", matching=0.97, waiting_time=10000):
                    not_found("aba_Campos")
                bot.click()
                
                # Searching for element 'incluirSmall '
                if not bot.find("incluirSmall", matching=0.97, waiting_time=10000):
                    not_found("incluirSmall")
                bot.click()

                self.type_keys_with_interval(50, "teste")
                self.tab()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.enter()
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'aba_Lista '
                if not bot.find("aba_Lista", matching=0.97, waiting_time=10000):
                    not_found("aba_Lista")
                bot.click()
                
                # Searching for element 'aba_CopiaConfig '
                if not bot.find("aba_CopiaConfig", matching=0.97, waiting_time=10000):
                    not_found("aba_CopiaConfig")
                bot.click()
                
                # Searching for element 'slCampo '
                if not bot.find("slCampo", matching=0.97, waiting_time=10000):
                    not_found("slCampo")
                bot.click_relative(-20, 35)                                
                
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
    
                # Searching for element 'Copiar '
                if not bot.find("Copiar", matching=0.97, waiting_time=10000):
                    not_found("Copiar")
                bot.click()
                
                # Searching for element 'Sim '
                if not bot.find("Sim", matching=0.97, waiting_time=10000):
                    not_found("Sim")
                bot.click()
                
                # Searching for element 'Ok '
                if not bot.find("Ok", matching=0.97, waiting_time=10000):
                    not_found("Ok")
                bot.click()
                
                # Searching for element 'aba_Ajustes '
                if not bot.find("aba_Ajustes", matching=0.97, waiting_time=10000):
                    not_found("aba_Ajustes")
                bot.click()
                
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.space()
                self.space()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-82, 68)

                self.space()
    
                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()
                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()
                
                # Searching for element 'LiberacaoeBloqeiodePeriodos '
                if not bot.find("LiberacaoeBloqeiodePeriodos", matching=0.97, waiting_time=10000):
                    not_found("LiberacaoeBloqeiodePeriodos")
                bot.click()
                                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'seleciona '
                if not bot.find("seleciona", matching=0.97, waiting_time=10000):
                    not_found("seleciona")
                bot.click()          
                
                # Searching for element 'Editar '
                if not bot.find("Editar", matching=0.97, waiting_time=10000):
                    not_found("Editar")
                bot.click()

                # Searching for element 'selecionaCampo '
                if not bot.find("selecionaCampo", matching=0.97, waiting_time=10000):
                    not_found("selecionaCampo")
                bot.click_relative(-4, 66)
                

                x = 0
                while x < 10:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.tab()
                    x = x + 1
                #o while acima preenche os campos de data da primeora aba
                
                # Searching for element 'aba_contabileePatrimonio '
                if not bot.find("aba_contabileePatrimonio", matching=0.97, waiting_time=10000):
                    not_found("aba_contabileePatrimonio")
                bot.click()
                
                # Searching for element 'selecionaCampo '
                if not bot.find("selecionaCampo", matching=0.97, waiting_time=10000):
                    not_found("selecionaCampo")
                bot.click_relative(-2, 65)
                
                
                x = 0
                while x < 3:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.tab()
                    x = x + 1
                
                # Searching for element 'abaFiscal '
                if not bot.find("abaFiscal", matching=0.97, waiting_time=10000):
                    not_found("abaFiscal")
                bot.click()
                
                # Searching for element 'selecionacampow '
                if not bot.find("selecionacampow", matching=0.97, waiting_time=10000):
                    not_found("selecionacampow")
                bot.click_relative(-2, 65)
                
                
                x = 0
                while x < 2:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.tab()
                    x = x + 1

                # Searching for element 'aba_MovimentodeItens '
                if not bot.find("aba_MovimentodeItens", matching=0.97, waiting_time=10000):
                    not_found("aba_MovimentodeItens")
                bot.click()
                
                # Searching for element 'selecttheCamp '
                if not bot.find("selecttheCamp", matching=0.97, waiting_time=10000):
                    not_found("selecttheCamp")
                bot.click_relative(-2, 66)
                
                
                x = 0
                while x < 2:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.tab()
                    x = x + 1
                
                # Searching for element 'ABA_RH '
                if not bot.find("ABA_RH", matching=0.97, waiting_time=10000):
                    not_found("ABA_RH")
                bot.click()
                
                # Searching for element 'selectTheCampRHpre '
                if not bot.find("selectTheCampRHpre", matching=0.97, waiting_time=10000):
                    not_found("selectTheCampRHpre")
                bot.click_relative(-3, 66)
                
                
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                # Searching for element 'ABA_Bloqueios '
                if not bot.find("ABA_Bloqueios", matching=0.97, waiting_time=10000):
                    not_found("ABA_Bloqueios")
                bot.click()
                
                # Searching for element 'seleBloqueCampos '
                if not bot.find("seleBloqueCampos", matching=0.97, waiting_time=10000):
                    not_found("seleBloqueCampos")
                bot.click_relative(-1, 66)
                

                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                
                # Searching for element 'ABA_Transportes '
                if not bot.find("ABA_Transportes", matching=0.97, waiting_time=10000):
                    not_found("ABA_Transportes")
                bot.click()
                
                # Searching for element 'transpSelectTheCamp '
                if not bot.find("transpSelectTheCamp", matching=0.97, waiting_time=10000):
                    not_found("transpSelectTheCamp")
                bot.click_relative(-3, 64)
                

                x = 0
                while x <= 2:
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.type_keys_with_interval(50, "123")
                    self.tab()
                    self.tab()
                    x = x + 1                  
                            
                # Searching for element 'salvar_AbaDatas '
                if not bot.find("salvar_AbaDatas", matching=0.97, waiting_time=10000):
                    not_found("salvar_AbaDatas")
                bot.click()
                
                # Searching for element 'returnRelactivePneuRef '
                if not bot.find("returnRelactivePneuRef", matching=0.97, waiting_time=10000):
                    not_found("returnRelactivePneuRef")
                bot.click_relative(-39, 69)
                
                # Searching for element 'reltiveReturnofNew '
                if not bot.find("reltiveReturnofNew", matching=0.97, waiting_time=10000):
                    not_found("reltiveReturnofNew")
                bot.click_relative(-40, 70)

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()
                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()
                
                # Searching for element 'LiberacaoeBloqeiodePeriodos '
                if not bot.find("LiberacaoeBloqeiodePeriodos", matching=0.97, waiting_time=10000):
                    not_found("LiberacaoeBloqeiodePeriodos")
                bot.click()
                                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'seleciona '
                if not bot.find("seleciona", matching=0.97, waiting_time=10000):
                    not_found("seleciona")
                bot.click()          
                
                # Searching for element 'Editar '
                if not bot.find("Editar", matching=0.97, waiting_time=10000):
                    not_found("Editar")
                bot.click()
                
                # Searching for element 'ExluirDatas '
                if not bot.find("ExluirDatas", matching=0.97, waiting_time=10000):
                    not_found("ExluirDatas")
                bot.click()
                # Searching for element 'SimExcluirDatasV '
                if not bot.find("SimExcluirDatasV", matching=0.97, waiting_time=10000):
                    not_found("SimExcluirDatasV")
                bot.click()
                
                # Searching for element 'returnRelactivePneuRef '
                if not bot.find("returnRelactivePneuRef", matching=0.97, waiting_time=10000):
                    not_found("returnRelactivePneuRef")
                bot.click_relative(-39, 69)
                
                # Searching for element 'reltiveReturnofNew '
                if not bot.find("reltiveReturnofNew", matching=0.97, waiting_time=10000):
                    not_found("reltiveReturnofNew")
                bot.click_relative(-40, 70)
                
                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()
                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()

                # Searching for element 'ConfDeIntefracaodetal '
                if not bot.find("ConfDeIntefracaodetal", matching=0.97, waiting_time=10000):
                    not_found("ConfDeIntefracaodetal")
                bot.click()

                # Searching for element 'selecionaCampoBicoabaparanhos '
                if not bot.find("selecionaCampoBicoabaparanhos", matching=0.97, waiting_time=10000):
                    not_found("selecionaCampoBicoabaparanhos")
                bot.click_relative(68, 40)

                self.type_keys_with_interval(50, "01")
                self.tab()
                self.type_keys_with_interval(50, "01")
                self.tab()

                # Searching for element 'salvarNewBicostest01 '
                if not bot.find("salvarNewBicostest01", matching=0.97, waiting_time=10000):
                    not_found("salvarNewBicostest01")
                bot.click()

                # Searching for element 'returnRelactivePneuRef '
                if not bot.find("returnRelactivePneuRef", matching=0.97, waiting_time=10000):
                    not_found("returnRelactivePneuRef")
                bot.click_relative(-39, 69)
                
                # Searching for element 'reltiveReturnofNew '
                if not bot.find("reltiveReturnofNew", matching=0.97, waiting_time=10000):
                    not_found("reltiveReturnofNew")
                bot.click_relative(-40, 70)

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()
                
                # Searching for element 'Parametros '
                if not bot.find("Parametros", matching=0.97, waiting_time=10000):
                    not_found("Parametros")
                bot.click()
                
                # Searching for element 'cadastroConfiguracaoWSDLMultiCTe '
                if not bot.find("cadastroConfiguracaoWSDLMultiCTe", matching=0.97, waiting_time=10000):
                    not_found("cadastroConfiguracaoWSDLMultiCTe")
                bot.click()
                
                # Searching for element 'addconfiuracaodoMultiCTE '
                if not bot.find("addconfiuracaodoMultiCTE", matching=0.97, waiting_time=10000):
                    not_found("addconfiuracaodoMultiCTE")
                bot.click()
                
                self.type_keys_with_interval(50, "teste")
                self.tab()
                self.type_keys_with_interval(50, "https://teorema.inf.br/")
                self.tab()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "teste")

                # Searching for element 'salvarConfiguracaodoMultiCTE '
                if not bot.find("salvarConfiguracaodoMultiCTE", matching=0.97, waiting_time=10000):
                    not_found("salvarConfiguracaodoMultiCTE")
                bot.click()

                # Searching for element 'editartestedescricaodatelaparametros '
                if not bot.find("editartestedescricaodatelaparametros", matching=0.97, waiting_time=10000):
                    not_found("editartestedescricaodatelaparametros")
                bot.click()

                self.type_keys_with_interval(50, "teste12")

                # Searching for element 'salvarConfiguracaodoMultiCTE '
                if not bot.find("salvarConfiguracaodoMultiCTE", matching=0.97, waiting_time=10000):
                    not_found("salvarConfiguracaodoMultiCTE")
                bot.click()

                # Searching for element 'excluirCadastroConfMultiCtesbj '
                if not bot.find("excluirCadastroConfMultiCtesbj", matching=0.97, waiting_time=10000):
                    not_found("excluirCadastroConfMultiCtesbj")
                bot.click()
                self.enter()

                # Searching for element 'addconfiuracaodoMultiCTE '
                if not bot.find("addconfiuracaodoMultiCTE", matching=0.97, waiting_time=10000):
                    not_found("addconfiuracaodoMultiCTE")
                bot.click()
                
                self.type_keys_with_interval(50, "teste")
                self.tab()
                self.type_keys_with_interval(50, "https://teorema.inf.br/")
                self.tab()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "teste")

                # Searching for element 'salvarConfiguracaodoMultiCTE '
                if not bot.find("salvarConfiguracaodoMultiCTE", matching=0.97, waiting_time=10000):
                    not_found("salvarConfiguracaodoMultiCTE")
                bot.click()

                # Searching for element 'fecharTelaCadastroCTEconfiguracao '
                if not bot.find("fecharTelaCadastroCTEconfiguracao", matching=0.97, waiting_time=10000):
                    not_found("fecharTelaCadastroCTEconfiguracao")
                bot.click_relative(616, -37)

                ########################################
                ###### CADASTROS DE PARAMETROS FISCAIS #############
                ########################################

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()
                
                # Searching for element 'RegionalizacaoReutilizar '
                if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                    not_found("RegionalizacaoReutilizar")
                bot.click()

                # Searching for element 'RegionalizacaoReutilizar '
                if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                    not_found("RegionalizacaoReutilizar")
                bot.click()
                
                # Searching for element 'PaisesRegionalizacoes '
                if not bot.find("PaisesRegionalizacoes", matching=0.97, waiting_time=10000):
                    not_found("PaisesRegionalizacoes")
                bot.click()

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "testePais")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "testePais2")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'Excluir '
                if not bot.find("Excluir", matching=0.97, waiting_time=10000):
                    not_found("Excluir")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()
                
                # Searching for element 'RegionalizacaoReutilizar '
                if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                    not_found("RegionalizacaoReutilizar")
                bot.click()

                # Searching for element 'RegionalizacaoReutilizar '
                if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                    not_found("RegionalizacaoReutilizar")
                bot.click()

                # Searching for element 'Regioes '
                if not bot.find("Regioes", matching=0.97, waiting_time=10000):
                    not_found("Regioes")
                bot.click()

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_down()
                self.tab()
                self.type_down()

                # # Searching for element 'clicaparaselecionarocampodatelaCadastroRegioes '
                # if not bot.find("clicaparaselecionarocampodatelaCadastroRegioes", matching=0.97, waiting_time=10000):
                #     not_found("clicaparaselecionarocampodatelaCadastroRegioes")
                # bot.click_relative(4, 30)
                # self.type_down()
                # self.type_down()

                # # Searching for element 'clicaparaselecionarocampodatelaCadastroRegioes22 '
                # if not bot.find("clicaparaselecionarocampodatelaCadastroRegioes22", matching=0.97, waiting_time=10000):
                #     not_found("clicaparaselecionarocampodatelaCadastroRegioes22")
                # bot.click_relative(5, 31)
                # self.type_down()
                # self.type_down()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "teste123!")
                self.tab()
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_up()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_up()
                self.type_up()

                # # Searching for element 'clicaparaselecionarocampodatelaCadastroRegioes '
                # if not bot.find("clicaparaselecionarocampodatelaCadastroRegioes", matching=0.97, waiting_time=10000):
                #     not_found("clicaparaselecionarocampodatelaCadastroRegioes")
                # bot.click_relative(4, 30)
                # self.type_down()
                # self.type_down()

                # Searching for element 'clicaparaselecionarocampodatelaCadastroRegioes22 '
                # if not bot.find("clicaparaselecionarocampodatelaCadastroRegioes22", matching=0.97, waiting_time=10000):
                #     not_found("clicaparaselecionarocampodatelaCadastroRegioes22")
                # bot.click_relative(5, 31)
                # self.type_down()
                # self.type_down()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()
                
                # Searching for element 'Excluir '
                if not bot.find("Excluir", matching=0.97, waiting_time=10000):
                    not_found("Excluir")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                #### Estados ###
                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()
                
                # Searching for element 'RegionalizacaoReutilizar '
                if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                    not_found("RegionalizacaoReutilizar")
                bot.click()

                # Searching for element 'RegionalizacaoReutilizar '
                if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                    not_found("RegionalizacaoReutilizar")
                bot.click()

                # Searching for element 'EstadosSelecionaparacadastrar '
                if not bot.find("EstadosSelecionaparacadastrar", matching=0.97, waiting_time=10000):
                    not_found("EstadosSelecionaparacadastrar")
                bot.click()

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "teste123!")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'Excluir '
                if not bot.find("Excluir", matching=0.97, waiting_time=10000):
                    not_found("Excluir")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                ###### AQUI TA DANDO UM BO NA AUTOMACAO

                # # Searching for element 'cadastros '
                # if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                #     not_found("cadastros")
                # bot.click()

                # # Searching for element 'ParametrosFiscais '
                # if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                #     not_found("ParametrosFiscais")
                # bot.click()
                
                # # Searching for element 'RegionalizacaoReutilizar '
                # if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                #     not_found("RegionalizacaoReutilizar")
                # bot.click()

                # # Searching for element 'RegionalizacaoReutilizar '
                # if not bot.find("RegionalizacaoReutilizar", matching=0.97, waiting_time=10000):
                #     not_found("RegionalizacaoReutilizar")
                # bot.click()

                # # Searching for element 'cadastroMunicipiosparametrosfiscaisparairparatelacadastro '
                # if not bot.find("cadastroMunicipiosparametrosfiscaisparairparatelacadastro", matching=0.97, waiting_time=10000):
                #     not_found("cadastroMunicipiosparametrosfiscaisparairparatelacadastro")
                # bot.click()

                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()

                # # Searching for element 'btn_cadastro_incluir'
                # if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                #     not_found("btn_cadastro_incluir")
                # bot.click()

                # self.type_keys_with_interval(50, "teste12!")
                # self.tab()
                # self.type_down()
                # self.type_up()
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(50, "01")
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "1")

                # # Searching for element 'btn_Salvar_form'
                # if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                #     not_found("btn_Salvar_form")
                # bot.click()

                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 68)

                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()

                # # Searching for element 'btn_cadastro_incluir'
                # if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                #     not_found("btn_cadastro_incluir")
                # bot.click()

                # self.type_keys_with_interval(50, "teste123!")
                # self.tab()
                # self.type_down()
                # self.type_up()
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(50, "01")
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # self.tab()
                # self.type_keys_with_interval(50, "1")

                # # Searching for element 'btn_Salvar_form'
                # if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                #     not_found("btn_Salvar_form")
                # bot.click()

                # # Searching for element 'subabacadastroFeriadosMunicipais '
                # if not bot.find("subabacadastroFeriadosMunicipais", matching=0.97, waiting_time=10000):
                #     not_found("subabacadastroFeriadosMunicipais")
                # bot.click()

                # # Searching for element 'adicionar+botaopequenoverde '
                # if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                #     not_found("adicionar+botaopequenoverde")
                # bot.click()

                # self.type_down()
                # self.type_down()
                # self.tab()
                # self.type_down()
                # self.type_down()
                # self.tab()
                # self.type_keys_with_interval(50, "Teste Descrição feriado")

                # # Searching for element 'checkverdepequenosalvardescricaocadastroferiadotela '
                # if not bot.find("checkverdepequenosalvardescricaocadastroferiadotela", matching=0.97, waiting_time=10000):
                #     not_found("checkverdepequenosalvardescricaocadastroferiadotela")
                # bot.click_relative(8, -13)

                # # Searching for element 'lixeirapequenaExluirferiado '
                # if not bot.find("lixeirapequenaExluirferiado", matching=0.97, waiting_time=10000):
                #     not_found("lixeirapequenaExluirferiado")
                # bot.click_relative(7, -36)
                # self.enter()

                # # Searching for element 'Excluir '
                # if not bot.find("Excluir", matching=0.97, waiting_time=10000):
                #     not_found("Excluir")
                # bot.click()
                
                # # Searching for element 'sIMV '
                # if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                #     not_found("sIMV")
                # bot.click()

                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 68)

                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 68)

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()

                # Searching for element 'clicapentrarTelaGrupoFiscaldeItens '
                if not bot.find("clicapentrarTelaGrupoFiscaldeItens", matching=0.97, waiting_time=10000):
                    not_found("clicapentrarTelaGrupoFiscaldeItens")
                bot.click()

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "Teste12!")
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "123")

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "Teste123!")
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "123")

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'Excluir '
                if not bot.find("Excluir", matching=0.97, waiting_time=10000):
                    not_found("Excluir")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                ############### Cadastro Parametros Fiscais Códigos Fiscais (CFOP) #############

                #Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()

                # Searching for element 'clickpentrartelaCadCodigodeOperacoesdeParametrosFiscais '
                if not bot.find("clickpentrartelaCadCodigodeOperacoesdeParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("clickpentrartelaCadCodigodeOperacoesdeParametrosFiscais")
                bot.click()

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.wait(1500)

                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()

                self.type_keys_with_interval(50, "teste Cadastro de código de operação")
                
                # Searching for element 'selectCampOperacaoEstoqueopn '
                if not bot.find("selectCampOperacaoEstoqueopn", matching=0.97, waiting_time=10000):
                    not_found("selectCampOperacaoEstoqueopn")
                bot.click_relative(32, 43)               

                x = 0
                while x < 34:
                    self.type_down() 
                    self.type_down() 
                    self.type_down() 
                    self.type_up()                    
                    self.tab()
                    x = x + 1
                self.tab()
                self.space()
                self.tab()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 28:
                    self.space()                    
                    self.tab()
                    x = x + 1
                # Searching for element 'incluirnumerosCadcodO '
                if not bot.find("incluirnumerosCadcodO", matching=0.97, waiting_time=10000):
                    not_found("incluirnumerosCadcodO")
                bot.click_relative(17, 27)

                x = 0
                while x < 6:
                    self.type_keys_with_interval(100, "123")                   
                    self.tab()
                    self.tab()
                    x = x + 1    

                # Searching for element 'botaoqueaoclicarSalvaOperacaotlcadcodop '
                if not bot.find("botaoqueaoclicarSalvaOperacaotlcadcodop", matching=0.97, waiting_time=10000):
                    not_found("botaoqueaoclicarSalvaOperacaotlcadcodop")
                bot.click()

                # Searching for element 'subAbaDadosAdicionaistelaCadcopOp '
                if not bot.find("subAbaDadosAdicionaistelaCadcopOp", matching=0.97, waiting_time=10000):
                    not_found("subAbaDadosAdicionaistelaCadcopOp")
                bot.click()

                # Searching for element 'subabaLPCFOPPadraodoMovimento '
                if not bot.find("subabaLPCFOPPadraodoMovimento", matching=0.97, waiting_time=10000):
                    not_found("subabaLPCFOPPadraodoMovimento")
                bot.click_relative(61, 25)

                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()

                # Searching for element 'subabaLPCadcodOpTabeladePreco '
                if not bot.find("subabaLPCadcodOpTabeladePreco", matching=0.97, waiting_time=10000):
                    not_found("subabaLPCadcodOpTabeladePreco")
                bot.click_relative(64, 30)

                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.backspace()

                # Searching for element 'subabaLPCadcodOpTabeladePreco '
                if not bot.find("subabaLPCadcodOpTabeladePreco", matching=0.97, waiting_time=10000):
                    not_found("subabaLPCadcodOpTabeladePreco")
                bot.click_relative(64, 30)

                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.backspace()

                # Searching for element 'addTextoObstestestest '
                if not bot.find("addTextoObstestestest", matching=0.97, waiting_time=10000):
                    not_found("addTextoObstestestest")
                bot.click_relative(64, 139)
                self.type_keys_with_interval(50, "Teste12!")
                self.tab()
                self.tab()

                # Searching for element 'subabaObservacoestelaCadCopOpteste '
                if not bot.find("subabaObservacoestelaCadCopOpteste", matching=0.97, waiting_time=10000):
                    not_found("subabaObservacoestelaCadCopOpteste")
                bot.click()

                self.type_keys_with_interval(50, "Teste 12 ! teste12!")
                self.wait(2000)

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()

                # Searching for element 'clickparaCadastroCodigosficaisCFOP '
                if not bot.find("clickparaCadastroCodigosficaisCFOP", matching=0.97, waiting_time=10000):
                    not_found("clickparaCadastroCodigosficaisCFOP")
                bot.click()

                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "1234")
                self.tab()
                self.type_keys_with_interval(50, "teste12!")
                self.tab()
                self.type_keys_with_interval(50, "01")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab() 
                self.space()
                self.tab() 
                self.space()
                self.tab() 
                self.space()
                self.tab() 
                self.space()
                self.tab() 
                self.space()
                self.tab() 
                self.type_keys_with_interval(50, "12")
                self.tab() 
                self.space()
                self.tab() 
                self.space()
                self.tab() 
                self.space()
                self.tab() 
                self.type_right()
                self.tab() 
                self.type_right()
                self.type_right()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                ######
                ###### Temporario
                # ######
                # # Searching for element 'tempCancelaropparavoltar '
                # if not bot.find("tempCancelaropparavoltar", matching=0.97, waiting_time=10000):
                #     not_found("tempCancelaropparavoltar")
                # bot.click()
                # # Searching for element 'SimTempoParaVoltarOp '
                # if not bot.find("SimTempoParaVoltarOp", matching=0.97, waiting_time=10000):
                #     not_found("SimTempoParaVoltarOp")
                # bot.click()
                # ######
                # ######
                ######

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                ######### Cadastro Parametros fiscais Decretos e Observações #####

                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()

                # Searching for element 'ParametrosFiscais '
                if not bot.find("ParametrosFiscais", matching=0.97, waiting_time=10000):
                    not_found("ParametrosFiscais")
                bot.click()
                # Searching for element 'entratelaCadDecretoseObservacoes '
                if not bot.find("entratelaCadDecretoseObservacoes", matching=0.97, waiting_time=10000):
                    not_found("entratelaCadDecretoseObservacoes")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                self.type_keys_with_interval(50, "Teste12!")
                # Searching for element 'clickdetretocamptest '
                if not bot.find("clickdetretocamptest", matching=0.97, waiting_time=10000):
                    not_found("clickdetretocamptest")
                bot.click()
                self.type_right()
                self.type_right()
                self.type_right()
                self.type_left()
                self.type_left()
                self.type_left()
                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                ##### Cadastro Parametros Fiscais -> Situações #####
                ######################################################################
                             ##############---SITUACOES---################
                ######################################################################
                
                self.wait(2000)
                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "situacoes", matching=0.97, waiting_time=10000):
                    self.not_found("situacoes")
                self.click()           
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()
                self.wait(500)
                # if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                #     not_found("fatu_cad_param_receituario_retornar")
                # bot.click()
                # if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                #     self.not_found("incluirco")
                # self.click()
                # if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                #     self.not_found("incluirco")
                # self.click()
                if not self.find( "operacaosituacao", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosituacao")
                self.click_relative(50, 27)
                self.wait(2000)
                self.type_keys_with_interval(100,"0047")
                self.wait(1500)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(500)
                if not self.find( "regiaosituacao", matching=0.97, waiting_time=10000):
                    self.not_found("regiaosituacao")
                self.click_relative(47, 26)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # if not bot.find( "fatu_nordeste_situacoes_achar_btn", matching=0.97, waiting_time=10000):
                #     not_found("fatu_nordeste_situacoes_achar_btn")
                # bot.click()                                 
                # Searching for element 'btn_selecionar'
                self.type_keys_with_interval(100,"03")
                
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(500)
                if not self.find( "grupofiscalsituacao", matching=0.97, waiting_time=10000):
                    self.not_found("grupofiscalsituacao")
                self.click_relative(51, 30)
                # if not self.find( "cod001btributado", matching=0.97, waiting_time=10000):
                #     self.not_found("cod001btributado")
                # self.click()
                # if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarcfoppadrao")
                # self.click()
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(500)
                                ####---ICMS---####                                
                if not self.find( "icmsbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("icmsbasecalculo")
                self.click_relative(146, 50)            
                self.type_keys_with_interval(1,'123')
                if not self.find( "icmsbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("icmsbasecalculo")
                self.click_relative(140, 29)
                self.type_keys_with_interval(1,'123')
                x=0
                while x<5:
                    if not self.find( "icmstipo", matching=0.97, waiting_time=10000):
                        self.not_found("icmstipo")
                    self.click_relative(621, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<5:
                    if not self.find( "icmstipo", matching=0.97, waiting_time=10000):
                        self.not_found("icmstipo")
                    self.click_relative(621, 47)
                    self.type_up()
                    self.enter()
                    x=x+1
                if not self.find( "redutoraliquotabase", matching=0.97, waiting_time=10000):
                    self.not_found("redutoraliquotabase")
                self.click_relative(140, 27)
                self.type_keys_with_interval(1,'123')
                if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                    self.not_found("saldobasereduzicms")
                self.click_relative(142, 31)
                self.type_down()
                self.enter()
                if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                    self.not_found("saldobasereduzicms")
                self.click_relative(142, 31)
                self.type_down()
                self.enter()
                if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                    self.not_found("saldobasereduzicms")
                self.click_relative(142, 31)
                self.type_down()
                self.enter()
                x=0
                while x<4:
                    if not self.find( "icmsmodalidade", matching=0.97, waiting_time=10000):
                        self.not_found("icmsmodalidade")
                    self.click_relative(1261, 45)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "icmsmodalidade", matching=0.97, waiting_time=10000):
                        self.not_found("icmsmodalidade")
                    self.click_relative(1261, 45)
                    self.type_up()
                    self.enter()
                    x=x+1
                x=0
                while x<20:
                    if not self.find( "situacaotributariaicms", matching=0.97, waiting_time=10000):
                        self.not_found("situacaotributariaicms")
                    self.click_relative(300, 96)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "baseicmsdiferencaliquota", matching=0.97, waiting_time=10000):
                    self.not_found("baseicmsdiferencaliquota")
                self.click_relative(141, 27)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aliquotadiferencialicms", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotadiferencialicms")
                self.click_relative(142, 27)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aliquotaicmsdesoneracao", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotaicmsdesoneracao")
                self.click_relative(141, 30)           
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                x=0
                while x<12:
                    if not self.find( "motivodesoneracaoicms", matching=0.97, waiting_time=10000):
                        self.not_found("motivodesoneracaoicms")
                    self.click_relative(296, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.enter()    
                if not self.find( "descontadovalortotalicms", matching=0.97, waiting_time=10000):
                    self.not_found("descontadovalortotalicms")
                self.click()
                if not self.find( "descontadovalortotalmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("descontadovalortotalmarcado")
                self.click()
                if not self.find( "descontadovalortotal1", matching=0.97, waiting_time=10000):
                    self.not_found("descontadovalortotal1")
                self.click()
                if not self.find( "calculardiferimentoicms", matching=0.97, waiting_time=10000):
                    self.not_found("calculardiferimentoicms")
                self.click()
                
                if not self.find( "cteemoutrasuf", matching=0.97, waiting_time=10000):
                    self.not_found("cteemoutrasuf")
                self.click()
                                
                if not self.find( "icmsstdifinterno", matching=0.97, waiting_time=10000):
                    self.not_found("icmsstdifinterno")
                self.click_relative(197, 25)
                self.type_down()
                self.enter()
                if not self.find( "icmsstdifinterno", matching=0.97, waiting_time=10000):
                    self.not_found("icmsstdifinterno")
                self.click_relative(197, 25)
                self.type_down()
                self.enter()
                
                self.wait(1000)
                                ####---ICMS SUBS TRIBU---####                  
                if not self.find( "icmssubstrib", matching=0.97, waiting_time=10000):
                    self.not_found("icmssubstrib")
                self.click_relative(143, 46)
                self.type_keys_with_interval(1,'123')
                self.wait(1000)
                self.enter()
                if not self.find( "icmssubstibaliq", matching=0.97, waiting_time=10000):
                    self.not_found("icmssubstibaliq")
                self.click_relative(305, 46)
                self.type_keys_with_interval(1,'123')
                self.wait(1000)
                self.enter()
                if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("stnototaldodocumento")
                self.click_relative(140, 28)
                self.type_up()
                self.enter()
                if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("stnototaldodocumento")
                self.click_relative(140, 28)
                self.type_down()
                self.enter()
                if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("stnototaldodocumento")
                self.click_relative(140, 28)
                self.type_down()
                self.enter()
                self.enter()
                if not self.find( "reduzirvalordoicms", matching=0.97, waiting_time=10000):
                    self.not_found("reduzirvalordoicms")
                self.click()
                if not self.find( "reduzirvalordoicmsmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("reduzirvalordoicmsmarcado")
                self.click()
                x=0
                while x<5:
                    if not self.find( "tipoantecipacaovalida", matching=0.97, waiting_time=10000):
                        self.not_found("tipoantecipacaovalida")
                    self.click_relative(295, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<7:
                    if not bot.find( "fatu_modalidade_rel_cad_situacoes", matching=0.97, waiting_time=10000):
                        not_found("fatu_modalidade_rel_cad_situacoes")
                    bot.click_relative(343, 92)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "percentualreducaobaseicmsst", matching=0.97, waiting_time=10000):
                    self.not_found("percentualreducaobaseicmsst")
                self.click_relative(175, 23)
                self.type_keys_with_interval(1,'123')
                self.wait(1000)
                if not bot.find( "fatu_cad_situacoes_flecha_esquerda", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_flecha_esquerda")
                bot.click()
                x = 0
                while x < 31:
                    self.click()
                    x += 1
                
                if not self.find( "baseicmsdifst", matching=0.97, waiting_time=10000):
                    self.not_found("baseicmsdifst")
                self.click_relative(140, 30)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aliquotadiferencialst", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotadiferencialst")
                self.click_relative(142, 30)
                self.type_keys_with_interval(1,'123') 
                self.wait(500)
                self.enter()             
                
                                ####---ICMS SUB TRIB RETIDA---####   
                
                if not self.find( "icmsretida", matching=0.97, waiting_time=10000):
                    self.not_found("icmsretida")
                self.click_relative(144, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()            
                if not self.find( "icmsretida", matching=0.97, waiting_time=10000):
                    self.not_found("icmsretida")
                self.click_relative(303, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()
                x=0
                while x<7:
                    if not self.find( "valororigembasedecalculo", matching=0.97, waiting_time=10000):
                        self.not_found("valororigembasedecalculo")
                    self.click_relative(297, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "aliquotafcpretida", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotafcpretida")
                self.click_relative(140, 32)
                self.type_keys_with_interval(1,'123')
                
                                ####---IPI---####
                
                if not self.find( "IPIbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("IPIbasecalculo")
                self.click_relative(143, 47)
                self.type_keys_with_interval(1,'123')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()
                
                if not self.find( "ipialiquota", matching=0.97, waiting_time=10000):
                    self.not_found("ipialiquota")
                self.click_relative(303, 46)
                self.type_keys_with_interval(1,'1')
                self.backspace()
                self.type_keys_with_interval(1,'0')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()
                
                x=0
                while x<6:
                    if not self.find( "ipitipo", matching=0.97, waiting_time=10000):
                        self.not_found("ipitipo")
                    self.click_relative(624, 46)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "enquadramentoipi", matching=0.97, waiting_time=10000):
                    self.not_found("enquadramentoipi")
                self.click_relative(40, 27)
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "ipirsquantidade", matching=0.97, waiting_time=10000):
                    self.not_found("ipirsquantidade")
                self.click_relative(141, 27)
                self.type_keys_with_interval(1,'123')

                # x=0
                # while x<14:
                #     if not bot.find( "fatu_btn_situacao_tributaria_2411_rel", matching=0.97, waiting_time=10000):
                #         not_found("fatu_btn_situacao_tributaria_2411_rel")
                #     bot.click_relative(453, 27)
                #     self.type_down()
                #     self.enter()
                #     x=x+1

                self.wait(500)
                self.enter()
                self.space()
                self.enter()
                self.space()
                

                if not bot.find( "fatu_cad_situacoes_flecha_esquerda", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_flecha_esquerda")
                bot.click()
                x = 0
                while x < 31:
                    self.click()
                    x += 1
                
                if not bot.find( "fatu_cad_btn_descer_flecha_situacoes", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_descer_flecha_situacoes")
                bot.click()

                x = 0
                while x < 30:
                    self.click()
                    x += 1
                
                self.wait(1500)
                if not bot.find( "fatu_cad_situacoes_frete_base_ipi", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_frete_base_ipi")
                bot.click()
                
                self.wait(1500)
                if not bot.find( "fatu_cad_situacoes_frete_base_marcado", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_frete_base_marcado")
                bot.click()
                if not bot.find( "fatu_cad_situacoes_ipi_base_sub", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_ipi_base_sub")
                bot.click()
                self.wait(1000)
                self.space()
                
                self.enter()
                if not self.find( "indicevariacaopreco", matching=0.97, waiting_time=10000):
                    self.not_found("indicevariacaopreco")
                self.click_relative(140, 30)
                self.type_keys_with_interval(1,'123')
                if not self.find( "cancelacalculadoraipi", matching=0.97, waiting_time=10000):
                    self.not_found("cancelacalculadoraipi")
                self.click()
                
                if not self.find( "basepresumidomapafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("basepresumidomapafiscal")
                self.click_relative(140, 26)
                self.type_keys_with_interval(1,'123')
                if not self.find( "cancelacalculadoraipi", matching=0.97, waiting_time=10000):
                    self.not_found("cancelacalculadoraipi")
                self.click()
                
                x=0
                while x<8:
                    if not self.find( "atividadepresumido", matching=0.97, waiting_time=10000):
                        self.not_found("atividadepresumido")
                    self.click_relative(300, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "aliquotaecf", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotaecf")
                self.click_relative(40, 27)
                self.type_keys_with_interval(1,'t1')
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "datadevalidadeipi", matching=0.97, waiting_time=10000):
                    self.not_found("datadevalidadeipi")
                self.click_relative(140, 25)
                if not self.find( "diadatavalidade", matching=0.97, waiting_time=10000):
                    self.not_found("diadatavalidade")
                self.click_relative(97, 74)
                
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixandotelasituacao1", matching=0.97, waiting_time=10000):
                    self.not_found("abaixandotelasituacao1")
                self.click()
                x=0
                while x<11:
                    if not self.find( "abaixandotelasituacao2", matching=0.97, waiting_time=10000):
                        self.not_found("abaixandotelasituacao2")
                    self.click()
                    x=x+1
                
                                ####---AJUSTE SPED ICMS C197---####
                                
                if not self.find( "codigo", matching=0.97, waiting_time=10000):
                    self.not_found("codigo")
                self.click_relative(22, 28)
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "descricaoajuste", matching=0.97, waiting_time=10000):
                    self.not_found("descricaoajuste")
                self.click_relative(188, 44)
                self.type_keys_with_interval(1,'te12!@')    
                
                                ####---PIS, COFINS, ISS---####
                self.wait(1000)       
                if not self.find( "aba2piscofinsiss", matching=0.97, waiting_time=10000):
                    self.not_found("aba2piscofinsiss")
                self.click()
                if not self.find( "pisbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("pisbasecalculo")
                self.click_relative(145, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "pisaliquota", matching=0.97, waiting_time=10000):
                    self.not_found("pisaliquota")
                self.click_relative(304, 47)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<5:
                    if not self.find( "tipopis", matching=0.97, waiting_time=10000):
                        self.not_found("tipopis")
                    self.click_relative(625, 47)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                if not self.find( "pisvalordeunidade", matching=0.97, waiting_time=10000):
                    self.not_found("pisvalordeunidade")
                self.click_relative(786, 46)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<33:
                    if not self.find( "pissituacaotributaria", matching=0.97, waiting_time=10000):
                        self.not_found("pissituacaotributaria")
                    self.click_relative(1101, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "pisrateiocreditocomuns", matching=0.97, waiting_time=10000):
                        self.not_found("pisrateiocreditocomuns")
                    self.click_relative(304, 94)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                #if not bot.find( "fatu_cad_situacoes_descontar_valor_icms", matching=0.97, waiting_time=10000):
                #    not_found("fatu_cad_situacoes_descontar_valor_icms")
                #bot.click()
                #if not bot.find( "fatu_cad_situacoes_descontar_valor_icms_marcado", matching=0.97, waiting_time=10000):
                #    not_found("fatu_cad_situacoes_descontar_valor_icms_marcado")
                #bot.click()
                #self.wait(500)
                #self.enter()
                #self.space()
                    
                                ####---COFINS---####
                                
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(145, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(304, 47)
                self.type_keys_with_interval(1,'123')
                x=0
                while x<5:
                    if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                    self.click_relative(625, 47)
                    self.type_up()
                    self.enter()
                    x=x+1
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                self.click_relative(786, 46)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<33:
                    if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                    self.click_relative(1101, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
            
                x=0
                while x<19:
                    if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                    self.click_relative(304, 94)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---ISS---####
                                
                if not self.find( "issbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("issbasecalculo")
                self.click_relative(145, 48)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'t1!')
                
                x=0
                while x<8:
                    if not self.find( "issexigiblidade", matching=0.97, waiting_time=10000):
                        self.not_found("issexigiblidade")
                    self.click_relative(787, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---OUTROS IMPOSTOS---####
                                
                if not self.find( "outrosimpostossuframa", matching=0.97, waiting_time=10000):
                    self.not_found("outrosimpostossuframa")
                self.click_relative(145, 46)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                                
                                ####---RETENCOES---####
                                
                if not self.find( "retencoesaliquotairrf", matching=0.97, waiting_time=10000):
                    self.not_found("retencoesaliquotairrf")
                self.click_relative(144, 49)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                                
                                ####---DECRETOS E OBSERVACOES---####
                                
                if not self.find( "decretoseobservacoesemsituacao", matching=0.97, waiting_time=10000):
                    self.not_found("decretoseobservacoesemsituacao")
                self.click()
                if not self.find( "decretonf1", matching=0.97, waiting_time=10000):
                    self.not_found("decretonf1")
                self.click_relative(43, 28)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                if not self.find( "decretonf2", matching=0.97, waiting_time=10000):
                    self.not_found("decretonf2")
                self.click_relative(43, 25)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                
                if not self.find( "observacaonf1", matching=0.97, waiting_time=10000):
                    self.not_found("observacaonf1")
                self.click_relative(43, 26)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                if not self.find( "observacaonf2", matching=0.97, waiting_time=10000):
                    self.not_found("observacaonf2")
                self.click_relative(44, 29)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                
                if not self.find( "cfopsituacao1", matching=0.97, waiting_time=10000):
                    self.not_found("cfopsituacao1")
                self.click_relative(58, 25)
                self.backspace()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                if not self.find( "buscarcfop", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcfop")
                self.click_relative(59, 30)
                self.type_keys_with_interval(1,'5.101')
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                
                if not self.find( "observacaocfop", matching=0.97, waiting_time=10000):
                    self.not_found("observacaocfop")
                self.click_relative(24, 50)
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---GNRE---####
                                
                if not self.find( "gnresituacao", matching=0.97, waiting_time=10000):
                    self.not_found("gnresituacao")
                self.click()
                if not self.find( "incluirnovoregistrognresituacao", matching=0.97, waiting_time=10000):
                    self.not_found("incluirnovoregistrognresituacao")
                self.click()
                # Searching for element 'cancelarAlternativoTelappequenaGNRE '
                if not bot.find("cancelarAlternativoTelappequenaGNRE", matching=0.97, waiting_time=10000):
                    not_found("cancelarAlternativoTelappequenaGNRE")
                bot.click_relative(21, -36)
                if not self.find( "cancelargnre", matching=0.97, waiting_time=10000):
                    self.not_found("cancelargnre")
                self.click()
                
                self.wait(1500)
                                ####---FINALIZACAO SITUACAO---### 
                                #                               
                # if not self.find( "salvarsituacao", matching=0.97, waiting_time=10000):
                #     self.not_found("salvarsituacao")
                # self.click()
                # if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                #     not_found("fatu_cad_param_receituario_retornar")
                # bot.click()
                # Searching for element 'Localizar '
                # Searching for element 'calcelartelaPequenaGNRE '
                # if not bot.find("calcelartelaPequenaGNRE", matching=0.97, waiting_time=10000):
                #     not_found("calcelartelaPequenaGNRE")
                # bot.click_relative(84, 10)
                # Searching for element 'btn_nao'
                # Searching for element 'cancelarTelaGNREinclusaoreceita '
                if not bot.find("cancelarTelaGNREinclusaoreceita", matching=0.97, waiting_time=10000):
                    not_found("cancelarTelaGNREinclusaoreceita")
                bot.click_relative(86, 11)

                # if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                #     not_found("btn_nao")
                # bot.click()

                # Searching for element 'SubABA-ICMS-IPI '
                if not bot.find("SubABA-ICMS-IPI", matching=0.97, waiting_time=10000):
                    not_found("SubABA-ICMS-IPI")
                bot.click()

                # Searching for element 'selectCampSituacaoTributariab '
                if not bot.find("selectCampSituacaoTributariab", matching=0.97, waiting_time=10000):
                    not_found("selectCampSituacaoTributariab")
                bot.click_relative(950, 112)
                self.type_down()
                self.enter()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 72)
                                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                ##################################
                #### Cadastro Plano de Custo e Finandeiro ######
                ###########################

                # Searching for element 'Cadastro '
                if not bot.find("Cadastro", matching=0.97, waiting_time=10000):
                    not_found("Cadastro")
                bot.click_relative(-93, -20)              

                # self.wait(1500)

                # Searching for element 'CAD_PlanoDeCustosEFinanceiro '
                if not bot.find("CAD_PlanoDeCustosEFinanceiro", matching=0.97, waiting_time=10000):
                    not_found("CAD_PlanoDeCustosEFinanceiro")
                bot.click()

                # Searching for element 'subMenuCADPlanoDeCustos '
                if not bot.find("subMenuCADPlanoDeCustos", matching=0.97, waiting_time=10000):
                    not_found("subMenuCADPlanoDeCustos")
                bot.click()

                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()

                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                # Searching for element 'GerarIDCadCodPlanoDeCustos '
                if not bot.find("GerarIDCadCodPlanoDeCustos", matching=0.97, waiting_time=10000):
                    not_found("GerarIDCadCodPlanoDeCustos")
                bot.click()
                
                self.type_keys_with_interval(50,'teste12@')
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                self.space()
                self.wait(1000)
                self.space()
                self.tab()
                self.type_keys_with_interval(50,'Teste Descritivo 12 @')   

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                self.type_keys_with_interval(50,'teste')  
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                # Searching for element 'Cadastro '
                if not bot.find("Cadastro", matching=0.97, waiting_time=10000):
                    not_found("Cadastro")
                bot.click_relative(-93, -20)          

                self.wait(1500)

                # Searching for element 'CAD_PlanoDeCustosEFinanceiro '
                if not bot.find("CAD_PlanoDeCustosEFinanceiro", matching=0.97, waiting_time=10000):
                    not_found("CAD_PlanoDeCustosEFinanceiro")
                bot.click()

                # Searching for element 'subMenuCADPlanoFinanceiro '
                if not bot.find("subMenuCADPlanoFinanceiro", matching=0.97, waiting_time=10000):
                    not_found("subMenuCADPlanoFinanceiro")
                bot.click()

                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()

                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()

                # Searching for element 'GerarIDCadCodPlanoDeCustos '
                if not bot.find("GerarIDCadCodPlanoDeCustos", matching=0.97, waiting_time=10000):
                    not_found("GerarIDCadCodPlanoDeCustos")
                bot.click()
                
                self.type_keys_with_interval(50,'teste12@')
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                self.space()
                self.wait(1000)
                self.space()
                self.tab()
                self.type_keys_with_interval(50,'Teste Descritivo 12 @')   

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                self.type_keys_with_interval(50,'teste')  
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                self.wait(1000)
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                #####################################
                ## CADASTRO DE CONTRATOS ####
                ## Menu Cadastros -> Contratos ###
                ####################################

                # Searching for element 'Cadastro '
                if not bot.find("Cadastro", matching=0.97, waiting_time=10000):
                    not_found("Cadastro")
                bot.click_relative(-93, -20)

                # Searching for element 'MenuCADContratos '
                if not bot.find("MenuCADContratos", matching=0.97, waiting_time=10000):
                    not_found("MenuCADContratos")
                bot.click()
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(800)

                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()
                self.wait(800)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                self.wait(800)

                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(800)

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()
                self.wait(800)
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.wait(800)

                self.tab()
                self.tab()
                self.tab()

                x = 0
                while x <= 7:
                    self.type_right()
                    self.wait(700)
                    self.type_right()
                    self.wait(700)
                    self.type_right()
                    self.wait(700)
                    self.type_right()
                    self.wait(700)
                    self.type_right()
                    self.wait(700)
                    self.type_right()
                    self.wait(700)
                    x = x + 1
                    self.tab()
                self.tab()    
                self.type_keys_with_interval(50, "12")
                self.tab()

                # Searching for element 'clickLPRemetentetelaCADContratos '
                if not bot.find("clickLPRemetentetelaCADContratos", matching=0.97, waiting_time=10000):
                    not_found("clickLPRemetentetelaCADContratos")
                bot.click_relative(62, 24)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'clickLPtelaCADContratosCodigoFiscal '
                if not bot.find("clickLPtelaCADContratosCodigoFiscal", matching=0.97, waiting_time=10000):
                    not_found("clickLPtelaCADContratosCodigoFiscal")
                bot.click_relative(48, 24)
                self.backspace()
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(2000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1000)
                # Searching for element 'clickrelativo0destinatarioLupaDestinatario '
                if not bot.find("clickrelativo0destinatarioLupaDestinatario", matching=0.97, waiting_time=10000):
                    not_found("clickrelativo0destinatarioLupaDestinatario")
                bot.click_relative(-277, 262)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'clickLPtelaCADContratosCNDPagamento '
                if not bot.find("clickLPtelaCADContratosCNDPagamento", matching=0.97, waiting_time=10000):
                    not_found("clickLPtelaCADContratosCNDPagamento")
                bot.click_relative(47, 24)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1000)
                # Searching for element 'clickLPtelaCADContratosConsignatario '
                if not bot.find("clickLPtelaCADContratosConsignatario", matching=0.97, waiting_time=10000):
                    not_found("clickLPtelaCADContratosConsignatario")
                bot.click_relative(60, 23)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1000)
                # Searching for element 'clickLPtelaCADContratosSeguradora '
                if not bot.find("clickLPtelaCADContratosSeguradora", matching=0.97, waiting_time=10000):
                    not_found("clickLPtelaCADContratosSeguradora")
                bot.click_relative(49, 21)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1000)
                # Searching for element 'cliclLPTelaCADContratosPagador '
                if not bot.find("cliclLPTelaCADContratosPagador", matching=0.97, waiting_time=10000):
                    not_found("cliclLPTelaCADContratosPagador")
                bot.click_relative(60, 23)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'clickLPCADTelaContratosUNIDADE '
                if not bot.find("clickLPCADTelaContratosUNIDADE", matching=0.97, waiting_time=10000):
                    not_found("clickLPCADTelaContratosUNIDADE")
                bot.click_relative(49, 24)
                self.type_keys_with_interval(50, "kg")
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1000)
                # Searching for element 'clickLPtelaCADContratosGRUPOFiscal '
                if not bot.find("clickLPtelaCADContratosGRUPOFiscal", matching=0.97, waiting_time=10000):
                    not_found("clickLPtelaCADContratosGRUPOFiscal")
                bot.click_relative(62, 25)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()

                self.wait(500)
                ######## SUB MENU TELA CADASTR0 De Contratos (Outras informações) #####
                self.type_keys_with_interval(50, "2")
                x = 0
                while x <= 8:
                    self.type_keys_with_interval(50, "12")
                    self.tab()
                    x = x + 1
                self.type_keys_with_interval(50, "Marca teste12@")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "Especie teste12@")
                self.tab()
                self.type_keys_with_interval(50, "Natureza teste")
                self.tab()
                self.type_keys_with_interval(50, "12")
                # Searching for element 'sltLPsubmenu2rtelaCADContratosMunicipioColeta '
                if not bot.find("sltLPsubmenu2rtelaCADContratosMunicipioColeta", matching=0.97, waiting_time=10000):
                    not_found("sltLPsubmenu2rtelaCADContratosMunicipioColeta")
                bot.click_relative(91, 23)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1200)
                
                # Searching for element 'sltLPsubmenu2rtelaCADContratosMunicipioEntrega '
                if not bot.find("sltLPsubmenu2rtelaCADContratosMunicipioEntrega", matching=0.97, waiting_time=10000):
                    not_found("sltLPsubmenu2rtelaCADContratosMunicipioEntrega")
                bot.click_relative(93, 49)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(500)
                self.tab()
                self.type_left()
                self.type_left()
                self.type_left()
                self.tab()
                self.type_left()
                self.type_left()
                self.type_left()
                # Searching for element 'sltLPsubMenu2telaCADContratosOperacao '
                if not bot.find("sltLPsubMenu2telaCADContratosOperacao", matching=0.97, waiting_time=10000):
                    not_found("sltLPsubMenu2telaCADContratosOperacao")
                bot.click_relative(50, 26)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(500)
                self.type_down()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "teste 12@")
                # Searching for element 'reduzselecyformselect '
                if not bot.find("reduzselecyformselect", matching=0.97, waiting_time=10000):
                    not_found("reduzselecyformselect")
                bot.click()
                self.type_left()
                self.type_left()
                self.wait(500)
                # Searching for element 'clickSubMenucadContratos3inforCTe '
                if not bot.find("clickSubMenucadContratos3inforCTe", matching=0.97, waiting_time=10000):
                    not_found("clickSubMenucadContratos3inforCTe")
                bot.click()

                x = 0 
                while x <= 5:
                    self.type_down()
                    self.wait(500)
                    self.type_down()
                    self.wait(500)
                    self.type_down()
                    self.wait(500)
                    self.type_down()
                    self.wait(500)
                    self.type_down()
                    self.wait(500)
                    self.type_down()
                    self.wait(500)
                    self.tab()
                    x = x + 1
                # self.type_keys_with_interval(50, "12")
                #Searching for element 'lupatransportadorexpedientedacarga '
                if not bot.find("lupatransportadorexpedientedacarga", matching=0.97, waiting_time=10000):
                    not_found("lupatransportadorexpedientedacarga")
                bot.click_relative(60, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'sllptomadordacargatelacadcontrsubmen3 '
                if not bot.find("sllptomadordacargatelacadcontrsubmen3", matching=0.97, waiting_time=10000):
                    not_found("sllptomadordacargatelacadcontrsubmen3")
                bot.click_relative(58, 25)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'sllptelacadconstrsubmenu3transportadorrecebedordaCarga '
                if not bot.find("sllptelacadconstrsubmenu3transportadorrecebedordaCarga", matching=0.97, waiting_time=10000):
                    not_found("sllptelacadconstrsubmenu3transportadorrecebedordaCarga")
                bot.click_relative(63, 23)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'clickboninhanaomarcado '
                if not bot.find("clickboninhanaomarcado", matching=0.97, waiting_time=10000):
                    not_found("clickboninhanaomarcado")
                bot.click()                
                self.type_left()
                self.tab()
                self.type_keys_with_interval(50, "teste 12@")
                self.tab()
                self.type_keys_with_interval(50, "teste 12@")
                self.tab()
                self.type_keys_with_interval(50, "codigo teste")
                # Searching for element 'clickBokinhaSim '
                if not bot.find("clickBokinhaSim", matching=0.97, waiting_time=10000):
                    not_found("clickBokinhaSim")
                bot.click()
                self.type_left()
                # Searching for element 'slcampotelaCADContratossubmenu3Serie '
                if not bot.find("slcampotelaCADContratossubmenu3Serie", matching=0.97, waiting_time=10000):
                    not_found("slcampotelaCADContratossubmenu3Serie")
                bot.click_relative(11, 26)
                self.type_keys_with_interval(50, "12")
                # Searching for element 'contratoativo '
                if not bot.find("contratoativo", matching=0.97, waiting_time=10000):
                    not_found("contratoativo")
                bot.click()
                self.wait(800)
                self.space()

                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 72)                
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                #########################################################
                ### Cadastros -> Clientes Fornecedores e Transportes ####
                #########################################################
               
                # Searching for element 'Cadastro '
                if not bot.find("Cadastro", matching=0.97, waiting_time=10000):
                    not_found("Cadastro")
                bot.click_relative(-93, -20)
                self.wait(900)
                # Searching for element 'menuCadastrosClientesForncedoreseTransportadores '
                if not bot.find("menuCadastrosClientesForncedoreseTransportadores", matching=0.97, waiting_time=10000):
                    not_found("menuCadastrosClientesForncedoreseTransportadores")
                bot.click()
                self.wait(900)
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)

                # Searching for element 'editar '
                if not bot.find("editar", matching=0.97, waiting_time=10000):
                    not_found("editar")
                bot.click()
                self.wait(4000)

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)
                self.wait(2000)

                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)

                # Searching for element 'btn_cadastro_incluir'
                if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro_incluir")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "10479352950")
                self.tab()
                self.type_keys_with_interval(50, "124556163")
                self.tab()
                self.type_keys_with_interval(50, "ssppr")
                self.tab()
                self.type_keys_with_interval(50, "04102018")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "R. Frei Caneca")
                self.tab()
                self.type_keys_with_interval(50, "1713")
                self.tab()
                self.type_keys_with_interval(50, "Teorema")
                self.tab()
                self.type_keys_with_interval(50, "85012000")
                self.tab()
                self.wait(1000)
                # Searching for element 'consultarCEP '
                if not bot.find("consultarCEP", matching=0.97, waiting_time=10000):
                    not_found("consultarCEP")
                bot.click()
                self.wait(1000)
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "teste")
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "4299999999")
                self.tab()
                x = 0
                while x < 8:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "4299999999")
                self.tab()
                x = 0
                while x < 8:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "4299999999")
                self.tab()
                x = 0
                while x < 8:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "4299999999")
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "nome fantasia teste")
                self.tab()
                self.type_keys_with_interval(50, "19021998")
                self.tab()
                self.type_keys_with_interval(50, "Hospital IDF")
                self.tab()
                self.type_down()
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                self.type_keys_with_interval(50, "teste12@")
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "Teste 12!")
                self.tab()
                self.type_keys_with_interval(50, "Teste 12!")
                self.tab()
                self.type_keys_with_interval(50, "76954-000")
                self.tab()
                self.type_keys_with_interval(50, "Teste 12!")
                self.tab()
                self.type_keys_with_interval(50, "Teste 12!")
                self.tab()
                self.type_keys_with_interval(50, "3")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "12@")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                self.type_keys_with_interval(50, "teste Skype!")
                self.tab()
                self.type_keys_with_interval(50, "https://teorema.inf.br/")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 16:
                    self.space()
                    self.space()
                    self.tab()
                    x = x + 1
                self.type_keys_with_interval(50, "2")
                # Searching for element 'lpSubAba2CDCEFPLocaldeCobranca '
                if not bot.find("lpSubAba2CDCEFPLocaldeCobranca", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPLocaldeCobranca")
                bot.click_relative(65, 30)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPRamodeAtividade '
                if not bot.find("lpSubAba2CDCEFPRamodeAtividade", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPRamodeAtividade")
                bot.click_relative(69, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPComissao '
                if not bot.find("lpSubAba2CDCEFPComissao", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPComissao")
                bot.click_relative(74, 32)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPVendedorComprador '
                if not bot.find("lpSubAba2CDCEFPVendedorComprador", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPVendedorComprador")
                bot.click_relative(66, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPPlanoFinanceiro '
                if not bot.find("lpSubAba2CDCEFPPlanoFinanceiro", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPPlanoFinanceiro")
                bot.click_relative(86, 26)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.tab()
                self.tab()
                self.type_down()      
                self.type_down()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPCentrodeCusto '
                if not bot.find("lpSubAba2CDCEFPCentrodeCusto", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPCentrodeCusto")
                bot.click_relative(83, 31)     
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.tab()
                self.tab()
                self.type_down()      
                self.type_down()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000) 
                # Searching for element 'lpSubAba2CDCEFPClassificacao '
                if not bot.find("lpSubAba2CDCEFPClassificacao", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPClassificacao")
                bot.click_relative(67, 31)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPCCContaCorrente '
                if not bot.find("lpSubAba2CDCEFPCCContaCorrente", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPCCContaCorrente")
                bot.click_relative(65, 30)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'#Searchingforelement'lpSubAba2CDCEFPCCCodigoContabilCliente(fixo) '
                if not bot.find("lpSubAba2CDCEFPCCCodigoContabilCliente(fixo)", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPCCCodigoContabilCliente(fixo)")
                bot.click_relative(65, 31)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00067")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPCodigoContabilFornecedor(fixo) '
                if not bot.find("lpSubAba2CDCEFPCodigoContabilFornecedor(fixo)", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPCodigoContabilFornecedor(fixo)")
                bot.click_relative(68, 30)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00067")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPSegmento '
                if not bot.find("lpSubAba2CDCEFPSegmento", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPSegmento")
                bot.click_relative(66, 25)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPLinha '
                if not bot.find("lpSubAba2CDCEFPLinha", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPLinha")
                bot.click_relative(67, 28)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPTabeladePrecos(itens) '
                if not bot.find("lpSubAba2CDCEFPTabeladePrecos(itens)", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPTabeladePrecos(itens)")
                bot.click_relative(69, 31)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00033")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPTabeladePrecos(Servicos) '
                if not bot.find("lpSubAba2CDCEFPTabeladePrecos(Servicos)", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPTabeladePrecos(Servicos)")
                bot.click_relative(68, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00033")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPOperacaoPDVBalcaoetc '
                if not bot.find("lpSubAba2CDCEFPOperacaoPDVBalcaoetc", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPOperacaoPDVBalcaoetc")
                bot.click_relative(67, 29)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPTransportadorsla '
                if not bot.find("lpSubAba2CDCEFPTransportadorsla", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPTransportadorsla")
                bot.click_relative(80, 29)                
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # self.type_keys_with_interval(80, "0002026")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element '#Searchingforelement'lpSubAba2CDCEFPCondicaodePagamento '
                if not bot.find("lpSubAba2CDCEFPCondicaodePagamento", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPCondicaodePagamento")
                bot.click_relative(68, 28)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # self.type_keys_with_interval(80, "0002026")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPOperacaoNFSeOrdemdeEtc '
                if not bot.find("lpSubAba2CDCEFPOperacaoNFSeOrdemdeEtc", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPOperacaoNFSeOrdemdeEtc")
                bot.click_relative(71, 28)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # self.type_keys_with_interval(80, "0002026")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAba2CDCEFPOperacaoNFtracoebarraNFceOrdemETC '
                if not bot.find("lpSubAba2CDCEFPOperacaoNFtracoebarraNFceOrdemETC", matching=0.97, waiting_time=10000):
                    not_found("lpSubAba2CDCEFPOperacaoNFtracoebarraNFceOrdemETC")
                bot.click_relative(64, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                # self.type_keys_with_interval(80, "0002026")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'subSUbabamenuCOntabilizacao(macros) '
                if not bot.find("subSUbabamenuCOntabilizacao(macros)", matching=0.97, waiting_time=10000):
                    not_found("subSUbabamenuCOntabilizacao(macros)")
                bot.click()
                # Searching for element 'macrosCodigoContabilCLIENTESLP '
                if not bot.find("macrosCodigoContabilCLIENTESLP", matching=0.97, waiting_time=10000):
                    not_found("macrosCodigoContabilCLIENTESLP")
                bot.click_relative(62, 29)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00067")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'LPCodigoContabilFORNECEDORESlp '
                if not bot.find("LPCodigoContabilFORNECEDORESlp", matching=0.97, waiting_time=10000):
                    not_found("LPCodigoContabilFORNECEDORESlp")
                bot.click_relative(67, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00067")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'aba5ObsRefLimitedeCredito '
                if not bot.find("aba5ObsRefLimitedeCredito", matching=0.97, waiting_time=10000):
                    not_found("aba5ObsRefLimitedeCredito")
                bot.click()
                # # Searching for element 'subsubabaMenuCodigosContabeis(multi-Empresa) '
                # if not bot.find("subsubabaMenuCodigosContabeis(multi-Empresa)", matching=0.97, waiting_time=10000):
                #     not_found("subsubabaMenuCodigosContabeis(multi-Empresa)")
                # bot.click()
                # self.type_keys_with_interval(50, "00067")                
                     # self.tab()  
                # self.tab()
                # self.type_keys_with_interval(50, "00067")
                # self.tab()
                # Searching for element 'limitedeCreditoclicanocampoabaixo '
                if not bot.find("limitedeCreditoclicanocampoabaixo", matching=0.97, waiting_time=10000):
                    not_found("limitedeCreditoclicanocampoabaixo")
                bot.click_relative(60, 25)
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                # Searching for element 'btn_Salvar_form'
                if not bot.find("btn_Salvar_form", matching=0.97, waiting_time=10000):
                    not_found("btn_Salvar_form")
                bot.click()
                self.enter()
                # Searching for element 'aba2Agrupamentoooo '
                if not bot.find("aba2Agrupamentoooo", matching=0.97, waiting_time=10000):
                    not_found("aba2Agrupamentoooo")
                bot.click()
                # Searching for element 'subabaCodContabeisMultiEmpresa '
                if not bot.find("subabaCodContabeisMultiEmpresa", matching=0.97, waiting_time=10000):
                    not_found("subabaCodContabeisMultiEmpresa")
                bot.click()
                # Searching for element 'lpCodContabilCliente_telasubaba '
                if not bot.find("lpCodContabilCliente_telasubaba", matching=0.97, waiting_time=10000):
                    not_found("lpCodContabilCliente_telasubaba")
                bot.click_relative(60, 31)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00067")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'lpSubAbacodcontabilFornecedor '
                if not bot.find("lpSubAbacodcontabilFornecedor", matching=0.97, waiting_time=10000):
                    not_found("lpSubAbacodcontabilFornecedor")
                bot.click_relative(62, 30)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_localizar")
                bot.click()
                self.wait(5000)
                self.type_keys_with_interval(80, "00067")
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(2000)
                # Searching for element 'botaoverdinhodeSalvarCodCOntabilCliente '
                if not bot.find("botaoverdinhodeSalvarCodCOntabilCliente", matching=0.97, waiting_time=10000):
                    not_found("botaoverdinhodeSalvarCodCOntabilCliente")
                bot.click_relative(-19, 57)
                self.type_keys_with_interval(50, "3") ### esse botao seleciona a aba 3
                self.type_keys_with_interval(50, "Profissao teste QA12!") 
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 6:
                    self.type_down()
                    x = x + 1
                self.tab()
                x = 0
                while x < 4:
                    self.type_keys_with_interval(50, "123")                    
                    self.tab()
                    x = x + 1
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "pai QA12!")
                self.tab()
                self.type_keys_with_interval(50, "mae QA12!")
                self.tab()
                self.type_keys_with_interval(50, "QA Junior 12!")
                self.tab()
                self.type_keys_with_interval(50, "123")  
                self.tab()
                self.type_keys_with_interval(50, "104.793.529-50")
                self.tab()
                x = 0
                while x < 6:
                    self.type_keys_with_interval(50, "42999999999")                    
                    self.tab()
                    x = x + 1
                x = 0
                while x < 7:
                    self.type_down()                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "124")
                self.tab()
                self.type_keys_with_interval(50, "4")
                self.type_keys_with_interval(50, "00003")
                self.tab()
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()                
                    x = x + 1
                self.tab()
                x = 0
                while x < 7:
                    self.space()               
                    self.space() 
                    self.space() 
                    self.tab()              
                    x = x + 1
                x = 0
                while x < 7:
                    self.type_keys_with_interval(50, "123")              
                    self.tab()              
                    x = x + 1
                x = 0
                while x < 7:
                    self.type_down()                     
                    x = x + 1
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()                     
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()                     
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "02.383.417/0001-06")
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()                     
                    x = x + 1
                ##
                ##
                ## os 3 campos não insere dados, não é erro
                ##
                ##
                ##
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()                     
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                # Searching for element 'aba5ObsRefLimitedeCredito '
                if not bot.find("aba5ObsRefLimitedeCredito", matching=0.97, waiting_time=10000):
                    not_found("aba5ObsRefLimitedeCredito")
                bot.click()
                # Searching for element 'seleciona01-limiteultrapassado '
                if not bot.find("seleciona01-limiteultrapassado", matching=0.97, waiting_time=10000):
                    not_found("seleciona01-limiteultrapassado")
                bot.click()
                x = 0
                while x < 7:
                    self.type_right()
                    self.wait(800)                     
                    x = x + 1
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x = 0
                while x < 5:
                    self.space()                    
                    self.space()  
                    self.tab()                  
                    x = x + 1
                x = 0
                while x < 3:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")

                ##### Aqui vai para sub aba Observações

                # Searching for element 'subABAObservacoes_ '
                if not bot.find("subABAObservacoes_", matching=0.97, waiting_time=10000):
                    not_found("subABAObservacoes_")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")

                ### Aqui vai para sub aba referencias
                # Searching for element 'subABAReferencias_ '
                if not bot.find("subABAReferencias_", matching=0.97, waiting_time=10000):
                    not_found("subABAReferencias_")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")

                ### Aqui vai para sub aba Bens, Contatos e Avalistas
                # Searching for element 'subABA_Bens,contatoseAvalistas_ '
                if not bot.find("subABA_Bens,contatoseAvalistas_", matching=0.97, waiting_time=10000):
                    not_found("subABA_Bens,contatoseAvalistas_")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'ABA_6Relacionamentos_ '
                if not bot.find("ABA_6Relacionamentos_", matching=0.97, waiting_time=10000):
                    not_found("ABA_6Relacionamentos_")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'botaoSalvarVerdePequenoCantoEsquerdo '
                if not bot.find("botaoSalvarVerdePequenoCantoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("botaoSalvarVerdePequenoCantoEsquerdo")
                bot.click_relative(9, -11)
                self.wait(700)
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()   

                #### aba representantes
                # Searching for element 'subSUbabaRepresentantes_ '
                if not bot.find("subSUbabaRepresentantes_", matching=0.97, waiting_time=10000):
                    not_found("subSUbabaRepresentantes_")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                self.type_keys_with_interval(50, "Nome teste qa12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "10479352950")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "0043")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "34990-000")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 6:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 6:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                self.type_keys_with_interval(50, "https://teorema.inf.br/")
                # Searching for element 'botaoSalvarVerdePequenoCantoEsquerdo '
                if not bot.find("botaoSalvarVerdePequenoCantoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("botaoSalvarVerdePequenoCantoEsquerdo")
                bot.click_relative(9, -11)
                self.wait(700)
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()

                ### subSub menu Local de Entrega

                # Searching for element 'subSubMenu_LocaldeEntrega_ '
                if not bot.find("subSubMenu_LocaldeEntrega_", matching=0.97, waiting_time=10000):
                    not_found("subSubMenu_LocaldeEntrega_")
                bot.click()

                # Searching for element 'incluirSmall '
                if not bot.find("incluirSmall", matching=0.97, waiting_time=10000):
                    not_found("incluirSmall")
                bot.click()

                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()

                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "564.732.579-34")
                self.tab()
                self.type_keys_with_interval(50, "12121212")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "0008")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "85012-000")
                self.tab()
                # Searching for element 'PesquisarMunicipioCEP '
                if not bot.find("PesquisarMunicipioCEP", matching=0.97, waiting_time=10000):
                    not_found("PesquisarMunicipioCEP")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_right()
                self.type_right()
                self.tab()
                self.tab()
                self.tab()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "124")
                self.wait(900)

                # Searching for element 'botaoSalvarVerdePequnocantoesquerdo2 '
                if not bot.find("botaoSalvarVerdePequnocantoesquerdo2", matching=0.97, waiting_time=10000):
                    not_found("botaoSalvarVerdePequnocantoesquerdo2")
                bot.click_relative(-100, 224)
                self.wait(700)
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()

                ## Adicionar Local de entrega

                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # Searching for element 'btn_Xnao'
                if not bot.find("btn_Xnao", matching=0.97, waiting_time=10000):
                    not_found("btn_Xnao")
                bot.click()

                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "564.732.579-34")
                self.tab()
                self.type_keys_with_interval(50, "12121212")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "0008")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "85012-000")
                self.tab()
                # Searching for element 'PesquisarMunicipioCEP '
                if not bot.find("PesquisarMunicipioCEP", matching=0.97, waiting_time=10000):
                    not_found("PesquisarMunicipioCEP")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_right()
                self.type_right()
                self.tab()
                self.tab()
                self.tab()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "124")
                self.wait(900)
                # Searching for element 'botaoSalvarVerdePequnocantoesquerdo2 '
                if not bot.find("botaoSalvarVerdePequnocantoesquerdo2", matching=0.97, waiting_time=10000):
                    not_found("botaoSalvarVerdePequnocantoesquerdo2")
                bot.click_relative(-100, 224)
                self.wait(700)
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()

                ### Pessoas contatos

                # Searching for element '_subsubmenuPessoas(Contatos) '
                if not bot.find("_subsubmenuPessoas(Contatos)", matching=0.97, waiting_time=10000):
                    not_found("_subsubmenuPessoas(Contatos)")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # # Searching for element 'btn_Xnao'
                # if not bot.find("btn_Xnao", matching=0.97, waiting_time=10000):
                #     not_found("btn_Xnao")
                # bot.click()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "564.732.579-34")
                self.tab()
                self.type_keys_with_interval(50, "12121212")
                self.tab()

                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "85012-000")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "0008")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "42999999999")
                self.tab()
                x = 0
                while x < 4:
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "teste@teste.com")
                self.tab()
                self.space()
                x = 0
                while x < 9:
                    self.space()
                    self.space()
                    self.type_down() 
                    self.wait(800)                                
                    x = x + 1
                self.tab()
                self.type_keys_with_interval(50, "Observacoes qa12!")
                self.wait(900)
                # Searching for element 'botaoSalvarVerdePequnocantoesquerdo2 '
                if not bot.find("botaoSalvarVerdePequnocantoesquerdo2", matching=0.97, waiting_time=10000):
                    not_found("botaoSalvarVerdePequnocantoesquerdo2")
                bot.click_relative(-100, 224)
                self.wait(700)
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()

                #### Avaliacoes
                ### não tem avaliacoes na aba avaliacoes para cadastrar

                # Searching for element '_subSubmenu_Avaliacoes '
                if not bot.find("_subSubmenu_Avaliacoes", matching=0.97, waiting_time=10000):
                    not_found("_subSubmenu_Avaliacoes")
                bot.click()

                #### Vendedor Auxiliares

                # Searching for element '_subSubmenuVendedorAuxiliares '
                if not bot.find("_subSubmenuVendedorAuxiliares", matching=0.97, waiting_time=10000):
                    not_found("_subSubmenuVendedorAuxiliares")
                bot.click()

                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # Searching for element 'selecionaCaixinha '
                if not bot.find("selecionaCaixinha", matching=0.97, waiting_time=10000):
                    not_found("selecionaCaixinha")
                bot.click_relative(26, 41)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()

                #### Documentos
                # Searching for element '_subSubMenuDocumentos '
                if not bot.find("_subSubMenuDocumentos", matching=0.97, waiting_time=10000):
                    not_found("_subSubMenuDocumentos")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # Searching for element 'selecionaPastaDocumentos '
                if not bot.find("selecionaPastaDocumentos", matching=0.97, waiting_time=10000):
                    not_found("selecionaPastaDocumentos")
                bot.click()
                # Searching for element 'CancelarbotaoCaixaselecionaDoc '
                if not bot.find("CancelarbotaoCaixaselecionaDoc", matching=0.97, waiting_time=10000):
                    not_found("CancelarbotaoCaixaselecionaDoc")
                bot.click()
                # Searching for element 'CancelarXvermelhopequeno '
                if not bot.find("CancelarXvermelhopequeno", matching=0.97, waiting_time=10000):
                    not_found("CancelarXvermelhopequeno")
                bot.click()
                # Searching for element 'retornarBotaoAlternativoTelaCadDocumentosdoSubMenuSuMenuDocumentos '
                if not bot.find("retornarBotaoAlternativoTelaCadDocumentosdoSubMenuSuMenuDocumentos", matching=0.97, waiting_time=10000):
                    not_found("retornarBotaoAlternativoTelaCadDocumentosdoSubMenuSuMenuDocumentos")
                bot.click_relative(29, -27)

                #### Contratos

                # Searching for element '_SubsubMenuContratos '
                if not bot.find("_SubsubMenuContratos", matching=0.97, waiting_time=10000):
                    not_found("_SubsubMenuContratos")
                bot.click()
                
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                ### este clique abaixo em nao vai depender se o cliente possui contrato ou nao, em regra marca como não
                # Searching for element 'btn_Xnao'
                if not bot.find("btn_Xnao", matching=0.97, waiting_time=10000):
                    not_found("btn_Xnao")
                bot.click()

                # Searching for element 'subAbaMenuclientesVinculados '
                if not bot.find("subAbaMenuclientesVinculados", matching=0.97, waiting_time=10000):
                    not_found("subAbaMenuclientesVinculados")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                ### este clique abaixo em nao vai depender se o cliente possui contrato ou nao, em regra marca como não
                # # Searching for element 'btn_Xnao'
                # if not bot.find("btn_Xnao", matching=0.97, waiting_time=10000):
                #     not_found("btn_Xnao")
                # bot.click()
                # Searching for element 'lpLocalizarVendedorVinculado '
                if not bot.find("lpLocalizarVendedorVinculado", matching=0.97, waiting_time=10000):
                    not_found("lpLocalizarVendedorVinculado")
                bot.click_relative(83, 211)
                # # Searching for element 'lpSelecionaLupoaVendedoresVinculados '
                # if not bot.find("lpSelecionaLupoaVendedoresVinculados", matching=0.97, waiting_time=10000):
                #     not_found("lpSelecionaLupoaVendedoresVinculados")
                # bot.click()
                self.wait(4000)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(100, 'qa12!')
                # Searching for element 'botaoSalvarVerdePequnocantoesquerdo2 '
                if not bot.find("botaoSalvarVerdePequnocantoesquerdo2", matching=0.97, waiting_time=10000):
                    not_found("botaoSalvarVerdePequnocantoesquerdo2")
                bot.click_relative(-100, 224)
                self.wait(700)
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                #por enquanto nao ta aparecendo o botao sim pq nao salvou registro completo, nao tem registro para salvar
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()
                # Searching for element 'bntMenuSubCategoriasCampanha '
                if not bot.find("bntMenuSubCategoriasCampanha", matching=0.97, waiting_time=10000):
                    not_found("bntMenuSubCategoriasCampanha")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'rateiodecustos '
                if not bot.find("rateiodecustos", matching=0.97, waiting_time=10000):
                    not_found("rateiodecustos")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # Searching for element 'selctLPBotaoLupa2.0 '
                if not bot.find("selctLPBotaoLupa2.0", matching=0.97, waiting_time=10000):
                    not_found("selctLPBotaoLupa2.0")
                bot.click_relative(204, 46)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(4000)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # print('O codigo veio ate aqui')
                # Searching for element 'btn_SalvarCadastroSocio'
                if not bot.find("btn_SalvarCadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("btn_SalvarCadastroSocio")
                bot.click()
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()
                # Searching for element 'SUB_ABA_RElacionamentos-Equipamentos '
                if not bot.find("SUB_ABA_RElacionamentos-Equipamentos", matching=0.97, waiting_time=10000):
                    not_found("SUB_ABA_RElacionamentos-Equipamentos")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "Descrição qa12!")  
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                x = 0
                while x < 6:
                    self.type_down()
                    x = x + 1
                # Searching for element 'btn_SalvarCadastroSocio'
                if not bot.find("btn_SalvarCadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("btn_SalvarCadastroSocio")
                bot.click()
                # Searching for element 'excluirLixeiraPequenaLadoEsquerdo '
                if not bot.find("excluirLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("excluirLixeiraPequenaLadoEsquerdo")
                bot.click_relative(-102, 201)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()
                # Searching for element 'CeCDFeT_ABA_RelacionamentosSubMenuRedesSociais '
                if not bot.find("CeCDFeT_ABA_RelacionamentosSubMenuRedesSociais", matching=0.97, waiting_time=10000):
                    not_found("CeCDFeT_ABA_RelacionamentosSubMenuRedesSociais")
                bot.click()
                self.wait(1000)
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                self.type_keys_with_interval(50, "https://www.linkedin.com/company/teorema-sistemas/")
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'btn_SalvarCadastroSocio'
                if not bot.find("btn_SalvarCadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("btn_SalvarCadastroSocio")
                bot.click()

                # Searching for element 'btnEditarPequenoLadoEsquerdoabaixo+verde '
                if not bot.find("btnEditarPequenoLadoEsquerdoabaixo+verde", matching=0.97, waiting_time=10000):
                    not_found("btnEditarPequenoLadoEsquerdoabaixo+verde")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "qa123!@")
                # Searching for element 'btn_SalvarCadastroSocio'
                if not bot.find("btn_SalvarCadastroSocio", matching=0.97, waiting_time=10000):
                    not_found("btn_SalvarCadastroSocio")
                bot.click()
                self.wait(1000)
                # Searching for element 'novaLixeiraPequenaLadoEsquerdo '
                if not bot.find("novaLixeiraPequenaLadoEsquerdo", matching=0.97, waiting_time=10000):
                    not_found("novaLixeiraPequenaLadoEsquerdo")
                bot.click()
                self.wait(1000)
                self.enter()
                self.wait(1000)

                # Searching for element 'CaddeClientesFornecETransporMenu_Historicos '
                if not bot.find("CaddeClientesFornecETransporMenu_Historicos", matching=0.97, waiting_time=10000):
                    not_found("CaddeClientesFornecETransporMenu_Historicos")
                bot.click()
                self.wait(4000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 72)
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 68)

                #################################################################
                ######### FIM CADASTRO Clientes, Fornecedores e Transportes #####
                #################################################################

                #################################################################
                ######### Cadastro -> Veiculos -> etc ###########################
                #################################################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Veiculos '
                if not bot.find("Cad_Veiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos")
                bot.click()
                # Searching for element 'Cad_Veiculos_ModelosdeVeiculos '
                if not bot.find("Cad_Veiculos_ModelosdeVeiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos_ModelosdeVeiculos")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ### cadastro -> veiculos -> grupo de veiculos

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Veiculos '
                if not bot.find("Cad_Veiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos")
                bot.click()
                # Searching for element 'cad_veiculos_grupodeveiculosCAD '
                if not bot.find("cad_veiculos_grupodeveiculosCAD", matching=0.97, waiting_time=10000):
                    not_found("cad_veiculos_grupodeveiculosCAD")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ### cadastro -> veiculos -> tipos de veiculos

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Veiculos '
                if not bot.find("Cad_Veiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos")
                bot.click()
                # Searching for element 'Cad_Veiculos_TiposDeVeiculos '
                if not bot.find("Cad_Veiculos_TiposDeVeiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos_TiposDeVeiculos")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(1000)
                self.type_keys_with_interval(150, "qa12!")
                self.tab()
                x=0
                while x < 7:
                    self.type_keys_with_interval(50, "12")
                    self.tab()
                    x = x + 1
                x=0
                while x < 20:
                    self.space()
                    self.wait(300)
                    self.space()
                    self.tab()
                    x = x + 1
                self.space()
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                
                #### Cadastro -> Veiculos -> Avaliações

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Veiculos '
                if not bot.find("Cad_Veiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos")
                bot.click()
                # Searching for element 'Cadastro_Veiculos_Avaliacoes '
                if not bot.find("Cadastro_Veiculos_Avaliacoes", matching=0.97, waiting_time=10000):
                    not_found("Cadastro_Veiculos_Avaliacoes")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()

                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                ####
                ###
                ### Não tem a opção de excluir
                ###
                ###
                # # Searching for element 'ExcluirEmpresa '
                # if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                #     not_found("ExcluirEmpresa")
                # bot.click()
                
                # # Searching for element 'sIMV '
                # if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                #     not_found("sIMV")
                # bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ###########
                ##### Cadastro -> Veiculos -> Veiculos
                ###########

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Veiculos '
                if not bot.find("Cad_Veiculos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos")
                bot.click()
                # Searching for element 'Cad_Ve_Veiculos2 '
                if not bot.find("Cad_Ve_Veiculos2", matching=0.97, waiting_time=10000):
                    not_found("Cad_Ve_Veiculos2")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(1000)
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "2025")
                self.tab()
                self.type_keys_with_interval(50, "2025")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "2025")
                self.tab()
                self.type_keys_with_interval(50, "black")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "123456789")
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "2025")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                x=0
                while x < 5:
                    self.type_down()
                    x = x + 1
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()

                self.tab()                
                self.tab()                
                #### sub menu 1

                x=0
                while x < 14:
                    self.type_keys_with_interval(50, "12")
                    self.tab()
                    x = x + 1
                x=0
                while x <= 4:
                    self.type_down()
                    self.type_down()
                    self.type_down()
                    self.type_down()
                    self.type_up()
                    self.tab()
                    x = x + 1
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")

                # Searching for element 'TIPO_Lupa '
                if not bot.find("TIPO_Lupa", matching=0.97, waiting_time=10000):
                    not_found("TIPO_Lupa")
                bot.click_relative(115, 4)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'MODELO_Lupa '
                if not bot.find("MODELO_Lupa", matching=0.97, waiting_time=10000):
                    not_found("MODELO_Lupa")
                bot.click_relative(129, 5)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()

                # Searching for element 'Proprietario2_Lupa '
                if not bot.find("Proprietario2_Lupa", matching=0.97, waiting_time=10000):
                    not_found("Proprietario2_Lupa")
                bot.click_relative(127, 27)

                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'MOTORISTA_Lupa '
                if not bot.find("MOTORISTA_Lupa", matching=0.97, waiting_time=10000):
                    not_found("MOTORISTA_Lupa")
                bot.click_relative(137, 7)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'MUNICIPIO_Lupa '
                if not bot.find("MUNICIPIO_Lupa", matching=0.97, waiting_time=10000):
                    not_found("MUNICIPIO_Lupa")
                bot.click_relative(138, 7)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'PLANOFINANCEIRO_Lupa '
                if not bot.find("PLANOFINANCEIRO_Lupa", matching=0.97, waiting_time=10000):
                    not_found("PLANOFINANCEIRO_Lupa")
                bot.click_relative(175, 5)
                self.type_keys_with_interval(50, "001001001")
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'CENTRODECUSTO_Lupa '
                if not bot.find("CENTRODECUSTO_Lupa", matching=0.97, waiting_time=10000):
                    not_found("CENTRODECUSTO_Lupa")
                bot.click_relative(176, 7)
                self.type_keys_with_interval(50, "001001001")
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'GRUPO_Lupa '
                if not bot.find("GRUPO_Lupa", matching=0.97, waiting_time=10000):
                    not_found("GRUPO_Lupa")
                bot.click_relative(88, 3)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'Classificacao_Lupa '
                if not bot.find("Classificacao_Lupa", matching=0.97, waiting_time=10000):
                    not_found("Classificacao_Lupa")
                bot.click_relative(124, 8)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_right()
                self.type_right()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                # self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                # return
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "Observações teste")
                # Searching for element 'SEGUROVEICULOData '
                if not bot.find("SEGUROVEICULOData", matching=0.97, waiting_time=10000):
                    not_found("SEGUROVEICULOData")
                bot.click_relative(80, 4)
                self.type_keys_with_interval(50, "123")
                self.tab()
                # Searching for element 'VEICULOPLACA1_Lupa '
                if not bot.find("VEICULOPLACA1_Lupa", matching=0.97, waiting_time=10000):
                    not_found("VEICULOPLACA1_Lupa")
                bot.click_relative(102, 47)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'VEICULOPLACA2_Lupa '
                if not bot.find("VEICULOPLACA2_Lupa", matching=0.97, waiting_time=10000):
                    not_found("VEICULOPLACA2_Lupa")
                bot.click_relative(-16, 50)
                self.type_keys_with_interval(50, "000002")
                # Searching for element 'VEICULOPLACA1_Lupa '
                if not bot.find("VEICULOPLACA1_Lupa", matching=0.97, waiting_time=10000):
                    not_found("VEICULOPLACA1_Lupa")
                bot.click_relative(102, 47)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'VEICULOPLACA3_Lupa '
                if not bot.find("VEICULOPLACA3_Lupa", matching=0.97, waiting_time=10000):
                    not_found("VEICULOPLACA3_Lupa")
                bot.click_relative(-19, 53)
                self.type_keys_with_interval(50, "00003")
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()

                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()

                # ### Outra aba antes de         

                ### Cadastro Veiculos->Veiculos Menu 2 Metas ####

                # Searching for element 'CadDeVeiculosVeiculos_2Metas '
                if not bot.find("CadDeVeiculosVeiculos_2Metas", matching=0.97, waiting_time=10000):
                    not_found("CadDeVeiculosVeiculos_2Metas")
                bot.click()
                self.wait(1000)
                # Searching for element 'KM_Janeiro__Relactive '
                if not bot.find("KM_Janeiro__Relactive", matching=0.97, waiting_time=10000):
                    not_found("KM_Janeiro__Relactive")
                bot.click_relative(80, 17)
                self.wait(1000)
                x=0
                while x < 12:
                    self.type_keys_with_interval(50, "12")
                    self.tab()
                    x = x + 1
                self.wait(1000)   
                x=0
                while x < 12:
                    self.type_keys_with_interval(50, "14")
                    self.tab()
                    x = x + 1
                self.wait(500)
                x=0
                while x < 12:
                    self.type_keys_with_interval(50, "22")
                    self.tab()
                    x = x + 1
                
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()

                ### FIM Cadastro Veiculos->Veiculos Menu 2 Metas ####

                #### Cadastro Veiculos->Veiculos Menu 3 Lacres ####

                # Searching for element 'CadVeiculsVeiculos_subMenu_3Lacres '
                if not bot.find("CadVeiculsVeiculos_subMenu_3Lacres", matching=0.97, waiting_time=10000):
                    not_found("CadVeiculsVeiculos_subMenu_3Lacres")
                bot.click()

                # Searching for element 'incluir_Socio'
                if not bot.find("incluir_Socio", matching=0.97, waiting_time=10000):
                    not_found("incluir_Socio")
                bot.click_relative(10, -15)
                self.type_keys_with_interval(50, "123")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                self.wait(500)
                # Searching for element 'Retornar_CadastroDeLacresDeVeiculos '
                if not bot.find("Retornar_CadastroDeLacresDeVeiculos", matching=0.97, waiting_time=10000):
                    not_found("Retornar_CadastroDeLacresDeVeiculos")
                bot.click_relative(12, 38)

                # Searching for element 'Excluir_LixeiraPqquenaLadoEsquerdow '
                if not bot.find("Excluir_LixeiraPqquenaLadoEsquerdow", matching=0.97, waiting_time=10000):
                    not_found("Excluir_LixeiraPqquenaLadoEsquerdow")
                bot.click_relative(8, 32)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()
                self.wait(2000)

                #### FIM Cadastro Veiculos->Veiculos Menu 3 Lacres ####

                #### Cadastro Veiculos->Veiculos Menu 4 Troca Odometro/Horimetro ####
                
                # Searching for element 'Cad_Veiculos_Veiculos_SbMen_4TrocaOdometroHorimetro '
                if not bot.find("Cad_Veiculos_Veiculos_SbMen_4TrocaOdometroHorimetro", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos_Veiculos_SbMen_4TrocaOdometroHorimetro")
                bot.click()

                # Searching for element 'incluir_Socio'
                if not bot.find("incluir_Socio", matching=0.97, waiting_time=10000):
                    not_found("incluir_Socio")
                bot.click_relative(10, -15)
                self.wait(700)
                self.tab()
                self.type_up()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "1234")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "1234")
                self.tab()
                self.type_keys_with_interval(50, "Obs QA 12!")

                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'RetornarTelaCaddeTrocadeOdometro '
                if not bot.find("RetornarTelaCaddeTrocadeOdometro", matching=0.97, waiting_time=10000):
                    not_found("RetornarTelaCaddeTrocadeOdometro")
                bot.click_relative(11, 38)

                self.wait(700)

                #### FIM Cadastro Veiculos->Veiculos Menu 4 Troca Odometro/Horimetro ####

                #### Cadastro Veiculos->Veiculos Menu 5 Pneu ####

                # Searching for element 'CAD_deVeiculos_VeiculosSubMenu_5Pneus '
                if not bot.find("CAD_deVeiculos_VeiculosSubMenu_5Pneus", matching=0.97, waiting_time=10000):
                    not_found("CAD_deVeiculos_VeiculosSubMenu_5Pneus")
                bot.click()

                #### FIM Cadastro Veiculos->Veiculos Menu 5 Pneu ####

                #### Cadastro Veiculos->Veiculos Menu 6 Observações ####

                # Searching for element 'CAD_deVeiculos_VeiculosSubMenu_6_Observacoes '
                if not bot.find("CAD_deVeiculos_VeiculosSubMenu_6_Observacoes", matching=0.97, waiting_time=10000):
                    not_found("CAD_deVeiculos_VeiculosSubMenu_6_Observacoes")
                bot.click()

                # Searching for element 'obsSelcionaCampo '
                if not bot.find("obsSelcionaCampo", matching=0.97, waiting_time=10000):
                    not_found("obsSelcionaCampo")
                bot.click_relative(32, 99)
                self.type_keys_with_interval(50, "Observação teste 12")
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                self.wait(700)

                # #### Fim Cadastro Veiculos->Veiculos Menu 6 Observações ####

                #### Cadastro Veiculos->Veiculos Menu 7 Fotos ####

                # Searching for element 'cad_veiculos_veiculos_subMenu_7Fotos '
                if not bot.find("cad_veiculos_veiculos_subMenu_7Fotos", matching=0.97, waiting_time=10000):
                    not_found("cad_veiculos_veiculos_subMenu_7Fotos")
                bot.click()
                # Searching for element 'incluir_Socio'
                if not bot.find("incluir_Socio", matching=0.97, waiting_time=10000):
                    not_found("incluir_Socio")
                bot.click_relative(10, -15)
                # Searching for element 'pastaxxxx '
                if not bot.find("pastaxxxx", matching=0.97, waiting_time=10000):
                    not_found("pastaxxxx")
                bot.click()
                # Searching for element 'CancelarbotaoCaixaselecionaDoc '
                if not bot.find("CancelarbotaoCaixaselecionaDoc", matching=0.97, waiting_time=10000):
                    not_found("CancelarbotaoCaixaselecionaDoc")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "Obs teste qa 12!")
                # Searching for element 'salvarConfiguracaodoMultiCTE '
                if not bot.find("salvarConfiguracaodoMultiCTE", matching=0.97, waiting_time=10000):
                    not_found("salvarConfiguracaodoMultiCTE")
                bot.click()
                self.wait(500)
                
                # Searching for element 'Excluir_LixeiraPqquenaLadoEsquerdow '
                if not bot.find("Excluir_LixeiraPqquenaLadoEsquerdow", matching=0.97, waiting_time=10000):
                    not_found("Excluir_LixeiraPqquenaLadoEsquerdow")
                bot.click_relative(8, 32)
                self.wait(700)
                # Searching for element 'btn_Vsim'
                if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                    not_found("btn_Vsim")
                bot.click()
                self.wait(1000)

                #### Fim Cadastro Veiculos->Veiculos Menu 7 Fotos ####

                #### Cadastro Veiculos->Veiculos Menu 8 Avaliações ####
                # Searching for element 'Cad_Veiculos_Veiculos_subMenu_8Avaliacoes '
                if not bot.find("Cad_Veiculos_Veiculos_subMenu_8Avaliacoes", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos_Veiculos_subMenu_8Avaliacoes")
                bot.click()
                # Searching for element 'include_relactive_buttonTest '
                if not bot.find("include_relactive_buttonTest", matching=0.97, waiting_time=10000):
                    not_found("include_relactive_buttonTest")
                bot.click_relative(9, -15)


                # # Searching for element 'avalicação_selecionaOCampo '
                # if not bot.find("avalicação_selecionaOCampo", matching=0.97, waiting_time=10000):
                #     not_found("avalicação_selecionaOCampo")
                # bot.click_relative(124, 21)

                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.wait(700)
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.wait(500)

                ###############################################################
                ####### AQUI TEM QUE VER PQ NAO DEIXA SALVAR O CAMPO ##########
                ###############################################################
                #### Para limpar o campo vai e volta o menu 
                # Searching for element 'cad_veiculos_veiculos_subMenu_7Fotos '
                if not bot.find("cad_veiculos_veiculos_subMenu_7Fotos", matching=0.97, waiting_time=10000):
                    not_found("cad_veiculos_veiculos_subMenu_7Fotos")
                bot.click()
                self.wait(500)
                # Searching for element 'Cad_Veiculos_Veiculos_subMenu_8Avaliacoes '
                if not bot.find("Cad_Veiculos_Veiculos_subMenu_8Avaliacoes", matching=0.97, waiting_time=10000):
                    not_found("Cad_Veiculos_Veiculos_subMenu_8Avaliacoes")
                bot.click()

                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()

                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)   
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)             

                # # # Searching for element 'salvarConfiguracaodoMultiCTE '
                # # if not bot.find("salvarConfiguracaodoMultiCTE", matching=0.97, waiting_time=10000):
                # #     not_found("salvarConfiguracaodoMultiCTE")
                # # bot.click()
                # # self.wait(500)
                # 
                # # # Searching for element 'Excluir_LixeiraPqquenaLadoEsquerdow '
                # # if not bot.find("Excluir_LixeiraPqquenaLadoEsquerdow", matching=0.97, waiting_time=10000):
                # #     not_found("Excluir_LixeiraPqquenaLadoEsquerdow")
                # # bot.click_relative(8, 32)
                # # self.wait(700)
                # # # Searching for element 'btn_Vsim'
                # # if not bot.find("btn_Vsim", matching=0.97, waiting_time=10000):
                # #     not_found("btn_Vsim")
                # # bot.click()
                # # self.wait(1000)


                ###################################################
                ######## Fim Cadastro Veiculos ####################
                ###################################################

                ###############################################################
                ########## Cadastros->Itens de Estoque->Cadastro de Unidade ###
                ###############################################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cadastro_ItensDeEstoque '
                if not bot.find("Cadastro_ItensDeEstoque", matching=0.97, waiting_time=10000):
                    not_found("Cadastro_ItensDeEstoque")
                bot.click()
                # Searching for element 'Cadastro_ItensDeEstoque_Unidades '
                if not bot.find("Cadastro_ItensDeEstoque_Unidades", matching=0.97, waiting_time=10000):
                    not_found("Cadastro_ItensDeEstoque_Unidades")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(1000)
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ############
                ##### Cadastro -> itens de estoque -> Itens
                ############

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cadastro_ItensDeEstoque '
                if not bot.find("Cadastro_ItensDeEstoque", matching=0.97, waiting_time=10000):
                    not_found("Cadastro_ItensDeEstoque")
                bot.click()
                
                # Searching for element 'Cad_ItensDeEstoque_Itens '
                if not bot.find("Cad_ItensDeEstoque_Itens", matching=0.97, waiting_time=10000):
                    not_found("Cad_ItensDeEstoque_Itens")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "Desc Item Cad Estoque qa12!")
                # Searching for element 'NCM_LP '
                if not bot.find("NCM_LP", matching=0.97, waiting_time=10000):
                    not_found("NCM_LP")
                bot.click_relative(137, 8)
                self.type_keys_with_interval(50, "1")
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "1")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.wait(500)
                # Searching for element 'Unidade_LP '
                if not bot.find("Unidade_LP", matching=0.97, waiting_time=10000):
                    not_found("Unidade_LP")
                bot.click_relative(90, 10)
                self.type_keys_with_interval(50, "1")
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()
                    x= x + 1
                # Searching for element 'GrupoFiscal_LP '
                if not bot.find("GrupoFiscal_LP", matching=0.97, waiting_time=10000):
                    not_found("GrupoFiscal_LP")
                bot.click_relative(113, 13)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()
                    x= x + 1
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.space()
                self.space()
                self.tab()
                x = 0
                while x < 7:
                    self.type_down()
                    x= x + 1
                # Searching for element 'contaContabil_LP '
                if not bot.find("contaContabil_LP", matching=0.97, waiting_time=10000):
                    not_found("contaContabil_LP")
                bot.click_relative(136, 12)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.backspace()
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                self.wait(500)
                self.enter()

                # Searching for element 'incluirSmall '
                if not bot.find("incluirSmall", matching=0.97, waiting_time=10000):
                    not_found("incluirSmall")
                bot.click()
                # Searching for element 'refAdFornecedor_LP '
                if not bot.find("refAdFornecedor_LP", matching=0.97, waiting_time=10000):
                    not_found("refAdFornecedor_LP")
                bot.click_relative(58, 56)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                # Searching for element 'refAd_Unidade_LP '
                if not bot.find("refAd_Unidade_LP", matching=0.97, waiting_time=10000):
                    not_found("refAd_Unidade_LP")
                bot.click_relative(58, 91)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                # Searching for element 'Gravar '
                if not bot.find("Gravar", matching=0.97, waiting_time=10000):
                    not_found("Gravar")
                bot.click()
                # Searching for element 'click_X '
                if not bot.find("click_X", matching=0.97, waiting_time=10000):
                    not_found("click_X")
                bot.click()
                self.enter()
                self.wait(5500)
                # Searching for element 'Excluir_LixeiraPqquenaLadoEsquerdow '
                if not bot.find("Excluir_LixeiraPqquenaLadoEsquerdow", matching=0.97, waiting_time=10000):
                    not_found("Excluir_LixeiraPqquenaLadoEsquerdow")
                bot.click_relative(8, 32)
                self.wait(700)
                self.enter()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ###############################################################
                ########## FIM Cadastros->Itens de Estoque->Cadastro de Unidade ###
                ###############################################################

                ###############################################################
                ########## Cadastros-> Pneus -> Marca ###
                ###############################################################
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                self.wait(700)
                # Searching for element 'Cad_Pneus_Marcas '
                if not bot.find("Cad_Pneus_Marcas", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus_Marcas")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ##### Cadastro _Pneus -> Modelos

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                self.wait(700)
                # Searching for element 'Cad_Pneus_Modelos '
                if not bot.find("Cad_Pneus_Modelos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus_Modelos")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                
                ###### Cadastro -> Pneus -> Tipo

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                self.wait(700)
                # Searching for element 'Cad_Pneus_Tipo '
                if not bot.find("Cad_Pneus_Tipo", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus_Tipo")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ####### Cadastro -> Pneus -> Tipo de Borracha 

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                self.wait(700)
                # Searching for element 'Cad_Pneus_TipoDeBorracha '
                if not bot.find("Cad_Pneus_TipoDeBorracha", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus_TipoDeBorracha")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ####### Cadastro -> Pneus -> Motivo de Sucateamento

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                self.wait(700)
                # Searching for element 'Cad_Pneus_MotivosDeSucateamento '
                if not bot.find("Cad_Pneus_MotivosDeSucateamento", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus_MotivosDeSucateamento")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ####### Cadastro -> Pneu -> Pneus 
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                self.wait(1500)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                self.wait(700)
                # Searching for element 'Cad_Pneus '
                if not bot.find("Cad_Pneus", matching=0.97, waiting_time=10000):
                    not_found("Cad_Pneus")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")  
                self.tab()
                self.type_keys_with_interval(50, "qa12!") 
                self.tab()
                self.type_keys_with_interval(50, "123")      
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(50, "qa12!") 
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.space()
                self.wait(500)
                self.space()
                self.wait(500)
                # Searching for element 'selelciona_LP_Fornecedor '
                if not bot.find("selelciona_LP_Fornecedor", matching=0.97, waiting_time=10000):
                    not_found("selelciona_LP_Fornecedor")
                bot.click_relative(135, 23)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                # Searching for element 'sl_LUPA_MARCAaaa '
                if not bot.find("sl_LUPA_MARCAaaa", matching=0.97, waiting_time=10000):
                    not_found("sl_LUPA_MARCAaaa")
                bot.click_relative(86, 7)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'sl_LUPA_MODELOooo '
                if not bot.find("sl_LUPA_MODELOooo", matching=0.97, waiting_time=10000):
                    not_found("sl_LUPA_MODELOooo")
                bot.click_relative(89, 5)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'sl_LUPA_TIPOoooo '
                if not bot.find("sl_LUPA_TIPOoooo", matching=0.97, waiting_time=10000):
                    not_found("sl_LUPA_TIPOoooo")
                bot.click_relative(75, 8)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'sl_LUPA_BORRACHAaaa '
                if not bot.find("sl_LUPA_BORRACHAaaa", matching=0.97, waiting_time=10000):
                    not_found("sl_LUPA_BORRACHAaaa")
                bot.click_relative(97, 9)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ###############################################################
                ########## FIM -> Cadastros-> Pneus ###
                ###############################################################

                ###############################################################
                ########## Cadastros-> Eventos ->  ###
                ###############################################################
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'Cad_Eventos '
                if not bot.find("Cad_Eventos", matching=0.97, waiting_time=10000):
                    not_found("Cad_Eventos")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.wait(700)
                # Searching for element 'AcertodeViagens '
                if not bot.find("AcertodeViagens", matching=0.97, waiting_time=10000):
                    not_found("AcertodeViagens")
                bot.click()                
                # Searching for element 'oVeiculo '
                if not bot.find("oVeiculo", matching=0.97, waiting_time=10000):
                    not_found("oVeiculo")
                bot.click()
                self.type_right()
                self.type_right()
                # Searching for element 'Debito '
                if not bot.find("Debito", matching=0.97, waiting_time=10000):
                    not_found("Debito")
                bot.click()
                self.type_right()
                self.type_right()
                self.type_right()
                # Searching for element 'Preventiva '
                if not bot.find("Preventiva", matching=0.97, waiting_time=10000):
                    not_found("Preventiva")
                bot.click()
                # Searching for element 'Mecanica '
                if not bot.find("Mecanica", matching=0.97, waiting_time=10000):
                    not_found("Mecanica")
                bot.click()
                self.type_right()
                self.type_right()
                self.tab()
                self.type_right()
                self.type_right()
                # Searching for element 'oNenhum '
                if not bot.find("oNenhum", matching=0.97, waiting_time=10000):
                    not_found("oNenhum")
                bot.click()
                self.type_right()
                self.type_right()
                self.type_right()
                self.type_right()
                # Searching for element 'oCorretiva '
                if not bot.find("oCorretiva", matching=0.97, waiting_time=10000):
                    not_found("oCorretiva")
                bot.click()
                self.wait(700)
                # Searching for element 'o.Ativo '
                if not bot.find("o.Ativo", matching=0.97, waiting_time=10000):
                    not_found("o.Ativo")
                bot.click()
                self.type_right()
                self.type_right()
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                ##############################################################
                ######### FIM -> Cadastros-> Eventos  ###
                ##############################################################

                ##############################################################
                ######### Cadastros-> Seguradoras ###
                ##############################################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'Cad_Seguradoras '
                if not bot.find("Cad_Seguradoras", matching=0.97, waiting_time=10000):
                    not_found("Cad_Seguradoras")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.wait(700)
                self.tab()
                self.type_keys_with_interval(50, "02.383.417/0001-06")
                self.tab()
                self.type_down()
                self.wait(500)
                self.type_up()
                self.tab()
                self.type_keys_with_interval(50, "R. Frei Caneca")
                self.tab()
                self.type_keys_with_interval(50, "teste@email.com")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'Seleciona_Lupacomsetaverdeparadireita '
                if not bot.find("Seleciona_Lupa com seta verde para direita", matching=0.97, waiting_time=10000):
                    not_found("Seleciona_Lupa com seta verde para direita")
                bot.click()
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'Seleciona_opcao_Averbadora '
                if not bot.find("Seleciona_opcao_Averbadora", matching=0.97, waiting_time=10000):
                    not_found("Seleciona_opcao_Averbadora")
                bot.click_relative(154, 11)
                self.type_down()
                self.type_down()
                self.enter()
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ###############################################################
                ########## FIM -> Cadastros-> Seguradoras ###
                ###############################################################

                ###############################################################
                ########## Cadastros-> Cadastro -> Percentuais seguradoras ####
                ###############################################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'Cad_PercentuaisSeguradoras '
                if not bot.find("Cad_PercentuaisSeguradoras", matching=0.97, waiting_time=10000):
                    not_found("Cad_PercentuaisSeguradoras")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                # Searching for element 'Sl_LUPA_EstadoOrigem '
                if not bot.find("Sl_LUPA_EstadoOrigem", matching=0.97, waiting_time=10000):
                    not_found("Sl_LUPA_EstadoOrigem")
                bot.click_relative(126, 7)
                self.wait(700)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'Sl_LUPA_EstadoDestino '
                if not bot.find("Sl_LUPA_EstadoDestino", matching=0.97, waiting_time=10000):
                    not_found("Sl_LUPA_EstadoDestino")
                bot.click_relative(130, 6)
                self.wait(700)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.enter()
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                # ###############################################################
                # ########## FIM -> Cadastros -> Percentuais seguradoras ####
                # ###############################################################

                # ###############################################################
                # ########## Cadastros -> Tabelas de impostos ####
                # ###############################################################
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'Cad_TabelasdeImpostos '
                if not bot.find("Cad_TabelasdeImpostos", matching=0.97, waiting_time=10000):
                    not_found("Cad_TabelasdeImpostos")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(1000)
                self.tab()
                self.tab()
                self.tab()
                x=0
                while x < 72:
                    self.type_keys_with_interval(50, "12")
                    self.tab()
                    x = x + 1
                self.space()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                # Searching for element 'TabelaImpostos_menu_DSRExposicaoaAgentesNocivos '
                if not bot.find("TabelaImpostos_menu_DSRExposicaoaAgentesNocivos", matching=0.97, waiting_time=10000):
                    not_found("TabelaImpostos_menu_DSRExposicaoaAgentesNocivos")
                bot.click()
                                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                ##### Continuar automação dessa tela dessa aba apos finalizar chamado 

                ###############################################################
                ########## FIM -> Cadastros -> Tabelas de impostos ####
                ###############################################################

                ###############################################################
                ########## Cadastros -> Condições de Pagamento ####
                ###############################################################
                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'Cad_condicoesDePagamento2 '
                if not bot.find("Cad_condicoesDePagamento2", matching=0.97, waiting_time=10000):
                    not_found("Cad_condicoesDePagamento2")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                # Searching for element 'Nao '
                if not bot.find("Nao", matching=0.97, waiting_time=10000):
                    not_found("Nao")
                bot.click()
                self.type_keys_with_interval(50, "qa12!")
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.tab()
                self.wait(500)
                self.type_up()
                self.wait(500)
                self.type_down()
                self.tab()
                self.wait(500)
                self.type_up()
                self.type_up()
                self.wait(500)
                self.type_down()
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.type_down()
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()

                self.tab()
                self.wait(500)
                self.space()
                self.space()
                self.tab()
                self.wait(500)
                self.space()
                self.space()
                self.tab()
                self.wait(500)
                self.space()
                self.space()
                self.tab()
                self.wait(500)
                self.space()
                self.space()
                self.tab()
                self.wait(500)
                self.space()
                self.space()
                # Searching for element 'LP_TipodePagamentoPrevisto33221 '
                if not bot.find("LP_TipodePagamentoPrevisto33221", matching=0.97, waiting_time=10000):
                    not_found("LP_TipodePagamentoPrevisto33221")
                bot.click_relative(54, 27)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.type_keys_with_interval(100, "002")
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'LP_PlanoFinanceiro472 '
                if not bot.find("LP_PlanoFinanceiro472", matching=0.97, waiting_time=10000):
                    not_found("LP_PlanoFinanceiro472")
                bot.click_relative(80, 28)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.type_keys_with_interval(100, "001001001")
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'LP_+OperacaoLanctoFinanceiro '
                if not bot.find("LP_+OperacaoLanctoFinanceiro", matching=0.97, waiting_time=10000):
                    not_found("LP_+OperacaoLanctoFinanceiro")
                bot.click_relative(56, 31)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'LP_OperacaoBaixaFinanceiro '
                if not bot.find("LP_OperacaoBaixaFinanceiro", matching=0.97, waiting_time=10000):
                    not_found("LP_OperacaoBaixaFinanceiro")
                bot.click_relative(53, 23)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'LP_Comissao43921 '
                if not bot.find("LP_Comissao43921", matching=0.97, waiting_time=10000):
                    not_found("LP_Comissao43921")
                bot.click_relative(50, 22)
                # Searching for element 'LP_LocaldeCobranca2314 '
                if not bot.find("LP_LocaldeCobranca2314", matching=0.97, waiting_time=10000):
                    not_found("LP_LocaldeCobranca2314")
                bot.click_relative(57, 25)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                # Searching for element 'adicionar+botaopequenoverde '
                if not bot.find("adicionar+botaopequenoverde", matching=0.97, waiting_time=10000):
                    not_found("adicionar+botaopequenoverde")
                bot.click()
                # Searching for element 'slsssContaBancaria_12312 '
                if not bot.find("slsssContaBancaria_12312", matching=0.97, waiting_time=10000):
                    not_found("slsssContaBancaria_12312")
                bot.click_relative(345, 27)
                self.type_down()
                self.type_down()
                self.type_down()
                self.tab()
                
                # Searching for element 'SalvarCheckVerdePequenoladoesquerdo894 '
                if not bot.find("SalvarCheckVerdePequenoladoesquerdo894", matching=0.97, waiting_time=10000):
                    not_found("SalvarCheckVerdePequenoladoesquerdo894")
                bot.click()
                self.wait(5000)
                # Searching for element 'lixeiraPequenaladoesquerdo_cod8483 '
                if not bot.find("lixeiraPequenaladoesquerdo_cod8483", matching=0.97, waiting_time=10000):
                    not_found("lixeiraPequenaladoesquerdo_cod8483")
                bot.click_relative(9, 34)
                self.wait(700)
                self.enter()
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                ###############################################################
                ########## FIM -> Cadastros -> Condições de Pagamento ####
                ###############################################################

                ###############################################################
                ########## Cadastros -> Bombas de Combustivel ####
                ###############################################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'CAD_BombadeCombustivel '
                if not bot.find("CAD_BombadeCombustivel", matching=0.97, waiting_time=10000):
                    not_found("CAD_BombadeCombustivel")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                self.type_keys_with_interval(50, "qa12!")
                # Searching for element 'LP_Item '
                if not bot.find("LP_Item", matching=0.97, waiting_time=10000):
                    not_found("LP_Item")
                bot.click_relative(65, 28)
                # Searching for element 'btn_localizar'
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                    not_found("btn_ localizar")
                bot.click()
                self.wait(500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(700)
                self.tab()
                self.tab()
                self.type_keys_with_interval(50, "12")
                self.tab()
                self.type_keys_with_interval(50, "12")
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)
                self.type_keys_with_interval(80, "qa12")
                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'qa12!_Imagem '
                if not bot.find("qa12!_Imagem", matching=0.97, waiting_time=10000):
                    not_found("qa12!_Imagem")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                # ###############################################################
                # ########## FIM Cadastros -> Bombas de Combustivel ####
                # ###############################################################,

                # ###############################################################
                # ########## Cadastros -> Cartão Pedágio ####
                # ###############################################################

                if not bot.find("btn_cadastro", matching=0.97, waiting_time=10000):
                    not_found("btn_cadastro")
                bot.click()
                # Searching for element 'CAD_CartaoPedagio '
                if not bot.find("CAD_CartaoPedagio", matching=0.97, waiting_time=10000):
                    not_found("CAD_CartaoPedagio")
                bot.click()
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir '
                if not bot.find("Incluir", matching=0.97, waiting_time=10000):
                    not_found("Incluir")
                bot.click()
                self.wait(500)
                # Searching for element 'LP_Conta '
                if not bot.find("LP_Conta", matching=0.97, waiting_time=10000):
                    not_found("LP_Conta")
                bot.click_relative(72, 27)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(500)
                # Searching for element 'SalvarV '
                if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                    not_found("SalvarV")
                bot.click()
                
                # Searching for element 'Retornar '
                if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                    not_found("Retornar")
                bot.click_relative(-79, 71)                
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'editar_btn'
                if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                    not_found("editar_btn")
                bot.click()
                # Searching for element 'ExcluirEmpresa '
                if not bot.find("ExcluirEmpresa", matching=0.97, waiting_time=10000):
                    not_found("ExcluirEmpresa")
                bot.click()
                
                # Searching for element 'sIMV '
                if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                    not_found("sIMV")
                bot.click()
                
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1000)
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)
                # ###############################################################
                # ########## FIM -> Cadastros -> Cartão Pedágio ####
                # ###############################################################

                ################################################
                ####### FIM CADASTROS ##################
                ###########################################

                #########################################
                ################## INICIO MOVIMENTOS ####
                #########################################

                #####





                                






def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  














































































































































