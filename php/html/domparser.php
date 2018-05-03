<?php

require __DIR__ . '/vendor/autoload.php';

use Symfony\Component\DomCrawler\Crawler;
//https://symfony.com/doc/current/components/dom_crawler.html

$html = <<<'HTML'
<!DOCTYPE html>
<html>
    <body>
        <p class="message">Hello World!</p>
        <p>Hello Crawler!</p>
    </body>
</html>
HTML;

$crawler = new Crawler($html);

foreach ($crawler as $domElement) {
    var_dump($domElement->nodeName);
}

$html2 = <<<'HTML'
<!DOCTYPE html>
<html>
    <head>
        <cloudbric>valuevalue</cloudbric>
        <meta name='1234'>Hello Crawler!</meta>
    </head>
</html>
HTML;

$crawler2 = new Crawler($html2);

$cb_key_node = $crawler2->filter('head > cloudbric')->last();
$cb_key_node2 = $crawler2->filter('head > nohead')->last();

var_dump($cb_key_node);
print('==================================================');
var_dump($cb_key_node2);
