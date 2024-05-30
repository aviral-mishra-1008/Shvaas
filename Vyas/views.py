
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Contact, Ayurveda, Clothing, Home_Appliances, software, Sports,  Education , grocery , PCH , Book , Art_N_Interior_Designing, Orders
from math import ceil
from .models import Music
from django.contrib.auth import authenticate, login , logout
from django.contrib import  messages
import random
import smtplib
from email.message import EmailMessage
from fpdf import FPDF
import os


# Create your views here.
def index(request):
    return render(request, "Vyas/Index.html")

def about(request):
    return render (request, "Vyas/about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        shop = request.POST.get('shop', '')
        description = request.POST.get('description','')
        contact = Contact(name=name, shop=shop, email=email, phone=phone, description=description)
        contact.save()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.starttls
        server.login("tailsavish.developers@gmail.com", "Vikram2021@avi_shaurya")
        subject = "[Shvass - Registration Success!]"
        body = "Hi " + name  + "\n" + "You have successfully registered with us, please hold on while we review your application and contact you back if you are verified as a seller"
        message = "Subject:{}\n\n{}".format(subject,body)
        server.sendmail("tailsavish.developers@gmail.com",email,message)
        server.quit()
    return render(request, 'Vyas/contact.html')

def gro(request):
    groc= grocery.objects.all()
    print(groc)
    n= len(groc)
    nSlides= n//4 + ceil((n/4) - (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'grocs': groc}
    return render(request,"Vyas/grocery.html", params)

def copies(request):
    books= Book.objects.all()
    n= len(books)
    nSlides= n//4 + ceil((n/4) - (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'book': books}
    return render(request,"Vyas/book.html", params)   

     
def care(request):
    personal= PCH.objects.all()
    n= len(personal)
    nSlides= n//4 + ceil((n/4) - (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'perso': personal}
    return render(request,"Vyas/personal care.html", params)   


    
def arts(request):
    design= Art_N_Interior_Designing.objects.all()
    n= len(design)
    nSlides= n//4 + ceil((n/4) - (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'des': design}
    return render(request,"Vyas/Art And design.html", params)   

def search(request):
    if request.method=="POST":
        query_s = request.POST.get('search', '')
        params = {}
        list1 = []
        try:
            smart = Product.objects.get(product_name=query_s)
            var_temp = smart.path
            list1.append(var_temp)
            params["query"]=list1[0]
        except:
            try:
                musical = Music.objects.get(music_name=query_s)
                ui = musical.prod_path
                list1.append(ui)
                params["query"]=list1[0]
                
            except:
                try:
                    Ayurveda_q = Ayurveda.objects.get(herb_name=query_s)
                    params["query"] = Ayurveda_q.prod_path
                except:
                    try:
                        JEE = Education.objects.get(education_name=query_s)
                        params["query"] = JEE.prod_path
                    except:
                        try:
                            cloths = Clothing.objects.get(Cloth_name=query_s)
                            params["query"] = cloths.prod_path
                        except:
                            try:
                                HP = Home_Appliances.objects.get(appliance_name=query_s)
                                params["query"] = HP.prod_path
                            except:
                                try:
                                    soft = software.objects.get(soft_name=query_s)
                                    params["query"] = soft.prod_path
                                except:
                                    try:
                                        sprot = Sports.objects.get(item_name=query_s)
                                        params["query"]=sprot.prod_path
                                    except:
                                        try:
                                            groce = grocery.objects.get(product_name=query_s)
                                            params["query"]=groce.prod_path
                                        except:
                                            try:
                                                book = Book.objects.get(book_name=query_s)
                                                params["query"] = book.prod_path
                                            except:
                                                params["query"] = "/Vyas/Erono"

    return render(request, 'Vyas/search.html',params)

def error_raise(request):
    return render(request, "Vyas/Erono.html")
def order(request):
    return render(request, "Vyas/order.html")

def product(request):
    # order_ID = str(random.randrange(1347829,19283942))
    # order = Orders(order_id=order_ID, title_order="Order", order_status="Order Placed!")
    # order.save()
    
    return render(request, 'Vyas/product.html')


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        cod = request.POST.get('cod','off')
        upi = request.POST.get('upi','off')
        if cod=="on":
            order_ID = str(random.randrange(1347829,19283942))
            str1 = str(items_json)
            lst = []
            lst2 = []
            str2  = str1.split('\\"')
            for i in range(1,len(str2)+1):
                if i%4==0:
                    lst.append(str2[i-1])
                else:
                    continue
            # for i in lst:
            #     print(i)
            print(lst,lst2)

            for j in range(2,len(str2)+1,4):
                x = str2[j]
                lst3 = list(x)
                for i in lst3:
                    if i!=':' and i!="[" and i!=",":
                        lst2.append(i)
                    else:
                        continue

            order = Orders(order_id=order_ID, title_order="Order", order_status="Order Placed!",items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone, price_total=amount)
            order.save()
            params = {"order_Id":order_ID}
            # making the invoice
            # json1 = []
            # for i in items_json:
            #     json1.append(i)
            from fpdf import FPDF
            with open(("A:\\Django Full On\\New Horizons\\Shvaas_Trials\\Vyas\\static\\Invoice\\"+order_ID+".txt"), "w+") as invoice:
                h = ["Shvaas By Tails AViSh\n","Invoice\n","Hi!!",name,'\n',"------------------------------------------------------\n","Net Price: ",amount," INR\n","------------------------------------------------------\n","Stay Safe Wear Mask and Use Sanitizer\n","------------------------------------------------------\n","Items include:\n","\n","------------------------------------------------------\n","Your Order ID: ",order_ID,"\n","Thanks For Choosing Us\n","  |  \n","| | |\n","  |  "]
                for i in range(len(lst)):
                    h.insert(12+i,lst[i]+"---"+lst2[i]+"\n")
                invoice.writelines(h)
            # coverting to pdf
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Times", size=12)
            file = open(("A:\\Django Full On\\New Horizons\\Shvaas_Trials\\Vyas\\static\\Invoice\\"+order_ID+".txt"),'r')
            for i in file:
                pdf.cell(200, 10, txt=i, ln=1, align="C", )
        
            pdf.output("A:\\Django Full On\\New Horizons\\Shvaas_Trials\\Vyas\\static\\Invoice\\"+order_ID+".pdf")

            # Sending email confirmation

            # opening file
            mess = EmailMessage()
            Email_Id = "tailsavish.developers@gmail.com"
            Email_pass = "Vikram@lizard.Shaurya@croc2004"
            mess['Subject'] = "[Shvass - Order Success!]"
            mess['From'] = Email_Id
            mess['To'] = email
            mess.set_content("Hi" + name +  "Your order has been successfully placed and your order ID is - " + order_ID)
            mess.add_alternative("""\
        <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
        <head>
            <!-- NAME: SELL PRODUCTS -->
            <!--[if gte mso 15]>
            <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
            </xml>
            <![endif]-->
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>*|MC:SUBJECT|*</title>
            
        <style type="text/css">
    @media only screen and (min-width:768px) {
    .templateContainer {
        width: 600px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    body,table,td,p,a,li,blockquote {
        -webkit-text-size-adjust: none !important;
    }
    }


    @media only screen and (max-width: 480px) {
    body {
        width: 100% !important;
        min-width: 100% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnRetinaImage {
        max-width: 100% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImage {
        width: 100% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnCartContainer,.mcnCaptionTopContent,.mcnRecContentContainer,.mcnCaptionBottomContent,.mcnTextContentContainer,.mcnBoxedTextContentContainer,.mcnImageGroupContentContainer,.mcnCaptionLeftTextContentContainer,.mcnCaptionRightTextContentContainer,.mcnCaptionLeftImageContentContainer,.mcnCaptionRightImageContentContainer,.mcnImageCardLeftTextContentContainer,.mcnImageCardRightTextContentContainer,.mcnImageCardLeftImageContentContainer,.mcnImageCardRightImageContentContainer {
        max-width: 100% !important;
        width: 100% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnBoxedTextContentContainer {
        min-width: 100% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImageGroupContent {
        padding: 9px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnCaptionLeftContentOuter .mcnTextContent,.mcnCaptionRightContentOuter .mcnTextContent {
        padding-top: 9px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImageCardTopImageContent,.mcnCaptionBottomContent:last-child .mcnCaptionBottomImageContent,.mcnCaptionBlockInner .mcnCaptionTopContent:last-child .mcnTextContent {
        padding-top: 18px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImageCardBottomImageContent {
        padding-bottom: 9px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImageGroupBlockInner {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImageGroupBlockOuter {
        padding-top: 9px !important;
        padding-bottom: 9px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnTextContent,.mcnBoxedTextContentColumn {
        padding-right: 18px !important;
        padding-left: 18px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnImageCardLeftImageContent,.mcnImageCardRightImageContent {
        padding-right: 18px !important;
        padding-bottom: 0 !important;
        padding-left: 18px !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcpreview-image-uploader {
        display: none !important;
        width: 100% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    h1 {
        font-size: 30px !important;
        line-height: 125% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    h2 {
        font-size: 26px !important;
        line-height: 125% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    h3 {
        font-size: 20px !important;
        line-height: 150% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    h4 {
        font-size: 18px !important;
        line-height: 150% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .mcnBoxedTextContentContainer .mcnTextContent,.mcnBoxedTextContentContainer .mcnTextContent p {
        font-size: 14px !important;
        line-height: 150% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .headerContainer .mcnTextContent,.headerContainer .mcnTextContent p {
        font-size: 16px !important;
        line-height: 150% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p {
        font-size: 16px !important;
        line-height: 150% !important;
    }
    }


    @media only screen and (max-width: 480px) {
    .footerContainer .mcnTextContent,.footerContainer .mcnTextContent p {
        font-size: 14px !important;
        line-height: 150% !important;
    }
    }
    </style>
                        <script>var w=window;if(w.performance||w.mozPerformance||w.msPerformance||w.webkitPerformance){var d=document;AKSB=w.AKSB||{},AKSB.q=AKSB.q||[],AKSB.mark=AKSB.mark||function(e,_){AKSB.q.push(["mark",e,_||(new Date).getTime()])},AKSB.measure=AKSB.measure||function(e,_,t){AKSB.q.push(["measure",e,_,t||(new Date).getTime()])},AKSB.done=AKSB.done||function(e){AKSB.q.push(["done",e])},AKSB.mark("firstbyte",(new Date).getTime()),AKSB.prof={custid:"184397",ustr:"",originlat:"0",clientrtt:"17",ghostip:"23.15.33.58",ipv6:false,pct:"10",clientip:"183.83.46.138",requestid:"2afb4ce5",region:"15849",protocol:"h2",blver:14,akM:"x",akN:"ae",akTT:"O",akTX:"1",akTI:"2afb4ce5",ai:"199322",ra:"false",pmgn:"",pmgi:"",pmp:"",qc:""},function(e){var _=d.createElement("script");_.async="async",_.src=e;var t=d.getElementsByTagName("script"),t=t[t.length-1];t.parentNode.insertBefore(_,t)}(("https:"===d.location.protocol?"https:":"http:")+"//ds-aksb-a.akamaihd.net/aksb.min.js")}</script>
                        </head>
        <body style="height: 100%; margin: 0; padding: 0; width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
            <!--*|IF:MC_PREVIEW_TEXT|*-->
            <!--[if !gte mso 9]><!----><span class="mcnPreviewText" style="font-size: 0px; line-height: 0px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; visibility: hidden; mso-hide: all; display: none;">*|MC_PREVIEW_TEXT|*</span><!--<![endif]-->
            <!--*|END:IF|*-->
            <center>
                <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; height: 100%; margin: 0; padding: 0; width: 100%;">
                    <tr>
                        <td align="center" valign="top" id="bodyCell" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; height: 100%; margin: 0; padding: 0; width: 100%;" width="100%" height="100%">
                            <!-- BEGIN TEMPLATE // -->
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                <tr>
                                    <td align="center" valign="top" id="templateHeader" data-template-container="" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background-color: #F7F7F7; background-image: url('https://mcusercontent.com/ae6c08049db0a7623219461f5/images/eb0008aa-0bd2-13b4-1be5-51c5dfdb16ee.jpg'); background-repeat: no-repeat; background-position: center; background-size: cover; border-top: 0; border-bottom: 0; padding-top: 45px; padding-bottom: 45px;" bgcolor="#F7F7F7" background="url("https://mcusercontent.com/ae6c08049db0a7623219461f5/images/eb0008aa-0bd2-13b4-1be5-51c5dfdb16ee.jpg")">
                                        <!--[if (gte mso 9)|(IE)]>
                                        <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                        <tr>
                                        <td align="center" valign="top" width="600" style="width:600px;">
                                        <![endif]-->
                                        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 600px;">
                                            <tr>
                                                <td valign="top" class="headerContainer" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background-color: transparent; background-image: none; background-repeat: no-repeat; background-position: center; background-size: cover; border-top: 0; border-bottom: 0; padding-top: 0; padding-bottom: 0;" bgcolor="transparent" background="none"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody class="mcnTextBlockOuter">
            <tr>
                <td valign="top" class="mcnTextBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 9px;">
                    <!--[if mso]>
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                    <tr>
                    <![endif]-->
                    
                    <!--[if mso]>
                    <td valign="top" width="600" style="width:600px;">
                    <![endif]-->
                    <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 100%; min-width: 100%;" width="100%" class="mcnTextContentContainer">
                        <tbody><tr>
                            
                            <td valign="top" class="mcnTextContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; word-break: break-word; color: #757575; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left; padding-top: 0; padding-right: 18px; padding-bottom: 9px; padding-left: 18px;" align="left">
                            
                                <div style="text-align: center;"><span style="font-size:32px"><strong><span style="color:#FFFFFF">SHVAAS BY TAILS AVISH</span></strong></span></div>

                            </td>
                        </tr>
                    </tbody></table>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                    
                    <!--[if mso]>
                    </tr>
                    </table>
                    <![endif]-->
                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody class="mcnImageBlockOuter">
                <tr>
                    <td valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding: 9px;" class="mcnImageBlockInner">
                        <table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
                            <tbody><tr>
                                <td class="mcnImageContent" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align: center;" align="center">
                                    
                                        
                                            <img align="center" alt="" src="https://mcusercontent.com/ae6c08049db0a7623219461f5/images/c0fc8c77-d29c-e8ac-f4c6-38e27680f6d2.jpg" width="152.28" style="border: 0; height: auto; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; max-width: 1080px; padding-bottom: 0px; vertical-align: bottom; display: inline; border-radius: 11%;" class="mcnImage">
                                        
                                    
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
        </tbody>
    </table></td>
                                            </tr>
                                        </table>
                                        <!--[if (gte mso 9)|(IE)]>
                                        </td>
                                        </tr>
                                        </table>
                                        <![endif]-->
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" valign="top" id="templateBody" data-template-container="" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background-color: #FFFFFF; background-image: url('https://mcusercontent.com/ae6c08049db0a7623219461f5/images/b891fd0f-bbe1-0472-a22b-85de85081b00.jpeg'); background-repeat: no-repeat; background-position: center; background-size: cover; border-top: 0; border-bottom: 0; padding-top: 36px; padding-bottom: 45px;" bgcolor="#FFFFFF" background="url("https://mcusercontent.com/ae6c08049db0a7623219461f5/images/b891fd0f-bbe1-0472-a22b-85de85081b00.jpeg")">
                                        <!--[if (gte mso 9)|(IE)]>
                                        <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                        <tr>
                                        <td align="center" valign="top" width="600" style="width:600px;">
                                        <![endif]-->
                                        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 600px;">
                                            <tr>
                                                <td valign="top" class="bodyContainer" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background-color: transparent; background-image: none; background-repeat: no-repeat; background-position: center; background-size: cover; border-top: 0; border-bottom: 0; padding-top: 0; padding-bottom: 0;" bgcolor="transparent" background="none"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody class="mcnTextBlockOuter">
            <tr>
                <td valign="top" class="mcnTextBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 9px;">
                    <!--[if mso]>
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                    <tr>
                    <![endif]-->
                    
                    <!--[if mso]>
                    <td valign="top" width="600" style="width:600px;">
                    <![endif]-->
                    <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 100%; min-width: 100%;" width="100%" class="mcnTextContentContainer">
                        <tbody><tr>
                            
                            <td valign="top" class="mcnTextContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; word-break: break-word; color: #757575; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left; padding-top: 0; padding-right: 18px; padding-bottom: 9px; padding-left: 18px;" align="left">
                            
                                <h3 style="display: block; margin: 0; padding: 0; color: #444444; font-family: Helvetica; font-size: 22px; font-style: normal; font-weight: bold; line-height: 150%; letter-spacing: normal; text-align: center;"><span style="color:#FFFFFF"><em>Thanks For Choosing Shvaas</em>!</span></h3>
    &nbsp;

    <center>
    <h3 style="display: block; margin: 0; padding: 0; color: #444444; font-family: Helvetica; font-size: 22px; font-style: normal; font-weight: bold; line-height: 150%; letter-spacing: normal; text-align: center;"><span style="color:#FFFFFF"><span style="font-size:18px">Your Order has been placed successfully and it will reach you within next 2 business days.<br>
    <br>
    Please keep the invoice (attached) safely with you. The invoice contains order Id which can be used to track your order on the shvaas website order tracker</span></span></h3>
    </center>

                            </td>
                        </tr>
                    </tbody></table>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                    
                    <!--[if mso]>
                    </tr>
                    </table>
                    <![endif]-->
                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; table-layout: fixed; min-width: 100%;">
        <tbody class="mcnDividerBlockOuter">
            <tr>
                <td class="mcnDividerBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%; padding: 18px;">
                    <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
                        <tbody><tr>
                            <td style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                <span></span>
                            </td>
                        </tr>
                    </tbody></table>
    <!--            
                    <td class="mcnDividerBlockInner" style="padding: 18px;">
                    <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
    -->
                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
        <tbody class="mcnCaptionBlockOuter">
            <tr>
                <td class="mcnCaptionBlockInner" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding: 9px;">
                    

    <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="282" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
        <tbody><tr>
            <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding: 0 9px 9px 9px;">
            
                

                <img alt="" src="https://mcusercontent.com/ae6c08049db0a7623219461f5/images/1f14bff4-3f87-00c5-f96f-0e528d377b99.jpg" width="264" style="border: 0; height: auto; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; vertical-align: bottom; max-width: 1024px;" class="mcnImage">
                
            
            </td>
        </tr>
        <tr>
            <td class="mcnTextContent" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; word-break: break-word; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left; padding: 0px 9px; color: #CC4C4C;" width="282" align="left">
                <h4 style="display: block; margin: 0; padding: 0; color: #949494; font-family: Georgia; font-size: 20px; font-style: italic; font-weight: normal; line-height: 125%; letter-spacing: normal; text-align: left;"><span style="color:#FFFFFF">Shvaas Offers You The Best Prices!</span></h4>

    <p style="margin: 10px 0; padding: 0; mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #757575; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left;"><span style="color:#FFFFFF">Visit Us Today</span></p>

            </td>
        </tr>
    </tbody></table>

    <table align="right" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="282" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
        <tbody><tr>
            <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding: 0 9px 9px 9px;">
            
                

                <img alt="" src="https://mcusercontent.com/ae6c08049db0a7623219461f5/images/abcc69cd-e889-d7df-2653-47e25e116d45.jpg" width="264" style="border: 0; height: auto; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; vertical-align: bottom; max-width: 1280px;" class="mcnImage">
                
            
            </td>
        </tr>
        <tr>
            <td class="mcnTextContent" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; word-break: break-word; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left; padding: 0px 9px; color: #CC4C4C;" width="282" align="left">
                <h4 style="display: block; margin: 0; padding: 0; color: #949494; font-family: Georgia; font-size: 20px; font-style: italic; font-weight: normal; line-height: 125%; letter-spacing: normal; text-align: left;"><span style="color:#FFFFFF">Purchase Your Next Phone Here!</span></h4>

    <p style="margin: 10px 0; padding: 0; mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #757575; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left;"><span style="color:#FFFFFF">We provide you the range of best budget phones like Micromax IN 1 to the best quality high end phones like Google Pixel 5</span></p>

    <p style="margin: 10px 0; padding: 0; mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #757575; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left;"><span style="color:#FFFFFF">Shop Today!</span></p>

            </td>
        </tr>
    </tbody></table>





                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; table-layout: fixed; min-width: 100%;">
        <tbody class="mcnDividerBlockOuter">
            <tr>
                <td class="mcnDividerBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%; padding: 18px;">
                    <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%; border-top: 2px solid #EAEAEA;">
                        <tbody><tr>
                            <td style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                <span></span>
                            </td>
                        </tr>
                    </tbody></table>
    <!--            
                    <td class="mcnDividerBlockInner" style="padding: 18px;">
                    <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
    -->
                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody class="mcnTextBlockOuter">
            <tr>
                <td valign="top" class="mcnTextBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 9px;">
                    <!--[if mso]>
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                    <tr>
                    <![endif]-->
                    
                    <!--[if mso]>
                    <td valign="top" width="600" style="width:600px;">
                    <![endif]-->
                    <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 100%; min-width: 100%;" width="100%" class="mcnTextContentContainer">
                        <tbody><tr>
                            
                            <td valign="top" class="mcnTextContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; word-break: break-word; color: #757575; font-family: Helvetica; font-size: 16px; line-height: 150%; text-align: left; padding-top: 0; padding-right: 18px; padding-bottom: 9px; padding-left: 18px;" align="left">
                            
                                <div style="text-align: center;"><strong><span style="color:#FF8C00">"AT SHVAAS YOUR SATISFACTION MATTERS THE MOST" </span></strong></div>

    <div style="text-align: center;"><strong><span style="color:#FF8C00">&nbsp;AVIRAL, VIKRAM AND SHAURYA.</span></strong></div>

                            </td>
                        </tr>
                    </tbody></table>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                    
                    <!--[if mso]>
                    </tr>
                    </table>
                    <![endif]-->
                </td>
            </tr>
        </tbody>
    </table></td>
                                            </tr>
                                        </table>
                                        <!--[if (gte mso 9)|(IE)]>
                                        </td>
                                        </tr>
                                        </table>
                                        <![endif]-->
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" valign="top" id="templateFooter" data-template-container="" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background-color: #825b3b; background-image: none; background-repeat: no-repeat; background-position: center; background-size: cover; border-top: 0; border-bottom: 0; padding-top: 45px; padding-bottom: 63px;" bgcolor="#825b3b" background="none">
                                        <!--[if (gte mso 9)|(IE)]>
                                        <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                                        <tr>
                                        <td align="center" valign="top" width="600" style="width:600px;">
                                        <![endif]-->
                                        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 600px;">
                                            <tr>
                                                <td valign="top" class="footerContainer" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background-color: transparent; background-image: none; background-repeat: no-repeat; background-position: center; background-size: cover; border-top: 0; border-bottom: 0; padding-top: 0; padding-bottom: 0;" bgcolor="transparent" background="none"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody class="mcnFollowBlockOuter">
            <tr>
                <td align="center" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding: 9px;" class="mcnFollowBlockInner">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentContainer" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody><tr>
            <td align="center" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-left: 9px; padding-right: 9px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;" class="mcnFollowContent">
                    <tbody><tr>
                        <td align="center" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 9px; padding-right: 9px; padding-left: 9px;">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                <tbody><tr>
                                    <td align="center" valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                        <!--[if mso]>
                                        <table align="center" border="0" cellspacing="0" cellpadding="0">
                                        <tr>
                                        <![endif]-->
                                        
                                            <!--[if mso]>
                                            <td align="center" valign="top">
                                            <![endif]-->
                                            
                                            
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; display: inline;">
                                                    <tbody><tr>
                                                        <td valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-right: 10px; padding-bottom: 9px;" class="mcnFollowContentItemContainer">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                <tbody><tr>
                                                                    <td align="left" valign="middle" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 10px; padding-bottom: 5px; padding-left: 9px;">
                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" width="" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                            <tbody><tr>
                                                                                
                                                                                    <td align="center" valign="middle" width="24" class="mcnFollowIconContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                                        <a href="http://www.facebook.com" target="_blank" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-light-facebook-48.png" alt="Facebook" style="-ms-interpolation-mode: bicubic; border: 0; height: auto; outline: none; text-decoration: none; display: block;" height="24" width="24" class=""></a>
                                                                                    </td>
                                                                                
                                                                                
                                                                            </tr>
                                                                        </tbody></table>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            
                                            <!--[if mso]>
                                            </td>
                                            <![endif]-->
                                        
                                            <!--[if mso]>
                                            <td align="center" valign="top">
                                            <![endif]-->
                                            
                                            
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; display: inline;">
                                                    <tbody><tr>
                                                        <td valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-right: 10px; padding-bottom: 9px;" class="mcnFollowContentItemContainer">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                <tbody><tr>
                                                                    <td align="left" valign="middle" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 10px; padding-bottom: 5px; padding-left: 9px;">
                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" width="" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                            <tbody><tr>
                                                                                
                                                                                    <td align="center" valign="middle" width="24" class="mcnFollowIconContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                                        <a href="http://www.twitter.com/" target="_blank" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-light-twitter-48.png" alt="Twitter" style="-ms-interpolation-mode: bicubic; border: 0; height: auto; outline: none; text-decoration: none; display: block;" height="24" width="24" class=""></a>
                                                                                    </td>
                                                                                
                                                                                
                                                                            </tr>
                                                                        </tbody></table>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            
                                            <!--[if mso]>
                                            </td>
                                            <![endif]-->
                                        
                                            <!--[if mso]>
                                            <td align="center" valign="top">
                                            <![endif]-->
                                            
                                            
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; display: inline;">
                                                    <tbody><tr>
                                                        <td valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-right: 10px; padding-bottom: 9px;" class="mcnFollowContentItemContainer">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                <tbody><tr>
                                                                    <td align="left" valign="middle" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 10px; padding-bottom: 5px; padding-left: 9px;">
                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" width="" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                            <tbody><tr>
                                                                                
                                                                                    <td align="center" valign="middle" width="24" class="mcnFollowIconContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                                        <a href="http://www.instagram.com/" target="_blank" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-light-instagram-48.png" alt="Link" style="-ms-interpolation-mode: bicubic; border: 0; height: auto; outline: none; text-decoration: none; display: block;" height="24" width="24" class=""></a>
                                                                                    </td>
                                                                                
                                                                                
                                                                            </tr>
                                                                        </tbody></table>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            
                                            <!--[if mso]>
                                            </td>
                                            <![endif]-->
                                        
                                            <!--[if mso]>
                                            <td align="center" valign="top">
                                            <![endif]-->
                                            
                                            
                                                <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; display: inline;">
                                                    <tbody><tr>
                                                        <td valign="top" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-right: 0; padding-bottom: 9px;" class="mcnFollowContentItemContainer">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                <tbody><tr>
                                                                    <td align="left" valign="middle" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 10px; padding-bottom: 5px; padding-left: 9px;">
                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" width="" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                            <tbody><tr>
                                                                                
                                                                                    <td align="center" valign="middle" width="24" class="mcnFollowIconContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                                                                        <a href="http://mailchimp.com" target="_blank" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/outline-light-link-48.png" alt="Website" style="-ms-interpolation-mode: bicubic; border: 0; height: auto; outline: none; text-decoration: none; display: block;" height="24" width="24" class=""></a>
                                                                                    </td>
                                                                                
                                                                                
                                                                            </tr>
                                                                        </tbody></table>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            
                                            <!--[if mso]>
                                            </td>
                                            <![endif]-->
                                        
                                        <!--[if mso]>
                                        </tr>
                                        </table>
                                        <![endif]-->
                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
            </td>
        </tr>
    </tbody></table>

                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; table-layout: fixed; min-width: 100%;">
        <tbody class="mcnDividerBlockOuter">
            <tr>
                <td class="mcnDividerBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%; padding: 18px;">
                    <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%; border-top: 2px solid #505050;">
                        <tbody><tr>
                            <td style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                                <span></span>
                            </td>
                        </tr>
                    </tbody></table>
    <!--            
                    <td class="mcnDividerBlockInner" style="padding: 18px;">
                    <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
    -->
                </td>
            </tr>
        </tbody>
    </table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; min-width: 100%;">
        <tbody class="mcnTextBlockOuter">
            <tr>
                <td valign="top" class="mcnTextBlockInner" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 9px;">
                    <!--[if mso]>
                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                    <tr>
                    <![endif]-->
                    
                    <!--[if mso]>
                    <td valign="top" width="600" style="width:600px;">
                    <![endif]-->
                    <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; max-width: 100%; min-width: 100%;" width="100%" class="mcnTextContentContainer">
                        <tbody><tr>
                            
                            <td valign="top" class="mcnTextContent" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; word-break: break-word; color: #FFFFFF; font-family: Helvetica; font-size: 12px; line-height: 150%; text-align: center; padding-top: 0; padding-right: 18px; padding-bottom: 9px; padding-left: 18px;" align="center">
                            
                                <em>Copyright © 2021 Shvaas, All rights reserved.</em><br>
    Visit Us :&nbsp;<a href="https://github.com/Developer-Pro-MAX/shvaas" target="_blank" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #FFFFFF; font-weight: normal; text-decoration: underline;">https://github.com/Developer-Pro-MAX/shvaas</a><br>
    <br>
    <strong>Our mailing address is:</strong><br>
    <a href="mailto:tailsavish.developers@gmail.com?subject=Query&amp;body=Hi%20Lords" target="_blank" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #FFFFFF; font-weight: normal; text-decoration: underline;">tailsavish.developers@gmail.com</a><br>
    <br>
    Want to change how you receive these emails?<br>
    You can <a href="*|UPDATE_PROFILE|*" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #FFFFFF; font-weight: normal; text-decoration: underline;">update your preferences</a> or <a href="*|UNSUB|*" style="mso-line-height-rule: exactly; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; color: #FFFFFF; font-weight: normal; text-decoration: underline;">unsubscribe from this list</a>.<br>
    &nbsp;
                            </td>
                        </tr>
                    </tbody></table>
                    <!--[if mso]>
                    </td>
                    <![endif]-->
                    
                    <!--[if mso]>
                    </tr>
                    </table>
                    <![endif]-->
                </td>
            </tr>
        </tbody>
    </table></td>
                                            </tr>
                                        </table>
                                        <!--[if (gte mso 9)|(IE)]>
                                        </td>
                                        </tr>
                                        </table>
                                        <![endif]-->
                                    </td>
                                </tr>
                            </table>
                            <!-- // END TEMPLATE -->
                        </td>
                    </tr>
                </table>
            </center>
        </body>
    </html>

            """
            , subtype='html')
            with open(("A:\\Django Full On\\New Horizons\\Shvaas_Trials\\Vyas\\static\\Invoice\\"+order_ID+".pdf"),"rb") as File:
                file_data = File.read()
                file_name = File.name
            
            mess.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename = file_name)


            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(Email_Id,Email_pass)
            server.send_message(mess)
            server.quit()
            os.remove(("A:\\Django Full On\\New Horizons\\Shvaas_Trials\\Vyas\\static\\Invoice\\"+order_ID+".pdf"))
            return render(request, 'Vyas/order.html',params)
        elif upi=="on":
            return render(request, 'Vyas/upi.html')
    return render(request, "Vyas/checkout.html")

