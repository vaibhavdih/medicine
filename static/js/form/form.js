function displayMore() {
    var checkBox = document.getElementById("yes");
    if (checkBox.checked == true) {
        document.getElementById("no").checked = false;
        document.querySelector('.inner-display').style.display = "block";
    } else {
        document.querySelector('.inner-display').style.display = "none";
    }
}

function displayError() {
    var checkBox = document.getElementById("no");
    if (checkBox.checked == true) {
        document.getElementById("yes").checked = false;
        document.querySelector('.inner-display').style.display = "none";
    }
}

function displayMask() {
    var checkBox = document.getElementById("mask-yes");
    if (checkBox.checked == true) {
        document.querySelector('.inner-mask').style.display = "block";
    } else {
        document.querySelector('.inner-mask').style.display = "none";
    }
}

function displayMaskNo() {
    var checkBox = document.getElementById("mask-no");
    if (checkBox.checked == true) {
        document.getElementById("mask-yes").checked = false;
        document.querySelector('.inner-mask').style.display = "none";
    }
}

function displaySanitizer() {
    var checkBox = document.getElementById("sanitizer-yes");
    if (checkBox.checked == true) {
        document.querySelector('.inner-sanitizer').style.display = "block";
    } else {
        document.querySelector('.inner-sanitizer').style.display = "none";
    }
}


function displaySanitizerNo() {
    var checkBox = document.getElementById("sanitizer-no");
    if (checkBox.checked == true) {
        document.getElementById("sanitizer-yes").checked = false;
        document.querySelector('.inner-sanitizer').style.display = "none";
    }
}

var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];

function modalDisplay() {
    modal.style.display = "block";
}
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}



