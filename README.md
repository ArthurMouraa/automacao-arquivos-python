

#  Desafio Proposto  
**Problema 1 | Automação de Ambientes Operacionais**

Um dos principais desafios para o gerenciamento de infraestrutura é implementar automação para permitir maior produtividade aos times de tecnologia, além de minimizar ações humanas nos ambientes dos clientes.  

O cliente **“Acme Co.”** possui um servidor centralizado de backup que:  
1. Recebe arquivos de outros servidores;  
2. Move os dados para um volume temporário;  
3. Esse volume é consumido por uma ferramenta de backup externa.  

Para reduzir a intervenção manual, foi solicitado o desenvolvimento de um **script em Python** que automatize as seguintes tarefas:

- 📂 Listar todos os arquivos (nome, tamanho, data de criação e última modificação) no diretório:  
  `/home/valcann/backupsFrom`  
- 📝 Salvar o resultado no arquivo de log:  
  `/home/valcann/backupsFrom.log`  
- 🗑️ Remover todos os arquivos com **data de criação superior a 3 dias**;  
- 📦 Copiar todos os arquivos com **data de criação menor ou igual a 3 dias** para:  
  `/home/valcann/backupsTo`  
- 📝 Salvar o resultado da cópia no arquivo de log:  
  `/home/valcann/backupsTo.log`.  

---

## Solução Implementada  

O código foi desenvolvido em **Python 3** utilizando a biblioteca padrão (`pathlib`, `datetime`, `shutil`).  
Ele é organizado em uma classe chamada `Arquivos`, que contém métodos para:  

- **`extrai_info_arquivos()`** → Extrai informações de arquivos (nome, tamanho, criação, modificação);  
- **`escreve_em_arquivo()`** → Registra logs em arquivos `.log`;  
- **`deleta_arquivos_por_dia()`** → Remove arquivos de acordo com a data limite;  
- **`backup_ultimos_por_dias()`** → Copia arquivos recentes e gera log.  

---

## Guia rápido de uso 


**A classe Arquivos centraliza todas as operações.**
**Aqui estão exemplos práticos para entender como cada método funciona:**

1. extrai_info_arquivos(diretorio: Path = None) -> list
Lista todos os arquivos do diretório especificado e retorna informações como:
- Nome do arquivo
- Tamanho em bytes
- Data de criação
- Data da última modificação

2. escreve_em_arquivo(lista_de_dados: list, arquivo_log: Path)
   - Recebe a lista gerada pelo método anterior e escreve os dados em um arquivo .log.
     
3. deleta_arquivos_por_dia(diretorio: Path, dias_atras: int)
   - Remove todos os arquivos cuja data de criação seja igual à data de dias_atras atrás.
     Exemplo: ao passar 3, ele vai procurar arquivos criados há 3 dias e removê-los.

4. backup_ultimos_por_dias(copia_de: Path, escreve_em: Path, dias: int)
   - Copia arquivos recentes (com data de criação menor ou igual ao limite de dias) para outro diretório e registra em log.
---

##  Como Executar  

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/automacao-arquivos-python.git
2. Acesse o diretório:
   ```bash
   cd src
3. Execute o script
   ```bash
   python execute.py

  
   

