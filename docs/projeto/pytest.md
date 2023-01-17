<h1>Pytest</h1>

<h2>O que é?</h2>
<p>O pytest é um framework do python para realização de testes de software, sendo muito usado pela comunidade por sua flexiblidade. Em nosso projeto estamos usando-o para executar teste unitários.</p>

<h2>Como usar?</h2>
<p> A biblioteca pode ser instalada no seu ambiente da seguinte maneira: </p>

```
pip install pytest
```
<p>Para executar o pytest: </p>

```
pytest
```

<p> A biblioteca fará um scan nas pastas procurando arquivos no formato test_*.py ou *_test.py. Dentro desse arquivo, o pytest executará as funções de teste no formato test_* e retornará o resultado dos testes. </p>