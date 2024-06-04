from bing_image_downloader import downloader


def DowloadImages(myQuery, myQuantidade):
    downloader.download(
        myQuery, 
        limit=myQuantidade, 
        output_dir='dataset', 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=myQuantidade, 
        verbose=True
        )
    
if __name__ == "__main__":
    myQueries = []
    myQueries.append(["sacolas plásticas no mar", 10])
    myQueries.append(["poluição marinha", 10])
    myQueries.append(["lixo marinho", 10])
    myQueries.append(["garrafas pet no mar", 10])
    myQueries.append(["tartarugas sacola plástica", 10])
    myQueries.append(["rede de pesca em tartaruga", 10])
    myQueries.append(["plático poluição mar", 10])
    myQueries.append(["água viva", 10])

    for myQuery in myQueries:
        DowloadImages(myQuery[0], myQuery[1])
