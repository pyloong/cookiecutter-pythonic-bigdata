# 使用说明

项目使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 编写，用于自动生成预编写好的项目模板。在使用时，通过交互
输入参数，控制生成逻辑，以达到一定的自定义化，方便更多场景组合使用。使用项目模板生成项目目录，极大程度减少了在项目开始时搭建项目环境的繁琐
步骤，既可以减少编写或复制重复代码，又能避免节省时间。

## 安装依赖

项目模板使用了新的 [PEP-517](https://www.python.org/dev/peps/pep-0517/) 打包规范，所以需要使用更新版本的 pip 。

将 pip 升级到最新版本：

```shell
pip install -U pip
```

安装 [Cookiecutter](https://pypi.org/project/cookiecutter/) :

```shell
pip install -U cookiecutter
```

为了更方便的使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) ，推荐在系统环境下或者当前用户环境下安装，而不是
在虚拟环境中安装。

## 生成项目模板

在项目生成目录运行如下命令：

```shell
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
```

这是使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 读取放在 Github 上的项目模板。
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) 会首先找到 `cookiecutter.json` 文件，读取其中的
配置，并开启交互提示。

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
```

在使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 时，会将项目模板下载到本地作为缓存。如果不是第一次使用，
且项目木板有更新时，建议根据提示重新下载项目模板。如果不需要可以跳过，使用上次下载的缓存记录生成项目。

### 项目名称(project_name)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
```

在运行交互时，首先需要输入一个项目名，请输入合法的项目名。

项目名遵循：

- 只能以 `_` 、 `a-z` 和 `A-Z` 开头
- 只能包含 `_` 、 `a-z` 和 `A-Z`
- 输入的前后空格会被删除
- 中间的空格、 `-` 和 `.` 都会被替换成 `_`
- 所有大写字符都会转换成小写字母

即将输入转换成 Python 的蛇形命名法。

### 项目包名称(project_slug)

输入的项目名称会在转换和检查后作为合法的 Python 包名称。

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]:
```

可以直接回车使用自动生成的包名称。或者手动输入想要的包名称。

### 项目描述(project_description)

输入项目描述文字，此参数暂时没有显示，你可以输入一段描述项目功能的文字。输入时不能换行，如果使用回车，则会直接进入下一个参数的提示。

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
```

### 项目作者(author_name)

```text
author_name [Author]: ming
```

### 作者邮箱(author_email)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
```

### 项目版本(version)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]:
```

输入合法的项目版本号。

[PEP-440](https://www.python.org/dev/peps/pep-0440/) 中规范了符合 Python 规范的版本号。也可以使用较为通用的
[语义化版本 2.0](https://semver.org/lang/zh-CN/) 中规定的版本号写法。

### Python 版本(python_version)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]:
Select python_version:
1 - 3.10
2 - 3.9
Choose from 1, 2 [1]:
```

选择使用的 Python 版本。建议使用 `Python 3.10` 。

### 使用 SRC 目录结构(use_src_layout)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]:
Select python_version:
1 - 3.10
2 - 3.9
Choose from 1, 2 [1]: 
use_src_layout [y]: 
```

选择是否使用 SRC 目录结构。

如果使用 SRC 目录结构，在项目根目录会有一个 `src` 的目录， Python 包在 `src` 下。这种结构方便一个项目包含多个包。

如果不使用 SRC ，则项目的包直接放在项目根目录。

更多关于 Python 目录结构的内容可以阅读[项目结构](https://pyloong.github.io/pythonic-project-guidelines/guidelines/project_structure/)。

### 使用 Poetry (use_poetry)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]:
Select python_version:
1 - 3.10
2 - 3.9
Choose from 1, 2 [1]: 
use_src_layout [y]: 
use_poetry [y]: 
use_framework[]:
1 - none
2 - pyspark
Choose from 1, 2 [1]: 
```

选择是否使用 [Poetry](https://python-poetry.org/) 作为虚拟环境管理工具。默认情况下是推荐使用的，
[Poetry](https://python-poetry.org/) 是虚拟环境管理工具中的新起之秀，同时包含了打包和发布功能，使用
`pyprojrct.toml` 管理元数据，减少大量配置文件。

如果不使用，则直接生成一个 `requirements.txt` 文件，也会包含所需要的依赖。

### 使用 Docker(use_docker)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
Select python_version:
1 - 3.10
2 - 3.9
Choose from 1, 2 [1]: 
use_src_layout [y]: 
use_poetry [y]: 
use_docker [n]: 
```

选择是否使用 Docker 。默认不使用。

如果选择使用，会在项目中生成简单的 `Dockerfile` 和 `.dockerignoer` 文件。

### CI 工具(ci_tools)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project-bigdata-etl
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]:
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]:
author_email [author@example.com]:
version [0.1.0]:
Select python_version:
1 - 3.10
2 - 3.9
Choose from 1, 2 [1]:
use_src_layout [y]:
use_poetry [y]:
use_docker [n]:
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]:
```

选择使用的 CI 工具，可选的有 `Gitlab` 和 `Github` 。如果选择一个 CI 工具，默认会生成项目的测试、构建、发布到索引服务器的三步操作。

## 使用生成后的项目

当上面的所有步骤操作完成后，就会在当前目录生成一个 Python 项目，其目录结构如下：

```text

