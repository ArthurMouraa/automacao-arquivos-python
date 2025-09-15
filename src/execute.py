from arquivos import Arquivos;
from pathlib import Path

diretorio = Path("./home/valcann/backupsFrom")

executar = Arquivos(diretorio)

#Listar todos arquivos (nome, tamanho, data de criação, data da última modificação)
#localizados no caminho /home/valcann/backupsFrom;
lista_dados = executar.extrai_info_arquivos()
print("lista dados ---->", lista_dados)

#Salvar o resultado no arquivo backupsFrom.log em /home/valcann/;
executar.escreve_em_arquivo(lista_dados,Path("./home/valcann/backupFrom.log"))

#Remover todos os arquivos com data de criação superior a 3 (três) dias;
executar.deleta_arquivos_por_dia(Path("./home/valcann/backupsFrom"),3)

#Copiar todos os arquivos os arquivos com data de criação menor ou igual a 3 (três) dias
# em homevalcann/backupsTo;
# Salvar o resultado no arquivo backupsTo.log em /home/valcann/.

executar.backup_ultimos_por_dias(Path("./home/valcann/backupsTo"), Path("./home/valcann/backUpTo.log"),3)

