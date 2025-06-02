# CRUD de Clientes com Flask e Banco de Dados H2

Este é um projeto de aprendizado que implementa um sistema de cadastro de clientes (CRUD) utilizando:

* Python com Flask (para backend e rotas)
* HTML com Jinja2 (para frontend)
* Banco de dados H2 (utilizando JayDeBeApi para integração com Java)
* Interface simples e funcional via navegador

## Funcionalidades

* ✅ Listar clientes
* ➕ Adicionar novo cliente
* 📝 Editar cliente existente
* ❌ Excluir cliente

## Requisitos

* Python 3.8+
* Java instalado (JDK)
* Ambiente virtual configurado

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie o ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

* **Windows**:

```bash
.\venv\Scripts\activate
```

* **Linux/Mac**:

```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Baixe o arquivo `.jar` do banco de dados H2 e coloque dentro da pasta `lib`. Exemplo:

```
lib/h2-2.3.232.jar
```

## Execução

```bash
python app.py
```

Abra seu navegador em:
📍 `http://127.0.0.1:5000`

## Estrutura de Pastas

```
├── app.py
├── conexao.py
├── requirements.txt
├── lib/
│   └── h2-2.3.232.jar
├── banco/
│   └── crud_db.mv.db
├── templates/
    ├── index.html
    └── editar.html
```

## Autor

**Nelson Cristiano Santos Jucoski**
👷️ Proprietário da Nelson Cristiano Santos Jucoski
👷️ Orientado pela Prof. Karina Casola
📘️ Projeto criado como parte do curso *Jovem Programador (Senac/Palhoça/SC)*
