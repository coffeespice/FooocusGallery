import PhotoSwipeLightbox from '/static/js/photoswipe-lightbox.esm.min.js';
import PhotoSwipe from '/static/js/photoswipe.esm.min.js';

const lightbox = new PhotoSwipeLightbox({
    gallery: '#gallery',
    children: 'a',
    pswpModule: () => PhotoSwipe,
    wheelToZoom: true,
    preload: [1, 4]
});

lightbox.on('uiRegister', function () {
    lightbox.pswp.ui.registerElement({
        name: 'copy-gen',
        ariaLabel: 'Copy image generation settings',
        title: 'Copy image generation settings',
        order: 9,
        isButton: true,
        html: '<i class="gg-clipboard" style="margin: auto;"></i>',
        onClick: () => {
            console.log(lightbox.pswp.currSlide.data.src);
            const click = lightbox.pswp.currSlide.data.element.dataset.pswpClick;
            if (!click) return alert('Incompatible log');
            eval(click);
        }
    });

    lightbox.pswp.ui.registerElement({
        name: 'gen',
        ariaLabel: 'Regenarte image using same parameters',
        title: 'Regenarte image using same parameters',
        order: 9,
        isButton: true,
        html: '<i class="gg-repeat" style="margin: auto;"></i>',
        onClick: () => {
            let click = lightbox.pswp.currSlide.data.element.dataset.pswpClick;
            if (!click) return alert('Incompatible log');
            click = click.replace('to_clipboard', 'generate');
            eval(click);
        }
    });

    lightbox.pswp.ui.registerElement({
        name: 'upscale',
        ariaLabel: 'Upscale image 1.5x',
        title: 'Upscale image 1.5x',
        order: 9,
        isButton: true,
        html: '<i class="gg-chevron-up" style="margin: auto;"></i>',
        onClick: () => {
            let click = lightbox.pswp.currSlide.data.element.dataset.pswpClick;
            if (!click) return alert('Incompatible log');
            const image = lightbox.pswp.currSlide.data.src;
            const action = "upscale_150"
            click = click.replace('to_clipboard', 'vary_upscale').replace(')', `,"${image}","${action}")`);
            eval(click);
        }
    });

    lightbox.pswp.ui.registerElement({
        name: 'upscale2',
        ariaLabel: 'Upscale image 2x',
        title: 'Upscale image 2x',
        order: 9,
        isButton: true,
        html: '<i class="gg-chevron-double-up" style="margin: auto;"></i>',
        onClick: () => {
            let click = lightbox.pswp.currSlide.data.element.dataset.pswpClick;
            if (!click) return alert('Incompatible log');
            const image = lightbox.pswp.currSlide.data.src;
            const action = "upscale_200"
            click = click.replace('to_clipboard', 'vary_upscale').replace(')', `,"${image}","${action}")`);
            eval(click);
        }
    });

    lightbox.pswp.ui.registerElement({
        name: 'vary',
        ariaLabel: 'Vary image subtle',
        title: 'Vary image subtle',
        order: 9,
        isButton: true,
        html: '<i class="gg-play-track-next" style="margin: auto;"></i>',
        onClick: () => {
            let click = lightbox.pswp.currSlide.data.element.dataset.pswpClick;
            if (!click) return alert('Incompatible log');
            const image = lightbox.pswp.currSlide.data.src;
            const action = "vary_subtle"
            click = click.replace('to_clipboard', 'vary_upscale').replace(')', `,"${image}","${action}")`);
            eval(click);
        }
    });

    lightbox.pswp.ui.registerElement({
        name: 'vary2',
        ariaLabel: 'Vary image strongly',
        title: 'Vary image strongly',
        order: 9,
        isButton: true,
        html: '<i class="gg-play-forwards" style="margin: auto;"></i>',
        onClick: () => {
            let click = lightbox.pswp.currSlide.data.element.dataset.pswpClick;
            if (!click) return alert('Incompatible log');
            const image = lightbox.pswp.currSlide.data.src;
            const action = "vary_strong"
            click = click.replace('to_clipboard', 'vary_upscale').replace(')', `,"${image}","${action}")`);
            eval(click);
        }
    });

    lightbox.pswp.ui.registerElement({
        name: 'custom-caption',
        order: 10,
        isButton: false,
        appendTo: 'root',
        onInit: (el, pswp) => {
            lightbox.pswp.on('change', () => {
                const data = lightbox.pswp.currSlide.data.element.dataset;
                if (!data.prompt) {
                    el.innerHTML = '';
                    return;
                }
                
                el.innerHTML = `
                <figcaption>
                        <h1>${data.prompt}</h1>
                        <h2>${data.styles}</h2>
                        <small>${data.base_model}</small>
                        <small>${data.refiner_model}</small>
                    </figcaption>
`

            });
        }
    });
});

lightbox.init();