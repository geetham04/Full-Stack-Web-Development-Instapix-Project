var uploadWindow = document.getElementById("upload_window");
var addPhotosButton = document.getElementById("add-btn");
var span = document.getElementsByClassName("close-window")[0];

addPhotosButton.onclick = function(){
    uploadWindow.style.display = "block";
}
span.onclick = function(){
    uploadWindow.style.display = "none";
}
window.onclick = function(event){
    if (event.target == uploadWindow){
        uploadWindow.style.display = "none";
    }
}

var uploadButton = document.getElementById("upload-btn");
var dbConnection = new ActiveXObject("adodb.connection");
var stringonnection = "driver={sql server}"
dbConnection.open();

uploadButton.onclick = function(){

}
