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
                
                # Searching for element 'lp_UsaPdCdE'
                if not bot.find("lp_UsaPdCdE", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaPdCdE")
                bot.click_relative(64, 26)
                # Searching for element 'btn_localizar'##
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()     
                # Searching for element 'lp_UsaHistoricodaEmpresa'
                if not bot.find("lp_UsaHistoricodaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaHistoricodaEmpresa")
                bot.click_relative(64, 21)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaCFdE'
                if not bot.find("lp_Usa CF d E", matching=0.97, waiting_time=10000):
                    not_found("lp_Usa CF d E")
                bot.click_relative(64, 24)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaItensdaEmpresa'
                if not bot.find("lp_Usa Itens da Empresa", matching=0.97, waiting_time=10000):
                    not_found("lp_Usa Itens da Empresa")
                bot.click_relative(63, 26)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaPrecodaempresa'
                if not bot.find("lp_Usa Preco da empresa", matching=0.97, waiting_time=10000):
                    not_found("lp_Usa Preco da empresa")
                bot.click_relative(64, 26)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_usaPlanodcPfde'
                if not bot.find("lp_usa Plano d c P f d e", matching=0.97, waiting_time=10000):
                    not_found("lp_usa Plano d c P f d e")
                bot.click_relative(62, 23)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaVendedoresdaEmpresa'
                if not bot.find("lp_UsaVendedoresdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaVendedoresdaEmpresa")
                bot.click_relative(64, 23)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaSituacoesdaEmpresa'
                if not bot.find("lp_UsaSituacoesdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaSituacoesdaEmpresa")
                bot.click_relative(63, 20)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_tabeladeprecositens'
                if not bot.find("lp_tabeladeprecositens", matching=0.97, waiting_time=10000):
                    not_found("lp_tabeladeprecositens")
                bot.click_relative(65, 26)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                self.backspace()
                self.tab()
                self.tab()
                # Searching for element 'lp_tabelaDePrecosServicos'
                if not bot.find("lp_tabelaDePrecosServicos", matching=0.97, waiting_time=10000):
                    not_found("lp_tabelaDePrecosServicos")
                bot.click_relative(70, 25)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                self.backspace()
                self.tab()
                self.tab()
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


                #################################################
                #### AQUI CONCLUI CADASTRO DE EMPRESA #########
                ############################################


                # Searching for element 'cadastros '
                if not bot.find("cadastros", matching=0.97, waiting_time=10000):
                    not_found("cadastros")
                bot.click_relative(-91, -20)
                
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
                
                # Searching for element 'lp_UsaPdCdE'
                if not bot.find("lp_UsaPdCdE", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaPdCdE")
                bot.click_relative(64, 26)
                # Searching for element 'btn_localizar'##
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()     
                # Searching for element 'lp_UsaHistoricodaEmpresa'
                if not bot.find("lp_UsaHistoricodaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaHistoricodaEmpresa")
                bot.click_relative(64, 21)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaCFdE'
                if not bot.find("lp_Usa CF d E", matching=0.97, waiting_time=10000):
                    not_found("lp_Usa CF d E")
                bot.click_relative(64, 24)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaItensdaEmpresa'
                if not bot.find("lp_Usa Itens da Empresa", matching=0.97, waiting_time=10000):
                    not_found("lp_Usa Itens da Empresa")
                bot.click_relative(63, 26)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaPrecodaempresa'
                if not bot.find("lp_Usa Preco da empresa", matching=0.97, waiting_time=10000):
                    not_found("lp_Usa Preco da empresa")
                bot.click_relative(64, 26)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_usaPlanodcPfde'
                if not bot.find("lp_usa Plano d c P f d e", matching=0.97, waiting_time=10000):
                    not_found("lp_usa Plano d c P f d e")
                bot.click_relative(62, 23)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaVendedoresdaEmpresa'
                if not bot.find("lp_UsaVendedoresdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaVendedoresdaEmpresa")
                bot.click_relative(64, 23)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_UsaSituacoesdaEmpresa'
                if not bot.find("lp_UsaSituacoesdaEmpresa", matching=0.97, waiting_time=10000):
                    not_found("lp_UsaSituacoesdaEmpresa")
                bot.click_relative(63, 20)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                # Searching for element 'lp_tabeladeprecositens'
                if not bot.find("lp_tabeladeprecositens", matching=0.97, waiting_time=10000):
                    not_found("lp_tabeladeprecositens")
                bot.click_relative(65, 26)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                self.backspace()
                self.tab()
                self.tab()
                # Searching for element 'lp_tabelaDePrecosServicos'
                if not bot.find("lp_tabelaDePrecosServicos", matching=0.97, waiting_time=10000):
                    not_found("lp_tabelaDePrecosServicos")
                bot.click_relative(70, 25)
                # Searching for element 'btn_localizar'####
                if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):##
                    not_found("btn_localizar")                                      ##
                bot.click()                                                         ##
                # Searching for element 'btn_selecionar'##
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):# REUTILIZAR LOCALIZAR E SELECIONAR
                    not_found("btn_selecionar")                                     ##
                bot.click()
                self.backspace()
                self.tab()
                self.tab()
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
                
                # Searching for element 'cadastro '
                if not bot.find("cadastro", matching=0.97, waiting_time=10000):
                    not_found("cadastro")
                bot.click()
                
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
                
                
                
                
                
        
    
                
    




def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  










# Searching for element 'selecionatesteGE '
if not bot.find("selecionatesteGE", matching=0.97, waiting_time=10000):
    not_found("selecionatesteGE")
bot.click()

















































