hello_world
│ .gitignore
│ LICENSE
│ pyproject.toml
│ README.md
│ tox.ini
│
├─src
│  │  __init__.py
│  │
│  └─pyspark_etl_template
│     │  cmdline.py
│     │  executor.py
│     │  constants.py
│     │  __init__.py
│     │
│     ├─configs
│     │  │  dev.toml
│     │  │  global.toml
│     │  │  prod.toml
│     │  └─ test.toml
│     │
│     ├─dependecies
│     │  │  log.py
│     │  │  config.py
│     │  │  spark.py
│     │  └─ __init__.py
│     │
│     ├─tasks
│     │  │  __init__.py
│     │  │
│     │  └─abstract
│     │     │  task.py
│     │     │  transform.py
│     │     └─ __init__.py
│     │
│     └─utils
│        │  exception.py
│        └─ __init__.py
|
├─tests
|   │  conftest.py
|   │  test_version.py
|   └─ __init__.py
|   
└─docs
    └─ development.md
```

在项目根目录，包含了一些描述性的文件：

- `LICENSE` ： 项目的许可证
- `pyproject.toml` ：由 [Poetry](https://python-poetry.org/) 生成的带有 [Poetry](https://python-poetry.org/) 配置的项目描述文件。
- `README.md` ：项目自述文件
- `tox.ini` ：自动化测试工具 [Tox](https://tox.readthedocs.io/en/latest/) 的配置文件。

还有一些目录：

- `docs` ：文档目录，用来记录开发和使用时的文档
- `src` ：使用了 SRC 目录结构生成目录，用来放置项目的包
- `tests` ：测试目录，用来放置对 `src` 下面的包做测试的目录。

## 使用项目

项目模板生成后，默认会在的当前目录生成一个可用的 Python 项目。

Python 项目开发时，强烈建议使用虚拟环境管理 Python 项目的依赖。在前面生成项目模板是，会默认使用 [Poetry](https://python-poetry.org/)
作为虚拟环境管理工具。当然你可以不使用 [Poetry](https://python-poetry.org/) ，选择更常见的 [Virtualenv](https://github.com/pypa/virtualenv) 。

后续步骤都假设你已经了解 [Poetry](https://python-poetry.org/) 并使用 [Poetry](https://python-poetry.org/) 。

如果没有安装 [Poetry](https://python-poetry.org/) ，可以使用 pip 命令安装。为了方便使用，推荐在系统环境下或者当前用户环境下安装 。

```bash
## 升级 pip
pip install -U pip
pip install -U poetry

## 进入项目目录
cd  hello_world

## 创建虚拟环境，并安装依赖
poetry install

## 进入虚拟环境
poetry shell
```

为了减少开发过程中遇到模板本身错误导致开发异常的情况，在开发前首先运行一遍自动化测试，直接执行 `tox` 命令。

<!-- markdownlint-disable MD013 MD033-->
```text
.package create: D:\GitHub\hello_world\.tox\.package
.package installdeps: poetry-core>=1.0.0
py310 create: D:\GitHub\hello_world\.tox\py310
py310 installdeps: poetry
py310 inst: D:\GitHub\hello_world\.tox\.tmp\package\1\hello_world-0.1.0.tar.gz
py310 installed: attrs==22.1.0,CacheControl==0.12.11,cachy==0.3.0,certifi==2022.9.14,charset-normalizer==2.1.1,cleo==1.0.0a5,click==8.1.3,colorama==0.4.5,crashtest==0.3.1,distlib==0.3.6,dulwich==0.20.46,dynaconf==3.1.9,filelock==3.8.0,hello-world @ file:///D:/GitHub/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz,html5lib==1.1,idna==3.4,jaraco.classes==3.2.2,jsonschema==4.16.0,keyring==23.9.1,lockfile==0.12.2,more-itertools==8.14.0,msgpack==1.0.4,packaging==21.3,pbr==5.10.0,pexpect==4.8.0,pkginfo==1.8.3,platformdirs==2.5.2,poetry==1.2.0,poetry-core==1.1.0,poetry-plugin-export==1.0.6,ptyprocess==0.7.0,py4j==0.10.9.5,pylev==1.4.0,pyparsing==3.0.9,pyrsistent==0.18.1,pyspark==3.3.0,pywin32-ctypes==0.2.0,requests==2.28.1,requests-toolbelt==0.9.1,shellingham==1.5.0,six==1.16.0,stevedore==4.0.0,tomlkit==0.11.4,urllib3==1.26.12,virtualenv==20.16.5,webencodings==0.5.1
py310 run-test-pre: PYTHONHASHSEED='461'
py310 run-test: commands[0] | poetry install -v
Using virtualenv: D:\GitHub\hello_world\.tox\py310
Installing dependencies from lock file

