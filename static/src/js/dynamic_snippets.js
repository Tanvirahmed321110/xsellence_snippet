/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.Products = publicWidget.Widget.extend({
    selector: '.dynamic-products',
    start() {

        let products = this.el.querySelector('#dynamic-products')
        let data = rpc('/all_products', {
            'res_id': '',
            'res_model': '',
        });

        data.then(response => {
            console.log('data', response);
        }).catch(error => {
            console.error('Error:', error);
        });


    },
});

export default publicWidget.registry.Products;
