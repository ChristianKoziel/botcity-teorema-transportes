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
"""# Searching for element 'teste '
if not bot.find("teste", matching=0.97, waiting_time=10000):
    not_found("teste")


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
                
                # Searching for element 'salvarNewBicostest01 '
                if not bot.find("salvarNewBicostest01", matching=0.97, waiting_time=10000):
                    not_found("salvarNewBicostest01")
                bot.click()# Searching for element 'teste '
                bot.click()if not bot.find("teste", matching=0.97, waiting_time=10000):
                bot.click()    not_found("teste")
                bot.click()bot.click()
                bot.click()
                # Searching for element 'testee '
                if not bot.find("testee", matching=0.97, waiting_time=10000):
                    not_found("testee")
                bot.click()
                
                
