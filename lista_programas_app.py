#import bibliotecas
import winapps

for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data da Instalação: {item.install_date}.')
    print(f'Data da publicação: {item.publisher}.')
    print(f'Data da desinstalação: {item.uninstall_string}.')
    print(f'-'*50)