Finding the necessary packages for the current system

Package operations: 28 installs, 0 updates, 0 removals, 13 skipped

  • Installing markupsafe (2.1.1)
  • Installing python-dateutil (2.8.2)
  • Installing pyyaml (6.0)
  • Installing zipp (3.8.1)
  • Installing ghp-import (2.1.0)
  • Installing importlib-metadata (4.12.0)
  • Installing jinja2 (3.1.2)
  • Installing mergedeep (1.3.4)
  • Installing markdown (3.3.7)
  • Installing watchdog (2.1.9)
  • Installing wrapt (1.14.1)
  • Installing pyyaml-env-tag (0.1)
  • Installing lazy-object-proxy (1.7.1)
  • Installing astroid (2.12.9)
  • Installing dill (0.3.5.1)
  • Installing iniconfig (1.1.1)
  • Installing mkdocs (1.3.1)
  • Installing isort (5.10.1)
  • Installing pluggy (1.0.0)
  • Installing pymdown-extensions (9.5)
  • Installing mccabe (0.7.0)
  • Installing mkdocs-material-extensions (1.0.3)
  • Installing pygments (2.13.0)
  • Installing tomli (2.0.1)
  • Installing py (1.11.0)
  • Installing attrs (22.1.0): Skipped for the following reason: Already installed
  • Installing click (8.1.3): Skipped for the following reason: Already installed
  • Installing colorama (0.4.5): Skipped for the following reason: Already installed
  • Installing dynaconf (3.1.9): Skipped for the following reason: Already installed
  • Installing mkdocs-material (8.4.4)
  • Installing packaging (21.3): Skipped for the following reason: Already installed
  • Installing pytest (7.1.3)
  • Installing platformdirs (2.5.2): Skipped for the following reason: Already installed
  • Installing py4j (0.10.9.5): Skipped for the following reason: Already installed
  • Installing pyspark (3.3.0): Skipped for the following reason: Already installed
  • Installing stevedore (4.0.0): Skipped for the following reason: Already installed
  • Installing pyparsing (3.0.9): Skipped for the following reason: Already installed
  • Installing tomlkit (0.11.4): Skipped for the following reason: Already installed
  • Installing six (1.16.0): Skipped for the following reason: Already installed
  • Installing pylint (2.15.2)
  • Installing pbr (5.10.0): Skipped for the following reason: Already installed

Installing the current project: hello_world (0.1.0)
py310 run-test: commands[1] | poetry run pytest tests
================================================= test session starts =================================================
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0
cachedir: .tox\py310\.pytest_cache
rootdir: D:\GitHub\hello_world
collected 1 item

tests\test_version.py .                                                                                          [100%]

