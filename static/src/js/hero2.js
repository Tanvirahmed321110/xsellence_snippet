odoo.define('MODULE_NAME.owl_carousel', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.owlCarousel = publicWidget.Widget.extend({
        selector: '.owl-carousel',
        disabledInEditableMode: false,

        start: function () {
            if (typeof $.fn.owlCarousel === 'undefined') {
                return $.Deferred().reject("Owl Carousel not loaded");
            }

            // Initialize Owl Carousel only in frontend
            if (!this.editableMode) {
                this.$el.owlCarousel({
                    loop: true,
                    margin: 10,
                    nav: true,
                    responsive: {
                        0: { items: 1 },
                        600: { items: 3 },
                        1000: { items: 5 }
                    }
                });
            }

            return this._super.apply(this, arguments);
        },

        destroy: function () {
            if (this.$el.data('owl.carousel')) {
                this.$el.trigger('destroy.owl.carousel');
            }
            this._super.apply(this, arguments);
        },
    });
});