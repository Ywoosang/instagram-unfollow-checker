// make variable fuction  
function $(selector: string): HTMLInputElement & HTMLElement {
    return document.querySelector(selector);
}

// DOM variables
const userId: HTMLInputElement = $('.Id');
const userPasswd: HTMLInputElement = $('.Passwd');
const idHolder: HTMLElement = $('.id-holder');
const pwHolder: HTMLElement = $('.pw-holder');
const submitBtn: HTMLElement = $('.form-submit');
const formContent: HTMLElement = $('.form-content');
const loaderContent: HTMLElement = $('.loader-atc');
const nodes: elems = document.querySelectorAll('.dot');
const doneBar: HTMLElement = $('.done-bar');
const profileArticle: HTMLElement = $('.profile');
const nextButton: HTMLElement = $('.next-btn');
const userImg = document.getElementsByClassName('user-img')[0] as HTMLImageElement;
const userName: HTMLElement = $('.pf-name');
const userPosts: HTMLElement = $('.des-content-1');
const userFollower: HTMLElement = $('.des-content-2');
const userFollowing: HTMLElement = $('.des-content-3');
const mainContent:HTMLElement = $('.main-content');  
const progressButton: HTMLButtonElement = $('.progress-btn');
const wrapper: HTMLElement = $('.content-wrapper');

// variables 
let delayTime: number; 
let count: number = 0; 
let barWidth: number = 0;
var done: boolean  = false; 

// event listeners  
progressButton.addEventListener('click', startCrawl)
submitBtn.addEventListener('click', makeProfile); 
userId.addEventListener('keyup', checkIdClass);
userPasswd.addEventListener('keyup', checkPasswdClass);
userId.addEventListener('keyup', changeBtnColor);
userPasswd.addEventListener('keyup', changeBtnColor);
userPasswd.addEventListener('keyup', showPasswd);

// interfaces   
interface elems {
    [index: number]: HTMLElement;
}
interface ProfileServerResponse {
    img: string;
    name: string;
    posts: string;
    follower: string;
    following: string;
}
interface CrawlServerResponse {
    id: string;
    name: string;
    img: string;
    link: string;
} 

// functions 

/**
* 인스타그램 로그인창 구현 
*
* hasClass 
* 해당 요소가 onInput 클래스를 포함하고 있는지 여부 반환하는 함수 
* @ param html element 
* @ return boolean 포함 여부 
* 
* checkIdClass
* 아이디 입력창에 글이 있다면 onInput,onPlaceholder 클래스 추가, 없다면 제거하는 함수 
* @ param Event 키보드 입력 이벤트 
*
* checkPasswdClass
* 비밀번호 입력창에 글이 있다면 onInput,onPlaceholder 클래스 추가, 없다면 제거하는 함수 
* @ param Event 키보드 입력 이벤트   
*  
* changeBtnColor 
* 비밀번호 6자 이상, 아이디 1자 이상 로그인 조건 만족시켰을 때, 버튼색 변경하는 함수  
*
* showPasswd 
* 비밀번호 보기 또는 숨기기를 눌렀을 때 비밀번호 표시 여부를 바꾸는 함수 
* @ param Event 클릭 이벤트 
*/  
function hasClass(element: HTMLInputElement): boolean {
    if (element.classList.contains('onInput')) {
        return true;
    }
    if (!element.classList.contains('onInput')) {
        return false;
    }
    alert('error')
}

function checkIdClass(e: Event): void {
    let target = e.target as HTMLInputElement;
    if (target.value == '' && hasClass(target)) {
        target.classList.remove('onInput');
        idHolder.classList.remove('onPlaceholder');
    }
    if (!(target.value == '') && !hasClass(target)) {
        target.classList.add('onInput');
        idHolder.classList.add('onPlaceholder');
    }
}

function checkPasswdClass(e: Event): void {
    let target = e.target as HTMLInputElement;
    if (target.value == '' && hasClass(target)) {
        target.classList.remove('onInput');
        pwHolder.classList.remove('onPlaceholder');
    }
    if (!(target.value == '') && !hasClass(target)) {
        target.classList.add('onInput');
        pwHolder.classList.add('onPlaceholder');
    }
}
function changeBtnColor(): void {
    if (userId.value.length >= 1 && userPasswd.value.length >= 6 && !submitBtn.classList.contains('onButton')) {
        submitBtn.classList.add('onButton');
    }
    if ((userId.value.length < 1 || userPasswd.value.length < 6) && submitBtn.classList.contains('onButton')) {
        submitBtn.classList.remove('onButton');
    }

} 
function showPasswd(e: Event): void {
    const target = e.target as HTMLInputElement;
    const node: HTMLElement = document.createElement('div');
    node.classList.add('show-passwd');
    node.innerHTML = '비밀번호 표시'
    node.addEventListener('click', (): void => {
        const show = (userPasswd: HTMLInputElement, node: HTMLElement): void => {
            userPasswd.type = 'password'
            node.innerHTML = '비밀번호 표시';
        }
        const hide = (userPasswd: HTMLInputElement, node: HTMLElement): void => {
            userPasswd.type = 'text';
            node.innerHTML = '숨기기';
        }
        userPasswd.type == 'password' ? hide(userPasswd, node) : show(userPasswd, node);

    })
    if (target.value.length >= 1 && target.parentNode.children.length == 2) {
        target.parentNode.appendChild(node);
    }
    if (target.value.length < 1 && target.parentNode.children.length == 3) {
        target.parentNode.removeChild(target.parentNode.lastChild);
    }
}

