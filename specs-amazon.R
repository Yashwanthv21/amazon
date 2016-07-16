library("rvest")

myArgs <- commandArgs(trailingOnly = TRUE)

productPage <- read_html(myArgs)
#productPage <- read_html('http://www.amazon.in/Apple-Macbook-MD101HN-Mavericks-Graphics/dp/B00DKMCB20/ref=sr_1_1?ie=UTF8&qid=1465156754&sr=8-1&keywords=mac+book')
#specs <- productPage %>% html_nodes(".col1 .label") %>% html_text()
#capture.output(productPage %>% html_nodes(".col1 .label") %>% html_text(), file="specs.txt",append=FALSE);
#print(specs)
#capture.output(productPage %>% html_node("#title_feature_div") %>% html_text(), file="product-title.txt", append=FALSE)

#title <- productPage %>% html_node("#title_feature_div") %>% html_text()
#print(title)

userReviewsPage <- productPage %>% html_nodes(".a-link-emphasis") %>% html_attr("href")
#print(userReviewsPage[1])
userReviewsPage = userReviewsPage[1]
while (userReviewsPage != "http://www.amazon.in") { 

	allReviews <- read_html(userReviewsPage);
	capture.output( allReviews %>%  html_nodes(".review-text")  %>%  html_text(),file="userReviews.txt", append=TRUE)

	userReviewsPage = allReviews %>% html_nodes(".a-last a") %>% html_attr("href") 
	userReviewsPage = paste("http://www.amazon.in",userReviewsPage,sep="")

Sys.sleep(3)
}
