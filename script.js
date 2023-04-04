const form = getElementById("generate-form");
const qr = document.getElementById("qrcode");

let url = window.location.href;
document.getElementById("url").defaultValue = url;
const onGenerateSubmit = (e) => {
    e.preventDefault();
    const size = document.getElementById("size").ariaValueMax;

}

form.addEventListener("share",onGenerate)