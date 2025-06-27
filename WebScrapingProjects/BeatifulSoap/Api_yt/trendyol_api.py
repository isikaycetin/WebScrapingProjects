from time import sleep
import requests
import time
import pandas as pd

cookies = {
    '_ym_uid': '1717103811568230494',
    'COOKIE_TY.UserAlreadyLogged': 'x=1&pp=gmzZ7qH19gWXfdueTp3NLhm5Eyg=&tx=gmzZ7qH19gWXfdueTp3NLhm5Eyg=&',
    '_ym_d': '1736100000',
    'hvtb': '1',
    'platform': 'web',
    'OptanonAlertBoxClosed': '2025-04-12T12:14:20.267Z',
    'pid': '8d73def6-1059-4ea3-a07a-b767c22b71cd',
    'WebAbTesting': 'A_49-B_22-C_69-D_57-E_2-F_26-G_18-H_83-I_37-J_60-K_18-L_3-M_90-N_95-O_30-P_57-Q_83-R_47-S_68-T_37-U_91-V_9-W_63-X_22-Y_78-Z_42',
    '_gcl_au': '1.1.2976034.1744460061',
    '_fbp': 'fb.1.1744460061155.49126982621029608',
    '_gcl_gs': '2.1.k1$i1745078506$u248742466',
    '_gcl_aw': 'GCL.1745078517.CjwKCAjwk43ABhBIEiwAvvMEB9Z46kM8s3RB9xNRIYD-VyNabAVHAtX9mjmv1UaUktzk0Qi2Ng9iXBoCDv4QAvD_BwE',
    '_hjSessionUser_3408726': 'eyJpZCI6IjAyM2RlMWZiLTM4ZjgtNTAyYS05YWFlLTZhNjM3MjVlOWRiMSIsImNyZWF0ZWQiOjE3NDQ2MzEyMTQ1NTIsImV4aXN0aW5nIjp0cnVlfQ==',
    'COOKIE_TY.Anonym': 'tx=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46dHJlbmR5b2w6YW5vbmlkIjoiYmE4MjUxYTI0ZWMzMTFmMDhhN2M5YWQzYTQ4NWRhNmMiLCJyb2xlIjoiYW5vbiIsImF0d3J0bWsiOiJiYTgyNTE5Zi00ZWMzLTExZjAtOGE3Yy05YWQzYTQ4NWRhNmMiLCJhcHBOYW1lIjoidHkiLCJhdWQiOiJzYkF5ell0WCtqaGVMNGlmVld5NXR5TU9MUEpXQnJrYSIsImV4cCI6MTkwODMxNDMwMCwiaXNzIjoiYXV0aC50cmVuZHlvbC5jb20iLCJuYmYiOjE3NTA1MjYzMDB9.UbNVf8mgF8U0utbBkKXGPkY1queSUz6peumC93VXntA',
    'storefrontId': '1',
    'language': 'tr',
    'countryCode': 'TR',
    'anonUserId': '03ff78b0-502d-11f0-b174-0f2cc5db5cee',
    'sid': '4auafCdcAC',
    'ForceUpdateSearchAbDecider': 'forced',
    'msearchAb': 'ABAdvertSlotPeriod_1-ABAD_B-ABQR_B-ABqrw_b-ABSimD_B-ABBSA_D-ABSuggestionLC_B',
    'homepageAb': 'homepage%3AadWidgetSorting_V1_1-componentSMHPLiveWidgetFix_V3_1-firstComponent_V3_1-sorter_V4_b-performanceSorting_V1_3-topWidgets_V1_1%2CnavigationSection%3Asection_V1_1%2CnavigationSideMenu%3AsideMenu_V1_1',
    'FirstSession': '0',
    '_cfuvid': 'rx2o8mJaeREjpeFXn5c1Z08XCepIpA0SFCxBPNhV6PA-1751028968453-0.0.1.1-604800000',
    '_ym_isad': '2',
    '_gid': 'GA1.2.784379285.1751030342',
    '_hjSession_3408726': 'eyJpZCI6IjYzYTViN2ZlLThhMWQtNDllMy05ZThkLTI2OTJkZTI4YjE5MSIsImMiOjE3NTEwMzAzNDMxNzYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '__cflb': '04dToYCH9RsdhPpttDDEnPngTWcVjd8fYcp2FpgMHP',
    'WebAbDecider': 'ABres_B-ABBMSA_B-ABRRIn_B-ABSCB_B-ABSuggestionHighlight_B-ABBP_B-ABCatTR_B-ABSuggestionTermActive_A-ABAZSmartlisting_62-ABBH2_B-ABMB_B-ABMRF_1-ABARR_B-ABMA_B-ABSP_B-ABPastSearches_B-ABSuggestionJFYProducts_B-ABSuggestionQF_B-ABBadgeBoost_A-ABFilterRelevancy_1-ABSuggestionBadges_B-ABProductGroupTopPerformer_B-ABOpenFilterToggle_2-ABRR_2-ABBS_2-ABSuggestionPopularCTR_B',
    'VisitCount': '28',
    'SearchMode': '0',
    'WebRecoAbDecider': 'ABattributeRecoVersion_1-ABbasketRecoVersion_1-ABcollectionRecoVersion_1-ABcrossRecoVersion_1-ABsimilarRecoVersion_1-ABsimilarSameBrandVersion_1-ABcompleteTheLookVersion_1-ABshopTheLookVersion_1-ABcrossRecoAdsVersion_1-ABsimilarRecoAdsVersion_1-ABcrossSameBrandVersion_1-ABpdpGatewayVersion_1-ABallInOneRecoVersion_1',
    'AbTesting': 'SFWBFP_A-SFWDBSR_A-SFWDQL_B-SFWDRS_A-SFWDSAOFv2_B-SFWDSFAG_B-SFWDTKV2_A-SFWPSCB_B-SFWPSlicerOB_A-SSTPRFL_B-STSBuynow_B-STSCouponV2_A-STSImageSocialProof_A-STSRecoRR_B-STSRecoSocialProof_A%7C1751032657%7C8d73def6-1059-4ea3-a07a-b767c22b71cd',
    '__cf_bm': 'YsNVHGGC3PXe.pXBAVv6fvjyrC47kT5LO9FUrxrrXAQ-1751030971-1.0.1.1-e5rO2TrqdRDFrRtYcWqkgdtShIWbVg9qvhwWHR.LiTfdIneGGfgQf1kXMwzP9oFfOYVgjh3emoSPW8.cPn8WR5bhx8AI7IG9uBgTeEZ9yR0',
    '_ga_NMNGDGYKS4': 'GS2.2.s1751030343$o11$g1$t1751031410$j60$l0$h0',
    '_ga': 'GA1.1.1614497015.1744460079',
    '_ga_1': 'GS2.1.s1751029239$o22$g1$t1751031508$j50$l0$h1713160641',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Jun+27+2025+16%3A38%3A30+GMT%2B0300+(GMT%2B03%3A00)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=V77%3A0%2CV67%3A0%2CV79%3A0%2CV71%3A0%2CV69%3A0%2CV7%3A0%2CV5%3A0%2CV9%3A0%2CV1%3A0%2CV70%3A0%2CV3%3A0%2CV68%3A0%2CV78%3A0%2CV17%3A0%2CV76%3A0%2CV80%3A0%2CV16%3A0%2CV72%3A0%2CV10%3A0%2CV40%3A0%2C&consentId=9c6be6cd-36a6-48a5-847e-f24ce5655425&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0001%3A1%2CC0007%3A1%2CC0009%3A1%2CC0005%3A0&geolocation=TR%3B06&AwaitingReconsent=false',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'ty.kbt.name=ViewSearchResult,ty.platform=Web,ty.business_unit=Core%20Commerce,ty.channel=TR,com.trendyol.observability.business_transaction.name=ViewSearchResult,ty.source.service.name=WEB%20Storefront%20TR,ty.source.deployment.environment=production,ty.source.service.version=1239e001,ty.source.client.path=%2Fsr,ty.source.service.type=client',
    'if-none-match': 'W/"122a2-5+3X4rKGNoT4qGQTsNlODT2j1Bo"',
    'origin': 'https://www.trendyol.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_ym_uid=1717103811568230494; COOKIE_TY.UserAlreadyLogged=x=1&pp=gmzZ7qH19gWXfdueTp3NLhm5Eyg=&tx=gmzZ7qH19gWXfdueTp3NLhm5Eyg=&; _ym_d=1736100000; hvtb=1; platform=web; OptanonAlertBoxClosed=2025-04-12T12:14:20.267Z; pid=8d73def6-1059-4ea3-a07a-b767c22b71cd; WebAbTesting=A_49-B_22-C_69-D_57-E_2-F_26-G_18-H_83-I_37-J_60-K_18-L_3-M_90-N_95-O_30-P_57-Q_83-R_47-S_68-T_37-U_91-V_9-W_63-X_22-Y_78-Z_42; _gcl_au=1.1.2976034.1744460061; _fbp=fb.1.1744460061155.49126982621029608; _gcl_gs=2.1.k1$i1745078506$u248742466; _gcl_aw=GCL.1745078517.CjwKCAjwk43ABhBIEiwAvvMEB9Z46kM8s3RB9xNRIYD-VyNabAVHAtX9mjmv1UaUktzk0Qi2Ng9iXBoCDv4QAvD_BwE; _hjSessionUser_3408726=eyJpZCI6IjAyM2RlMWZiLTM4ZjgtNTAyYS05YWFlLTZhNjM3MjVlOWRiMSIsImNyZWF0ZWQiOjE3NDQ2MzEyMTQ1NTIsImV4aXN0aW5nIjp0cnVlfQ==; COOKIE_TY.Anonym=tx=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46dHJlbmR5b2w6YW5vbmlkIjoiYmE4MjUxYTI0ZWMzMTFmMDhhN2M5YWQzYTQ4NWRhNmMiLCJyb2xlIjoiYW5vbiIsImF0d3J0bWsiOiJiYTgyNTE5Zi00ZWMzLTExZjAtOGE3Yy05YWQzYTQ4NWRhNmMiLCJhcHBOYW1lIjoidHkiLCJhdWQiOiJzYkF5ell0WCtqaGVMNGlmVld5NXR5TU9MUEpXQnJrYSIsImV4cCI6MTkwODMxNDMwMCwiaXNzIjoiYXV0aC50cmVuZHlvbC5jb20iLCJuYmYiOjE3NTA1MjYzMDB9.UbNVf8mgF8U0utbBkKXGPkY1queSUz6peumC93VXntA; storefrontId=1; language=tr; countryCode=TR; anonUserId=03ff78b0-502d-11f0-b174-0f2cc5db5cee; sid=4auafCdcAC; ForceUpdateSearchAbDecider=forced; msearchAb=ABAdvertSlotPeriod_1-ABAD_B-ABQR_B-ABqrw_b-ABSimD_B-ABBSA_D-ABSuggestionLC_B; homepageAb=homepage%3AadWidgetSorting_V1_1-componentSMHPLiveWidgetFix_V3_1-firstComponent_V3_1-sorter_V4_b-performanceSorting_V1_3-topWidgets_V1_1%2CnavigationSection%3Asection_V1_1%2CnavigationSideMenu%3AsideMenu_V1_1; FirstSession=0; _cfuvid=rx2o8mJaeREjpeFXn5c1Z08XCepIpA0SFCxBPNhV6PA-1751028968453-0.0.1.1-604800000; _ym_isad=2; _gid=GA1.2.784379285.1751030342; _hjSession_3408726=eyJpZCI6IjYzYTViN2ZlLThhMWQtNDllMy05ZThkLTI2OTJkZTI4YjE5MSIsImMiOjE3NTEwMzAzNDMxNzYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __cflb=04dToYCH9RsdhPpttDDEnPngTWcVjd8fYcp2FpgMHP; WebAbDecider=ABres_B-ABBMSA_B-ABRRIn_B-ABSCB_B-ABSuggestionHighlight_B-ABBP_B-ABCatTR_B-ABSuggestionTermActive_A-ABAZSmartlisting_62-ABBH2_B-ABMB_B-ABMRF_1-ABARR_B-ABMA_B-ABSP_B-ABPastSearches_B-ABSuggestionJFYProducts_B-ABSuggestionQF_B-ABBadgeBoost_A-ABFilterRelevancy_1-ABSuggestionBadges_B-ABProductGroupTopPerformer_B-ABOpenFilterToggle_2-ABRR_2-ABBS_2-ABSuggestionPopularCTR_B; VisitCount=28; SearchMode=0; WebRecoAbDecider=ABattributeRecoVersion_1-ABbasketRecoVersion_1-ABcollectionRecoVersion_1-ABcrossRecoVersion_1-ABsimilarRecoVersion_1-ABsimilarSameBrandVersion_1-ABcompleteTheLookVersion_1-ABshopTheLookVersion_1-ABcrossRecoAdsVersion_1-ABsimilarRecoAdsVersion_1-ABcrossSameBrandVersion_1-ABpdpGatewayVersion_1-ABallInOneRecoVersion_1; AbTesting=SFWBFP_A-SFWDBSR_A-SFWDQL_B-SFWDRS_A-SFWDSAOFv2_B-SFWDSFAG_B-SFWDTKV2_A-SFWPSCB_B-SFWPSlicerOB_A-SSTPRFL_B-STSBuynow_B-STSCouponV2_A-STSImageSocialProof_A-STSRecoRR_B-STSRecoSocialProof_A%7C1751032657%7C8d73def6-1059-4ea3-a07a-b767c22b71cd; __cf_bm=YsNVHGGC3PXe.pXBAVv6fvjyrC47kT5LO9FUrxrrXAQ-1751030971-1.0.1.1-e5rO2TrqdRDFrRtYcWqkgdtShIWbVg9qvhwWHR.LiTfdIneGGfgQf1kXMwzP9oFfOYVgjh3emoSPW8.cPn8WR5bhx8AI7IG9uBgTeEZ9yR0; _ga_NMNGDGYKS4=GS2.2.s1751030343$o11$g1$t1751031410$j60$l0$h0; _ga=GA1.1.1614497015.1744460079; _ga_1=GS2.1.s1751029239$o22$g1$t1751031508$j50$l0$h1713160641; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+27+2025+16%3A38%3A30+GMT%2B0300+(GMT%2B03%3A00)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=V77%3A0%2CV67%3A0%2CV79%3A0%2CV71%3A0%2CV69%3A0%2CV7%3A0%2CV5%3A0%2CV9%3A0%2CV1%3A0%2CV70%3A0%2CV3%3A0%2CV68%3A0%2CV78%3A0%2CV17%3A0%2CV76%3A0%2CV80%3A0%2CV16%3A0%2CV72%3A0%2CV10%3A0%2CV40%3A0%2C&consentId=9c6be6cd-36a6-48a5-847e-f24ce5655425&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0001%3A1%2CC0007%3A1%2CC0009%3A1%2CC0005%3A0&geolocation=TR%3B06&AwaitingReconsent=false',
}

