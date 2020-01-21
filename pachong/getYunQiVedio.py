import requests

import logging
import re

def get_page(url):
    response = requests.get(url)
    return response

def download(name):
    file_name = str(name)
    print(file_name)
    # file_name = "1QIyv1Kg3296" + str_name + '.ts'  # 【根据url修改】
    uri = url.rsplit("/",1)[0];
    newUrl = uri + "/" +file_name
    print(newUrl)
    try:
        res = requests.get(url=newUrl, timeout=30)
        content = res.content

        with open(r'D:\workspace\python\vedio4\%s' % file_name, 'wb')as f:
            f.write(content)
            print(file_name + '\x1b[1;30;42m 下载成功 \033[0m')
            # num = name // 20
            # print(file_name + '下载完成，' + '已下载' + ' %s %% %s' % (name / 11, '>' * num))  # 【假的进度条，能看个大概，根据url修改】

    except Exception as e:
        # 报错提示
        print(file_name + '\x1b[1;30;41m 下载失败 \033[0m')
        print(e)
        # name = re.findall('1QIyv1Kg3296(\d+).ts', file_name)[0]  # 【根据url修改】
        print(name + ' 下载失败')

        # 记录日志
        my_log = logging.getLogger('lo')
        my_log.setLevel(logging.DEBUG)
        file = logging.FileHandler('error.log', encoding='utf-8')
        file.setLevel(logging.ERROR)
        my_log_fmt = logging.Formatter('%(asctime)s-%(levelname)s:%(message)s')
        file.setFormatter(my_log_fmt)
        my_log.addHandler(file)
        my_log.error(file_name + ' 下载失败 ')
        my_log.error(e)

        # 重新下载
        download(name)  # 如果报错，递归执行一遍


from concurrent.futures import ThreadPoolExecutor  # 线程池

p = ThreadPoolExecutor(8)
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/026b23f313014b71b01846693932ac67/tranbox/026b23f313014b71b01846693932ac67_g4Z81.m3u8?aliyun_uuid=e385a302ec794ec2b3451b77b13794df'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/3adab29d4b624aa1ba19ec9879610105/tranbox/3adab29d4b624aa1ba19ec9879610105_EGDK0.m3u8?aliyun_uuid=1cd3f3d1e2a24cc6ad43d7ee27d86edf'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/015f13ff8a2f4fdab21bfca2c37ef480/tranbox/015f13ff8a2f4fdab21bfca2c37ef480_P6Tth.m3u8?aliyun_uuid=d406f704e9204c60b1cea9ff79caec94'
url = f'http://cdn-host.media.yunxi.tv/recordM3u8/d3eb9fd533bd4eff94101c9b6e30a04a/tranbox/d3eb9fd533bd4eff94101c9b6e30a04a_treD0.m3u8?aliyun_uuid=8e30180720b3462e996255c5b6d99e82'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/d3eb9fd533bd4eff94101c9b6e30a04a/tranbox/d3eb9fd533bd4eff94101c9b6e30a04a_treD0.m3u8?aliyun_uuid=8295b41bc0f344f09510659ed20a86a5'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/2fd1b599671f43438a8c37857f3912a4/tranbox/2fd1b599671f43438a8c37857f3912a4_tAHRw.m3u8?aliyun_uuid=5b0a179e68cf4b6a9e68fa0eae937442'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/e4e96aaadc724772a052d0e4aee0cea3/tranbox/e4e96aaadc724772a052d0e4aee0cea3_xzkBe.m3u8?aliyun_uuid=6453a9b769764bd4a49eb81b2d9c90a9'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/e4e96aaadc724772a052d0e4aee0cea3/tranbox/e4e96aaadc724772a052d0e4aee0cea3_xzkBe.m3u8?aliyun_uuid=539551a10b5c45149ace5270bd2494a7'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/0fe2615f0bae45a998835df6fea42f09/tranbox/0fe2615f0bae45a998835df6fea42f09_QWRiC.m3u8?aliyun_uuid=ba4f774119fb46e5b8de126ca055916b'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/7cb6303d3b2e4c9c8dec1d56df76ab47/tranbox/7cb6303d3b2e4c9c8dec1d56df76ab47_tKmLr.m3u8?aliyun_uuid=a8ebb10e7de14c2ab257efe14e031c9a'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/afa3eaf1859745e094cab0104e6c021d/tranbox/afa3eaf1859745e094cab0104e6c021d_RJLRp.m3u8?aliyun_uuid=2429032119144624a65107d6a2637879'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/147b64a356d34bb59f71124b37991401/tranbox/147b64a356d34bb59f71124b37991401_HNI9K.m3u8?aliyun_uuid=abc8644b83ff433189e29ce240ba7b02'
# url = f'http://cdn-host.media.yunxi.tv/recordM3u8/83d24a3be5eb4c30a00a2534cbe824fe/tranbox/83d24a3be5eb4c30a00a2534cbe824fe_3Lytl.m3u8?aliyun_uuid=2c22c21dcb334f5b9faf5ae629b8c8b0'

# 发送请求
response = get_page(url)
# print(respone)
# # 返回响应状态码
# print(response.status_code)
# 返回响应文本
# print(response.text)
list1 = response.text.split("\n");
list2 = [];
for x in list1:
    if '.ts' in x:
        list2.append(x);

# print(len(list2))
for name in list2:  # 【根据url修改】
    p.submit(download, name)

# 功能：失败提示，失败重试，失败记录日志，线程池提高并发，超时重试。
# 打开cmd，切进目录，执行copy /b *.ts video.ts合并速度超快。
# 打开cmd，切进目录，执行copy /b *.ts video.mp4合并速度超快。