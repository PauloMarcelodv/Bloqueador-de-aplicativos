Bloqueador de Aplicativos
Aplicativo desktop desenvolvido em Python para auxiliar no foco e produtividade, permitindo bloquear a execução de aplicativos específicos por um tempo determinado.
O sistema monitora processos em segundo plano e encerra automaticamente qualquer aplicativo selecionado que tente ser aberto durante o período de bloqueio.

Funcionalidades

Definir um tempo de bloqueio para qualquer aplicativo instalado
Monitoramento contínuo de processos em segundo plano
Encerramento automático do aplicativo bloqueado caso seja aberto
Interface gráfica simples e intuitiva construída com Tkinter
Execução local no Windows


Tecnologias utilizadas
TecnologiaUsoPython 3.xLinguagem principalTkinterInterface gráficaPsutilMonitoramento e controle de processos

Como rodar localmente
Pré-requisitos: Python 3.x instalado

Clone o repositório:

bashgit clone https://github.com/PauloMarcelodv/Bloqueador-de-aplicativos.git
cd Bloqueador-de-aplicativos

Instale a dependência:

bashpip install psutil

Execute o aplicativo:

bashpython Bloqueador.py

O Tkinter já vem incluído na instalação padrão do Python. Caso não esteja disponível, instale com pip install tk.


Como usar

Abra o aplicativo
Digite o nome do processo que deseja bloquear (ex: chrome.exe, discord.exe)
Defina o tempo de bloqueio em minutos
Clique em Iniciar — o monitoramento começa em segundo plano
Qualquer tentativa de abrir o aplicativo bloqueado será encerrada automaticamente


Aprendizados

Manipulação de processos do sistema operacional com Psutil
Construção de interfaces gráficas desktop com Tkinter
Programação orientada a eventos em Python
Lógica de monitoramento em background
