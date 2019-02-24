import random
def bullshit_data():
    
    number = random.randint(1,5)
    names = {
        1:"Class Dojo" , 2:"Codecademy" ,3:"Flipgrid", 4:"Scratch", 5:"Kahn Academy", 6:"Edpuzzle", 7:"Book Creator", 8:"Newsela", 9:"Epic!", 10:"Seesaw",
        11:"Quizlet", 12:"Google Classroom"
    }
    URLs = {
        1:"https://www.classdojo.com/", 2:"https://www.codecademy.com/", 3:"https://info.flipgrid.com/", 4:"https://scratch.mit.edu/", 5:"https://www.khanacademy.org/", 6:"https://edpuzzle.com/", 7:"https://bookcreator.com/",
        8:"https://newsela.com/", 9:"https://www.getepic.com/", 10:"https://web.seesaw.me/", 11:"https://quizlet.com/", 12:"https://edu.google.com/intl/en/products/classroom/?modal_active=none"
    }
    logo = {
        1:"https://static.classdojo.com/img/page_learn-more/top-asset-2@2x.png",
        2:"https://www.codecademy.com/webpack/44e01805165bfde4e6e4322c540abf81.svg",
        3:"https://static.flipgrid.com/fg-svgs/flipgrid_logo.svg",
        4:"https://scratch.mit.edu/static/assets/1e9652bec24bcaacf5285be19746a750.svg",
        5:"https://cdn.kastatic.org/images/khan-logo-dark-background.new.png",
        6:"https://edpuzzle.imgix.net/edpuzzle-logos/vertical-logo.png",
        7:"http://37wz5x2r8vbh3om46wmfhy71-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Book-Creator-colour-logo.png",
        8:"https://www.iu1.org/images/partners_vendors/newselalogo500x500.png",
        9:"https://www.iu1.org/images/partners_vendors/newselalogo500x500.png",
        10:"https://www.iu1.org/images/partners_vendors/newselalogo500x500.png",
        11:"https://www.iu1.org/images/partners_vendors/newselalogo500x500.png",
        12:"https://www.iu1.org/images/partners_vendors/newselalogo500x500.png"
    }
    
    phrases = {
        1:"This technology makes students utilize ", 2:"A large part of using this recource is allowing the students to utilize ", 3:"A recource superb for ", 4:"Re-imagining "
    }
    buzzwords = {
        
        1:"active learning", 2:"project oriented learning", 3:"choice created learning", 4:"creative learning"
    }
    selector = random.randint(1,6)
    name = names[selector]
    URL = URLs[selector]
    for i in range(2):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(2):
                        for n in range(4):
                            for o in range(2):
                                select = random.randint(1,4)
                                buzzword= buzzwords[select]
                                phraze = phrases[select]
                                des = phraze+buzzword
                          
                                if j==3:
                                        des+=" and allowing you to teach students through collaboration "
                                if j==2:
                                        des+=" and allowing students to leverage technology to enhance their other capabilities in a new way "
                                if j==1:
                                        des+=" and allowing students to demonstrate knowledge "
                                else:
                                    des+=""
                                if n==1:
                                    des+=". This technology allows your students to express themselves by using video as a medium for education"
                                if n==3:
                                    des+=". This technology allows your students use technology to include a textual medium in their education"
                                if n==2:
                                    des+=". Allowing students to use audio or podcasts to express themselves and learn new things is pivotal to this application"
                                if n==4:
                                    des+=". Allowing your students to use this platform will teach them about the world of technology and coding"
                                else: 
                                    des+=""
                                if o==1:
                                    des+= ". Plus it's free!"
                                else:
                                    des+= ""

                                number = random.randint(1,5)
                                selector = random.randint(1,12)
                                log = logo[selector]
                                name = names[selector]
                                URL = URLs[selector]
                                print "(\"" +name+"\", \""+URL+ "\", "+str((i+1))+str((j+1))+str((k+1))+str((l+1))+str((m+1))+str((n+1))+str((o+1))+", "+str(number)+", \""+des+"\", \""+log+"\"),"


bullshit_data();

