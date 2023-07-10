let menu_open = document.getElementById('menu_open');
let navbar = document.querySelector('.navbar');
let menu_img = document.querySelector('.menu_img');

menu_open.addEventListener('click',function(){
    console.log(menu_open.checked)
    if(menu_open.checked){
        menu_img.src = '../img/close.svg'
        anime({
            targets: navbar,
            translateX: '0%',
            easing: 'linear',
            duration: 200
        })
    }
    else{
        menu_img.src = '../img/menu.svg'
        anime({
            targets: navbar,
            translateX: '-100%',
            easing: 'linear',
            duration: 200
        })
    }
})