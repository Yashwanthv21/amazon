library("rvest")
productPage <- read_html("http://www.amazon.in/Moto-Plus-4th-Gen-Black/dp/B01DDP7GZK/ref=sr_1_1?s=electronics&ie=UTF8&qid=1468597837&sr=1-1&keywords=moto+g")
image <- productPage %>% html_nodes("#imgTagWrapperId") %>% html_attr("href")
print image