/**  
* 로딩시 움직이는 점 만드는 구현 
*  
*  setLoadingDot  
*/ 
setInterval(() => {
    var another: number = setLoadingDot(count);
    count = another;},500);
// 올라가는 진행바   

const setLoadingDot = (count: number): number => {
    if (count == 0) {
        nodes[count].style.fontSize = '50px'
        nodes[count].style.color = 'red'
        nodes[count + 1].style.fontSize = '40px'
        nodes[count + 1].style.color = 'green'
        nodes[count + 2].style.fontSize = '40px'
        nodes[count + 2].style.color = 'blue'
        return 1
    }
    if (count == 1) {
        nodes[count].style.fontSize = '50px'
        nodes[count].style.color = 'red'
        nodes[count + 1].style.fontSize = '40px'
        nodes[count + 1].style.color = 'green'
        nodes[count - 1].style.fontSize = '40px'
        nodes[count - 1].style.color = 'blue'
        return 2
    }
    if (count == 2) {
        nodes[count].style.fontSize = '50px'
        nodes[count].style.color = 'red'
        nodes[count - 2].style.fontSize = '40px'
        nodes[count - 2].style.color = 'green'
        nodes[count - 1].style.fontSize = '40px'
        nodes[count - 1].style.color = 'blue'
        return 0
    }
}
function progressBar(): void {
    const plusWidth = setInterval(() => {
        doneBar.style.width = barWidth.toString() + 'px';
        barWidth++;
        if(done== true || barWidth > 400){
            clearInterval(plusWidth); 
        }
    },delayTime)
}

/**
* 서버에서 로그인 시도한 사용자 이미지, 이름, 게시물수, 팔로워수, 팔로잉수 가져옴 
*/
function makeProfile(): void {
    let url = `${window.origin}/response/set`
    let data: object = {
        Id: userId.value,
        passwd: userPasswd.value
    }
    if (userId.value == '' || userPasswd.value == '') {
        alert('Id or passwd is empty ! try again')
        window.location.reload() 
        return 
    }
      // 크롤링 도중 오류 발생 혹은 사용자가 아이디,비밀번호 잘못입력  
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(data), // data can be `string` or {object}
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => {
        console.log(res.json());
        formContent.classList.add('hide');
        loaderContent.classList.remove('hide');
        const progress = setInterval(() => {
            doneBar.style.width = barWidth.toString() + 'px';
            barWidth++;
            if (barWidth > 110) {
                clearInterval(progress);
            }
        }, 150)
        requestProfile();
    })
}

/**
* requestProfile 
* 
* 
* @ exception 예외사항
*/ 

function requestProfile(): void {
    let url = `${window.origin}/response/crawl/profile`;
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then(res => {
            if(res.status == 504){ 
                window.location.reload(); 
                return 
            }
            return res.json()}
            )
        .then((response: ProfileServerResponse) => {
            const img = response.img
            const name = response.name
            const posts = response.posts
            const follower = response.follower
            const following = response.following
            userImg.src = img;
            userName.innerHTML = name;
            userPosts.innerHTML = posts;
            userFollower.innerHTML = follower;
            userFollowing.innerHTML = following;
            delayTime = Number(follower) + Number(following) ; 
            setTimeout(() => nextButton.classList.remove('hide'), 1000);
            profileArticle.classList.remove('hide');
        });

}
// 버튼 클릭하면 시작 
/**
*  startCrawl
*  
* @ param int a 메서드의 파라미터 설명
* @ return 반환하는 것 설명
* @ exception 예외사항
*/

