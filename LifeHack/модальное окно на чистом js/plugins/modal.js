function _createModal(options) {
    const modal = document.createElement(tagName: "div")
    modal.classList.add("vmodal")
    modal.insertAdjacentHTML(where: "afterbegin", html:`
        <div class="modal-overlay">
            <div class="modal-window">
            
                <div class="modal-header">
                    <span class="modal-title">Modal title</span>
                    <span class="modal-close">&times;</span>
                </div>

                <div class="modal-body">
                    <p>lorem4</p>
                    <p>lorem4</p>
                </div>
                <div class="model-footer">
                    <button>Ok</button>
                    <button>Cancel</button>
                </div>
            </div>
        </div>
    `)
    document.body.appendChild(modal)
    return modal
}

$.modal = function (options) {
    const $modal = _createModal(options)

    return {
        open() {},
        close() {},
        destroy() {}
    }
}