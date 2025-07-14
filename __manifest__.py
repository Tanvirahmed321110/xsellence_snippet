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
        'views/footer.xml',
        # 'views/snippets/dynamic_products.xml',
        'views/snippets/hero/hero1.xml',
        # 'views/snippets/new_product.xml',

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
            # 'https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css',
            # 'https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.theme.default.min.css',
            # 'https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js',

            # ==============   For All Snippets Css File  ===============
            'xsellence_snippets/static/src/css/hero/hero.css',

            # ==============   For Js   ===============
            'xsellence_snippets/static/src/js/swiper-bundle.min.js',
            # 'xsellence_snippets/static/src/js/hero/hero1.js',
            # 'xsellence_snippets/static/src/js/dynamic_snippets.js',
            # 'xsellence_snippets/static/src/js/hero2.js',
            # 'xsellence_snippets/static/src/js/hero2.js',
            # 'theme_tutorial/static/src/js/new_product_snippet.js',
        ]
    },
    'license': 'LGPL-3',
}
