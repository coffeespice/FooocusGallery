async function getPhotos(page = 1) {
    const response = await fetch('/photos/' + page);
    return await response.json();
}

async function searchPhotos(prompt, page) {
    const response = await fetch(`/search?prompt=${prompt}&page=${page}`);
    return await response.json();
}

const mainFormData = {
    photos: [], page: 0, columns: 4, prompt: '', busy: false,
    async loadPhotos(page) {
        document.body.scrollTop = 0;
        this.busy = true;
        this.photos = this.prompt ? await searchPhotos(this.prompt, page) : await getPhotos(page);
        this.busy = false;
    }
}

function to_clipboard(txt) {
    txt = decodeURIComponent(txt);
    if (navigator.clipboard && navigator.permissions) {
        navigator.clipboard.writeText(txt)
    } else {
        const textArea = document.createElement('textArea')
        textArea.value = txt
        textArea.style.width = 0
        textArea.style.position = 'fixed'
        textArea.style.left = '-999px'
        textArea.style.top = '10px'
        textArea.setAttribute('readonly', 'readonly')
        document.body.appendChild(textArea)

        textArea.select()
        document.execCommand('copy')
        document.body.removeChild(textArea)
    }
    alert('Copied to Clipboard!\nPaste to prompt area to load parameters.\nCurrent clipboard content is:\n\n' + txt);
}