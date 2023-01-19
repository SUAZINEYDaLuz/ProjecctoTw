const file = document.getElementById("upload_costum");
const back = document.getElementById("image-back");

function getimage(event) {
    var file = event.target.files[0]
    back.src = URL.createObjectURL(file)
}