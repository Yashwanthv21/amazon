library("rvest")


productPage <- read_html("http://www.amazon.in/Moto-Plus-4th-Gen-Black/dp/B01DDP7GZK/ref=pd_cp_147_2?ie=UTF8&refRID=1CCPKF13D6REPDGAGDVY")

specs <- productPage %>% html_nodes(".col1 td") %>% html_text()
