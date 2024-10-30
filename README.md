# Khiata Repository
**Conectando costureiras e clientes**  
Um repositório completo para o desenvolvimento, documentação e análise do **Khiata**, aplicativo voltado a facilitar o encontro entre costureiras e pessoas interessadas em seus produtos.

Este repositório reúne todos os arquivos e documentos necessários para gerenciar dados, desenvolver funcionalidades de IA, criar dashboards de monitoramento, e fornecer uma base robusta para a aplicação **Khiata**.

---

## 📑 Índice

- [Descrição do Projeto](#📝-descrição-do-projeto)
- [Estrutura do Repositório](#📁-estrutura-do-repositório)
- [Pré-requisitos](#✅-pré-requisitos)
- [Instruções de Uso](#🚀-instruções-de-uso)
- [Documentação](#📚-documentação)

---

## 📝 Descrição do Projeto

O **Khiata** é um aplicativo inovador que facilita o encontro entre costureiras e pessoas que procuram produtos feitos sob medida. Este repositório centraliza scripts de dados, dashboards de monitoramento e análise, e módulos de IA, apoiando o desenvolvimento e a manutenção do app.

---

## 📁 Estrutura do Repositório

Para melhor organização, os arquivos e diretórios são estruturados da seguinte forma:

### `/scripts`
Scripts de dados e consultas em SQL, MongoDB, e Redis:

- **`sql/`** - Scripts SQL
- **`mongo/`** - Scripts MongoDB
- **`redis/`** - Scripts Redis

### `/dashboards`
Dashboards e relatórios sobre o aplicativo:

- **`reports/`** - Arquivos com análises e as bases utilizadas para a criação dos dashboards
- **`visuals/`** - Arquivos no formato .pbix

### `/python`
Scripts Python relacionados à Inteligência Artificial:

- **`model/`** - Modelo de IA e aprendizado de máquina.
- **`notebooks/`** - Notebooks Jupyter com análises.
- **`utils/`** - Scripts de pré-processamento de dados e as bases utilizadas.

### `/docs`
Documentação completa sobre o app e as tecnologias usadas:

- **`database/`** - Descrição das estruturas de dados e modelos relacionais e não relacionais.
- **`AI/`** - Detalhes sobre os modelos de IA.

---

## ✅ Pré-requisitos

Para clonar e utilizar este repositório, você precisará de:

- **Python 3.8+**
- **MongoDB, Redis e PostgreSQL**
- Bibliotecas Python para IA e visualizações:

  ```bash
  pip install -r requirements.txt
  ```

---

## 🚀 Instruções de Uso

1. **Clone o Repositório:**
   ```bash
   https://github.com/Ovetoreti/Khiata_Dados.git
   ```

2. **Configuração do Banco de Dados:**
   - Configure as conexões e os scripts iniciais dentro da pasta `/scripts`.

3. **Executar Análises com IA:**
   - Navegue até a pasta `/python/models` para treinar ou usar os modelos.

4. **Visualização de Dashboards:**
   - Dashboards e visualizações estão localizados em `/dashboards/reports`.

---

## 📚 Documentação

A documentação detalhada do **Khiata** pode ser encontrada na pasta **`/docs`**, com orientações para desenvolvedores sobre:

- Modelos de dados em SQL, MongoDB e Redis
- Arquitetura de IA
- Estrutura de dashboards e relatórios

---