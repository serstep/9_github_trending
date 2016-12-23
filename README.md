# 9_github_trending

Скрипт позволяет найти 20 самых популярных проэктов созданных в течение недели.



Для работы скрипта требуется пакет requests. Проверить его наличие можно так:
  
  pip show requests
  
Должно появиться похожее сообщение

  Name: requests
  Version: 2.11.1
  Location: /usr/lib/python3.5/dist-packages
  Requires: 

Если пакет не установлен, его можно установить следующим образом:

  pip install requests

##Использование

  $python3 github_trending
  
В результате получите нечто подобное:

  Имя: webpack-tricks
  URL: https://github.com/rstacruz/webpack-tricks
  Количество звезд: 1228
  Количество задач: 4

  Имя: awesome-bits
  URL: https://github.com/keonkim/awesome-bits
  Количество звезд: 906
  Количество задач: 10
  
  ...
  
  
