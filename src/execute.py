from arquivos import Arquivos;
from pathlib import Path

diretorio = Path("./home/valcann/backupsFrom")

executar = Arquivos(diretorio)


lista_dados = executar.extrai_info_arquivos()
print("lista dados ---->", lista_dados)


executar.escreve_em_arquivo(lista_dados,Path("./home/valcann/backupFrom.log"))


executar.deleta_arquivos_por_dia(Path("./home/valcann/backupsFrom"),3)

executar.backup_ultimos_por_dias(Path("./home/valcann/backupsTo"), Path("./home/valcann/backUpTo.log"),3)

