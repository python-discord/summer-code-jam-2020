const bulmaCarousel = require("../../../../static/js/bulma-carousel");

bulmaCarousel.attach('#bg-carousel', {
    slidesToScroll: 1,
    slidesToShow: 1,
    infinite: true,
    navigation: true,
    navigationKeys: true,
});