# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.

{
    'name':'Theme Aliment',
    'description': 'Theme Aliment is theme developed by 73Lines Development Team consist of 17  snippets to build a beautiful website with 6 color variations, 6 font options, 2 Layouts and 8 Patterns.',
    'category': 'Theme/Ecommerce',
    'version':'1.0',
    'author':'73Lines',
    'depends': [
                'website',        
                'theme_default',
                'website_animate',
                'website_mass_mailing',
                'website_blog',
                'snippet_blog_carousel_73lines',
                'snippet_boxed_73lines',
                'snippet_brand_carousel_73lines',
                'snippet_object_carousel_73lines',
                'snippet_product_carousel_73lines',
                'snippet_product_category_carousel_73lines',
                'snippet_recently_viewed_products_carousel_73lines',
                'website_category_banner_73lines',
                'website_customize_model_73lines',
                'website_language_flag_73lines',
                'website_mega_menu_73lines',
                'website_product_by_brand_73lines',
                'website_product_content_block_73lines',
                'website_product_features_73lines',
                'website_product_multi_image_73lines',
                'website_product_price_filter_73lines',
                'website_product_share_button_73lines',
                'website_product_sorting_73lines',
                'website_product_tags_73lines',
                'website_user_wishlist_73lines',
                ],
    'data': [
             
              # Snippets
            'snippets/s_state_counter.xml',
            'snippets/s_parallax_two.xml',
            'snippets/s_parallax_one.xml',
            'snippets/s_footer_one.xml',
            'snippets/s_aliment_banner.xml',
            'snippets/s_our_menu.xml',
            'snippets/s_our_usp.xml',

             'views/assets.xml',
             'views/chat_template.xml',
             'views/home_page_carousel.xml',
             'views/home_page_mini_carousel.xml',
             'views/products_template.xml',
             'views/single_product_template.xml',
             'views/attribute_filter_template.xml',
             'views/product_collapse_categories_template.xml',
             'views/navbar_template.xml',
             'views/customize_model.xml',
             'views/rating_template.xml',
             'views/homepage_cate_carousel_template.xml',
        ],
     'demo': [
            'demo_pages/homepage.xml',
            'demo_pages/menu_data.xml',
            'demo_pages/footer_template.xml',
            'demo_pages/blog_post_demo.xml',
            'demo_pages/brand_demo.xml',
    ],
     'images': [
        'static/description/aliment-banner.png',
    ],
    'price': 200,
    'license': 'OEEL-1',
    'currency': 'EUR',
    'live_test_url': 'http://theme-aliment.73lines.com'
}

