library(rvest)
url <- "http://www.amazon.in/Moto-Plus-4th-Gen-Black/dp/B01DDP7GZK/ref=sr_1_1?s=electronics&ie=UTF8&qid=1468597837&sr=1-1&keywords=moto+g"
imgsrc <- read_html(url) %>%
  html_node(xpath = '//*/img') %>%
  html_attr('src')
imgsrc