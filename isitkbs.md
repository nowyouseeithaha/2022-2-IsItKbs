# Pacote

## Módulo ks


### _class_ isitkbs.ks.isitkbs(model='randomforest')


#### freqkbs(input_data, graph=False)
Conta a frequência das letras que formam os keyboard smashings identificados em input_data e as retorna como um dicionário, caso graph=True também plota o gráfico correspondente.


* **Parâmetros**

    
    * **input_data** (*string ou lista*) – Dado de entrada


    * **graph** (*bool**, **opcional*) – Caso ‘True’ plota o gráfico de frequência, caso contrário não, default=False



* **Retorna**

    Um dicionário em que as chaves são as letras que formam os keyboard smashings presentes em input_data e os valores são a quantidade de vezes em que elas aparecem.



* **Tipo de retorno**

    dicionário



#### replacekbs(input_data, value=None, inplace=False, just_word=False)
Identifica os keyboard smashings em uma lista, string ou pd.DataFrame input_data e os substitui pelo valor de value, caso value seja vazio os keyboard smashings
são deletados. Caso input_data seja um dataframe e just_word=False substitui toda a linha em que o keyboard smashing estiver presente


* **Parâmetros**

    
    * **input_data** (*string ou lista ou pd.DataFrame*) – Dados de entrada.


    * **value** (*string**, **opcional*) – Valor pelo qual os keyboard smashings serão substituídos, caso vazio os mashings são apagados, default=None


    * **inplace** (*bool**, **opcional*) – Só faz efeito caso input_data seja um pd.DataFrame. Caso ‘True’ a substituição ocorre diretamente no dataframe, caso contrário é criada uma cópia dele, default=False


    * **just_word** (*bool**, **opcional*) – Caso ‘True’ somente o keyboard smashing é substituído, caso contrário toda a linha do dataframe ou string da lista em que ele está inserido é substituída, default=False



* **Retorna**

    Uma cópia de input_data com os keyboard smashings identificados substituídos pelo valor passado no parâmetro value. Caso input_data seja um pd.DataFrame e o parâmetro inplace=True o retorno é nulo, pois as substituições são feitas inplace.



* **Tipo de retorno**

    string ou lista ou pd.DataFrame



#### sentkbs(input_data)
Verifica se input_data apresenta algum keyboard smashing, e caso apresente, retorna a lista de mashings.


* **Parâmetros**

    **input_data** (*string ou lista*) – Dado de entrada



* **Retorna**

    Uma lista com os keyboard smashings que foram identificados em input_data



* **Tipo de retorno**

    lista



#### wordkbs(input_data)
Verifica se a string input_data apresenta algum keyboard smashing ou não. Se input_data for uma única palavra
a função retorna se essa palavra é ou não keyboard smashing. Já no caso de input_data ser uma frase, a função retorna se essa frase
apresenta algum keyboard smashing ou não.


* **Parâmetros**

    **input_data** (*string*) – Dado de entrada



* **Levanta**

    **TypeError** – Se a entrada não for uma string esse erro é lançado



* **Retorna**

    1 se input_data é um keyboard smashing, 0 caso contrário



* **Tipo de retorno**

    int



### _class_ isitkbs.ks.lex_extractor()

Classe auxiliar da isitkbs para extração de features lexicais.


#### _classmethod_ bigram_counter(lista)
Função auxiliar da bigrams que conta a quantidade de cada bigrama em uma lista e retorna um dicionário em que os bigramas são as chaves e sua quantidade na lista de entrada os valores


* **Parâmetros**

    **lista** (*lista*) – Lista com os bigramas.



* **Retorna**

    Dicionário em que os bigramas são as chaves e sua quantidade na lista de entrdada os valores



* **Tipo de retorno**

    dicionário



#### _classmethod_ bigram_max_occurance(string)
Dada uma string de entrada retorna qual a quantidade máxima de ocorrência de um mesmo bigrama


* **Parâmetros**

    **string** (*string*) – String da qual os bigramas serão extraídos.



* **Retorna**

    Quantidade máxima de ocorrência de um mesmo bigrama



* **Tipo de retorno**

    int



#### _classmethod_ bigrams(string)
Dada uma string de entrada retorna um dicionário em que seus bigramas são as chaves e sua quantidade os valores


* **Parâmetros**

    **string** (*string*) – String da qual os bigramas serão extraídos.



* **Retorna**

    Dicionário em que os bigramas são as chaves e sua quantidade na lista de entrdada os valores



* **Tipo de retorno**

    dicionário



#### _classmethod_ letter_counter(string, type)
Conta a quantidade de cada vogal ou consoante em uma string de entrada.


* **Parâmetros**

    
    * **string** (*string*) – String da qual será feita a contagem das letras.


    * **type** (*string*) – {‘v’, ‘c’}, Se serão contadas as vogais ou consoantes



* **Retorna**

    Um dicionário em que as letras sãos as chaves e os valores são sua quantidade em string



* **Tipo de retorno**

    dicionário



#### _classmethod_ ttr(string)
Calcula o TypeTokenRatio (TTR) de uma string de entrada. O TTR é a quantidade de carácteres únicos divididade pelo tamanho total da string


* **Parâmetros**

    **string** (*string*) – String da qual será realizado o cálculo do TTR.



* **Retorna**

    TypeTokenRatio (TTR) da string de entrada



* **Tipo de retorno**

    float



#### _classmethod_ type_counter(string, type)
Conta a quantidade total de vogais ou consoantes em uma string de entrada.


* **Parâmetros**

    
    * **string** (*string*) – String da qual será feita a contagem das letras.


    * **type** (*string*) – {‘v’, ‘c’}, Se serão contadas as vogais ou consoantes



* **Retorna**

    A soma da quantidade total de vogais ou de consoantes da palavra



* **Tipo de retorno**

    int



#### _classmethod_ type_ratio(string, type)
Cálcula a proporção de vogais ou consoantes em uma string de entrada.


* **Parâmetros**

    
    * **string** (*string*) – String da qual será feito o cálculo.


    * **type** (*string*) – {‘v’, ‘c’}, Se a propoção cálculada será de vogais ou consoantes



* **Retorna**

    Proporção de vogais ou consoantes na palavra



* **Tipo de retorno**

    float
