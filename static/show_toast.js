// store toast_box container to a variable
let toast_box = document.getElementById('toast_box');

// create a function that will handle toast notification display generation
function show_toast(type, msg) {
    // create a new div element and store it in a variable
    let toast = document.createElement('div');

    // set a css class to newly-created div
    toast.classList.add('toast', type);

    // set a text message in said div class
    toast.innerHTML = msg;
    
    // append newly-created div in toast_box container
    toast_box.appendChild(toast);

    // set a timeout to make toast disappear after 5000 milliseconds (5 seconds)
    setTimeout(() => {
        toast.remove();
    }, 5000);
}