const dataSvg = [
    { regionId: 'hrodnenskaia-voblasts', desc: 'Гродненская область — самая маленькая по площади и населению в Беларуси. Впрочем, достопримечательностей здесь немало — отнюдь, многие экскурсии показывают, насколько богат региона потрясающими замками, дворцами, храмами и природными изюминками, порой уникальными для всей Европы.', title: 'Гродненская область' },
    { regionId: 'vitsebskaia-voblasts', desc: 'Богата интересными и уникальными местами Витебская область, что в Республике Беларусь. Древние города, старинные костёлы и живописные озёра — эти достопримечательности привлекают туристов из разных уголков мира. Путешествие по этому удивительному краю будет насыщенным, а отдых разнообразным.', title: 'Витебеская область' },
    { regionId: 'mahiliouskaia-voblasts', desc: 'Каждого может удивить достопримечательностями Могилев – древний белорусский город на берегах могучего Днепра, отражение богатой истории народа Республики Беларусь. Побывав в Могилеве, каждый проникнется любовью к этой прекрасной нации, ее ратным подвигам и удивительной культуре.', title: 'Могилёвская область' },
    { regionId: 'homelskaia-voblasts', desc: 'Гомельская область — самый крупный по площади регион Республики Беларусь, который к тому же является еще и самым южным, гранича на юге с Украиной, а на востоке с Россией (Брянская область). Территория ее была заселена давно, но главные достопримечательности появились здесь значительно позже. Впрочем, природных красот на Гомельщине тоже немало.', title: 'Гомельская область' },
    { regionId: 'minskaia-voblasts', desc: 'Минская область — столичная для Беларуси, ведь здесь располагается столица Республики, город Минск. Но не им одним славится регион. Кроме мегаполиса, здесь немало других городов и поселков, на территории которых встречаются порой куда более интересные и колоритные достопримечательности.', title: 'Минская область' },
    { regionId: 'brestskaia-voblasts', desc: 'Брестская область — наверное, один из самых героических регионов Республики Беларусь, в первую очередь за счет расположенной в Бресте, областном центре Крепости, которая является одной из самых известных достопримечательностей страны. Впрочем, здесь есть и другие, не менее интересные места, которые обязательно стоит увидеть.', title: 'Бресткая область' }
]

// const btnAuthWindow = document.getElementById('btnAuthWindow');
// const authWindow = document.getElementById('authWindow');
// const toRegister = document.getElementById('toRegister');
// const toLogin = document.getElementById('toLogin');
const descSvg = document.getElementById('descSvg')
const regions = document.querySelectorAll('.region');
const scrollBtns = document.querySelectorAll('#scrollBtn');
const sections = document.querySelectorAll('#imgSection');
const scrollUp = document.getElementById('scrollUp');
const header = document.getElementById('header')




// if(btnAuthWindow){btnAuthWindow.addEventListener('click', openAuthWindow)};
// if(authWindow){authWindow.addEventListener('click', closeAuthWindow)};
// if(toRegister){toRegister.addEventListener('click', registerWindow)};
// if(toLogin){toLogin.addEventListener('click', loginWindow)};
if(scrollUp){scrollUp.addEventListener('click', funcScrollUp)};

function funcScrollUp(){
    const headerCoord = document.getElementById('header').getBoundingClientRect().y
    window.scrollBy(0, headerCoord)
}

if (scrollUp) {
    window.addEventListener('scroll', () =>{
        if(window.pageYOffset + header.getBoundingClientRect().top < window.pageYOffset){
            scrollUp.style.display = "block"
        }else{
            scrollUp.style.display = "none"
        }
    })  
}



scrollBtns.forEach((el, index) =>{
    el.addEventListener('click', () =>{
      for (let i = 0; i < sections.length; i++) {
       if(i === index){
          const coord = sections[i].getBoundingClientRect().y
          window.scrollBy(0, coord)
        }    
      };
    })
});

regions.forEach(el => {
    el.addEventListener('mouseenter', () => {
        const dataRegion = dataSvg.find((elem) => elem.regionId == el.id)
        descSvg.style.opacity = 1
        descSvg.children[0].innerText = `${dataRegion.title}`
        descSvg.children[1].innerText = `${dataRegion.desc}`
    })

    el.addEventListener('mouseleave', () => {
        descSvg.style.transition = 0.3 + 's'
        descSvg.style.opacity = 0
    })
});

// function openAuthWindow() {
//     authWindow.classList.remove('hidden');
//     authWindow.classList.add('auth-form__blur');
// };

// function registerWindow() {
//     const logSection = authWindow.children.item(0);
//     const regSection = authWindow.children.item(1);

//     logSection.style.display = 'none';
//     regSection.style.display = 'block';
// };

// function loginWindow() {
//     const logSection = authWindow.children.item(0);
//     const regSection = authWindow.children.item(1);

//     logSection.style.display = 'block';
//     regSection.style.display = 'none';
// };

// function closeAuthWindow(e) {
//     if (e.currentTarget === e.target) {
//         authWindow.classList.remove('auth-form__blur');
//         authWindow.classList.add('hidden');
//     }
//     const btnLogCloseAuthWindow = authWindow.querySelector('#logCloseAuthWindow');
//     const btnRegCloseAuthWindow = authWindow.querySelector('#regCloseAuthWindow');

//     btnLogCloseAuthWindow.addEventListener('click', () => {
//         authWindow.classList.remove('auth-form__blur');
//         authWindow.classList.add('hidden');
//     });

//     btnRegCloseAuthWindow.addEventListener('click', () => {
//         authWindow.classList.remove('auth-form__blur');
//         authWindow.classList.add('hidden');
//     });
// };