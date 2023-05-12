from relatorioAfastamento import *

r = RelatorioDeAfastamento('05','2023','2729')
r.unico_acess()
sleep(3)
r.login_user()
r.acess_folha()
r.acess_unico()
sleep(1)
r.aba_relatorio()
r.prepara_relatorio()
r.gerar_relatorio()