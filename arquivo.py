

from pathlib import Path
from datetime import datetime, timedelta
import shutil
import time 


pasta_arquivos = Path("C:\\home\\valcann\\backupsFrom")

arquivo_log =  Path("C:\\home\\valcann\\backupsFrom.log")

def extrai_info_arquivos(diretorio: Path):
  dados_dos_arquivos = []

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


def escreve_em_arquivo(lista_de_dados: list, arquivo_log: Path):
   with arquivo_log.open("a", encoding="utf-8") as log :
    for dado in lista_de_dados:
        log.write(f"Arquivo: {dado['nome']}\n")
        log.write(f"Tamanho: {dado['tamanho']}\n")
        log.write(f"Criação: {dado['criado']}\n")
        log.write(f"Última modificação: {dado['modificado']}\n")
        log.write(" " "\n")



def deleta_arquivos_por_dia(diretorio: Path, dias_atras: int):
    data_alvo = (datetime.now() - timedelta(days=dias_atras)).date()
    removidos = 0
    print(f"**********Procurando arquivos criados em {data_alvo} no diretório {diretorio} \n")

    for arquivo in diretorio.iterdir():
        if arquivo.is_file():
            data_criacao = datetime.fromtimestamp(arquivo.stat().st_birthtime).date()

            if data_criacao == data_alvo:
                print(f"******Removendo: {arquivo} \n")
                arquivo.unlink()
                removidos += 1
            else:
               print(f"Não existe arquivo com essa data -> {data_alvo}")


def backup_ultimos_por_dias(diretorioCopia:Path, arquivoCola:Path, dias:int) :
    if dias < 1 :
       dias = 1
    
    limite = datetime.now() - timedelta(days=dias)
        
        # Extrai informações dos arquivos
    arquivos_info = extrai_info_arquivos(diretorioCopia)
        
        # Filtra apenas arquivos recentes
    arquivos_recentes = [
            arquivo for arquivo in arquivos_info
            if datetime.strptime(arquivo['criado'], "%Y-%m-%d %H:%M:%S") >= limite
            
    ]

    escreve_em_arquivo(arquivos_recentes, arquivoCola)

cp = Path(r"C:\home\valcann\backupsFrom")
cl = Path(r"C:\home\valcann\backUpTo.log")
backup_ultimos_por_dias(cp, cl,3)
    

