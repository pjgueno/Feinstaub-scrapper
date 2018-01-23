import requests

import time

sensor_id = ['739','753','787','797','1018','1020','1022','1100','1102','1114','1116','1260','1304','1471','1763','1769','1775','1845','1925','1953','1961','2033','2035','2037','2039','2213','2215','2223','2229','2231','2235','2263','2265','2291','2293','2322','2400','2402','2404','2442','2606','2674','2676','2678','2888','3048','3091','3095','3101','3191','3249','3251','3253','3325','3427','3431','3433','3435','3437','3439','3459','3463','3467','3469','3473','3479','3499','3505','3511','3555','3557','3619','3633','3635','3641','3657','3835','3837','3839','3981','4059','4178','4357','4414','4466','4468','4470','4472','4474','4476','4478','4557','4573','4607','4616','4618','4624','4660','4744','4796','4798','4800','4802','4889','5028','5123','5293','5295','5297','5299','5305','5325','5349','5353','5377','5379','5471','5473','5499','5501','5513','5527','5545','5563','5565','5628','5662','5690','5708','5738','5740','5752','5754','5776','5807','5863','5865','5876','5878','5888','5904','5906','5908','5910','5914','5916','5951','5953','5965','6023','6025','6027','6029','6031','6033','6035','6037','6039','6041','6045','6087','6089','6091','6093','6095','6129','6131','6133','6135','6137','6139','6149','6187','6189','6191','6193','6195','6197','6199','6201','6203','6223','6225','6227','6231','6276','6320','6340','6342','6344','6346','6348','6350','6352','6384','6386','6388','6390','6392','6394','6396','6410','6416','6418','6422','6424','6426','6430','6432','6434','6461','6463','6465','6525','6527','6529','6531','6533','6564','6566','6568','6584','6586','6598','6614','6628','6673','6675','6679','6681','6693','6697','6731','6769','6771','6781','6783','6799','6801','6805','6832','6834','6850','6852','6858','6868','6872','6898','6900','6906','6914','6931','6933','6937','6965','6967','6993','7017','7019','7021','7023','7025','7057','7102','7104','7106','7108','7110','7169','7175','7177','7179','7181','7183','7185','7251','7257','7267','7332','7334','7336','7375','7450','7473','7477','7479','7481','7543','7581','7583','7585','7593','7611','7613','7615','7639','7641','7667','7669','7671','7701','7723','7745','7747','7749','7751','7753','7767','7769','7773','7775','7831','7835','7837','7839','7881','7915','7917','7921','7929','7961','7963','7965','7985','7987','7989','7991','7993','8046','8050','8052','8058','8060','8068','8074','8076','8084','8279','8281','8283','8285','8291','8293','8297','8312','8319','8333','8365','8369','8415','8433','8476','8482','8512','8534','8570','8572','8574','8578','8638','8640','8648','8671','8702','8704','8747','8753','8755','8757','8759','8761']