def track(request):        
    return render(request,"Vyas/track.html")

def track_result(request):
    iD = request.POST.get('text','Nothing To Display Folk!')
    params = {}
    order_summary = []
    try:
        order_id_fetch_info = Orders.objects.get(order_id=iD)
        order_stat = order_id_fetch_info.order_status
        order_summary.append(order_stat)
    except:
        order_summary.append('We cannot find your order, incase you feel that there has been something malicious please contact us using the contact us page')
    params["order"]=order_summary[0]
    return render(request,"Vyas/track_result.html", params)


def Prodview1(request):
    products = Product.objects.all()
    l = len(products)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(1,slides),'product':products}
    return render(request, "Vyas/Prodview1.html", parameters)

def music(request):
    musics = Music.objects.all()
    l = len(musics)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(1,slides),'music':musics}
    return render(request, "Vyas/music.html", parameters)

def ayurveda(request):
    herbs = Ayurveda.objects.all()
    l = len(herbs)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(1,slides),'herb':herbs}
    return render(request, "Vyas/ayurveda.html", parameters)

def insider(request):
    return render(request, "Vyas/insider.html")

def education(request):
    educations = Education.objects.all()
    l = len(educations)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(slides),'education':educations}
    return render(request, "Vyas/education.html", parameters )

def Cloth(request):
    products = Clothing.objects.all()
    l = len(products)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(slides),'product':products}
    return render(request, "Vyas/Clothing.html", parameters)

def soft(request):
    products = software.objects.all()
    l = len(products)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(slides),'product':products}
    return render(request, "Vyas/Software.html", parameters)

def Home_App(request):
    products = Home_Appliances.objects.all()
    l = len(products)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(slides),'product':products}
    return render(request, "Vyas/Home_Appliances.html", parameters)

def Sport(request):
    products = Sports.objects.all()
    l = len(products)
    slides = l//4 + ceil((l/4)-(l//4))
    parameters = {'number of slides':slides,'range': range(slides),'product':products}
    return render(request, "Vyas/Sports.html", parameters)
    

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/Vyas")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/Vyas/about")

    return HttpResponse("404- Not found")
    
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/Vyas/Iaminsider')

def collab(request):
    return render(request, "Vyas/collaborators.html")

def DSN(request):
    return render(request, "Vyas/dsn.html")



