#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pandera as pa
import sqlalchemy as sa
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# usando as inicias da palavra DataFrame foi criada uma variavel para que possa receber a função read que irá ler o arquivo desejado.
# 
# Dentro da variavel ainda carescentamos parametros para melhorar a extração:
# -ecoding = 'UTF-8' para informar ao sistema que estamos usando caracteres especiais para que possa ser reconhecido; 
# -sep ="," para informar que o nosso arquivo está separado por virgulas; 
# -parse_data = [nome das colunas] para transformar essas colunas que antes eram objetos em formato de data;
# -dateFirst = True, o sistema de data no arquivo está yy/mm/dd e quando usamos o parse_data transforma o objeto em yy/dd/mm, então para corrigir esse impasse, usamos essa função para que possa deixar o dia antes do mês e ano.

# In[24]:


df = pd.read_csv(
    "C:\\Users\\User\\Desktop\\soulcode\\Atividade0-Py\\Atividade17\\modules\\beneficios-assistencia-estudantil-jan-jun-2021-proaes-ufpe.csv", encoding="UTF-8",sep=",", parse_dates=["DATA_INICIO","DATA_FIM","MES_REFERENCIA"], dayfirst = True)


# Para excluir as possiveis linhas duplicadas, usei a função drop_duplicates () da biblioteca pandas

# In[25]:


df.drop_duplicates(inplace = True)


# Criei uma variavel schema que servirá para receber as validações que queremos do nosso arquivo. Usando a função pa.DataFrameSchema colocamos nele o nome das colunas e o que esperamos dela, como tipo do dado, tamanho e se poderá receber valores nulos ou não. Caso o arquivo esteja de acordo com o que pedi, a validação rodará, caso não apresentará um erro informando o motivo.

# In[26]:


schema = pa.DataFrameSchema(
    columns={
        "NU_MATRICULA": pa.Column(pa.Int),
        "TIPO_BOLSA": pa.Column(pa.String, pa.Check.str_length(10,70)),
        "ID_UNIDADE": pa.Column(pa.Int),
        "NOME_UNIDADE": pa.Column(pa.String, pa.Check.str_length(10,70)),
        "DATA_INICIO": pa.Column(pa.DateTime),
        "DATA_FIM": pa.Column(pa.DateTime, nullable = True),
        "VALOR_BOLSA": pa.Column(pa.Int),
        "MES_REFERENCIA": pa.Column(pa.DateTime)
    }
)


# Validei o schema

# In[27]:


schema.validate(df)


# In[28]:


df.dtypes


# Para saber quantos dados tem em cada coluna podemos usar a função count()

# In[29]:


df.count()


# 

# Fiz um filtro pra ver quais tabelas tem valores nulos

# In[30]:


filtro = df.DATA_INICIO.isnull()
print(filtro)


# In[31]:


filtro2 = df.DATA_FIM.isnull()
print(filtro2)


# Vou filtrar quais as unidades que receberam "AUXÍLIO EMERGENCIAL COVID19 VINC. NÍVEIS"

# In[32]:


filtro3 = df.TIPO_BOLSA == "AUXÍLIO EMERGENCIAL COVID19 VINC. NÍVEIS"
df.loc[filtro3,["TIPO_BOLSA"]]


# Vou filtrar quem recebeu a "BOLSA RECIFE NÍVEL 4" na data de "2019-07-08"

# In[33]:


filtro4 = df.TIPO_BOLSA == "BOLSA RECIFE NÍVEL 4"
filtro5 = df.DATA_INICIO == "2019-07-08"
df.loc[filtro4 & filtro5]


# Filtrar os beneficios dados no mês de agosto

# In[34]:


filtro6 = df.DATA_INICIO.dt.month == 8
df.loc[filtro4 & filtro6]


# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




