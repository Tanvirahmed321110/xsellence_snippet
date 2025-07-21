{
    'name': 'Xsellence Snippets',
    'description': 'Xsellence Snippets Desc',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',

        'views/header.xml',
        # 'views/footer.xml',
        # 'views/snippets/dynamic_products.xml',
        'views/snippets/hero/hero1.xml',
        'views/snippets/blog/blog1.xml',
        'views/snippets/offer/offer1.xml',
        'views/snippets/hero/hero2.xml',
        'views/snippets/dynamic/dynamic_cart1.xml',

        # ==============   Backend View   ===============
        'views/back_end_views/new_product_views.xml',

        # ==============   Main Snippets File   ===============
        'views/snippets/snippets.xml',
        # ==============   Main Menu   ===============
        'views/back_end_views/menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # ==============   For Main Css   ===============
            'xsellence_snippets/static/src/css/common.css',

            # ==============   For All Snippets Css File  ===============
            'xsellence_snippets/static/src/css/hero/hero.css',
            'xsellence_snippets/static/src/css/blog/blog_snippet.css',
            'xsellence_snippets/static/src/css/offer/offer.css',

            # ==============   For Js   ===============
            'xsellence_snippets/static/src/js/swiper-bundle.min.js',
            'xsellence_snippets/static/src/js/dynamic_snippets.js',
            'xsellence_snippets/static/src/js/dynamic-cart1.js',
            # 'xsellence_snippets/static/src/js/hero2.js',
            # 'xsellence_snippets/static/src/js/hero2.js',
            # 'theme_tutorial/static/src/js/new_product_snippet.js',
        ]
    },
    'license': 'LGPL-3',
}
