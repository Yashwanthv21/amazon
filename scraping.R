library("rvest")

myArgs <- commandArgs(trailingOnly = TRUE)

productPage <- read_html("http://www.amazon.in/Moto-Plus-4th-Gen-Black/dp/B01DDP7GZK/ref=pd_cp_147_2?ie=UTF8&refRID=1CCPKF13D6REPDGAGDVY")
#productPage <- read_html('http://www.amazon.in/Apple-Macbook-MD101HN-Mavericks-Graphics/dp/B00DKMCB20/ref=sr_1_1?ie=UTF8&qid=1465156754&sr=8-1&keywords=mac+book')
#specs <- productPage %>% html_nodes(".col1 .label") %>% html_text()

#print(specs)


img <- productPage %>% html_nodes(".col1 td") %>% html_text()
img