params = {
    'wc': '104156',
    'wb': '794',
    'lc': '104156',
    'qt': 'televizyon',
    'st': 'televizyon',
    'os': '1',
    'pi': '1',
    'culture': 'tr-TR',
    'userGenderId': '1',
    'pId': '0',
    'isLegalRequirementConfirmed': 'false',
    'searchStrategyType': 'DEFAULT',
    'productStampType': 'TypeA',
    'scoringAlgorithmId': '2',
    'fixSlotProductAdsIncluded': 'true',
    'searchAbDecider': 'AdvertSlotPeriod_1,AD_B,QR_B,qrw_b,SimD_B,BSA_D,SuggestionLC_B,res_B,BMSA_B,RRIn_B,SCB_B,SuggestionHighlight_B,BP_B,CatTR_B,SuggestionTermActive_A,AZSmartlisting_62,BH2_B,MB_B,MRF_1,ARR_B,MA_B,SP_B,PastSearches_B,SuggestionJFYProducts_B,SuggestionQF_B,BadgeBoost_A,FilterRelevancy_1,SuggestionBadges_B,ProductGroupTopPerformer_B,OpenFilterToggle_2,RR_2,BS_2,SuggestionPopularCTR_B',
    'location': 'null',
    # 'offset': '7200000',
    # 'offsetParameters': 'Product_72',
    'channelId': '1',
}



