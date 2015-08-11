(function () {
var filesUpload = document.getElementById("file");
var fileList = document.getElementById("file-list");
var ext = ['png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif'];
function getFiles (files) {
    if (typeof files !== "undefined") {
        for (var i=0, l=files.length; i<l; i++) {
            var file = files[i]
              var li = document.createElement("li"),
        div = document.createElement("div");

    li.appendChild(div);

    // Present file info and append it to the list of files#
    if( ext.indexOf(file.name.split('.').pop()) > -1 ){
        div.innerHTML = "<div class='bold center p2 mb2 bg-yellow rounded' style='display: inline-block;'>"+file.name +" <span class='inline-block px1 white bg-green rounded'>Yes!</span></div> ";
    }else{
        div.innerHTML = "<div class='bold center p2 mb2 bg-yellow rounded' style='display: inline-block;'>"+file.name +" <span class='inline-block px1 white bg-red rounded'>No!</span></div>";
    }

    fileList.appendChild(div);
        }
    }
}
document.addEventListener('DOMContentLoaded', function () {
filesUpload.addEventListener("change", function () {
    getFiles(this.files);
}, false);
});
     })();