/* Most of the code is from https://blog.benoitblanchon.fr/django-htmx-modal-form/ */


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

// Show success alert message after adding, editing, or deleting a task
htmx.on("showMessage", (e) => {
    document.getElementById("messageDiv").innerHTML = `
    <div class="d-flex justify-content-center">
        <div class='alert alert-success alert-dismissible fade show w-50' role='alert'>
            ${e.detail.value}
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
        </div>
    </div>`;
})