params['pi'] = 1
total_products = 0
excel_datas = []
while True:
    base_url='https://apigw.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr'
    response = requests.get(url=base_url,params=params,cookies=cookies,headers=headers,timeout=15)

    if response.status_code != 200:
        print(f"Hata oluştu. Kod: {response.status_code}")
        break

    data = response.json()
    result = data.get('result')

    if not result or not result.get('products'):
        print("Artık kitap yok veya ürün bulunamadı, döngü durduruluyor.")
        break

    products = result['products']
    for product in products:
        total_products += 1
        product_group_id = product.get('productGroupId', 'Grup İd Yok')
        product_name = product.get('imageAlt', 'Name Yok')
        product_url = product.get('url', 'URL Yok')

        price = product.get('price', 'Price Yok')
        original_price = price['originalPrice']
        rating_score = product.get('ratingScore', {})
        averageRating = rating_score.get('averageRating', 'averageRating Yok')
        totalCount = rating_score.get('totalCount', 'totalCount Yok')

        try:
            averageRating_float = float(averageRating)
            averageRating_str = f"{averageRating_float:.1f}"
        except (ValueError, TypeError):
            averageRating_str = "Yok"

        if product_url != 'URL Yok':
            full_url = f"https://www.trendyol.com{product_url}"
        else:
            full_url = "URL Yok"

        # ❗ averageRating değil, averageRating_str yazılmalı
        print(f"{total_products}.{product_name} -- {original_price}TL {averageRating_str} Rating - {totalCount} Değerlendirme -- {full_url}")
        excel_datas.append({
            "name": product_name,
            "price": original_price,
            "averageRating_str": averageRating_str,
            "totalCount": totalCount,
            "url": full_url,
        })
    params['pi'] += 1
    
