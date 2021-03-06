import PAsearchSites
import PAgenres
import PAactors

def search(results,encodedTitle,title,searchTitle,siteNum,lang,searchByDateActor,searchDate,searchSiteID):
    if searchSiteID != 9999:
        siteNum = searchSiteID
    searchResults = HTML.ElementFromURL(PAsearchSites.getSearchSearchURL(siteNum) + encodedTitle)
    for searchResult in searchResults.xpath('//article[@class="release-card scene"]'):
        titleNoFormatting = searchResult.xpath('./div[@class="card-title/a"]')[0].text_content().strip()
        curID = searchResult.xpath('./div[@class="card-title/a"]')[0].get('href').replace('/','_').replace('?','!')
        subSite = searchResult.xpath('./div[@class="site-domain"]')[0].text_content().strip()
        releaseDate = parse(searchResult.xpath('./div[@class="release-date"]')[0].text_content().strip()).strftime('%Y-%m-%d')
        if searchDate:
            score = 100 - Util.LevenshteinDistance(searchDate, releaseDate)
        else:
            score = 100 - Util.LevenshteinDistance(searchTitle.lower(), titleNoFormatting.lower())
        results.Append(MetadataSearchResult(id = curID + "|" + str(siteNum), name = titleNoFormatting + " [SexyHub/"+subSite+"] " + releaseDate, score = score, lang = lang))

    return results

def update(metadata,siteID,movieGenres,movieActors):
    Log('******UPDATE CALLED*******')

    url = str(metadata.id).split("|")[0].replace('_','/').replace('?','!').replace('/vids.html','_vids.html')
    detailsPageElements = HTML.ElementFromURL(url)
    art = []
    metadata.collections.clear()
    movieGenres.clearGenres()
    movieActors.clearActors()

    # Studio
    metadata.studio = 'Studio Name here'

    # Title
    metadata.title = detailsPageElements.xpath('//title')[0].text_content().strip()

    #Tagline and Collection(s)
    tagline = PAsearchSites.getSearchSiteName(siteID).strip()
    metadata.tagline = tagline
    metadata.collections.add(tagline)

    # Genres
    genres = detailsPageElements.xpath('//span[@class="update_tags"]/a')
    if len(genres) > 0:
        for genreLink in genres:
            genreName = genreLink.text_content().strip().lower()
            movieGenres.addGenre(genreName)

    # Release Date
    date = detailsPageElements.xpath('//div[@class="cell update_date"]')[0].text_content().strip()
    if len(date) > 0:
        date_object = parse(date)
        metadata.originally_available_at = date_object
        metadata.year = metadata.originally_available_at.year

    # Actors
    actors = detailsPageElements.xpath('span[@class="update_models"]/a')
    if len(actors) > 0:
        for actorLink in actors:
            actorName = str(actorLink.text_content().strip())
            actorPageURL = actorLink.get("href")
            actorPage = HTML.ElementFromURL(actorPageURL)
            actorPhotoURL = actorPage.xpath('//img[@class="model_bio_thumb"]')[0].get("src")
            if 'http' not in actorPhotoURL:
            	actorPhotoURL = PAsearchSites.getSearchBaseURL(siteID) + actorPhotoURL
            movieActors.addActor(actorName,actorPhotoURL)

    ### Posters and artwork ###

    # Video trailer background image
    try:
        twitterBG = detailsPageElements.xpath('//meta[@name="twitter:image"]')[0].get('content')
        art.append(twitterBG)
    except:
        pass

    # Scene photos page
    try:
        photoPageUrl = PAsearchSites.getSearchBaseURL(siteID)+detailsPageElements.xpath('//a[@class="photo_page"]')[0].get('href')
        photoPage = HTML.ElementFromURL(photoPageUrl)
        unlockedPhotos = photoPage.xpath('//a[@class="imgLink"]')
        for unlockedPhoto in unlockedPhotos:
            if 'http' not in unlockedPhoto.get('href'):
                art.append(PAsearchSites.getSearchBaseURL(siteID) + unlockedPhoto.get('href'))
            else:
                art.append(unlockedPhoto.get('href'))
    except:
        pass

    j = 1
    Log("Artwork found: " + str(len(art)))
    for posterUrl in art:
        if not PAsearchSites.posterAlreadyExists(posterUrl,metadata):            
            #Download image file for analysis
            try:
                img_file = urllib.urlopen(posterUrl)
                im = StringIO(img_file.read())
                resized_image = Image.open(im)
                width, height = resized_image.size
                #Add the image proxy items to the collection
                if width > 1 or height > width:
                    # Item is a poster
                    metadata.posters[posterUrl] = Proxy.Preview(HTTP.Request(posterUrl, headers={'Referer': 'http://www.google.com'}).content, sort_order = j)
                if width > 100 and width > height:
                    # Item is an art item
                    metadata.art[posterUrl] = Proxy.Preview(HTTP.Request(posterUrl, headers={'Referer': 'http://www.google.com'}).content, sort_order = j)
                j = j + 1
            except:
                pass

    return metadata