var images = [
    { src: 'french_polynesia.jpg', title: 'Bora Bora, French Polynesia' },
    { src: 'vietnam.jpg', title: 'Ha Long Bay, Vietnam' },
    { src: 'peru.jpg', title: 'Machu Picchu, Peru' },
    { src: 'scotland.jpg', title: 'Edinburgh, Scotland' },
    { src: 'hawaii.jpg', title: 'Hawaii' },
    { src: 'south_africa.jpg', title: 'Kruger National Park, South Africa' }
];

$(function () {
    var gridSize = $('#levelPanel :radio:checked').val();
    imagePuzzle.startGame(images, gridSize);
    $('#newPhoto').click(function () {
        var gridSize = $('#levelPanel :radio:checked').val();
        imagePuzzle.startGame(images, gridSize);
    });

    $('#levelPanel :radio').change(function (e) {
        var gridSize = $(this).val();
        imagePuzzle.startGame(images, gridSize);
    });
});
