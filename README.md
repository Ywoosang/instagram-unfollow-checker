# <em> InstaChecker </em>

## 서비스 설명
아이디, 비밀번호를 입력하면 이용자의 계정을 찾습니다.  
원클릭으로 이용자 계정 언팔로워의 프로필이미지, 아이디, 이름을 제공합니다. 
언팔 프로필을 클릭하면 인스타그램 해당 계정으로 이동해 확인할 수 있습니다.  
개인정보를 별도로 저장하지 않습니다.   

![inistagram-Helper](https://user-images.githubusercontent.com/68385605/103441352-a9a38680-4c90-11eb-977b-691afee49dd4.gif)


# FrontEnd 

## npm 환경 세팅
설정 파일 생성 
```
$ npm init -y # package.json
$ tsc -init # tsconfig.json
``` 
npm install 
``` 
# TypeScript
$ npm i -D typescript

# Babel
$ npm i -D @babel/core @babel/preset-env @babel/preset-typescript

# ESLint packages
$ npm i -D eslint

# TypeScript ESLint packages
$ npm i -D @typescript-eslint/eslint-plugin @typescript-eslint/parser

#Prettier
$ npm i -D prettier eslint-plugin-prettier 
``` 
tsconfig.json
``` 
{
   "compilerOptions": {
       "allowJS" :true,  
       "target" : "ES5",   
       "outDir" :  "./built", 
       "moduleResolution" : "Node", 
       "lib" : ["ES2015","DOM","DOM.Iterable"]
   },
   "include" : ["./src/**/*"]  
}
``` 

## linting 설정
```
// .eslintrc.js  
module.exports = {
    root: true,
    env: {
        browser: true,
        node: true,
    },
    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/eslint-recommended',
        'plugin:@typescript-eslint/recommended',
    ],
    plugins: ['prettier', '@typescript-eslint'],
    rules: {
        'prettier/prettier': [
            'error',  // if conditions are not satisfied, warn or error 
            {
                endOfLine: 'auto', // to prevent Delete `cr` error 
                singleQuote: true,
                semi: true,
                useTabs: false,
                tabWidth: 4,  // tab 
                printWidth: 80,
                bracketSpacing: true,
                arrowParens: 'avoid',
            },
        ],
    },
    parserOptions: {
        parser: '@typescript-eslint/parser',
    },
};
``` 

# BackEnd 

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
Selenium 설치 
```
$ pip install selenium 
``` 
BeautifulSoup 설치
```
$ pip install beautifulsoup
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
