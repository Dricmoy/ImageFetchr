$(document).ready(function() {
    // Load images from images.json
    $.getJSON('images.json', function(imageUrls) {
        let gallery = $('#gallery');

        imageUrls.forEach(function(url) {
            gallery.append(`
                <div class="gallery-item">
                    <img src="${url}" alt="Photo" class="gallery-image">
                </div>
            `);
        });

        // Initialize lightbox functionality
        $('.gallery-image').click(function() {
            $('#lightbox-img').attr('src', $(this).attr('src'));
            $('#lightbox').fadeIn();
        });

        $('#lightbox .close').click(function() {
            $('#lightbox').fadeOut();
        });

        $('#lightbox').click(function(event) {
            if ($(event.target).is('#lightbox')) {
                $('#lightbox').fadeOut();
            }
        });
    });
});
