import pynput
from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
from pag import *
from img import images
from time import sleep
import pyautogui

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

downloads = str(pathlib.Path.cwd() / "downloads" / "Relação de afastamento")


class RelatorioDeAfastamento:

    """A clase 'RelatorioDeAfastamento' é reponsável por emitir relatório de afastamento disponibilizados no UNICO.
    Para criar uma instância da classe é preciso fornecer  : mês,ano e código da empresa
    """

    def __init__(self, mes: str, ano: str, cod_empresa: str) -> None:
        self.__mes = mes
        self.__ano = ano
        self.__cod_empresa = cod_empresa
        self.__competencia = self.__mes + self.__ano

    def get_mes(self) -> None:
        """retorna o mês"""
        return self.__mes

    def get_ano(self) -> None:
        """retorna o ano"""
        return self.__ano

    def get_cod_empresa(self) -> None:
        """retorna o código da empresa"""

        return self.__cod_empresa

    def unico_acess(self) -> None:
        """Método é reponsável por inicializar o UNICO clicando sobre o atalho do software encontrado na área de trabalho"""

        double_click(images.IMAGES["ICON"]["ICON-UNICO"])
        double_click(images.IMAGES["BUTTON"]["EXE"])

    def login_user(self) -> None:
        """Método é reponsável por realizar o login do usuário no UNICO"""

        username = "ROBOT"
        password = "123mudar."
        to_click(images.IMAGES["LABEL"]["USER"])
        keyboard.type(username)
        to_click(images.IMAGES["LABEL"]["PASSWORD"])
        keyboard.type(password)
        sleep(1)
        double_click(images.IMAGES["BUTTON"]["ACCEPTED"])
        sleep(1)
        try:
            to_click(images.IMAGES["BUTTON"]["ALERT"])
            to_click(images.IMAGES["BUTTON"]["CLOSE"])
        except:
            pass

    def acess_folha(self) -> None:
        """Método é reponsável  entrar no modo FOLHA UNICO"""

        sleep(2)
        double_click(images.IMAGES["PAGES"]["UNI"])

    def acess_unico(self) -> None:
        double_click(images.IMAGES["MENUBAR"]["UNIFOLHA"])
        sleep(1)

    def aba_relatorio(self) -> None:
        """Método responsável por navegar nas abas de menu do unico e abrir janela de relatório"""

        sleep(1)
        to_click(images.IMAGES["MENUBAR"]["RELATORIO"])
        sleep(1)
        to_click(images.IMAGES["MENUBAR"]["PERIODICOS"])
        sleep(1)
        to_click(images.IMAGES["MENUBAR"]["RELATORIOASTAMENTO"])
        sleep(1)

    def prepara_relatorio(self) -> None:
        """Método responsável por preencher campos da janela de relatório e confirmar impressão no botão de impressora."""

        to_click(images.IMAGES["LABEL"]["COD.EMPRESA"])
        keyboard.type(self.get_cod_empresa())
        keyboard.press(Key.enter)
        keyboard.press(Key.tab)
        sleep(1)
        to_click(images.IMAGES["LABEL"]["COMPETENCIA"], x=20)
        sleep(1)
        keyboard.type(self.__competencia)

    def gerar_relatorio(self) -> None:
        """Método responsável por realizar download do arquivo e carregar o mesmo na pasta downloads"""

        to_click(images.IMAGES["BUTTON"]["PRINT"])
        sleep(1)
        to_click(images.IMAGES["BUTTON"]["OKPRINT"])
        sleep(1)
        to_click(images.IMAGES["LABEL"]["SAVE"], x=20)
        keyboard.press(Key.backspace)
        sleep(1)
        keyboard.type(downloads)
        to_click(images.IMAGES["LABEL"]["SAVETWO"])
