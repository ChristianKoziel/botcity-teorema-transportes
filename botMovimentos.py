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
                #########################################
                ########### INICIO MOVIMENTOS ###########
                #########################################

                # # Searching for element 'CAD_Movimentos_Menu '
                # if not bot.find("CAD_Movimentos_Menu", matching=0.97, waiting_time=10000):
                #     not_found("CAD_Movimentos_Menu")
                # bot.click()     
                # # Searching for element 'Mov_TrocaDeMotoristasPorVeiculos '
                # if not bot.find("Mov_TrocaDeMotoristasPorVeiculos", matching=0.97, waiting_time=10000):
                #     not_found("Mov_TrocaDeMotoristasPorVeiculos")
                # bot.click() 
                # # Searching for element 'btn_nao'
                # if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                #     not_found("btn_nao")
                # bot.click()    
                # # Searching for element 'LP_Motoristaqwe321523 '
                # if not bot.find("LP_Motoristaqwe321523", matching=0.97, waiting_time=10000):
                #     not_found("LP_Motoristaqwe321523")
                # bot.click_relative(60, 25)
                # self.wait(500)
                # # Searching for element 'btn_localizar'
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                #     not_found("btn_ localizar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click() 
                # # Searching for element 'btn_localizar'
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                #     not_found("btn_ localizar")
                # bot.click()
                # # Searching for element 'btn_cadastro_incluir'
                # if not bot.find("btn_cadastro_incluir", matching=0.97, waiting_time=10000):
                #     not_found("btn_cadastro_incluir")
                # bot.click()
                # self.wait(1000)
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
                # # Searching for element 'LP_Motoristaqwe321523 '
                # if not bot.find("LP_Motoristaqwe321523", matching=0.97, waiting_time=10000):
                #     not_found("LP_Motoristaqwe321523")
                # bot.click_relative(60, 25)
                # self.wait(500)
                # # Searching for element 'btn_localizar'
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                #     not_found("btn_ localizar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # # Searching for element 'LP_Veiculo_573592 '
                # if not bot.find("LP_Veiculo_573592", matching=0.97, waiting_time=10000):
                #     not_found("LP_Veiculo_573592")
                # bot.click_relative(61, 25)
                # # Searching for element 'btn_localizar'
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                #     not_found("btn_ localizar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(50, "qa12!")
                # # Searching for element 'SalvarV '
                # if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                #     not_found("SalvarV")
                # bot.click()
                
                # # Searching for element 'Retornar '
                # if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                #     not_found("Retornar")
                # bot.click_relative(-79, 71)                
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # # Searching for element 'Retornar '
                # if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                #     not_found("Retornar")
                # bot.click_relative(-79, 71)

                # ##
                # ######### Movimentos -> Engates / Desengates de Veiculos #######
                # ##

                # # Searching for element 'CAD_Movimentos_Menu '
                # if not bot.find("CAD_Movimentos_Menu", matching=0.97, waiting_time=10000):
                #     not_found("CAD_Movimentos_Menu")
                # bot.click()                
                # # Searching for element 'Mov_EngateesBARRADesengatesdeVeiculos '
                # if not bot.find("Mov_EngateesBARRADesengatesdeVeiculos", matching=0.97, waiting_time=10000):
                #     not_found("Mov_EngateesBARRADesengatesdeVeiculos")
                # bot.click()
                # # Searching for element 'NovaLUPA_Localizar '
                # if not bot.find("NovaLUPA_Localizar", matching=0.97, waiting_time=10000):
                #     not_found("NovaLUPA_Localizar")
                # bot.click()
                # # Searching for element 'NOVO_INCLUIR_PLUS '
                # if not bot.find("NOVO_INCLUIR_PLUS", matching=0.97, waiting_time=10000):
                #     not_found("NOVO_INCLUIR_PLUS")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'LP_VEICULO_8495 '
                # if not bot.find("LP_VEICULO_8495", matching=0.97, waiting_time=10000):
                #     not_found("LP_VEICULO_8495")
                # bot.click_relative(65, 28)
                # # Searching for element 'btn_localizar'
                # if not bot.find("btn_localizar", matching=0.97, waiting_time=10000):
                #     not_found("btn_ localizar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(100, "123")
                # self.tab()
                # # Searching for element 'DATA_DESENGATE '
                # if not bot.find("DATA_DESENGATE", matching=0.97, waiting_time=10000):
                #     not_found("DATA_DESENGATE")
                # bot.click_relative(101, 28)
                # self.wait(500)
                # # Searching for element 'TODAY '
                # if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                #     not_found("TODAY")
                # bot.click()
                # self.tab()
                # self.type_keys_with_interval(50, "123")
                # # Searching for element 'Engate1_LP '
                # if not bot.find("Engate1_LP", matching=0.97, waiting_time=10000):
                #     not_found("Engate1_LP")
                # bot.click_relative(63, 27)
                # self.wait(500)
                
                
                # # # Searching for element 'NEW_LOCALIZAR_3518 '
                # # if not bot.find("NEW_LOCALIZAR_3518", matching=0.97, waiting_time=10000):
                # #     not_found("NEW_LOCALIZAR_3518")
                # # bot.click()
                # self.wait(500)
                # self.type_keys_with_interval(50, "000002")
                # # Searching for element 'NEW_LOCALIZAR_3518 '
                # if not bot.find("NEW_LOCALIZAR_3518", matching=0.97, waiting_time=10000):
                #     not_found("NEW_LOCALIZAR_3518")
                # bot.click()
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()                
                # self.wait(500)
                # # Searching for element 'LP_ENGATE2_439 '
                # if not bot.find("LP_ENGATE2_439", matching=0.97, waiting_time=10000):
                #     not_found("LP_ENGATE2_439")
                # bot.click_relative(66, 27)
                # self.wait(500)
                # self.type_keys_with_interval(50, "000003")
                # # Searching for element 'NEW_LOCALIZAR_3518 '
                # if not bot.find("NEW_LOCALIZAR_3518", matching=0.97, waiting_time=10000):
                #     not_found("NEW_LOCALIZAR_3518")
                # bot.click()
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()                
                # self.wait(500)
                # # Searching for element 'LP_ENGATE3_53425 '
                # if not bot.find("LP_ENGATE3_53425", matching=0.97, waiting_time=10000):
                #     not_found("LP_ENGATE3_53425")
                # bot.click_relative(63, 27)
                # self.wait(500)
                # self.type_keys_with_interval(50, "000004")
                # # Searching for element 'NEW_LOCALIZAR_3518 '
                # if not bot.find("NEW_LOCALIZAR_3518", matching=0.97, waiting_time=10000):
                #     not_found("NEW_LOCALIZAR_3518")
                # bot.click()
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()                
                # self.wait(500)
                # self.tab()
                # self.type_keys_with_interval(50, "qa12!")
                # # Searching for element 'obc '
                # if not bot.find("obc", matching=0.97, waiting_time=10000):
                #     not_found("obc")
                # bot.click()
                # # Searching for element 'SalvarV '
                # if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                #     not_found("SalvarV")
                # bot.click()
                
                # # Searching for element 'Retornar '
                # if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                #     not_found("Retornar")
                # bot.click_relative(-79, 71)
                # # Searching for element 'selecionaDATAAtual '
                # if not bot.find("selecionaDATAAtual", matching=0.97, waiting_time=10000):
                #     not_found("selecionaDATAAtual")
                # bot.click_relative(62, 26)
                # # Searching for element 'TODAY '
                # if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                #     not_found("TODAY")
                # bot.click()
                # # Searching for element 'LocalizarDNV213124 '
                # if not bot.find("LocalizarDNV213124", matching=0.97, waiting_time=10000):
                #     not_found("LocalizarDNV213124")
                # bot.click()

                # # # Searching for element 'SLC_DATAATUAL43423 '
                # # if not bot.find("SLC_DATAATUAL43423", matching=0.97, waiting_time=10000):
                # #     not_found("SLC_DATAATUAL43423")
                # # bot.click_relative(151, 50)
                # # # Searching for element 'TODAY '
                # # if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                # #     not_found("TODAY")
                # # bot.click()
                # # # Searching for element 'Localizar '
                # # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                # #     not_found("Localizar")
                # # bot.click()
                # # Searching for element 'NOVO_EDITAR_433 '
                # if not bot.find("NOVO_EDITAR_433", matching=0.97, waiting_time=10000):
                #     not_found("NOVO_EDITAR_433")
                # bot.click()
                # # Searching for element 'Excluir_233 '
                # if not bot.find("Excluir_233", matching=0.97, waiting_time=10000):
                #     not_found("Excluir_233")
                # bot.click()
                
                # # Searching for element 'sIMV '
                # if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                #     not_found("sIMV")
                # bot.click()
                
                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 70)
                # self.wait(2000)
                # # Searching for element 'LocalizarDNV213124 '
                # if not bot.find("LocalizarDNV213124", matching=0.97, waiting_time=10000):
                #     not_found("LocalizarDNV213124")
                # bot.click()
                # self.wait(2000)
                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 70)
                # self.wait(1000)

                # #################################################
                # ########## Movimentos -> Pedidos de Frete #######
                # #################################################
                # # Searching for element 'CAD_Movimentos_Menu '
                # if not bot.find("CAD_Movimentos_Menu", matching=0.97, waiting_time=10000):
                #     not_found("CAD_Movimentos_Menu")
                # bot.click()
                # # Searching for element 'CAD_Mov_PedidosDeFretes '
                # if not bot.find("CAD_Mov_PedidosDeFretes", matching=0.97, waiting_time=10000):
                #     not_found("CAD_Mov_PedidosDeFretes")
                # bot.click()  
                # # Searching for element 'btn_nao'
                # if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                #     not_found("btn_nao")
                # bot.click()
                # self.wait(1000) 
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()

                # # Searching for element 'Incluir_nv523 '
                # if not bot.find("Incluir_nv523", matching=0.97, waiting_time=10000):
                #     not_found("Incluir_nv523")
                # bot.click()
                # # Searching for element 'lp_Veiculo_45334 '
                # if not bot.find("lp_Veiculo_45334", matching=0.97, waiting_time=10000):
                #     not_found("lp_Veiculo_45334")
                # bot.click_relative(64, 23)
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # self.wait(1500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'Remetente_lp_125 '
                # if not bot.find("Remetente_lp_125", matching=0.97, waiting_time=10000):
                #     not_found("Remetente_lp_125")
                # bot.click_relative(64, 22)
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # self.wait(1500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'Destinatario_lpnv9892 '
                # if not bot.find("Destinatario_lpnv9892", matching=0.97, waiting_time=10000):
                #     not_found("Destinatario_lpnv9892")
                # bot.click_relative(63, 26)
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # self.wait(1500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'Mn_cl_lp_32232 '
                # if not bot.find("Mn_cl_lp_32232", matching=0.97, waiting_time=10000):
                #     not_found("Mn_cl_lp_32232")
                # bot.click_relative(60, 23)
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # self.wait(1500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'LP_municipior_entrega_2323 '
                # if not bot.find("LP_municipior_entrega_2323", matching=0.97, waiting_time=10000):
                #     not_found("LP_municipior_entrega_2323")
                # bot.click_relative(65, 26)
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # self.wait(1500)
                # # Searching for element 'btn_selecionar'
                # if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                #     not_found("btn_selecionar")
                # bot.click()
                # self.wait(500)
                # # Searching for element 'qtdadeKGsl '
                # if not bot.find("qtdadeKGsl", matching=0.97, waiting_time=10000):
                #     not_found("qtdadeKGsl")
                # bot.click_relative(51, 29)
                # self.wait(500)
                # self.type_keys_with_interval(50, "123")
                # # Searching for element 'LP_Entrega_dataAual '
                # if not bot.find("LP_Entrega_dataAual", matching=0.97, waiting_time=10000):
                #     not_found("LP_Entrega_dataAual")
                # bot.click_relative(74, 24)
                # # Searching for element 'TODAY '
                # if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                #     not_found("TODAY")
                # bot.click()
                # # Searching for element 'Carregamento_DATA_ATUAL '
                # if not bot.find("Carregamento_DATA_ATUAL", matching=0.97, waiting_time=10000):
                #     not_found("Carregamento_DATA_ATUAL")
                # bot.click_relative(70, 26)
                # # Searching for element 'TODAY '
                # if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                #     not_found("TODAY")
                # bot.click()
                # # Searching for element 'SalvarV '
                # if not bot.find("SalvarV", matching=0.97, waiting_time=10000):
                #     not_found("SalvarV")
                # bot.click()
                
                # # Searching for element 'Retornar '
                # if not bot.find("Retornar", matching=0.97, waiting_time=10000):
                #     not_found("Retornar")
                # bot.click_relative(-79, 71)
                
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                
                # # Searching for element 'editar_btn'
                # if not bot.find("editar_btn", matching=0.97, waiting_time=10000):
                #     not_found("editar_btn")
                # bot.click()
                # # Searching for element 'Excluir_42342 '
                # if not bot.find("Excluir_42342", matching=0.97, waiting_time=10000):
                #     not_found("Excluir_42342")
                # bot.click()                
                # # Searching for element 'sIMV '
                # if not bot.find("sIMV", matching=0.97, waiting_time=10000):
                #     not_found("sIMV")
                # bot.click()
                
                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 70)
                # self.wait(1000)
                # # Searching for element 'Localizar '
                # if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                #     not_found("Localizar")
                # bot.click()
                # self.wait(1000)
                # # Searching for element 'retornar '
                # if not bot.find("retornar", matching=0.97, waiting_time=10000):
                #     not_found("retornar")
                # bot.click_relative(-83, 70)

                #################################################
                ########## Movimentos -> Pedidos de Frete #######
                #################################################
                # Searching for element 'CAD_Movimentos_Menu '
                if not bot.find("CAD_Movimentos_Menu", matching=0.97, waiting_time=10000):
                    not_found("CAD_Movimentos_Menu")
                bot.click()
                # Searching for element 'CAD_Movimentos_ORDdeCarregamento '
                if not bot.find("CAD_Movimentos_ORDdeCarregamento", matching=0.97, waiting_time=10000):
                    not_found("CAD_Movimentos_ORDdeCarregamento")
                bot.click()
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.wait(1000) 
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'retornar '
                if not bot.find("retornar", matching=0.97, waiting_time=10000):
                    not_found("retornar")
                bot.click_relative(-83, 70)

                #################################################
                ########## Movimentos -> Ordem de Carregamento #######
                #################################################
                # Searching for element 'CAD_Movimentos_Menu '
                if not bot.find("CAD_Movimentos_Menu", matching=0.97, waiting_time=10000):
                    not_found("CAD_Movimentos_Menu")
                bot.click()
                # Searching for element 'Mov_OrdemDeCarregamento '
                if not bot.find("Mov_OrdemDeCarregamento", matching=0.97, waiting_time=10000):
                    not_found("Mov_OrdemDeCarregamento")
                bot.click()
                # Searching for element 'btn_nao'
                if not bot.find("btn_nao", matching=0.97, waiting_time=10000):
                    not_found("btn_nao")
                bot.click()
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                # Searching for element 'Incluir_botaoComMaisVerde '
                if not bot.find("Incluir_botaoComMaisVerde", matching=0.97, waiting_time=10000):
                    not_found("Incluir_botaoComMaisVerde")
                bot.click()
                self.wait(1000)
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.wait(1000)
                # Searching for element 'Validade_today '
                if not bot.find("Validade_today", matching=0.97, waiting_time=10000):
                    not_found("Validade_today")
                bot.click_relative(76, 28)
                self.wait(1000)
                # Searching for element 'TODAY '
                if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                    not_found("TODAY")
                bot.click()
                self.wait(1000)
                # Searching for element 'DataCarregamentoToday839283 '
                if not bot.find("DataCarregamentoToday839283", matching=0.97, waiting_time=10000):
                    not_found("DataCarregamentoToday839283")
                bot.click_relative(73, 27)
                # Searching for element 'TODAY '
                if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                    not_found("TODAY")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "23")
                self.tab()
                # Searching for element 'DataEntrega_troday932893 '
                if not bot.find("DataEntrega_troday932893", matching=0.97, waiting_time=10000):
                    not_found("DataEntrega_troday932893")
                bot.click_relative(79, 30)
                self.wait(1000)
                # Searching for element 'TODAY '
                if not bot.find("TODAY", matching=0.97, waiting_time=10000):
                    not_found("TODAY")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "23")
                # Searching for element 'LP_Cliente4314 '
                if not bot.find("LP_Cliente4314", matching=0.97, waiting_time=10000):
                    not_found("LP_Cliente4314")
                bot.click_relative(57, 23)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                self.tab()
                self.type_keys_with_interval(50, "123")
                # Searching for element 'lp_veiculo13221 '
                if not bot.find("lp_veiculo13221", matching=0.97, waiting_time=10000):
                    not_found("lp_veiculo13221")
                bot.click_relative(61, 24)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'lp_proprietario321321 '
                if not bot.find("lp_proprietario321321", matching=0.97, waiting_time=10000):
                    not_found("lp_proprietario321321")
                bot.click_relative(60, 22)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'lp_motorista533243 '
                if not bot.find("lp_motorista533243", matching=0.97, waiting_time=10000):
                    not_found("lp_motorista533243")
                bot.click_relative(58, 24)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                self.wait(1000)
                # Searching for element 'incluirSmall '
                if not bot.find("incluirSmall", matching=0.97, waiting_time=10000):
                    not_found("incluirSmall")
                bot.click()
                # Searching for element 'lpEmbarque4343 '
                if not bot.find("lpEmbarque4343", matching=0.97, waiting_time=10000):
                    not_found("lpEmbarque4343")
                bot.click_relative(113, 7)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'LP_Destinatario43342 '
                if not bot.find("LP_Destinatario43342", matching=0.97, waiting_time=10000):
                    not_found("LP_Destinatario43342")
                bot.click_relative(122, 3)
                self.wait(1000)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()
                # Searching for element 'LP_Tomador432432 '
                if not bot.find("LP_Tomador432432", matching=0.97, waiting_time=10000):
                    not_found("LP_Tomador432432")
                bot.click_relative(108, 4)
                # Searching for element 'Localizar '
                if not bot.find("Localizar", matching=0.97, waiting_time=10000):
                    not_found("Localizar")
                bot.click()
                self.wait(1500)
                # Searching for element 'btn_selecionar'
                if not bot.find("btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("btn_selecionar")
                bot.click()










def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()