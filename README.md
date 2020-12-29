# Instagram_Webcrawling

## python 환경 세팅
가상환경 생성
```
$python3 -m venv venv
$ py -3 -m venv venv 
``` 
가상환경 활성화 
```
$ . venv/bin/activate 
# windows 
$ venv/Scripts/activate 
```  
Flask 설치
```
$ pip install Flask 
```
 

## npm 환경 세팅
설정 파일 생성 
```
$ npm init -y # package.json
$ tsc -init # tsconfig.json
``` 
linting tool 및 패키지 설치
```
package.json  
``` 
...생략
 "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "lint": "eslint src/**/*.ts",
    "lint:fix": "eslint --fix src/**/*.ts"
  },
...생략 

```
# TypeScript
$ npm i -D typescript

# ESLint packages
$ npm i -D eslint eslint-config-airbnb-base eslint-plugin-import

# TypeScript ESLint packages
$ npm i -D @typescript-eslint/eslint-plugin @typescript-eslint/parser
``` 

## 서버 띄우기
```
# Bash 
$ export FLASK_ENV=development
$ flask run

# CMD
> set FLASK_ENV=development
> flask run

#Powershell
> $env:FLASK_ENV = "development"
> flask run 
``` 
