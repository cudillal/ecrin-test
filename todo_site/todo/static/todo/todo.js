// Most of the code is from https://blog.benoitblanchon.fr/django-htmx-modal-form/


const modal = new bootstrap.Modal(document.getElementById("taskModal"))

htmx.on("htmx:afterSwap", (e) => {
    // Response targeting #dialog => show the modal
    if (e.detail.target.id == "dialog") {
        modal.show()
    }
})

htmx.on("htmx:beforeSwap", (e) => {
    // Empty response targeting #dialog => hide the modal
    if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
    }
})

// In case of cancelling the edit, empty the dialog
htmx.on("hidden.bs.modal", () => {
    document.getElementById("dialog").innerHTML = ""
})
  

function done(taskId) { 
    let current = document.getElementById(`text_${taskId}`);
    const classExit = current.classList.contains("text-decoration-line-through");
    if (classExit == true) {
        current.classList.remove("text-decoration-line-through");
    } else {
        current.classList.add("text-decoration-line-through");
    }
}