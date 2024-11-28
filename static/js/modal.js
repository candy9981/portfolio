//モーダル情報読み取り
const btn = document.querySelector("#modal");
const modalBtn = document.querySelector("#modalBtn");
const dialog = document.querySelector("#dia");
const body = document.querySelector("#body");
const prevbtn = document.getElementById("prevbtn");
const nextbtn = document.getElementById("nextbtn");
let count = 1;

//モーダルの作成
btn.addEventListener("click", () => {
  dialog.classList.add('open');
  dialog.showModal();
  body.classList.add('modal-open');
})

modalBtn.addEventListener('click', () => {
  dialog.classList.remove('open');
  dialog.classList.add('closing');
  setTimeout(() => {
    body.classList.remove('modal-open');
    dialog.classList.remove('closing');
    dialog.close(); // 0.5秒後にモーダルを閉じる
  }, 500);
});

//画像の変更
function changeMainImage(source) {
  let mainImage = document.querySelector("#main-image img");
  mainImage.src = source;
}

prevbtn.addEventListener("click",()=>{
  count --;
  if(count == 0){
    count = 12;
  }
  let src = `../static/img/menubook${count}.jpg`
  changeMainImage(src);
})

nextbtn.addEventListener("click",()=>{
  count ++;
  if(count == 13){
    count = 1;
  }
  let src = `../static/img/menubook${count}.jpg`
  changeMainImage(src);
})
