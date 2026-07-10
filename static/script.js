// Count selected symptoms

const checkboxes = document.querySelectorAll('input[type="checkbox"]');

checkboxes.forEach(box => {

    box.addEventListener("change", updateCounter);

});

function updateCounter(){

    const selected = document.querySelectorAll('input[type="checkbox"]:checked').length;

    let counter = document.getElementById("selected-count");

    if(counter){

        counter.innerHTML = selected;

    }

}


// Reset confirmation

function resetForm() {

    if (confirm("Are you sure you want to reset?")) {

        window.location.href = "/";

    }

}

