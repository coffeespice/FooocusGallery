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
    navigator.clipboard.writeText(txt)
        .then(() => alert('Copied to Clipboard!\nPaste to prompt area to load parameters.\nCurrent clipboard content is:\n\n' + txt))
        .catch(() => alert('Not possible to copy, if using remote server HTTPS is needed'));
}