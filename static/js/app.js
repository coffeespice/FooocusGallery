async function getPhotos(page = 1) {
    const response = await fetch('/photos/' + page);
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
    photos: [], page: 0, columns: 4, prompt: '', busy: false, pagesInfo: {},
    async loadPhotos(page) {
        if (page < 0) page = this.page = this.pagesInfo.pages;
        if (page > this.pagesInfo.pages) page = this.page = 0;
        document.body.scrollTop = 0;
        this.busy = true;
        const data = this.prompt ? await searchPhotos(this.prompt, page) : await getPhotos(page);
        this.photos = data.photos;
        this.pagesInfo = data.pages_info;
        this.busy = false;
    }
}

function to_clipboard(txt) {
    txt = decodeURIComponent(txt);
    const modal = document.querySelector('#modal_prompt');
    const textarea = modal.querySelector('textarea');
    textarea.value = txt;
    modal.showModal();
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