print(f"Toplam çekilen ürün sayısı: {total_products}")

df = pd.DataFrame(excel_datas)
df.to_excel('trendyol.xlsx', index=False)
print("\n Veriler Excel dosyasına kaydedildi: trendyol.xlsx")    


#hatalı
# i =0
# for product_link in product_links:
#     response = requests.get(url=product_link,headers=headers, cookies=cookies,timeout=15)
#     if response.status_code != 200:
#         print(f"Sayfa  erişim hatası: {response.status_code}")
#         break

    # i+=1
    # tree = html.fromstring(response.content)
    #
    # other_sellers_div = tree.xpath('//div[@class="pr-omc"]')
    #
    # if other_sellers_div:
    #     other_sellers_items = other_sellers_div[0].xpath('.//div[@class="pr-mc-w"]')
    #
    #     if other_sellers_items:
    #
    #       for other_seller in other_sellers_items:
    #           name = other_seller.xpath('.//a[@class="seller-name-text"]/text()')
    #           price = other_seller.xpath('.//span[@class="prc-dsc"]/text()')
    #
    #           seller_name = name[0].strip() if name else "Adı Bilinmiyor"
    #           seller_price = price[0].strip() if price else "Fiyatı Bilinmiyor"
    #
    #           print(f"{i}.{seller_name}-{seller_price}TL- - {product_link}")
    #
    #     else:
    #         other_sellers_items ='İtems satıcı yok'
    #
    # else:
    #     other_sellers_div ='Div başka satıcı yok'





