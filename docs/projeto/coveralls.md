# Coveralls

## O que é

O coveralls é um serviço que permite aos usuários rastrear a cobertura dos testes da sua aplicação ao longo do tempo com o intuito de otimizar a efetividade dos seus testes.


## Instalação do coveralls

Para utilizar o coveralls, é necessário instalá-lo no seu ambiente. Para fazê-lo, utilize o seguinte comando: 

```
pip install coveralls
```

## Setup do coveralls

Após a instalação e os testes estarem em ordem, aplique os seguintes comando para executar o teste de cobertura:

```
covarage run -m pytest
coveralls
```

Após a execução dos comandos acima, a cobertura de código dos testes é mandada para o sistema do coveralls fazer a análise.