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
</div>

<h4 align="center">
    <img src="https://img.shields.io/coverallsCoverage/github/fga-eps-mds/2022-2-IsItKbs?color=%2340BE25&&style=for-the-badge"></img>
    <img src="https://img.shields.io/codeclimate/maintainability-percentage/fga-eps-mds/2022-2-IsItKbs?color=40BE25&style=for-the-badge"></img>
</h4>

<br>


[*Leia isso em português.*](https://github.com/fga-eps-mds/2022-2-IsItKbs)

## 📑 Summary

- [](#)
  - [📑 Summary](#-summary)
  - [🔎 Overview](#-overview)
  - [🛠 Technologies used](#-technologies-used)
  - [📝 Installation guide](#-installation-guide)
  - [⚙ Functionalities](#-functionalities)
  - [📋 Examples](#-examples)
  - [📚 Documentation](#-documentation)
  - [📁 Directories](#-directories)
  - [👨‍🔧 Want to contribute?](#-want-to-contribute?)
  - [👨‍💻 Contributors](#-contributors)
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

<li>Python3 and pip required.</li>
<li>Install our package using pip on your python terminal with the following command:</li>

```
pip install isitkbs
```
(the other necessary libraries used in this project are installed automatically with the command above)

<br>

## ⚙ Functionalities

### ***isitkbs***
```python
isitkbs(model='randomforest')
```
Instantiate the object with the desired model.

<br>

### ***wordkbs***

```python
wordkbs(input_data)
```
Analyzes a word and classifies it as keyboard smashing or normal.

<br>

### ***sentkbs***
```python
sentkbs(input_data)
```
Retorna uma lista dos keyboard smashings encontrados em uma frase.

<br>

### ***freqkbs***
```python
freqkbs(input_data, graph=False)
```
Returns a list of keyboard smashings found in a sentence.

<br>

### ***replacekbs***
```python
replacekbs(input_data, value=None, inplace=False, just_word=False)
```
Replaces keyboard smashing found in a dataframe/list/string, with a user-specified value.

<br>

*In case you want to see the details of the functions, here is the [link to our documentation](https://github.com/fga-eps-mds/2022-2-IsItKbs/blob/main/isitkbs.md).*

<br>


## 📋 Examples

### ***isitkbs***
```python
# Object instantiation
kbs = isitkbs() # Random Forest
kbs = isitkbs(model='randomforest') # Random Forest
kbs = isitkbs(model='naivebayes') # Naive Bayes
```

<br>

### ***wordkbs***
```python
kbs.wordkbs('yyyyyy')
1
```

```python
kbs.wordkbs('Hello')
0
```

<br>

### ***sentkbs***
```python
kbs.sentkbs('Hello world')
[]
```

```python
kbs.sentkbs('aspdo asocjn')
['aspdo', 'asocjn']
```

<br>

### ***freqkbs***
```python
kbs.freqkbs('aaddsffgd', graph=False)
{'a': 2, 'd': 3, 'f': 2, 'g': 1, 's': 1}
```

```python
kbs.freqkbs('aaddsffgd', graph=True)
{'a': 2, 'd': 3, 'f': 2, 'g': 1, 's': 1}
```

<img src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/freqkbs_example.png" height=200 width=300></img>

<br>

### ***replacekbs***
```python
# Creation of an example DataFrame
d = {'Example': ["The World is beautiful", "Our project detects khhyaktvb"]}
df_example = pandas.DataFrame(data=d)
```

|  Example |
|----------|
|  The World is beautiful |
| Our project detects khhyaktvb |

```python
kbs.replacekbs(df_example, value="Detected", just_word=False)
```

|  Example |
|----------|
|  The World is beautiful |
| Detected |

```python
kbs.replacekbs(df_example, value="Detected", just_word=True)
```

|  Example |
|----------|
| The World is beautiful |
| Our project detects Detected |

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

## 👨‍🔧 Want to contribute

For information on how to contribute to our project, click on this [link.](https://fga-eps-mds.github.io/2022-2-IsItKbs/projeto/contribution_guide.html)

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