async function startCrawl(e: Event) {
    const targetbtn = e.target as HTMLButtonElement;
    const parentNode = targetbtn.parentNode as HTMLElement;
    const stateDes = parentNode.firstChild as HTMLElement;
    parentNode.removeChild(targetbtn);
    stateDes.innerHTML = 'Collecting Data'; 
    progressBar();
    try{
        const response:CrawlServerResponse[] =  await requestCrawl();  
        console.log('완료 전',done);
        done = true; 
        console.log('완료',done);
        doneBar.classList.add('full-width'); 
        console.log(doneBar.style.width); 
        setTimeout(()=> {
        mainContent.classList.add('hide')
        makeResultDom(response); 
        },3000); 
    }catch(error){
        alert(error);
    }
}
/**
* 메서드의 기능을 설명 중이다.. 간략하게 적을 것.
* 
* @ param int a 메서드의 파라미터 설명
* @ return 반환하는 것 설명
* @ exception 예외사항
*/

 
async function requestCrawl(): Promise<CrawlServerResponse[]> {
    let url = `${window.origin}/response/crawl/unfollower`;
    let ServerData:CrawlServerResponse[]; 
    await fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then(res => {
            if(res.status == 203){
                window.location.reload(); 
            }
            return res.json(); 
        })
        .then((response: CrawlServerResponse[]) => {
            ServerData = response; 
        });
    return  ServerData; 
}
/**
* 메서드의 기능을 설명 중이다.. 간략하게 적을 것.
* 
* @ param int a 메서드의 파라미터 설명
* @ return 반환하는 것 설명
* @ exception 예외사항
*/

function makeResultDom(response: CrawlServerResponse[]) {
    const section = document.createElement('section');
    section.classList.add('resolved'); 
    console.log(response)
    // for each 로 article 생성하기 
    response.forEach((item: CrawlServerResponse) => {
        const article = makeProfileDom(item.id,item.name,item.img,item.link);
        section.appendChild(article); 
    })
    wrapper.appendChild(section); 
}

function makeProfileDom(id: string, name: string, img: string, link: string): HTMLElement {
    const article = document.createElement('article');
    article.classList.add('margin');
    article.classList.add('profile');
    const profileWrapper = document.createElement('div');
    profileWrapper.classList.add('pf-wrapper')
    //pf- left 
    const profileLeft = document.createElement('div');
    profileLeft.classList.add('pf-wrapper');
    const profileImg = document.createElement('div');
    profileImg.classList.add('pf-img')
    const userImg: HTMLImageElement = document.createElement('img');
    userImg.classList.add('user-img');
    if(img === 'notSet' || img.indexOf('448842') !== -1){
        img = '../static/img/noimg.PNG' 
        userImg.classList.add('user-no-img')
    }
    userImg.src = img; 
    profileImg.appendChild(userImg);
    profileLeft.appendChild(profileImg);
    //pf-right 
    const profileRight = document.createElement('div')
    profileRight.classList.add('pf-right');

    // 1-1 
    const profileId = document.createElement('div');
    profileId.classList.add('pf-id')
    profileId.innerText = id;
    // 1-2 
    const desWrapper = document.createElement('div');
    desWrapper.classList.add('pf-des-wrapper')
    desWrapper.classList.add('white')

    // 여기에 넣기
    const userNameWrapper = document.createElement('div');
    userNameWrapper.classList.add('pf-des');
    userNameWrapper.classList.add('uf-name');

    const userNameDes = document.createElement('div');
    userNameDes.classList.add('des-title');
    userNameDes.classList.add('bold');
    userNameDes.innerText = '이름'

    const userName = document.createElement('div');
    userName.classList.add('des-content-1');
    userName.innerText = name

    userNameWrapper.appendChild(userNameDes);
    userNameWrapper.appendChild(userName);

    // 
    const goProfileWrapper = document.createElement('div');
    goProfileWrapper.classList.add('pf-des')
    goProfileWrapper.classList.add('pf-go')
    const goProfileDes = document.createElement('div');
    goProfileDes.classList.add('pf-go-title');
    goProfileDes.classList.add('bold');
    goProfileDes.innerText = '프로필로 이동';

    const goProfileButtom = document.createElement('div');
    goProfileButtom.classList.add('pf-go-btn');
    const iconCover = document.createElement('a');
    iconCover.innerHTML = '<i class="fab fa-instagram insta-icon"></i>'
    iconCover.href = link; 
    iconCover.target ="_blank";
    goProfileButtom.appendChild(iconCover);

    goProfileWrapper.appendChild(goProfileDes);
    goProfileWrapper.appendChild(goProfileButtom);

    //pf des wrapper 
    desWrapper.appendChild(userNameWrapper);
    desWrapper.appendChild(goProfileWrapper);

    profileRight.appendChild(profileId);
    profileRight.appendChild(desWrapper);

    profileWrapper.appendChild(profileLeft);
    profileWrapper.appendChild(profileRight);

    article.appendChild(profileWrapper);

    return article; 
}