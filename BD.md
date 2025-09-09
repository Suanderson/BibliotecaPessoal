# 📌 Conectando o Django ao MySQL (Workbench)

Este guia explica como configurar e conectar seu projeto **Django** ao banco de dados criado no **MySQL Workbench**.

---

## 🔹 1. Instalar dependências no ambiente virtual

Dentro do ambiente virtual (`venv`) do seu projeto, instale o **PyMySQL**:

```bash
pip install pymysql
✅ Verifique se a instalação foi concluída:


pip list
✅ Veja detalhes da instalação (nome e versão):


pip show pymysql
⚠️ Possíveis erros de instalação:

Se aparecer erro de compilação, execute antes:


pip install --upgrade pip setuptools wheel
No Windows, certifique-se de que o MySQL Server está instalado corretamente e rodando.

🔹 2. Configurar o PyMySQL no Django
No arquivo __init__.py da pasta principal do projeto (mesmo nível do settings.py), adicione:

import pymysql
pymysql.install_as_MySQLdb()
Isso faz o Django reconhecer o PyMySQL como se fosse o MySQLdb.

🔹 3. Configurar o banco no settings.py
Abra o arquivo settings.py e edite a seção DATABASES:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Driver do MySQL
        'NAME': 'biblioteca',   # Nome do banco criado no Workbench
        'USER': 'root',         # Usuário do MySQL
        'PASSWORD': 'exemplo',  # Senha do MySQL
        'HOST': '127.0.0.1',    # Servidor local
        'PORT': '3306',         # Porta padrão do MySQL
    }
}
⚠️ Possíveis erros de conexão:

django.db.utils.OperationalError: (1045, "Access denied...")
→ Usuário ou senha incorretos. Verifique no Workbench.

django.db.utils.OperationalError: (2003, "Can't connect to MySQL...")
→ O servidor MySQL não está rodando. Inicie o serviço no MySQL Workbench.

🔹 4. Migrar tabelas do Django para o MySQL
Depois de configurar o banco, execute os comandos abaixo:


python manage.py makemigrations
Se quiser rodar apenas para um app específico:


python manage.py makemigrations nome_do_app
Agora migre para o banco:


python manage.py migrate
Se tudo estiver correto, o banco de dados biblioteca no Workbench terá as tabelas do Django criadas.

🔹 5. Erro de criptografia (caso apareça)
Se houver erro relacionado a criptografia (principalmente com senhas):

pip install cryptography