================================================== 1 passed in 0.01s ==================================================
isort create: D:\GitHub\hello_world\.tox\isort
isort installdeps: isort
isort inst: D:\GitHub\hello_world\.tox\.tmp\package\1\hello_world-0.1.0.tar.gz
isort installed: click==8.1.3,colorama==0.4.5,dynaconf==3.1.9,hello-world @ file:///D:/GitHub/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz,isort==5.10.1,pbr==5.10.0,py4j==0.10.9.5,pyspark==3.3.0,stevedore==4.0.0
isort run-test-pre: PYTHONHASHSEED='461'
isort run-test: commands[0] | isort . --check-only --diff
Skipped 1 files
pylint create: D:\GitHub\hello_world\.tox\pylint
pylint installdeps: poetry
pylint inst: D:\GitHub\hello_world\.tox\.tmp\package\1\hello_world-0.1.0.tar.gz
pylint installed: attrs==22.1.0,CacheControl==0.12.11,cachy==0.3.0,certifi==2022.9.14,charset-normalizer==2.1.1,cleo==1.0.0a5,click==8.1.3,colorama==0.4.5,crashtest==0.3.1,distlib==0.3.6,dulwich==0.20.46,dynaconf==3.1.9,filelock==3.8.0,hello-world @ file:///D:/GitHub/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz,html5lib==1.1,idna==3.4,jaraco.classes==3.2.2,jsonschema==4.16.0,keyring==23.9.1,lockfile==0.12.2,more-itertools==8.14.0,msgpack==1.0.4,packaging==21.3,pbr==5.10.0,pexpect==4.8.0,pkginfo==1.8.3,platformdirs==2.5.2,poetry==1.2.0,poetry-core==1.1.0,poetry-plugin-export==1.0.6,ptyprocess==0.7.0,py4j==0.10.9.5,pylev==1.4.0,pyparsing==3.0.9,pyrsistent==0.18.1,pyspark==3.3.0,pywin32-ctypes==0.2.0,requests==2.28.1,requests-toolbelt==0.9.1,shellingham==1.5.0,six==1.16.0,stevedore==4.0.0,tomlkit==0.11.4,urllib3==1.26.12,virtualenv==20.16.5,webencodings==0.5.1
pylint run-test-pre: PYTHONHASHSEED='461'
pylint run-test: commands[0] | poetry install -v
Using virtualenv: D:\GitHub\hello_world\.tox\pylint
Installing dependencies from lock file

Finding the necessary packages for the current system

Package operations: 28 installs, 0 updates, 0 removals, 13 skipped

  • Installing markupsafe (2.1.1)
  • Installing python-dateutil (2.8.2)
  • Installing pyyaml (6.0)
  • Installing zipp (3.8.1)
  • Installing ghp-import (2.1.0)
  • Installing importlib-metadata (4.12.0)
  • Installing jinja2 (3.1.2)
  • Installing mergedeep (1.3.4)
  • Installing pyyaml-env-tag (0.1)
  • Installing lazy-object-proxy (1.7.1)
  • Installing watchdog (2.1.9)
  • Installing wrapt (1.14.1)
  • Installing markdown (3.3.7)
  • Installing astroid (2.12.9)
  • Installing dill (0.3.5.1)
  • Installing isort (5.10.1)
  • Installing mkdocs (1.3.1)
  • Installing pluggy (1.0.0)
  • Installing pygments (2.13.0)
  • Installing tomli (2.0.1)
  • Installing mccabe (0.7.0)
  • Installing mkdocs-material-extensions (1.0.3)
  • Installing iniconfig (1.1.1)
  • Installing pymdown-extensions (9.5)
  • Installing py (1.11.0)
  • Installing attrs (22.1.0): Skipped for the following reason: Already installed
  • Installing click (8.1.3): Skipped for the following reason: Already installed
  • Installing colorama (0.4.5): Skipped for the following reason: Already installed
  • Installing dynaconf (3.1.9): Skipped for the following reason: Already installed
  • Installing py4j (0.10.9.5): Skipped for the following reason: Already installed
  • Installing pyparsing (3.0.9): Skipped for the following reason: Already installed
  • Installing pytest (7.1.3)
  • Installing stevedore (4.0.0): Skipped for the following reason: Already installed
  • Installing mkdocs-material (8.4.4)
  • Installing pyspark (3.3.0): Skipped for the following reason: Already installed
  • Installing platformdirs (2.5.2): Skipped for the following reason: Already installed
  • Installing packaging (21.3): Skipped for the following reason: Already installed
  • Installing tomlkit (0.11.4): Skipped for the following reason: Already installed
  • Installing six (1.16.0): Skipped for the following reason: Already installed
  • Installing pylint (2.15.2)
  • Installing pbr (5.10.0): Skipped for the following reason: Already installed

Installing the current project: hello_world (0.1.0)
pylint run-test: commands[1] | poetry run pylint tests src

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.37/10, +1.63)

_______________________________________________________ summary _______________________________________________________
  py310: commands succeeded
  isort: commands succeeded
  pylint: commands succeeded
  congratulations :)
```
<!-- markdownlint-restore -->

可以看到 tox 做了如下事情：

- 执行了 `py310` 的测试，
- [isort](https://pycqa.github.io/isort/) 的包导入检查，
- [pylint](https://www.pylint.org/) 的 Python 语法规范检查。

当所有检查都正常时， Tox 的自动化逻辑才会正常通过，否则会报出异常，此时你需要根据提示调整代码，并再次运行，直到全部通过。

如果你讨厌这些繁琐的检查，也可以修改 `tox.ini` 文件，删除不喜欢的配置，或者不运行 `tox` 。但是并不推荐你这么做。因为良好的编码习惯
是一个优秀的开发人员最基本的要求。
