class PhoenixActors:
    actorsTable = None
    photosTable = None
    actorsNum = 0
    def __init__(self):
        self.actorsTable = [None] * 100
        self.photosTable = [None] * 100
        self.actorsNum = 0
    def addActor(self,newActor,newPhoto):
        self.actorsTable[self.actorsNum] = newActor
        self.photosTable[self.actorsNum] = newPhoto
        self.actorsNum = self.actorsNum + 1
    def clearActors(self):
        self.actorsNum = 0
    def processActors(self,metadata):
        actorsProcessed = 0
        while actorsProcessed < self.actorsNum:
            skip = False
            # Save the potentional new Actor or Actress to a new variable, replace &nbsp; with a true space, and strip off any surrounding whitespace
            newActor = self.actorsTable[actorsProcessed].replace("\xc2\xa0", " ").replace(',','').strip().title()
            newPhoto = self.photosTable[actorsProcessed].strip()

            ##### Skip an actor completely; this could be used to filter out male actors if desired
            if "Bad Name" == newActor:
                skip = True

            ##### Replace by actor name; for actors that have different aliases in the industry
            if "Josephine" == newActor or "Conny" == newActor or "Conny Carter" == newActor or "Connie" == newActor:
                newActor = "Connie Carter"
            if "Doris Ivy" == newActor:
                newActor = "Gina Gerson"
            if "Anjelica" == newActor or "Ebbi" == newActor or "Abby H" == newActor or "Katherine A" == newActor:
                newActor = "Krystal Boyd"
            if "Nathaly" == newActor or "Nathalie Cherie" == newActor:
                newActor = "Nathaly Cherie"
            if newActor == "Alex D":
                newActor = "Alex D."
            if "Crissy Kay" == newActor or "Emma Hicks" == newActor or "Emma Hixx" == newActor:
                newActor = "Emma Hix"
            if newActor == "Elsa Dream":
                newActor = "Elsa Jean"
            if newActor == "Hailey Reed":
                newActor = "Haley Reed"
            if "Lilly LaBeau" == newActor or "Lilly Labuea" == newActor or "Lily La Beau" == newActor or "Lily Lebeau" == newActor or "Lily Luvs" == newActor:
                newActor = "Lily Labeau"
            if "Noe Milk" == newActor or "Noemiek" == newActor:
                newActor = "Noemilk"
            if "Riley Jenson" == newActor or "Riley Anne" == newActor or "Rilee Jensen" == newActor:
                newActor = "Riley Jensen"
            if "Stella Bankxxx" == newActor or "Stella Ferrari" == newActor:
                newActor = "Stella Banxxx"
            if newActor == "Lara Craft":
                newActor = "Lora Craft"
            if newActor == "Amia Moretti":
                newActor = "Amia Miley"
            if newActor == "Abby Rains":
                newActor = "Abbey Rain"

            ##### Replace by site + actor; use when an actor just has an alias or abbreviated name on one site
            if metadata.studio == "21Sextury" and "Abbie" == newActor:
                newActor = "Krystal Boyd"
            if metadata.studio == "Babes" and "Angelica" == newActor:
                newActor = "Krystal Boyd"
            if metadata.studio == "LegalPorno" and "Abby" == newActor:
                newActor = "Krystal Boyd"
            if metadata.studio == "Joymii":
                if newActor == "Valentina":
                    newActor = "Valentina Nappi"
                if newActor == "Gina G.":
                    newActor = "Gina Gerson"
                if newActor == "Tasha R.":
                    newActor = "Tasha Reign"
                if newActor == "Piper P.":
                    newActor = "Piper Perri"
                if newActor == "Lara":
                    newActor = "Dido Angel"
                if newActor == "Cindy L.":
                    newActor = "Cindy Carson"
                if newActor == "Denisa":
                    newActor = "Denisa Heaven"
                if newActor == "Abigail":
                    newActor = "Abigaile Johnson"
            if metadata.studio == "Nubiles":
                if newActor == "Abbey":
                    newActor = "Amia Miley"
                if newActor == "Addie":
                    newActor = "Addie Moore"
                if newActor == "Addison":
                    newActor = "Addison Rose"
                if newActor == "Adella":
                    newActor = "Adel Bye"
                if newActor == "Adelle":
                    newActor = "Keira Albina"
                if newActor == "Adri":
                    newActor = "Sandra Bina"
                if newActor == "Adrianne":
                    newActor = "Adrianna Gold"
                if newActor == "Agnessa":
                    newActor = "Nessa Shine"
                if newActor == "Alana":
                    newActor = "Jayme Langford"
                if newActor == "Alanaleigh":
                    newActor = "Alana Leigh"
                if newActor == "Alana G":
                    newActor = "Alana Jade"
                if newActor == "Alena":
                    newActor = "Lucie Theodorova"
                if newActor == "Aletta":
                    newActor = "Aletta Ocean"
                if newActor == "Alexa":
                    newActor = "Aleska Diamond"
                if newActor == "Alexcia":
                    newActor = "Black Panther"
                if newActor == "Alexiasky":
                    newActor = "Alexia Sky"
                if newActor == "Alexis":
                    newActor = "Alexis Love"
                if newActor == "Aliana":
                    newActor = "Alice Miller"
                if newActor == "Alicia":
                    newActor = "Alicia Angel"
                if newActor == "Alliehaze":
                    newActor = "Allie Haze"
                if newActor == "Allyann":
                    newActor = "Ally Ann"
                if newActor == "Allyssa":
                    newActor = "Allyssa Hall"
                if newActor == "Alyssia":
                    newActor = "Nikita Black"
                if newActor == "Amai":
                    newActor = "Amai Liu"
                if newActor == "Amalie":
                    newActor = "Anita Pearl"
                if newActor == "Amber":
                    newActor = "Roxy Carter"
                if newActor == "Ami":
                    newActor = "Ami Emerson"
                if newActor == "Amy":
                    newActor = "Amy Reid"
                if newActor == "Amybrooke":
                    newActor = "Amy Brooke"
                if newActor == "Amysativa":
                    newActor = "Amy Sativa"
                if newActor == "Andie":
                    newActor = "Andie Valentino"
                if newActor == "Andrea":
                    newActor = "Jenny Sanders"
                if newActor == "Angela":
                    newActor = "Angie Emerald"
                if newActor == "Angelica":
                    newActor = "Black Angelika"
                if newActor == "Angelina":
                    newActor = "Nadia Taylor"
                if newActor == "Angelinaash":
                    newActor = "Angelina Ashe"
                if newActor == "Angellina":
                    newActor = "Angelina Brooke"
                if newActor == "Angie":
                    newActor = "Yulia Bright"
                if newActor == "Aniya":
                    newActor = "Stasia"
                if newActor == "Annabelle":
                    newActor = "Annabelle Lee"
                if newActor == "Annastevens":
                    newActor = "Anna Stevens"
                if newActor == "Anne":
                    newActor = "Playful Ann"
                if newActor == "Annette":
                    newActor = "Annette Allen"
                if newActor == "Annika":
                    newActor = "Annika Eve"
                if newActor == "Anoli":
                    newActor = "Anoli Angel"
                if newActor == "April":
                    newActor = "April Aubrey"
                if newActor == "Apriloneil":
                    newActor = "April O'Neil"
                if newActor == "Ariadna":
                    newActor = "Ariadna Moon"
                if newActor == "Ariel":
                    newActor = "Ariel Rebel"
                if newActor == "Ashlee":
                    newActor = "Ashlee Allure"
                if newActor == "Ashleyjane":
                    newActor = "Ashley Jane"
                if newActor == "Ashlynrae":
                    newActor = "Ashlyn Rae"
                if newActor == "Asuna":
                    newActor = "Asuna Fox"
                if newActor == "Athina":
                    newActor = "Tyra Moon"
                if newActor == "Aundrea":
                    newActor = "Andrea Anderson"
                if newActor == "Austin":
                    newActor = "Austin Reines"
            if metadata.studio == "TeamSkeet":
                if newActor == "Ada S":
                    newActor = "Ada Sanchez"
                if newActor == "Ariel R":
                    newActor = "Ariel Rose"
                if newActor == "Artemida":
                    newActor = "Valentina Cross"
                if newActor == "Arika":
                    newActor = "Arika Foxx"
                if newActor == "Ariana":
                    newActor = "Emma Brown"
                if newActor == "Ariadna":
                    newActor = "Ariadna Moon"
                if newActor == "Argentina":
                    newActor = "Lisa Smiles"
                if newActor == "Anfisa":
                    newActor = "Nicoline"
                if newActor == "Aliya":
                    newActor = "Rima"
                if newActor == "Ava":
                    newActor = "Ava Dalush"
                if newActor == "Avery":
                    newActor = "Diana Dali"
                if newActor == "Avina":
                    newActor = "Sunny Rise"
                if newActor == "Bailey":
                    newActor = "Lena Love"
                if newActor == "Bella":
                    newActor = "Bella Rossi"
                if newActor == "Betty":
                    newActor = "Camila"
                if newActor == "Jane":
                    newActor = "Camila"
                if newActor == "Briana":
                    newActor = "Milana Blanc"
                if newActor == "Brianna":
                    newActor = "Milana Blanc"
                if newActor == "Callie":
                    newActor = "Callie Nicole"
                if newActor == "Carre":
                    newActor = "Candy C"
                if newActor == "Casi J":
                    newActor = "Casi James"
                if newActor == "Catania":
                    newActor = "Jessi Gold"
                if newActor == "Colette":
                    newActor = "Inga E"
                if newActor == "Darla":
                    newActor = "Alektra Sky"
                if newActor == "Dinara":
                    newActor = "Arian Joy"
                if newActor == "Dunya":
                    newActor = "Alice Marshall"
                if newActor == "Ema":
                    newActor = "Chloe Blue"
                if newActor == "Erica":
                    newActor = "Kristall Rush"
                if newActor == "Sasha":
                    newActor = "Kristall Rush"
                if newActor == "Eva":
                    newActor = "Mia Reese"
                if newActor == "Fantina":
                    newActor = "Mariya C"
                if newActor == "Olga":
                    newActor = "Mariya C"
                if newActor == "Gabi":
                    newActor = "Izi"
                if newActor == "Gerta":
                    newActor = "Erika Bellucci"
                if newActor == "Hannah":
                    newActor = "Milana Fox"
                if newActor == "Jade":
                    newActor = "Netta"
                if newActor == "Jana":
                    newActor = "Janna"
                if newActor == "Janette":
                    newActor = "Lisa C"
                if newActor == "Joanna":
                    newActor = "Joanna Pret"
                if newActor == "Jordan":
                    newActor = "Rebeca Taylor"
                if newActor == "Kail":
                    newActor = "Kortny"
                if newActor == "Kajira":
                    newActor = "Kajira Bound"
                if newActor == "Kameya":
                    newActor = "Sandra Luberc"
                if newActor == "Katherine":
                    newActor = "Selena Stuart"
                if newActor == "Katie C":
                    newActor = "Katie Cummings"
                if newActor == "Katie K":
                    newActor = "Katie Kay"
                if newActor == "Kendall":
                    newActor = "Alison Faye"
                if newActor == "Kimberly":
                    newActor = "Pola Sunshine"
                if newActor == "Krista":
                    newActor = "Krista Evans"
                if newActor == "Lily L":
                    newActor = "Lily Labeau"
                if newActor == "Lada":
                    newActor = "Jay Dee"
                if newActor == "Luna":
                    newActor = "Rita Rush"
                if newActor == "Lusil":
                    newActor = "Ananta Shakti"
                if newActor == "Mackenzie":
                    newActor = "Alice Smack"
                if newActor == "Madelyn":
                    newActor = "Anna Taylor"
                if newActor == "Madison":
                    newActor = "Karina Grand"
                if newActor == "Magda":
                    newActor = "Taissia Shanti"
                if newActor == "Mai":
                    newActor = "Mai Ly"
                if newActor == "Mara":
                    newActor = "Marly Romero"
                if newActor == "Mariah":
                    newActor = "Aubree Jade"
                if newActor == "Mina":
                    newActor = "Mila Beth"
                if newActor == "Nadya":
                    newActor = "Nadia Bella"
                if newActor == "Seren":
                    newActor = "Nadia Bella"
                if newActor == "Nika":
                    newActor = "Sabrina Moor"
                if newActor == "Nora R":
                    newActor = "Sheri Vi"
                if newActor == "Parvin":
                    newActor = "Adelle Booty"
                if newActor == "Peachy":
                    newActor = "Margarita C"
                if newActor == "Petra":
                    newActor = "Dominica Phoenix"
                if newActor == "Rahyndee":
                    newActor = "Rahyndee James"
                if newActor == "Rebecca":
                    newActor = "Anita Sparkle"
                if newActor == "Riley J":
                    newActor = "Riley Jensen"
                if newActor == "Rosanna":
                    newActor = "Kate G."
                if newActor == "Sadine G":
                    newActor = "Sadine Godiva"
                if newActor == "Sarai":
                    newActor = "Sarai Keef"
                if newActor == "Serena":
                    newActor = "Carol Miller"
                if newActor == "Sheila":
                    newActor = "Marina Visconti"
                if newActor == "Sierra":
                    newActor = "Sierra Sanders"
                if newActor == "Skye":
                    newActor = "Skye West"
                if newActor == "Soleil":
                    newActor = "Soliel Marks"
                if newActor == "Sophia":
                    newActor = "Grace C"
                if newActor == "Stella":
                    newActor = "Stella Banxxx"
                if newActor == "Tori":
                    newActor = "Lola Taylor"
                if newActor == "Veiki":
                    newActor = "Miranda Deen"
                if newActor == "Viki":
                    newActor = "Bonnie Shai"
                if newActor == "Vilia":
                    newActor = "Lilu Tattoo"
                if newActor == "Viviana":
                    newActor = "Autumn Viviana"
                if newActor == "Yanie":
                    newActor = "Milla Yul"
                if newActor == "Yoga":
                    newActor = "Arya Fae, Megan Sage, and Nina North"
                if newActor == "Zarina":
                    newActor = "Aruna Aghora"
                if newActor == "Zoi":
                    newActor = "Liona Levi"

            if not skip:
                if newPhoto == '':
                    newPhoto = actorDBfinder(newActor)
                Log("Actor: "+newActor+" "+newPhoto)

                role = metadata.roles.new()
                role.name = newActor
                role.photo = newPhoto
            actorsProcessed = actorsProcessed + 1

