# ![Detecting Keyboard Smashing](https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/title.png)

<div align="center">
    <img src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/logo.png" width="250"></img>
</div>

<br>

<div align="center">
    <img src="https://img.shields.io/github/issues-raw/fga-eps-mds/2022-2-IsItKbs?color=00a8f0&style=for-the-badge"></img>
    <img src="https://img.shields.io/github/issues-pr-raw/fga-eps-mds/2022-2-IsItKbs?color=00a8f0&label=open%20PRs&style=for-the-badge"></img>
    <img src="https://img.shields.io/pypi/v/isitkbs?color=00a8f0&style=for-the-badge"></img>
    <img src="https://img.shields.io/github/license/fga-eps-mds/2022-2-IsItKbs?color=00a8f0&style=for-the-badge"></img>
    <img src="https://img.shields.io/coverallsCoverage/github/fga-eps-mds/2022-2-IsItKbs?color=%2300a8f0&style=for-the-badge"></img>

</div>

<br>

<h4 align="center"> 
    <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</h4>

[Leia isso em português.](https://github.com/fga-eps-mds/2022-2-IsItKbs)

## 📑 Summary

- [](#)
  - [📑 Summary](#-sumário)
  - [🔎 Overview](#-visão-geral)
  - [🛠 Technologies used](#-tecnologias-utilizadas)
  - [📝 Installation guide](#-guia-de-instalação)
  - [⚙ Functionalities](#-funcionalidades)
    - [is_kbs(input_data, analyzer, model)](#is_kbsinput_data-analyzer-model)
  - [📋 Examples](#-exemplos)
  - [👨‍🔧 How to contribute?](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/contribution_guide.html)
  - [📚 Documentation](#-documentação)
  - [📁 Directories](#-diretórios)
  - [👨‍💻 Contributors](#-contribuidores)
  - [©Licence](#licença)
    <br>

<br>

## 🔎 Overview

<li>What is the purpose of this software?</li>
Is it KBS is a python package with functions capable of determining whether or not text entries are considered keyboard smashing, so data scientists can use the library to assist them in the process of cleaning up databases.

<br>

<li>What is keyboard smashing?</li>
Keyboard smashing is illogical and disorderly data entry, which ends up compromising textual analysis by software systems.
Ex.:
<li>yyyyyy - Is keyboard smashing.</li>
<li>aslkhfg - IS keyboard smashing.</li>
<li>hello - Is not keyboard smashing.</li>

<br>

## 🛠 Technologies used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/-NLTK-lightgrey?style=for-the-badge)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

<br>

## 📝 Installation guide

<li>Python 3 and pip required.</li>
<li>Install our package with pip in your python terminal (the other necessary libraries are installed automatically with the command below):</li>

```
pip install isitkbs
```

<br>

## ⚙ Functionalities

### is_kbs(input_data, analyzer, model)

```python
from isitkbs import *
is_kbs(input_data, analyzer, model)
```

- input_data: dados de entrada representados por uma string
- analyzer='word': análise de uma palavra (retorna positivo(1) ou negativo (0) se é keyboard smashing)
- analyzer='phrases': retorna quais palavras são keyboard smashing de uma frase de entrada
- model: modelo utilizado ('randomForest' por padrão)

<br>

For new versions, the idea is to develop features that help in the treatment of keyboard smashing in texts, databases, among others.

<br>

## 📋 Examples

```python
is_kbs('yyyyyy')
1
```

```python
is_kbs('Hello')
0
```

```python
is_kbs('Hello world', analyzer='phrases')
0
```

```python
is_kbs('aspdo asocjn', analyzer='phrases')
[['aspdo'], ['asocjn']]
```
<br>

## 📚 Documentation

* [Code of conduct](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/conduct_code.html)<br>
* [Communicational Methodology](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/metodologia_comunicacao.html)<br>
* [User story map](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/usermap_story.html)<br>
* [WorkFlow](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/workflow.html)<br>
* [RoadMap](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/roadmap.html)

<br>

## 📁 Directories

<p>/.github <- Templates for issues and pull requests.<p>
<p>/studies <- Small projects and scripts for team training.<p>
<p>/data <- Databases used in algorithm training.<p>
<p>/dist <- Compressed distributions of our package.<p>
<p>/docs <- Documentation, mainly from gitpage.<p>
<p>/isitkbs.egg-info <- Packaging information.<p>
<p>/isitkbs <- Definition of functions that will be used by users.<p>
<p>/models <- Models already trained.<p>
<p>/notebooks <- Jupyter notebooks used for feature testing.<p>
<p>/src <- Scripts for data processing, feature engineering and algorithm training.<p>
  
<br>

## 👨‍💻 Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/arthurmlv"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/arthur m.jpg" width="100px;" alt=""/><br /><sub><b>Arthur de Melo</b></sub></a><br />
    <td align="center"><a href="https://github.com/arthurgrandao"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/arthur grandao.jpg" width="100px;" alt=""/><br /><sub><b>Arthur Grandão</b></sub></a><br />
    <td align="center"><a href="https://github.com/dougAlvs"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/douglas.jpg" width="100px;" alt=""/><br /><sub><b>Douglas Alves</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
    <td align="center"><a href="https://github.com/g16c"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/gabriel.jpg" width="100px;" alt=""/><br /><sub><b>Gabriel Campello</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
    <td align="center"><a href="https://github.com/PauloVictorFS"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/paulo victor.jpg" width="100px;" alt=""/><br /><sub><b>Paulo Victor</b></sub></a><br />
    <td align="center"><a href="https://github.com/RafaelCLG0"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/rafael.jpg" width="100px;" alt=""/><br /><sub><b>Rafael Ferreira</b></sub></a><br />
    <td align="center"><a href="https://github.com/nando3d3"><img style="border-radius: 50%;" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/sidney.jpg" width="100px;" alt=""/><br /><sub><b>Sidney Fernando</b></sub></a><br /> 
  </tr>
</table>

<br>

## ©Licence

This software is licensed under the [MIT](https://github.com/nhn/tui.editor/blob/master/LICENSE) ©
