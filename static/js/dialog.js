;(function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"))
  

    // htmx.on() functions as event listeners for htmx events
    // htmx:afterSwap is triggered after content is swapped
    htmx.on("htmx:afterSwap", (e) => {
      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "dialog") {
        modal.show()
      }
    })
  
    // htmx:beforeSwap is triggered before content is swapped
    htmx.on("htmx:beforeSwap", (e) => {
      // Empty response targeting #dialog => hide the modal
      if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })
  
    // Remove dialog content after hiding
    htmx.on("hidden.bs.modal", () => {
      document.getElementById("dialog").innerHTML = ""
    })
  })()