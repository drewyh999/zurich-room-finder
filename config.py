#Print verbose information or not
VERBOSE_MODE = False

WGZIMMER_HEADERS = {
   "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
   "cookie":"wc_currencyLocale=de_CH; wc_color=babyblue; wc_email=\"info@wgzimmer.ch\"; wc_currencySign=sFr.; _ga=GA1.2.223238142.1621679202; _pk_id.1.02e6=bac4849e8492533a.1621679204.; wc_language=en; ezCMPCCS=true; __qca=P0-1584377785-1622526586520; ezux_ifep_122604=true; ezosuigenerisc=b9f0f8334082639d8057253f3f99fb54; ezosuigeneris=d05af44140e621a3808e0cb61b09af19; ezds=ffid%3D1%2Cw%3D1920%2Ch%3D1080; ezohw=w%3D1858%2Ch%3D976; ezouspvh=950; ezouspvv=302; ezouspva=25; __gads=ID=53d78ed7fcff0bf7-220a772d29ca0019:T=1625478347:RT=1625478347:S=ALNI_MZRv0KZYKE__CK0giRuZM8GxnMXOg; _gid=GA1.2.578977251.1626012193; JSESSIONID=F5830DB75AC3DD35747D9100B925A0BB; ezoadgid_122604=-1; ezoref_122604=wgzimmer.ch; ezoab_122604=mod1; lp_122604=https://www.wgzimmer.ch/en/wgzimmer/search/mate.html?wgSearchStartOver=true; ezovuuid_122604=2edc70fb-c4ed-474b-5c99-1bcc0112d319; active_template::122604=orig_site.1626055904; ezovuuidtime_122604=1626055905; ezopvc_122604=13; _gat_gtag_UA_974772_2=1; ezux_lpl_122604=1626055912636|0d0d4f67-5dfe-48af-6f71-4990efc90596|true; ezux_et_122604=7778; ezux_tos_122604=596010",
   "connection":"close"
}
ETH_HEADERS = {
   "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
   "cookie":"ORA_FPC=id=8db844b9-175f-4e72-afb9-2ad2e4e0733c; _ga=GA1.2.399428582.1629553942; PHPSESSID=b4798f9f4b00e3629d97aa0e4b2922bf; lang=TV5RL4j%2BmaA1ORKbZEAFETE7O90Bu5h7GGYst7EWRpIQZP5dt3g10B9Va4dxM9rWqDy0sv%2BKcRy8w0z86d6i2w%3D%3D; sid=fe95aa25dbebc059347e9a860e12f8c3",
   "connection":"keep-alive"
}

SENDER_EMAIL_ACCOUNT = {
   "account":"1251956930@qq.com",
   "host":"smtp.qq.com",
   "port":"465"
}

pre_ads_found = -1

WGZIMMER_CONDITIONS = {
      "query":"",
      "priceMin":"200",
      "priceMax":"1500",
      "state":"zurich-stadt",
      "permanent":"true",
      "student":"none",
      "orderBy":"@sortDate",
      "orderDir":"descending",
      "startSearchMate":"true",
      "wgStartSearch":"true",
      "start":"0"
}

RECEIVER_EMAIL = "drewyh1999@outlook.com"

FREQUENCY = 4 #Determines how many times refresh within an hour

#City names and values
CITY_NAMES = {
   "Aargau":"aargau",
   "Aarau (Stadt)":"aarau",
   "Appenzell Innerrhoden":"appenzell-innerrhoden",
   "Appenzell Ausser.":"appenzell-ausser",
   "Baden":"baden",
   "Basel City":"baselstadt",
   "Basel Land":"baselland",
   "Bern":"bern",
   "Biel":"biel",
   "Brugg":"brugg",
   "Burgdorf":"burgdorf",
   "Chur":"chur",
   "Emmental":"emmental",
   "Frauenfeld":"frauenfeld",
   "Fribourg":"fribourg",
   "Jura":"jura",
   "Geneva":"genf",
   "Glarus":"glarus",
   "Graub??nden":"graubunden",
   "Interlaken":"interlaken",
   "Kloten (Z??rich)":"zurich-kloten",
   "Langenthal":"langenthal",
   "Langnau":"langnau",
   "Laufenburg":"laufenburg",
   "Lausanne":"lausanne",
   "L??rrach (DE)":"loerrach",
   "Lucerne":"luzern",
   "Neuch??tel":"neuenburg",
   "Nidwalden":"nidwalden",
   "Obwalden":"obwalden",
   "Olten":"olten",
   "Ostschweiz":"ostschweiz",
   "Rapperswil-Jona":"rapperswil-jona",
   "Schaffhausen":"schaffhausen",
   "Solothurn":"solothurn",
   "Schwyz":"schwyz",
   "Spiez":"spiez",
   "St. Gallen":"st-gallen",
   "Saint-Louis (FR)":"saint-louis-fr",
   "Simmental/Saanenland":"simmental-saanenland",
   "Ticino":"tessin",
   "Thun":"thun",
   "Thurgau":"thurgau",
   "Uri":"uri",
   "Vaud":"waadt",
   "W??denswil (ZHAW)":"waedenswil",
   "Wallis":"wallis",
   "Weil am Rhein (DE)":"weil-am-rhein-de",
   "Wil":"wil",
   "Winterthur &amp; Agglomeration":"winterthur",
   "Zug":"zug",
   "Zurich (City)":"zurich-stadt",
   "Z??rich (Altstetten, H??ngg)":"zurich-altstetten",
   "Z??rich (Oerlikon, Seebach, Affoltern)":"zurich-oerlikon",
   "Z??rich (Rund um den See)":"zurich-lake",
   "Z??rich (Aeugstertal, Affoltern am Albis)":"zurich-aeugstertal",
   "Zurich (Unterland, Weinland, Limmattal)":"zurich",
   "Z??rich (Oberland, Glattal)":"zurich-oberland",
   "Liechtenstein":"liechtenstein"
}

