
library("rvest")
userReviewsPage = "http://www.amazon.in/Moto-Plus-4th-Gen-Black/product-reviews/B01DDP7GZK/ref=cm_cr_getr_d_paging_btm_38?showViewpoints=1&pageNumber=38"
allReviews <- read_html(userReviewsPage);
allReviews %>%  html_nodes(".review-text")