# https://www.indexxx.com/models/59558/anjelica-1/

# For sites without a proper actor profile picture, this method looks in external databases based on actorName            
def actorDBfinder(actorName):
    try:
        databaseName = "AdultDVDEmpire"
        actorsearch = HTML.ElementFromURL("https://www.adultdvdempire.com/performer/search?q=" + actorName.replace(' ','%20'))
        actorPageURL = actorsearch.xpath('//div[@class="col-xs-6 col-sm-3 grid-item grid-item-performer grid-item-performer-145"]/a')[0].get("href")
        actorPageURL = "https://www.adultdvdempire.com" + actorPageURL
        actorPage = HTML.ElementFromURL(actorPageURL)
        actorPhotoURL = actorPage.xpath('//a[@class="fancy headshot"]')[0].get("href")
        Log(actorName + " found in " + databaseName)
        Log("PhotoURL: " + actorPhotoURL)
    except:
        try:
            databaseName = "Boobpedia"
        # Code Removed - website has standardized actor page
            # searchURL = "http://www.boobpedia.com/wiki/index.php?title=Special%3ASearch&profile=default&search=" + actorName.replace(' ', '+') + "&fulltext=Search"
            # Log(databaseName + "-searchURL: " + searchURL)
            # actorSearch = HTML.ElementFromURL(searchURL)
            # actorPageURL = actorSearch.xpath('//div[@class="mw-search-result-heading"]/a')[0].get("href")
            # actorPageURL = "http://www.boobpedia.com" + actorPageURL
            actorPageURL = "http://www.boobpedia.com/boobs/" + actorName.lower().replace(" ", "_")
            # Log(databaseName + "-PageURL: " + actorPageURL)
            actorPage = HTML.ElementFromURL(actorPageURL)
            actorPhotoURL = actorPage.xpath('//table[@class="infobox"]//a[@class="image"]//img')[0].get("src")
            actorPhotoURL = "http://www.boobpedia.com" + actorPhotoURL
            Log(actorName + " found in " + databaseName)
            Log("PhotoURL: " + actorPhotoURL)
        except:
            try:
                databaseName = "Babes and Stars"
                # searchURL = "http://www.babesandstars.com/search/?t=models&q=" + actorName.replace(' ','+')
                # Log(databaseName + "-searchURL: " + searchURL)
                # actorSearch = HTML.ElementFromURL(searchURL)
                # actorPageURL = actorSearch.xpath('//div[contains(@class,"thumb")]//a')[0].get("href")
                actorPageURL = "http://www.babesandstars.com/" + actorName[0:1] + "/" + actorName.lower().replace(" ","-") +"/"
                actorPage = HTML.ElementFromURL(actorPageURL)
                actorPhotoURL = actorPage.xpath('//div[@class="profile"]//div[@class="thumb"]/img')[0].get("src")
                Log(actorName + " found in " + databaseName)
                Log("PhotoURL: " + actorPhotoURL)
            except:
                try:
                    databaseName = "IAFD"
                    searchURL = "http://www.iafd.com/results.asp?searchtype=comprehensive&searchstring=" + actorName.replace(' ', '+')
                    actorSearch = HTML.ElementFromURL(searchURL)
                    actorPageURL = actorSearch.xpath('//table[@id="tblFem"]//tbody//a')[0].get("href")
                    actorPageURL = "http://www.iafd.com" + actorPageURL
                    actorPage = HTML.ElementFromURL(actorPageURL)
                    actorPhotoURL = actorPage.xpath('//div[@id="headshot"]//img')[0].get("src")
                    Log(actorName + " found in " + databaseName)
                    Log("PhotoURL: " + actorPhotoURL)
                except:
                    try:
                        databaseName = "Babepedia"
                        # searchURL = "https://www.babepedia.com/search/" + actorName.replace(' ', '%20')
                        # Log(databaseName + "-searchURL: " + searchURL)
                        # actorSearch = HTML.ElementFromURL(searchURL)
                        # actorPageURL = actorSearch.xpath('//div[contains(@class,"thumbshot")]//a')[0].get("href")
                        # actorPageURL = "http://www.babepedia.com" + actorPageURL
                        # actorPageURL = "http://www.babepedia.com/babe/" + actorName.lower().replace(" ", "_")
                        # actorPage = HTML.ElementFromURL(actorPageURL)
                        # actorPhotoURL = actorPage.xpath('//div[@id="profimg"]//a')[0].get("href")
                        # actorPhotoURL = "http://www.babepedia.com" + actorPhotoURL
                        actorPhotoURL = "http://www.babepedia.com/pics/" + actorName.title().replace(" ", "%20") + ".jpg"
                        Log(actorName + " found in " + databaseName)
                        Log("PhotoURL: " + actorPhotoURL)
                    except:
                        Log(actorName + "not found.")
                        actorPhotoURL = ""
    return actorPhotoURL