dates = ['2015-10-01','2015-10-02','2015-10-03','2015-10-04','2015-10-05','2015-10-06','2015-10-07','2015-10-08','2015-10-09','2015-10-10','2015-10-11','2015-10-12','2015-10-13','2015-10-14','2015-10-15','2015-10-16','2015-10-17','2015-10-18','2015-10-19','2015-10-20','2015-10-21','2015-10-22','2015-10-23','2015-10-24','2015-10-25','2015-10-26','2015-10-27','2015-10-28','2015-10-29','2015-10-30','2015-10-31','2015-11-01','2015-11-02','2015-11-03','2015-11-04','2015-11-05','2015-11-06','2015-11-07','2015-11-08','2015-11-09','2015-11-10','2015-11-11','2015-11-12','2015-11-13','2015-11-14','2015-11-15','2015-11-16','2015-11-17','2015-11-18','2015-11-19','2015-11-20','2015-11-21','2015-11-22','2015-11-23','2015-11-24','2015-11-25','2015-11-26','2015-11-27','2015-11-28','2015-11-29','2015-11-30','2015-12-01','2015-12-02','2015-12-03','2015-12-04','2015-12-05','2015-12-06','2015-12-07','2015-12-08','2015-12-09','2015-12-10','2015-12-11','2015-12-12','2015-12-13','2015-12-14','2015-12-15','2015-12-16','2015-12-17','2015-12-18','2015-12-19','2015-12-20','2015-12-21','2015-12-22','2015-12-23','2015-12-24','2015-12-25','2015-12-26','2015-12-27','2015-12-28','2015-12-29','2015-12-30','2015-12-31','2016-01-01','2016-01-02','2016-01-03','2016-01-04','2016-01-05','2016-01-06','2016-01-07','2016-01-08','2016-01-09','2016-01-10','2016-01-11','2016-01-12','2016-01-13','2016-01-14','2016-01-15','2016-01-16','2016-01-17','2016-01-18','2016-01-19','2016-01-20','2016-01-21','2016-01-22','2016-01-23','2016-01-24','2016-01-25','2016-01-26','2016-01-27','2016-01-28','2016-01-29','2016-01-30','2016-01-31','2016-02-01','2016-02-02','2016-02-03','2016-02-04','2016-02-05','2016-02-06','2016-02-07','2016-02-08','2016-02-09','2016-02-10','2016-02-11','2016-02-12','2016-02-13','2016-02-14','2016-02-15','2016-02-16','2016-02-17','2016-02-18','2016-02-19','2016-02-20','2016-02-21','2016-02-22','2016-02-23','2016-02-24','2016-02-25','2016-02-26','2016-02-27','2016-02-28','2016-02-29','2016-03-01','2016-03-02','2016-03-03','2016-03-04','2016-03-05','2016-03-06','2016-03-07','2016-03-08','2016-03-09','2016-03-10','2016-03-11','2016-03-12','2016-03-13','2016-03-14','2016-03-15','2016-03-16','2016-03-17','2016-03-18','2016-03-19','2016-03-20','2016-03-21','2016-03-22','2016-03-23','2016-03-24','2016-03-25','2016-03-26','2016-03-27','2016-03-28','2016-03-29','2016-03-30','2016-03-31','2016-04-01','2016-04-02','2016-04-03','2016-04-04','2016-04-05','2016-04-06','2016-04-07','2016-04-08','2016-04-09','2016-04-10','2016-04-11','2016-04-12','2016-04-13','2016-04-14','2016-04-15','2016-04-16','2016-04-17','2016-04-18','2016-04-19','2016-04-20','2016-04-21','2016-04-22','2016-04-23','2016-04-24','2016-04-25','2016-04-26','2016-04-27','2016-04-28','2016-04-29','2016-04-30','2016-05-01','2016-05-02','2016-05-03','2016-05-04','2016-05-05','2016-05-06','2016-05-07','2016-05-08','2016-05-09','2016-05-10','2016-05-11','2016-05-12','2016-05-13','2016-05-14','2016-05-15','2016-05-16','2016-05-17','2016-05-18','2016-05-19','2016-05-20','2016-05-21','2016-05-22','2016-05-23','2016-05-24','2016-05-25','2016-05-26','2016-05-27','2016-05-28','2016-05-29','2016-05-30','2016-05-31','2016-06-01','2016-06-02','2016-06-03','2016-06-04','2016-06-05','2016-06-06','2016-06-07','2016-06-08','2016-06-09','2016-06-10','2016-06-11','2016-06-12','2016-06-13','2016-06-14','2016-06-15','2016-06-16','2016-06-17','2016-06-18','2016-06-19','2016-06-20','2016-06-21','2016-06-22','2016-06-23','2016-06-24','2016-06-25','2016-06-26','2016-06-27','2016-06-28','2016-06-29','2016-06-30','2016-07-01','2016-07-02','2016-07-03','2016-07-04','2016-07-05','2016-07-06','2016-07-07','2016-07-08','2016-07-09','2016-07-10','2016-07-11','2016-07-12','2016-07-13','2016-07-14','2016-07-15','2016-07-16','2016-07-17','2016-07-18','2016-07-19','2016-07-20','2016-07-21','2016-07-22','2016-07-23','2016-07-24','2016-07-25','2016-07-26','2016-07-27','2016-07-28','2016-07-29','2016-07-30','2016-07-31','2016-08-01','2016-08-02','2016-08-03','2016-08-04','2016-08-05','2016-08-06','2016-08-07','2016-08-08','2016-08-09','2016-08-10','2016-08-11','2016-08-12','2016-08-13','2016-08-14','2016-08-15','2016-08-16','2016-08-17','2016-08-18','2016-08-19','2016-08-20','2016-08-21','2016-08-22','2016-08-23','2016-08-24','2016-08-25','2016-08-26','2016-08-27','2016-08-28','2016-08-29','2016-08-30','2016-08-31','2016-09-01','2016-09-02','2016-09-03','2016-09-04','2016-09-05','2016-09-06','2016-09-07','2016-09-08','2016-09-09','2016-09-10','2016-09-11','2016-09-12','2016-09-13','2016-09-14','2016-09-15','2016-09-16','2016-09-17','2016-09-18','2016-09-19','2016-09-20','2016-09-21','2016-09-22','2016-09-23','2016-09-24','2016-09-25','2016-09-26','2016-09-27','2016-09-28','2016-09-29','2016-09-30','2016-10-01','2016-10-02','2016-10-03','2016-10-04','2016-10-05','2016-10-06','2016-10-07','2016-10-08','2016-10-09','2016-10-10','2016-10-11','2016-10-12','2016-10-13','2016-10-14','2016-10-15','2016-10-16','2016-10-17','2016-10-18','2016-10-19','2016-10-20','2016-10-21','2016-10-22','2016-10-23','2016-10-24','2016-10-25','2016-10-26','2016-10-27','2016-10-28','2016-10-29','2016-10-30','2016-10-31','2016-11-01','2016-11-02','2016-11-03','2016-11-04','2016-11-05','2016-11-06','2016-11-07','2016-11-08','2016-11-09','2016-11-10','2016-11-11','2016-11-12','2016-11-13','2016-11-14','2016-11-15','2016-11-16','2016-11-17','2016-11-18','2016-11-19','2016-11-20','2016-11-21','2016-11-22','2016-11-23','2016-11-24','2016-11-25','2016-11-26','2016-11-27','2016-11-28','2016-11-29','2016-11-30','2016-12-01','2016-12-02','2016-12-03','2016-12-04','2016-12-05','2016-12-06','2016-12-07','2016-12-08','2016-12-09','2016-12-10','2016-12-11','2016-12-12','2016-12-13','2016-12-14','2016-12-15','2016-12-16','2016-12-17','2016-12-18','2016-12-19','2016-12-20','2016-12-21','2016-12-22','2016-12-23','2016-12-24','2016-12-25','2016-12-26','2016-12-27','2016-12-28','2016-12-29','2016-12-30','2016-12-31','2017-01-01','2017-01-02','2017-01-03','2017-01-04','2017-01-05','2017-01-06','2017-01-07','2017-01-08','2017-01-09','2017-01-10','2017-01-11','2017-01-12','2017-01-13','2017-01-14','2017-01-15','2017-01-16','2017-01-17','2017-01-18','2017-01-19','2017-01-20','2017-01-21','2017-01-22','2017-01-23','2017-01-24','2017-01-25','2017-01-26','2017-01-27','2017-01-28','2017-01-29','2017-01-30','2017-01-31','2017-02-01','2017-02-02','2017-02-03','2017-02-04','2017-02-05','2017-02-06','2017-02-07','2017-02-08','2017-02-09','2017-02-10','2017-02-11','2017-02-12','2017-02-13','2017-02-14','2017-02-15','2017-02-16','2017-02-17','2017-02-18','2017-02-19','2017-02-20','2017-02-21','2017-02-22','2017-02-23','2017-02-24','2017-02-25','2017-02-26','2017-02-27','2017-02-28','2017-03-01','2017-03-02','2017-03-03','2017-03-04','2017-03-05','2017-03-06','2017-03-07','2017-03-08','2017-03-09','2017-03-10','2017-03-11','2017-03-12','2017-03-13','2017-03-14','2017-03-15','2017-03-16','2017-03-17','2017-03-18','2017-03-19','2017-03-20','2017-03-21','2017-03-22','2017-03-23','2017-03-24','2017-03-25','2017-03-26','2017-03-27','2017-03-28','2017-03-29','2017-03-30','2017-03-31','2017-04-01','2017-04-02','2017-04-03','2017-04-04','2017-04-05','2017-04-06','2017-04-07','2017-04-08','2017-04-09','2017-04-10','2017-04-11','2017-04-12','2017-04-13','2017-04-14','2017-04-15','2017-04-16','2017-04-17','2017-04-18','2017-04-19','2017-04-20','2017-04-21','2017-04-22','2017-04-23','2017-04-24','2017-04-25','2017-04-26','2017-04-27','2017-04-28','2017-04-29','2017-04-30','2017-05-01','2017-05-02','2017-05-03','2017-05-04','2017-05-05','2017-05-06','2017-05-07','2017-05-08','2017-05-09','2017-05-10','2017-05-11','2017-05-12','2017-05-13','2017-05-14','2017-05-15','2017-05-16','2017-05-17','2017-05-18','2017-05-19','2017-05-20','2017-05-21','2017-05-22','2017-05-23','2017-05-24','2017-05-25','2017-05-26','2017-05-27','2017-05-28','2017-05-29','2017-05-30','2017-05-31','2017-06-01','2017-06-02','2017-06-03','2017-06-04','2017-06-05','2017-06-06','2017-06-07','2017-06-08','2017-06-09','2017-06-10','2017-06-11','2017-06-12','2017-06-13','2017-06-14','2017-06-15','2017-06-16','2017-06-17','2017-06-18','2017-06-19','2017-06-20','2017-06-21','2017-06-22','2017-06-23','2017-06-24','2017-06-25','2017-06-26','2017-06-27','2017-06-28','2017-06-29','2017-06-30','2017-07-01','2017-07-02','2017-07-03','2017-07-04','2017-07-05','2017-07-06','2017-07-07','2017-07-08','2017-07-09','2017-07-10','2017-07-11','2017-07-12','2017-07-13','2017-07-14','2017-07-15','2017-07-16','2017-07-17','2017-07-18','2017-07-19','2017-07-20','2017-07-21','2017-07-22','2017-07-23','2017-07-24','2017-07-25','2017-07-26','2017-07-27','2017-07-28','2017-07-29','2017-07-30','2017-07-31','2017-08-01','2017-08-02','2017-08-03','2017-08-04','2017-08-05','2017-08-06','2017-08-07','2017-08-08','2017-08-09','2017-08-10','2017-08-11','2017-08-12','2017-08-13','2017-08-14','2017-08-15','2017-08-16','2017-08-17','2017-08-18','2017-08-19','2017-08-20','2017-08-21','2017-08-22','2017-08-23','2017-08-24','2017-08-25','2017-08-26','2017-08-27','2017-08-28','2017-08-29','2017-08-30','2017-08-31','2017-09-01','2017-09-02','2017-09-03','2017-09-04','2017-09-05','2017-09-06','2017-09-07','2017-09-08','2017-09-09','2017-09-10','2017-09-11','2017-09-12','2017-09-13','2017-09-14','2017-09-15','2017-09-16','2017-09-17','2017-09-18','2017-09-19','2017-09-20','2017-09-21','2017-09-22','2017-09-23','2017-09-24','2017-09-25','2017-09-26','2017-09-27','2017-09-28','2017-09-29','2017-09-30','2017-10-01','2017-10-02','2017-10-03','2017-10-04','2017-10-05','2017-10-06','2017-10-07','2017-10-08','2017-10-09','2017-10-10','2017-10-11','2017-10-12','2017-10-13','2017-10-14','2017-10-15','2017-10-16','2017-10-17','2017-10-18','2017-10-19','2017-10-20','2017-10-21','2017-10-22','2017-10-23','2017-10-24','2017-10-25','2017-10-26','2017-10-27','2017-10-28','2017-10-29','2017-10-30','2017-10-31','2017-11-01','2017-11-02','2017-11-03','2017-11-04','2017-11-05','2017-11-06','2017-11-07','2017-11-08','2017-11-09','2017-11-10','2017-11-11','2017-11-12','2017-11-13','2017-11-14','2017-11-15','2017-11-16','2017-11-17','2017-11-18','2017-11-19','2017-11-20','2017-11-21','2017-11-22','2017-11-23','2017-11-24','2017-11-25','2017-11-26','2017-11-27','2017-11-28','2017-11-29','2017-11-30','2017-12-01','2017-12-02','2017-12-03','2017-12-04','2017-12-05','2017-12-06','2017-12-07','2017-12-08','2017-12-09','2017-12-10','2017-12-11','2017-12-12','2017-12-13','2017-12-14','2017-12-15','2017-12-16','2017-12-17','2017-12-18','2017-12-19','2017-12-20','2017-12-21','2017-12-22','2017-12-23','2017-12-24','2017-12-25','2017-12-26','2017-12-27','2017-12-28','2017-12-29','2017-12-30','2017-12-31','2018-01-01','2018-01-02','2018-01-03','2018-01-04','2018-01-05','2018-01-06','2018-01-07','2018-01-08','2018-01-09','2018-01-10','2018-01-11','2018-01-12','2018-01-13','2018-01-14','2018-01-15','2018-01-16','2018-01-17','2018-01-18','2018-01-19','2018-01-20','2018-01-21']

url_deb = 'http://archive.luftdaten.info/'

for n1 in range(0,len(dates)):

    #print(dates[n1])

    date = dates[n1]

    url_ok = url_deb + date

    #print(url_ok)

    r1 = requests.get(url_ok)
    source_code = r1.text


    for n2 in range(0,len(sensor_id)):

        test = 'sensor_'+sensor_id[n2]+'.csv'

        #print(test)

        if test in source_code:

            split1 = source_code.split(test)[0]
            split2 = split1.split('<a href="')[-1]

            url_fin = url_ok + '/' + split2 + test

            #print(url_fin)

            r2 = requests.get(url_fin)

            data = r2.text

            print(data)
