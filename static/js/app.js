async function getPhotos(page = 1) {
    const response = await fetch('/photos/' + page);
    return await response.json();
}

async function getPagesInfo() {
    const response = await fetch('/pages/');
    return await response.json();
}

async function searchPhotos(prompt, page) {
    const response = await fetch(`/search?prompt=${prompt}&page=${page}`);
    return await response.json();
}

async function regeneratePhoto(prompt) {
    const options = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: prompt
    }
    const response = await fetch(`/regenerate`, options);
    return await response.json();
}

async function varyUpscalePhoto(prompt, photo_path, action) {
    const options = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({prompt: prompt, photo_path: photo_path})
    }

    const response = await fetch(`/${action}`, options);
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

const pagesInfoData = {
    pagesInfo: {},
    async loadPagesInfo() {
        this.pagesInfo = await getPagesInfo()
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

function generate(txt) {
    const prompt = decodeURIComponent(txt);
    regeneratePhoto(prompt).then(() => alert('Generation finished.')).catch(() => alert('Failed to Generate'));
    alert('Generation queued');
}

function vary_upscale(txt, photo_path, action) {
    const prompt = decodeURIComponent(txt);
    varyUpscalePhoto(prompt, photo_path, action).then(() => alert('Generation finished.')).catch(() => alert('Failed to Generate'));
    alert('Generation queued');
}