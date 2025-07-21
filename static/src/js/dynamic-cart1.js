/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.DynamicCart1 = publicWidget.Widget.extend({
    selector: '.dynamic-cart1',
    start() {
      // Prevent duplicate initialization
        let nameTag = this.el.querySelector('.name')
        console.log('h2Tags',nameTag)

        let productWrapper = this.el.querySelector('#dynamic-cart1')
        productWrapper.innerHTML = ' '
        console.log('new html are', productWrapper)


        let data = rpc('/dynamic_cart1', {
            'res_id': '',
            'res_model': '',
        });

        data.then(response => {
            console.log('data', response);

            response.forEach(item=>{

//                 const productDiv = document.createElement('div');
//                 productDiv.innerHTML = `
//                <div>
//                    <h5>  Name: <span> ${item.name}  </span> </h5>
//                 </div>
    //            `
                const cart = document.createElement('div');
                cart.innerHTML = `
                            <div class="my-card my-p-2 my-border">
                                <img class="my-w-100" src="${item.image_url || '/default-image.png'}"
                                    alt="${item.name}"/>
                                <h3 class="name my-mt-2">Name: <span> ${item.name}</span></h3>
                            </div>
                    `
                       productWrapper.appendChild(cart);
                    })

        }).catch(error => {
            console.error('Error:', error);
        });

    },
});

//export default publicWidget.registry.Products;