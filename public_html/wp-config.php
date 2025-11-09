<?php
define('DB_NAME', 'nafdzavwhr');
define('DB_USER', 'nafdzavwhr');
define('DB_PASSWORD', '7aVdF7N9hs');
define('DB_HOST', 'localhost');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');

define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', false);

$table_prefix = 'wp_';

define('AUTH_KEY',         'EdjB+++G#)mmgc)rXZN8y{Vcxn$B[X|jRD+*cIGR[hC]so(Ds20e7vc+H]rT@w`t');
define('SECURE_AUTH_KEY',  'YOwuKcn)Z53,{[S:6&J|ktbA)Gd+^:kFzD}E=ho>A.B9_a_Rg2jO+ZF3;uE2-y>f');
define('LOGGED_IN_KEY',    '86lAJI*|8}0:2w1CU2OvA*iI(TLJ/nXjf<AYA3CU/8!vP5oB4A:a$[pjc|fotJ]~');
define('NONCE_KEY',        'ox(8K4:{:[PFQ>UV%+G--ms?*woGgb^2I!JO&S&&.7)nQNjtt~Np+LK9moO&4*4R');
define('AUTH_SALT',        '{M))ONM#v^H]_zf-KV,?<KJfD;Z<-`DoO!0j<K[krDW!vIcYlY5#=(=@~2V)+[|A');
define('SECURE_AUTH_SALT', 'P4t?@^vgseA3mrcP<37l7-kUE_eUkiT-_Fjs*PYv1bh$Z5le:6rd-/:d7T2pf4$R');
define('LOGGED_IN_SALT',   '/V+N9psg%90)S{l($3-)<-T0|M1X//;[YJB6mT-~7AHLTG<X^x+|Ew++`P(IK&+1');
define('NONCE_SALT',       ']Wv.O?,+wA6,JFO9{a^YAchb0[6$_~0>RvO+S0zse8MF[+1xA6g>)#Uj9=3xw<-4');

if ( !defined('ABSPATH') )
    define('ABSPATH', dirname(__FILE__) . '/');

require_once(ABSPATH . 'wp-settings.php');
