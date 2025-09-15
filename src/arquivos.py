
from pathlib import Path
from datetime import datetime, timedelta
from pathlib import Path
from datetime import datetime, timedelta
import shutil
import time 

class Arquivos:

  def __init__(self, diretorio: Path):
      self.diretorio = diretorio


  def extrai_info_arquivos(self, diretorio: Path = None) -> list:

    if diretorio == None :
       diretorio = self.diretorio
    dados_dos_arquivos = []

    if not diretorio.exists() or not any(diretorio.iterdir()):
        print("Não existe arquivos no diretório atual")
        return dados_dos_arquivos

    for arquivo in diretorio.iterdir():
        if arquivo.is_file():  
            stat = arquivo.stat()

            lidos_do_arquivo = {
                "nome" : arquivo.name,
                "tamanho": f'{stat.st_size}b',
                "criado": datetime.fromtimestamp(stat.st_birthtime).strftime("%Y-%m-%d %H:%M:%S"),
                "modificado": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                }
            dados_dos_arquivos.append(lidos_do_arquivo)
        else :
          print("Não existe arquivos no diretório atual")
    return dados_dos_arquivos


  def escreve_em_arquivo(self, lista_de_dados: list, arquivo_log: Path):
    with arquivo_log.open("a", encoding="utf-8") as log :
      for dado in lista_de_dados:
          log.write(f"Arquivo: {dado['nome']}\n")
          log.write(f"Tamanho: {dado['tamanho']}\n")
          log.write(f"Criação: {dado['criado']}\n")
          log.write(f"Última modificação: {dado['modificado']}\n")
          log.write(" " "\n")

  def deleta_arquivos_por_dia(self, diretorio: Path, dias_atras: int):
        limite = (datetime.now() - timedelta(days=dias_atras)).date()
        removidos = 0
        print(f"**********Procurando arquivos mais antigos que {limite} no diretório {diretorio}\n")

        for arquivo in diretorio.iterdir():
            if arquivo.is_file():
                data_criacao = datetime.fromtimestamp(arquivo.stat().st_birthtime).date()

                if data_criacao < limite:
                    print(f"****** Removendo: {arquivo} (criado em {data_criacao})\n")
                    arquivo.unlink()
                    removidos += 1

        if removidos == 0:
            print(f"Não foram encontrados arquivos com mais de {dias_atras} dias.")
        else:
            print(f"Total de arquivos removidos: {removidos}")


  def backup_ultimos_por_dias(self, copia_de:Path, escreve_em:Path, dias:int) :
      if dias < 1 :
        dias = 1
      
      limite = datetime.now() - timedelta(days=dias)
          
          
      arquivos_info = self.extrai_info_arquivos(copia_de)
          
          
      arquivos_recentes = [
              arquivo for arquivo in arquivos_info
              if datetime.strptime(arquivo['criado'], "%Y-%m-%d %H:%M:%S") >= limite
        
      ]
      self.escreve_em_arquivo(arquivos_recentes, escreve_em)

  
      
