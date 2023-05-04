from django.db import models

# Create your models here.
class Product(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    product_id=models.AutoField
    path = models.CharField(max_length=108, default = "/Vyas/Prodview1/")
    product_name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pulish_date=models.DateField()
    Ram = models.CharField(max_length=100,default="")
    Rom = models.CharField(max_length=100,default="")
    Camera_rear = models.CharField(max_length=200,default="")
    Camera_front = models.CharField(max_length=200,default="")
    Processor = models.CharField(max_length=100,default = "")
    Battery = models.CharField(max_length=50,default="")
    Screen_size = models.CharField(max_length=50, default="")
    Strike_price = models.CharField(max_length=50, default="")
    product_image = models.ImageField(upload_to="Vyas/images", default="")
    product_link = models.CharField(max_length=1000, default="")
    
    def __str__(self):
        return self.product_name

class Music(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    music_id=models.AutoField
    prod_path = models.CharField(max_length=108, default = "/Vyas/Music/")
    music_name=models.CharField(max_length=100)
    music_description=models.CharField(max_length=1000)
    music_category = models.CharField(max_length=50, default="")
    music_subcategory = models.CharField(max_length=50, default="")
    music_price = models.IntegerField(default=0)
    release_date=models.DateField()
    band = models.CharField(max_length=1000, default="")
    special_mention = models.CharField(max_length=1000, default="")
    list_songs = models.CharField(max_length=500, default="")
    music_image = models.ImageField(upload_to="Vyas/images", default="")
    music_link = models.CharField(max_length=1000, default="")
    music_strike_price = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.music_name
 
class Ayurveda(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    ayurveda_id=models.AutoField
    herb_name=models.CharField(max_length=100,default="")
    herb_strike_price = models.CharField(max_length=50, default="")
    use = models.CharField(max_length=1000, default="")
    herb_description=models.CharField(max_length=1000, default="")
    herb_category = models.CharField(max_length=50, default="")
    herb_subcategory = models.CharField(max_length=50, default="")
    herb_price = models.IntegerField(default=0)
    herb_image = models.ImageField(upload_to="Vyas/images", default="")
    herb_link = models.CharField(max_length=1000, default="")
    prod_path = models.CharField(max_length=108, default = "/Vyas/ayurveda/")

    def __str__(self):
        return self.herb_name
    
class Education(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    education_id=models.AutoField
    prod_path = models.CharField(max_length=108, default = "/Vyas/education/")
    education_name=models.CharField(max_length=100,default="")
    education_strike_price = models.CharField(max_length=50, default="")
    Company = models.CharField(max_length=1000, default="")
    education_description=models.CharField(max_length=1000, default="")
    education_category = models.CharField(max_length=50, default="")
    education_subcategory = models.CharField(max_length=50, default="")
    education_price = models.IntegerField(default=0)
    education_image = models.ImageField(upload_to="Vyas/images", default="")
    education_link = models.CharField(max_length=1000, default="")
    author_name = models.CharField(max_length=100, default="")
    books_in_pack = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.education_name
 

class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50,default='')
    email = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=70, default = '')
    description = models.CharField(max_length=4000, default = '')
    shop = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name

class Clothing(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")    
    product_id=models.AutoField
    cloth_name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    prod_path = models.CharField(max_length=108, default = "/Vyas/Clothing/")
    category = models.CharField(max_length=50)          #category - Upper Lower Footwear Watches    
    size = models.CharField(max_length=2,default="")
    gender = models.CharField(max_length=6,default="")
    foot_size = models.IntegerField(default=0)
    
    warranty = models.IntegerField(default=0)
        

    price = models.IntegerField(default=0)
    publish_date=models.DateField()
    product_image = models.ImageField(upload_to="Vyas/images", default="")
    off_site = models.URLField(max_length=1000,default="")
    
    def __str__(self):
        return self.cloth_name



class Home_Appliances(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    product_id=models.AutoField
    appliance_name=models.CharField(max_length=100)
    prod_path = models.CharField(max_length=108, default = "/Vyas/Home_Appliances/")
    
    brand_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)            #category - washing machine , television , air conditioners, security cameras
    
    wm_capacity = models.IntegerField(default=0)
    star = models.IntegerField(default=0)
    ac_type = models.CharField(max_length=100,default="")            #split or window
    ac_ton = models.IntegerField(default=0) 
    tv_size = models.IntegerField(default=0)
    tv_resolution = models.IntegerField(default=0)
    tv_refresh_rate= models.IntegerField(default=0)

    d1 = models.CharField(max_length=1000)
    d2 = models.CharField(max_length=1000)
    d3 = models.CharField(max_length=1000)

    price = models.IntegerField(default=0)
    publish_date=models.DateField()
    product_image = models.ImageField(upload_to="Vyas/images", default="")
    off_site = models.URLField(max_length=1000,default="")
    def __str__(self):
        return self.appliance_name

class software(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    product_id=models.AutoField
    prod_path = models.CharField(max_length=108, default = "/Vyas/Software/")
    soft_name =models.CharField(max_length=100)
    brand_name =models.CharField(max_length=100)
    category=models.CharField(max_length=100)             #category -  productivity, antivirus, gaming 
    app_size = models.IntegerField(default=0)
    no_of_downloads = models.CharField(max_length=10 , default ="0")
    age_required = models.IntegerField(default=0)
    pd_os = models.CharField(max_length=100,default="")         #mac windows linux
    anti_os = models.CharField(max_length=100,default="")
    anti_subs = models.IntegerField(default=0)
    gaming_platform = models.CharField(max_length=100,default="")     #pc playstiation xbox etc
    price = models.IntegerField(default=0)
    publish_date=models.DateField()
    product_image = models.ImageField(upload_to="Vyas/images", default="")
    off_site = models.URLField(max_length=1000,default="")
    def __str__(self):
        return self.soft_name


class Sports(models.Model):
    product_id=models.AutoField
    sub_desc = models.CharField(max_length=1000,default="")
    prod_path = models.CharField(max_length=108, default = "/Vyas/Sports/")
    item_name =models.CharField(max_length=100)
    brand_name =models.CharField(max_length=100)
    associated_sport = models.CharField(max_length=100,default=" ")
    category=models.CharField(max_length=100,default=" ")                              # football cricket chess table tennis weightlifting
    
    cricketbat_size = models.CharField(max_length=100,default="")
    cricketbat_willow = models.CharField(max_length=100,default="")
    
    football_size = models.IntegerField(default=0)
    football_weight = models.IntegerField(default=0)

    tt_material = models.CharField(max_length=100,default=" ")

    d1 = models.CharField(max_length=1000,default=" ")
    d2 = models.CharField(max_length=1000,default=" ")
    d3 = models.CharField(max_length=1000,default=" ")

    price = models.IntegerField(default=0)
    publish_date=models.DateField()
    product_image = models.ImageField(upload_to="Vyas/images", default="")
    off_site = models.URLField(max_length=1000,default="")
    def __str__(self):
        return self.item_name



class grocery(models.Model):
    product_id=models.AutoField
    sub_desc = models.CharField(max_length=1000,default="")
    prod_path = models.CharField(max_length=108, default = "/Vyas/grocery/")
    product_name=models.CharField(max_length=5000)
    category= models.CharField(max_length=5000, default="")
    sub_category= models.CharField(max_length=5000, default="")
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=300000)
    publish_date=models.DateField()
    image= models.ImageField(upload_to="Vyas/images",default="")
    def __str__(self):
        return self.product_name


class Book(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    book_id=models.AutoField
    prod_path = models.CharField(max_length=108, default = "/Vyas/Book/")
    book_name=models.CharField(max_length=50,default="")
    Class=models.CharField(max_length=50,default="")
    subject= models.CharField(max_length=50, default="")
    author= models.CharField(max_length=50, default="")
    book_price=models.IntegerField(default=0)
    book_description=models.CharField(max_length=300000, default="")
    publisher=models.CharField(max_length=60,default="")
    book_image= models.ImageField(upload_to="Vyas/images",default="")
    


    def __str__(self):
        return self.book_name


class PCH(models.Model):
    PCH_id=models.AutoField
    sub_desc = models.CharField(max_length=1000,default="")
    prod_path = models.CharField(max_length=108, default = "/Vyas/PCH/")
    PCH_name=models.CharField(max_length=5000,default="")
    PCH_type=models.CharField(max_length=5000,default="")
    PCH_company= models.CharField(max_length=5000, default="")
    PCH_price=models.IntegerField(default=0)
    PCH_description=models.CharField(max_length=300000, default="")
    PCH_publish_date=models.DateField()
    PCH_image= models.ImageField(upload_to="Vyas/images",default="")
    


    def __str__(self):
        return self.PCH_name    


class Art_N_Interior_Designing(models.Model):
    sub_desc = models.CharField(max_length=1000,default="")
    Art_id=models.AutoField
    prod_path = models.CharField(max_length=108, default = "/Vyas/Art/")
    Art_name=models.CharField(max_length=2000,default="")
    Art_company=models.CharField(max_length=2000,default="")
    Art_type= models.CharField(max_length=2000, default="")
    for_place= models.CharField(max_length=5000, default="")
    Art_price=models.IntegerField(default=0)
    Art_description=models.CharField(max_length=300000, default="")
    publish_date=models.DateField()
    Art_image= models.ImageField(upload_to="Vyas/images",default="",null=True)


    def __str__(self):
        return self.Art_name

class Index(models.Model):
    index_id=models.AutoField
    title = models.CharField(max_length=100, default="")
    description_index = models.CharField(max_length=5000, default="")
    index_image= models.ImageField(upload_to="Vyas/images", default="")
    path = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.title

class Orders(models.Model):
    index_id=models.AutoField
    items_json= models.CharField(max_length=50000,default="")
    price_total =models.CharField(max_length=100, default="")
    name =models.CharField(max_length=90,default="")
    email=models.CharField(max_length=111,default="")
    address=models.CharField(max_length=111,default="")
    title_order = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")
    order_id = models.CharField(max_length=25,default="")
    order_status = models.CharField(max_length=500,default="")
    city=models.CharField(max_length=111,default="")
    state=models.CharField(max_length=111,default="")
    zip_code=models.CharField(max_length=111,default="")
    phone=models.CharField(max_length=111,default="")
    
    def __str__(self):
        return self.order_id







