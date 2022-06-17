str = '":"/images/search?pos=0&img_url=https%3A%2F%2Fic.pics.livejournal.com%2Frenat_homidoff%2F23699620%2F379084%2F379084_original.jpg&text=%D0%BB%D0%B5%D1%81&isize=large&rpt=simage&lr=50&iorient=vertical","img_href":"https://vsegda-pomnim.com/uploads/posts/2022-04/1648927316_5-vsegda-pomnim-com-p-krasivaya-priroda-les-foto-5.jpg","useProxy":false,"pos":0,"id":"63e645f8ae3239ff02ff0224000de374","rimId":"210d4bea2c7a2296d954572530e057f9","docid":"Z1DA1209CCCF58BD6","isMarketIncut":false,"counterPath":"thumb/normal'

print(str)

str = str.split('img_href')[-1:]
str = str[0].split('useProxy')[:-1]
str = str[0][3:]
str = str[:-3]

print(str)